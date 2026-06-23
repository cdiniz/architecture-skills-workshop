# 0001. Adopt an event-driven architecture with Kafka for Open Banking APIs

- Status: Proposed
- Date: 2026-06-23
- Deciders: [OPEN QUESTION: who is driving and reviewing this decision — name the architects, engineering leads, and review forum]
- Decision owner: [OPEN QUESTION: name the accountable individual or role (e.g. Head of Open Banking Architecture)]
- Regulatory scope: PSD2 / Open Banking (in scope — the affected APIs are Open Banking APIs). Likely also GDPR / data protection (Open Banking APIs carry customer account and transaction data). [NEEDS COMPLIANCE/RISK REVIEW: confirm the full set of applicable regimes — see "Regulatory & compliance impact" below]

## Context

We currently expose and operate Open Banking APIs that are served by a set of
internal services communicating synchronously over REST. This synchronous,
point-to-point coupling has two drawbacks that motivate this decision:

- **Latency** — request/response chains across services add round-trip latency
  to API calls, and a slow downstream service degrades the whole chain.
- **Tight coupling** — services must know about and be available to one another
  at request time; a failure or deployment in one service can cascade to others,
  and adding consumers of an event (e.g. notifications, analytics, fraud checks)
  requires changes to the producing service.

We want to re-architect the inter-service communication behind these Open Banking
APIs to an **event-driven design using Apache Kafka**, to reduce latency on the
critical path and decouple services so they can evolve, scale, and fail
independently.

[OPEN QUESTION: which specific Open Banking flows/endpoints are in scope —
e.g. Account Information (AIS), Payment Initiation (PIS), or both? PIS carries
materially higher conduct and operational risk than read-only AIS, and the
regulatory and resilience treatment differs.]

[OPEN QUESTION: is the externally-facing API contract still synchronous
REST (with Kafka used internally between services), or does this change the
contract exposed to TPPs? This materially affects the PSD2/Open Banking
conformance assessment.]

## Decision

We will replace synchronous REST calls **between our internal services** with an
event-driven architecture using Apache Kafka. Services will publish domain events
to Kafka topics and consume the events they need, rather than calling each other
directly at request time. The goal is lower latency on the critical path and
looser coupling between services.

[DECISION PENDING: the externally-exposed Open Banking API contract — whether it
remains synchronous REST backed by event-driven internals, or moves toward an
async/callback model. Defer to the API design owner.]

## Options considered

- **Option A — Keep synchronous REST between services (status quo).**
  Pros: simplest, well understood, request/response semantics map cleanly to the
  Open Banking API model; strong consistency and straightforward error handling.
  Cons: latency accumulates across chains; tight runtime coupling and cascading
  failure; adding new consumers requires producer changes.
  Risk/compliance: lowest change risk, but does not address the resilience and
  scalability drivers.

- **Option B — Event-driven architecture with Apache Kafka (chosen).**
  Pros: lower critical-path latency; temporal decoupling (producers and consumers
  need not be simultaneously available); new consumers added without touching
  producers; Kafka log provides a natural ordered, replayable audit trail.
  Cons: introduces eventual consistency and the operational complexity of running
  Kafka; harder error handling, ordering, idempotency, and exactly-once concerns;
  a new piece of critical infrastructure to secure and operate.
  Risk/compliance: introduces a new data-carrying channel that must be brought
  into PSD2/GDPR and security scope; eventual consistency must be reconciled with
  Open Banking response-correctness expectations.

- **Option C — Alternative async/messaging technology** (e.g. a managed message
  broker / cloud-native eventing).
  [OPEN QUESTION: was any non-Kafka messaging option evaluated, and why was Kafka
  preferred — throughput, replay/log semantics, existing skills, existing
  platform? Recording the rationale strengthens the audit trail.]

## Regulatory & compliance impact

**PSD2 / Open Banking.** These are Open Banking APIs, so PSD2 and the applicable
Open Banking standard are in scope. Moving inter-service communication to events
introduces eventual consistency; the decision must ensure that API responses to
Third-Party Providers remain correct and within any mandated response-time /
availability requirements. [NEEDS COMPLIANCE/RISK REVIEW: confirm that an
event-driven backend does not breach Open Banking conformance, availability, or
response-time obligations, and whether the external API contract change (if any)
needs notification to the regulator/scheme.]

**Data protection (GDPR / equivalent).** Open Banking APIs carry customer account
holder identity and transaction data, i.e. personal and financial data. Events on
Kafka topics will contain or reference this data, creating a new processing
channel and a new at-rest store (the Kafka log and its retention).
[NEEDS COMPLIANCE/RISK REVIEW: data classification of event payloads, lawful
basis unchanged, and whether a DPIA / DPIA update is required for the new
processing channel and the log retention period.]

**Data minimisation & retention.** Kafka topics retain messages for a configured
period and can be replayed. [OPEN QUESTION: what is the retention policy for
topics carrying personal/financial data, and how does it reconcile with data-
minimisation and records-retention rules?]

[NEEDS COMPLIANCE/RISK REVIEW: confirm whether any other regime applies (e.g.
PCI DSS if card data ever traverses a topic; AML/KYC data flows; DORA operational-
resilience obligations — see Security & resilience). No card-data or AML scope was
established in the conversation, so these are not asserted here.]

## Risk assessment

The decision changes the risk profile in several directions. Ratings below are
**indicative and pending formal review** — they were not established in the
conversation.

- **Operational risk — introduced.** Kafka becomes new critical infrastructure
  whose failure could affect all Open Banking flows. Eventual consistency,
  message ordering, duplicate delivery, and consumer lag are new failure modes.
  [NEEDS COMPLIANCE/RISK REVIEW: qualitative rating and mitigation plan.]
- **Concentration risk — introduced.** Many services depending on a single
  messaging backbone concentrates failure impact. [NEEDS COMPLIANCE/RISK REVIEW.]
- **Conduct risk — potential, depends on scope.** If payment initiation (PIS) is
  in scope, eventual consistency or lost/duplicated events could lead to customer
  detriment (e.g. duplicated or delayed payments). [OPEN QUESTION: confirm PIS
  scope and the idempotency/ordering guarantees required.]
- **Resilience benefit — reduction.** Decoupling removes synchronous cascading-
  failure paths and can improve fault isolation — a positive if Kafka itself is
  made highly available.
- **Risk owner:** [OPEN QUESTION: name the risk owner accountable for the residual
  risk.]
- **Residual risk accepted:** [DECISION PENDING: to be recorded once risk review
  has assigned ratings and mitigations.]

## Security & resilience

**Security.**
- New data-carrying channel (Kafka) must be brought into the security control
  scope: encryption in transit (TLS) between clients and brokers, encryption at
  rest for the topic logs, authentication (e.g. mTLS / SASL) and topic-level
  authorisation (ACLs) so services can only read/write the topics they need.
  [NEEDS COMPLIANCE/RISK REVIEW: confirm these controls are mandated and met for
  topics carrying personal/financial data.]
- **Key management & secrets:** [OPEN QUESTION: how are broker credentials,
  client certificates, and encryption keys managed and rotated?]
- **Segregation of duties / least privilege** across producing and consuming
  services via topic ACLs. [OPEN QUESTION: who owns topic-access governance?]

**Resilience & continuity.**
- Kafka must be deployed for high availability (replication, multi-broker, and
  ideally multi-AZ) given it becomes critical to all in-scope Open Banking flows.
- [OPEN QUESTION: what are the RTO/RPO targets for the Open Banking platform, and
  does the Kafka topology meet them? DR / failover strategy for the cluster?]
- [NEEDS COMPLIANCE/RISK REVIEW: if DORA (or an equivalent operational-resilience
  regime) applies, this critical-infrastructure change likely needs to be
  reflected in operational-resilience mapping and ICT-risk assessment.]

**Third-party & concentration risk.**
- [OPEN QUESTION: will Kafka be self-managed or a managed/cloud service? A managed
  service introduces a third-party/outsourcing arrangement that needs vendor and
  exit-strategy assessment; self-managing adds operational burden.]

**Data residency & sovereignty.**
- [OPEN QUESTION: where will the Kafka cluster and its topic logs be hosted, and
  does that satisfy data-residency constraints for the customer financial data
  carried in events? Not established in the conversation.]

## Consequences

**Easier:**
- Lower critical-path latency by removing synchronous request chains.
- Adding new event consumers (analytics, notifications, fraud, audit) without
  changing producers.
- Independent scaling, deployment, and failure isolation of services.
- The Kafka log provides an ordered, replayable record of events that can support
  audit and reprocessing.

**Harder / trade-offs accepted:**
- Eventual consistency replaces synchronous request/response certainty;
  components must handle out-of-order, duplicate, and delayed events
  (idempotency, ordering keys).
- New operational burden: running, monitoring, securing, and capacity-managing
  Kafka.
- Debugging and tracing become harder across asynchronous flows; distributed
  tracing and observability investment is needed.
- New critical-infrastructure and concentration risk (see Risk assessment).

**Reversibility / exit:**
- Migration can be phased (strangler-style, per flow), which limits blast radius
  and keeps the change partially reversible during rollout. [OPEN QUESTION:
  confirm a phased migration and rollback plan per Open Banking flow.]

**Follow-up work:**
- DPIA / DPIA update for the new processing channel and retention.
- Topic-level data classification, schema governance, and retention policy.
- HA/DR design for the cluster and RTO/RPO validation.
- Security control mapping (encryption, authn/z, key management) and SoD review.

## Approvals

The following must sign off before this moves from `Proposed` to `Accepted`:

- [OPEN QUESTION: Architecture Review Board — confirm the forum and date.]
- [NEEDS COMPLIANCE/RISK REVIEW: CISO / security function — for the new Kafka
  channel's controls.]
- [NEEDS COMPLIANCE/RISK REVIEW: DPO / data protection — for the new processing
  channel, retention, and DPIA.]
- [NEEDS COMPLIANCE/RISK REVIEW: Risk Committee / operational-resilience owner —
  for concentration risk and (if applicable) DORA obligations.]
- [NEEDS COMPLIANCE/RISK REVIEW: Open Banking / PSD2 conformance owner — to
  confirm the change does not breach scheme/regulatory obligations.]

## References

- [OPEN QUESTION: link the platform/architecture spec for the re-architecture.]
- [OPEN QUESTION: link the threat model for the Kafka deployment.]
- [OPEN QUESTION: link the DPIA / DPIA update.]
- [OPEN QUESTION: link the risk register entry.]
- [OPEN QUESTION: link related ADRs (e.g. messaging platform selection,
  observability).]
