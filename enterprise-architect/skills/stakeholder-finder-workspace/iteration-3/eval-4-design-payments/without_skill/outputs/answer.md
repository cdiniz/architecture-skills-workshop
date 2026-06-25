# Who should be in the room — Instant-Payments Processing Flow & Systems Integration Design Session

This is a **hands-on technical design session** focused on (a) the instant-payments processing flow and (b) how it integrates with our systems. The right room is small, technical, and decision-capable, combining payments domain depth, integration design, and the non-functional concerns (resilience, data, cloud) that instant payments stress. Compliance is included because instant payments carry specific regulatory obligations.

Based on the available stakeholder data, the following people should attend.

## Core attendees (must be in the room)

### Bram Hendriks — Domain Architect, Payments
Owns payments architecture standards and payment-processing patterns. His explicit concerns are instant payments, fragmented payment rails, resilience under high transaction volumes, event-driven processing, and reconciliation patterns. He is the natural design lead/owner for the instant-payments flow and the person who must ensure it aligns with core banking and integration standards. **Essential.**

### Ahmed Benali — Integration Architect
The session is explicitly about "how it integrates with our systems." Ahmed designs cross-domain integration patterns, governs API contracts, and drives the event backbone — directly the "integrates with our systems" half of the task. He guards against point-to-point sprawl and brittle batch interfaces, both critical for a real-time payments flow. **Essential.**

### Aisha Khan — Tribe Lead, Payments
Leads payments delivery and owns throughput, resilience, and time-to-market for payment products, including the operational risk of high-volume processing. She connects the design to what the tribe can actually build and run, and aligns it to regulatory deadlines. Brings delivery and operational reality into a hands-on session. **Essential.**

## Recommended attendees (strong value for this specific topic)

### Anika Sharma — Head of Data Architecture
Instant-payments processing produces high-volume event/transaction data that needs lineage, consistent models, and a scalable data platform (for reconciliation, reporting, fraud/AML feeds, and audit). Her input on data products, models, and pipeline design matters for the processing flow and downstream integration. Recommended.

### Carlos Mendes — Cloud Architect
Instant payments demand high availability, low latency, and scalable, resilient infrastructure. Carlos governs landing zones, network/security baselines, and well-architected reviews — directly relevant to where and how the real-time flow runs. Recommended, especially if any new services or scaling are in scope.

### Charlotte Dubois — Compliance Officer, Architecture
Instant payments are subject to regulatory requirements (e.g. PSD2, instant-payments regulation) that Bram already flags as a domain concern. Charlotte ensures the design keeps audit trails, handles exceptions, and stays within approved standards. For a hands-on design session she can attend part-time or review the output, but should be looped in to avoid late-stage compliance rework. Recommended.

## Optional / consult as needed
None of the remaining available stakeholders are a direct fit for a hands-on payments-flow design session, though several referenced people (e.g. Maria Oliveira and Jonas Bakker, who report into the payments tribe/domain) may be relevant as hands-on engineers if their full profiles are available.

## Summary table

| Person | Role | Why in the room | Priority |
|---|---|---|---|
| Bram Hendriks | Domain Architect — Payments | Owns payments architecture & instant-payments patterns; design lead | Core |
| Ahmed Benali | Integration Architect | Owns API contracts & event backbone — the integration half | Core |
| Aisha Khan | Tribe Lead — Payments | Delivery, throughput, resilience, operational reality | Core |
| Anika Sharma | Head of Data Architecture | Transaction/event data, lineage, reconciliation & reporting feeds | Recommended |
| Carlos Mendes | Cloud Architect | Resilience, latency, scaling of the real-time platform | Recommended |
| Charlotte Dubois | Compliance Officer — Architecture | Regulatory obligations, audit trails for instant payments | Recommended (part-time) |

## Notes
- Only six stakeholder profiles were available in the data. Several people referenced in relationships (e.g. payments engineers Maria Oliveira and Jonas Bakker, core-banking and security/risk roles) do not have profiles present; if available, hands-on payments engineers and a core-banking representative would strengthen an integration-focused technical session.
