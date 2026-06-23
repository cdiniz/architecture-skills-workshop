# ADR 0001: Event-Driven Open Banking APIs with Kafka

- **Status:** Proposed
- **Date:** 2026-06-23
- **Deciders:** Enterprise Architecture, Open Banking Platform Team
- **Tags:** open-banking, event-driven, kafka, integration, decoupling

## Context

Our open banking platform is currently built around synchronous REST calls
between internal services (account information, payment initiation, consent
management, fraud screening, notifications, etc.). When a request enters the
platform, services call one another in a request/response chain.

This design has produced several recurring problems:

- **Latency and tail latency.** End-to-end request latency is the sum of every
  synchronous hop. Slow downstream dependencies inflate p95/p99 latency and
  cause client timeouts.
- **Tight coupling.** Each service must know the network location, contract, and
  availability of its downstream callees. A change or outage in one service
  ripples directly into its callers.
- **Cascading failures.** A degraded downstream service back-pressures its
  callers, and the failure propagates up the chain. We rely on timeouts,
  retries, and circuit breakers to contain this, which adds complexity.
- **Scaling friction.** Producers and consumers of data must scale together
  because they are coupled in a synchronous path, even when their load profiles
  differ.
- **Difficult fan-out.** When multiple services need to react to the same domain
  event (e.g. "payment initiated"), the originating service must call each of
  them explicitly, and the list grows over time.

We want to move to an **event-driven architecture (EDA)** using **Apache Kafka**
as the backbone for inter-service communication, while keeping
externally-facing, standards-mandated open banking REST APIs intact.

## Decision

We will **adopt Apache Kafka as the primary mechanism for asynchronous,
event-driven communication between internal open banking services**, replacing
synchronous service-to-service REST calls where the interaction does not require
an immediate, in-band response.

Key elements of the decision:

1. **Externally-facing APIs stay REST.** Open Banking / PSD2-style external
   APIs (mandated by regulation and consumed by third-party providers) remain
   synchronous REST/HTTPS. This ADR concerns *internal* inter-service
   communication only. An API/edge layer accepts the external request and
   translates it into events.

2. **Events as the integration contract.** Services communicate by publishing
   domain events (e.g. `ConsentGranted`, `PaymentInitiated`,
   `AccountAccessRequested`, `FraudCheckCompleted`) to Kafka topics. Consumers
   subscribe to the topics they care about. Producers do not know their
   consumers.

3. **Schema governance.** All events use a versioned, registered schema
   (Avro or Protobuf via a Schema Registry) with enforced backward/forward
   compatibility, so producers and consumers can evolve independently.

4. **Topic design and ordering.** Topics are partitioned by a stable key
   (e.g. account id / consent id / payment id) so that all events for a given
   business entity are ordered within a partition.

5. **Synchronous where genuinely needed.** Interactions that truly require an
   immediate answer in the request path (e.g. real-time authorization decisions
   the caller must block on) may retain REST, or use a request/reply pattern
   over Kafka with care. We do not force every interaction to be asynchronous.

6. **Reliability semantics.** We target at-least-once delivery with idempotent
   consumers. For money-movement flows we use the transactional outbox pattern
   on the producing side and idempotency keys on the consuming side to avoid
   duplicate or lost financial events.

## Consequences

### Positive

- **Lower and more predictable latency** in the producing path: a service
  publishes an event and returns, rather than blocking on a chain of downstream
  calls.
- **Strong decoupling.** Producers are unaware of consumers. New consumers can
  be added to react to existing events without changing producers.
- **Resilience.** A downstream outage no longer fails the caller; events buffer
  in Kafka and are processed when the consumer recovers.
- **Independent scaling.** Producers and consumers scale independently based on
  their own load via consumer groups and partitions.
- **Replay and auditability.** Kafka's retained, ordered log gives us event
  replay for recovery, reprocessing, and a natural audit trail — valuable in a
  regulated financial domain.
- **Easy fan-out.** Multiple services subscribe to the same event without the
  producer knowing or caring.

### Negative / Trade-offs

- **Eventual consistency.** Asynchronous processing means state across services
  is eventually consistent. Flows and UIs must be designed to tolerate "in
  progress" states; read-after-write expectations must be revisited.
- **Operational complexity.** Running Kafka (brokers, ZooKeeper/KRaft, schema
  registry, connectors), or operating a managed offering, adds infrastructure
  and on-call burden, plus topic/partition/retention/ACL management.
- **Harder end-to-end tracing and debugging.** Tracing a business transaction
  across asynchronous hops requires correlation ids and distributed-tracing
  discipline.
- **Delivery semantics are subtle.** At-least-once delivery means consumers must
  be idempotent; getting exactly-once-effective behaviour requires deliberate
  design (outbox, dedup, idempotency keys).
- **Schema evolution discipline.** A broken schema change can break many
  consumers; the schema registry and compatibility rules are mandatory, not
  optional.
- **Ordering only within a partition.** Cross-entity global ordering is not
  guaranteed; partition keys must be chosen carefully.
- **Migration risk.** Running REST and event-driven paths in parallel during
  transition increases short-term complexity.

## Alternatives Considered

- **Keep synchronous REST + service mesh.** Improve the current model with a
  mesh (retries, circuit breaking, mTLS, observability). Lower disruption, but
  does not solve fundamental coupling, fan-out, or buffering-on-failure
  problems; latency remains additive across the call chain.
- **Other messaging brokers (RabbitMQ / cloud pub-sub / SQS+SNS).** Viable for
  decoupling, but Kafka's durable, replayable, partitioned log, high throughput,
  ecosystem (Connect, Streams, Schema Registry), and strong ordering semantics
  fit the audit, replay, and scale needs of open banking better.
- **gRPC instead of REST.** Reduces per-call overhead but stays synchronous and
  point-to-point; does not address decoupling or resilience.

## Implementation Notes

- Introduce an **anti-corruption / edge layer** that converts external REST
  requests into internal events and aggregates responses where needed.
- Adopt the **transactional outbox pattern** for services that must publish an
  event as part of a state change atomically.
- Define **event schemas** and register them in a Schema Registry with
  `BACKWARD` (or `FULL`) compatibility enforced in CI.
- Establish **topic naming and partitioning conventions** (e.g.
  `obanking.payments.payment-initiated.v1`, keyed by `paymentId`).
- Plan a **strangler-style migration**: pick one bounded context (e.g. consent
  or notifications) as the pilot, run event and REST paths side by side, and
  cut over incrementally.
- Add **correlation/trace ids** to every event and integrate distributed
  tracing before broad rollout.
- Define **retention, dead-letter, and replay** policies, especially for
  money-movement topics, to meet regulatory record-keeping requirements.
