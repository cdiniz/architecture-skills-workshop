# 0001. Host the core banking ledger in AWS eu-west-1 with a DR read replica in eu-central-1

- Status: Proposed
- Date: 2026-06-23
- Deciders: Architecture Review Board (scheduled), [OPEN QUESTION: which named architects, CISO, DPO, and risk representatives will attend and decide?]
- Decision owner: [OPEN QUESTION: who is the accountable individual/role for the core banking ledger platform?]
- Regulatory scope: Data residency / data sovereignty within the EU; resilience and operational continuity obligations. [NEEDS COMPLIANCE/RISK REVIEW: confirm the specific regimes in scope — likely candidates given a core banking ledger include GDPR, DORA, and the prudential/operational-resilience expectations of the relevant national competent authority, but none of these were established in the request.]

## Context

We need to decide where to host the core banking ledger — the authoritative
system of record for customer account balances and posted transactions. The
decision must be settled now because it is going to the Architecture Review
Board next week and the hosting choice is foundational: it constrains data
residency, disaster-recovery design, and our cloud-provider relationships for
the lifetime of the platform.

The ledger holds regulated customer financial data, so where it is stored and
processed, and how it recovers from a regional failure, are first-order
concerns rather than implementation details.

[ASSUMPTION: "core banking ledger" refers to the authoritative store of
customer balances and posted transactions. If the scope is narrower or wider,
the data-classification and resilience assessments below should be revisited.]

## Decision

We will host the core banking ledger in **AWS region eu-west-1 (Ireland)** as
the primary, with a **read replica in AWS eu-central-1 (Frankfurt)** maintained
for disaster recovery.

## Options considered

- **Option A — AWS eu-west-1 primary + eu-central-1 read-replica DR (chosen).**
  Single cloud provider, two EU regions. Pros: both regions are inside the EU,
  supporting EU data-residency; managed cross-region replication reduces
  operational effort; consistent tooling and a single operating model. Cons:
  concentration on a single cloud provider (AWS) for a critical system —
  provider-level outage or commercial/exit risk is not diversified;
  [OPEN QUESTION: is the eu-central-1 copy a warm DR replica only, or can it be
  promoted to serve writes, and what is the promotion/failover procedure?].

- **Option B — On-premises hosting.** Pros: maximum control over data location
  and physical custody; avoids cloud-provider concentration and outsourcing
  considerations. Cons: we own all resilience, capacity, and DR engineering;
  typically higher RTO/RPO unless heavily invested in a second data centre;
  slower to scale. [NEEDS COMPLIANCE/RISK REVIEW: an on-prem option changes the
  outsourcing/third-party risk profile materially — the comparison should note
  why it was not chosen, which was not captured in the request.]

- **Option C — Multi-cloud.** Pros: reduces single-provider concentration risk
  and strengthens the exit/portability position. Cons: significantly higher
  complexity for a stateful, strongly-consistent ledger (cross-provider
  replication, consistency, networking, and dual operating models); larger
  attack surface and more places to secure and audit.

[OPEN QUESTION: the request states an on-prem option and a multi-cloud option
were considered, but not the specific reasons each was rejected in favour of
Option A. The rationale must be recorded here before the ARB can rely on this
record.]

## Regulatory & compliance impact

- **Data residency & sovereignty.** Both the primary (eu-west-1, Ireland) and
  the DR replica (eu-central-1, Frankfurt) are within the EU, so the design
  keeps the ledger's data inside the EU under normal operation and during a
  regional failover. [NEEDS COMPLIANCE/RISK REVIEW: confirm there is no
  out-of-EU processing path — e.g. via AWS support access, backups,
  observability/telemetry, or control-plane metadata — and that this satisfies
  the institution's residency policy and any contractual customer commitments.]

- **Data classification & privacy.** A core banking ledger holds customer PII
  and customer financial data, which is highly sensitive.
  [NEEDS COMPLIANCE/RISK REVIEW: confirm the formal data classification, the
  resulting encryption/retention requirements, and whether a DPIA is required
  given the volume and sensitivity of personal data.]

- **Applicable regulation.** [NEEDS COMPLIANCE/RISK REVIEW: the specific regimes
  were not established. For a core banking ledger handling EU customer data,
  GDPR (data protection / cross-border transfer) and DORA (ICT and
  operational-resilience, including third-party/cloud risk) are likely in scope,
  alongside the operational-resilience and outsourcing expectations of the
  relevant competent authority. These must be confirmed, not assumed.]

## Risk assessment

- **Concentration / third-party risk — material.** Hosting a critical system on
  a single cloud provider concentrates dependency on AWS at the provider level;
  using two AWS regions mitigates *regional* failure but not *provider-level*
  outage, commercial, or exit risk. This is the principal trade-off versus the
  multi-cloud option.
  [NEEDS COMPLIANCE/RISK REVIEW: rate against the institution's
  concentration-risk appetite and outsourcing policy.]

- **Operational / resilience risk.** Mitigated relative to single-region hosting
  by the cross-region DR replica, subject to the failover design being proven
  (see Security & resilience).

- **Security risk.** See Security & resilience.

- **Qualitative rating and risk owner.** [NEEDS COMPLIANCE/RISK REVIEW: no
  overall risk rating or risk owner was provided. The Risk function must assign
  a rating and owner, and record any residual risk formally accepted, before
  acceptance.]

## Security & resilience

- **Resilience / continuity.** Primary in eu-west-1 with a DR read replica in
  eu-central-1 gives cross-region recovery for a regional failure.
  [OPEN QUESTION: what are the agreed RTO and RPO for the ledger, and does
  asynchronous read-replica replication meet the RPO (i.e. is bounded data loss
  on failover acceptable)?]
  [OPEN QUESTION: is failover to eu-central-1 manual or automated, has the
  promotion procedure been defined, and how frequently is DR failover tested?]
  [NEEDS COMPLIANCE/RISK REVIEW: confirm the design meets the institution's
  operational-resilience obligations and impact-tolerance thresholds (relevant
  under DORA if in scope).]

- **Security controls.** [NEEDS COMPLIANCE/RISK REVIEW: encryption in transit
  and at rest, key management (including whether keys are
  customer-managed/HSM-backed and where they reside relative to the EU
  residency requirement), secrets handling, network segregation between regions,
  and access control / segregation of duties were not specified. These must be
  defined and reviewed by Security before acceptance.]

## Consequences

- **Easier.** A single-provider, two-region design keeps one operating model and
  tooling, uses managed cross-region replication, and keeps the ledger's data
  within the EU.

- **Harder / trade-offs accepted.** We accept single-cloud-provider
  concentration for a critical system as the price of operational simplicity,
  in preference to the multi-cloud option. Provider-level outage and commercial
  lock-in are not diversified by this design.

- **Reversibility / exit.** Migrating a stateful, strongly-consistent ledger off
  AWS later would be substantial work. [OPEN QUESTION: what is the documented
  exit/portability plan for the ledger off AWS, as required for a critical
  outsourced service?]

- **Follow-up work.** Resolve the open questions on RTO/RPO and failover,
  complete the security and encryption/key-management design, and obtain the
  compliance, risk, and security reviews flagged above.

## Approvals

- **Architecture Review Board** — scheduled for next week; this record is
  prepared as input to that session.
- [NEEDS COMPLIANCE/RISK REVIEW: confirm whether CISO (security design), DPO
  (data-residency/DPIA), and the Risk Committee (concentration-risk acceptance)
  must also sign off before this moves from Proposed to Accepted.]

This ADR remains **Proposed** until the open questions and compliance/risk/
security reviews above are resolved and the required forums have signed off.

## References

[OPEN QUESTION: link the relevant artefacts once they exist — solution/spec
document, DPIA, threat model, risk-register entry, the AWS outsourcing/exit
assessment, and any related ADRs.]
