# ADR 0001: Host Core Banking Ledger in AWS eu-west-1 with DR Read Replica in eu-central-1

- Status: Proposed (for Architecture Review Board, week of 2026-06-29)
- Date: 2026-06-23
- Deciders: Enterprise Architecture, Platform Engineering, Risk & Compliance
- Tags: core-banking, hosting, disaster-recovery, data-residency

## Context

The core banking ledger is the system of record for customer accounts and
financial transactions. It is mission-critical and subject to financial
regulatory requirements, including data residency within the EU/EEA, strong
durability and availability guarantees, and a credible disaster recovery (DR)
posture.

We need to decide where and how to host this ledger. The decision must balance:

- Regulatory and data residency obligations (data must remain within the EU/EEA).
- Availability and recovery objectives (low RTO/RPO for a system of record).
- Operational maturity and the ability to scale the platform team.
- Total cost of ownership and capital expenditure.
- Time to delivery, given upcoming business commitments.

Three options were considered:

1. AWS single primary region (eu-west-1) with a DR read replica (eu-central-1).
2. On-premises hosting in owned/co-located data centres.
3. Multi-cloud, spreading the ledger across two cloud providers.

## Decision

We will host the core banking ledger primarily in **AWS eu-west-1 (Ireland)**,
with a **read replica in AWS eu-central-1 (Frankfurt)** maintained for disaster
recovery.

- The primary region (eu-west-1) handles all read and write traffic under
  normal operation.
- The read replica in eu-central-1 provides a geographically separate DR copy
  within the EU, available for promotion to primary in a regional failure or
  declared disaster.
- Both regions are within the EU, satisfying data residency requirements.

## Options Considered

### Option 1: AWS single primary (eu-west-1) + DR read replica (eu-central-1) — CHOSEN

Pros:

- Both regions are inside the EU, meeting data residency requirements.
- Geographic separation between Ireland and Frankfurt gives genuine regional
  fault isolation for DR.
- Managed AWS services reduce operational burden and accelerate delivery.
- Mature, well-understood AWS tooling for cross-region replication, backup,
  and failover.
- Predictable, consumption-based cost without large up-front capital spend.

Cons:

- Concentration risk on a single cloud provider (AWS).
- DR is read-replica based; failover to a writable primary requires a
  promotion step and tested runbooks to meet RTO/RPO targets.

### Option 2: On-premises (owned / co-located data centres)

Pros:

- Maximum control over hardware, data location, and physical security.
- No dependency on a public cloud provider.

Cons:

- High capital expenditure and long lead times to procure and stand up
  redundant data centres for DR.
- Significant operational burden: hardware lifecycle, patching, capacity
  planning, and 24/7 facilities operations.
- Slower to scale and to deliver against business timelines.
- Achieving cloud-equivalent durability and multi-site DR is costly and
  complex.

### Option 3: Multi-cloud (ledger split / replicated across two providers)

Pros:

- Reduces single-provider concentration risk.
- Potential resilience against a provider-wide outage.

Cons:

- High complexity: data consistency, replication, and failover across
  heterogeneous platforms for a strongly consistent system of record is hard
  and error-prone.
- Duplicated tooling, skills, and operational processes across providers
  increase cost and cognitive load.
- Slower delivery and a larger attack/compliance surface to assure for
  regulators.
- Marginal resilience benefit does not justify the complexity for the current
  stage of the platform.

## Consequences

Positive:

- Data residency is satisfied with both regions in the EU.
- Clear, testable DR posture using cross-region replication into eu-central-1.
- Lower operational overhead and faster delivery via managed AWS services.
- Avoided premature complexity of multi-cloud while retaining a clean path to
  revisit if concentration risk grows.

Negative / risks to manage:

- Single-provider (AWS) concentration risk must be acknowledged and tracked at
  the risk register; revisit if exposure becomes material.
- DR depends on a read replica, so RTO/RPO targets must be defined, the
  promotion/failover runbook documented, and failover regularly tested.
- Cross-region data transfer and a second region carry ongoing cost that must
  be budgeted.

## Follow-ups / Open Items

- Define explicit RTO and RPO targets for the ledger and confirm the
  replication approach meets them.
- Document and rehearse the eu-central-1 promotion/failover runbook.
- Confirm regulatory sign-off on the chosen regions with Risk & Compliance.
- Define encryption, key management (KMS), and access controls for both
  regions.
