# Stakeholder Alignment — SEPA Instant Payments & PSD2 Modernisation

**Question:** We need to modernise our payment rails to support SEPA instant payments and the PSD2 deadlines are coming. Who do I need to align with?

This initiative touches three things at once: **payments architecture and rails**, **regulatory/compliance deadlines (PSD2, instant payments)**, and the **integration and delivery** needed to ship it. The stakeholders below are drawn from the available people files, grouped by why they matter to you.

> Note: The stakeholder files cross-reference several people (e.g. Mark van Dijk, Miguel Santos, Jeroen Meijer, Maria Oliveira, Jonas Bakker, Hannah Schulz, Daan Verhoeven, Sanne Vermeulen) who do not yet have their own profile files. Where they are clearly relevant to this initiative, they are flagged at the end as people to also pull in.

---

## Tier 1 — Primary stakeholders (align first)

### Bram Hendriks — Domain Architect, Payments
**The single most important person for this initiative.** His remit is defining payments architecture standards, governing payment processing patterns, and ensuring regulatory and resilience requirements are met. His recorded concerns explicitly name **regulatory change (PSD2, instant payments)**, **fragmented payment rails**, and **resilience under high transaction volumes**. He promotes a unified payments platform, event-driven processing, and strong reconciliation patterns. He is the functional leader for the payments tribe. Your modernisation effort should be shaped with him from the start.

### Aisha Khan — Tribe Lead, Payments
Owns delivery for the payments tribe and is responsible for ensuring payments delivery **complies with architecture and regulatory standards** and aligns with the unified payments platform strategy. Her concerns include **legacy rail dependencies**, throughput, resilience, and time-to-market — directly the trade-offs in moving to SEPA instant rails. She aligns the tribe roadmap with payments architecture and **regulatory deadlines**, so she is the person who turns this into delivered work and owns the timeline against the PSD2 deadline. (She has direct reports Maria Oliveira and Jonas Bakker who will do the build.)

### Charlotte Dubois — Compliance Officer, Architecture
PSD2 is a hard regulatory deadline, so compliance must be aligned early, not at the end. Charlotte reviews architecture decisions for **regulatory compliance** and ensures **audit trails and exception handling**. Her concerns — undocumented exceptions, gaps in audit trails, divergence from approved standards — are exactly what a regulator will probe on a PSD2 programme. Engage her to confirm the compliance evidence and review path.

---

## Tier 2 — Closely involved (align early)

### Ahmed Benali — Integration Architect
SEPA instant payments require real-time, always-on connectivity to payment schemes and internal systems. Ahmed governs **API contracts** and drives the **event backbone**, and is concerned with point-to-point sprawl and brittle batch interfaces. Bram's preferred event-driven processing pattern depends on Ahmed's integration backbone, so he must be aligned on the rails' integration design and PSD2's open-banking API obligations.

---

## Tier 3 — Consult / keep informed

### Carlos Mendes — Cloud Architect
Instant payments are 24/7, low-latency, high-availability workloads. If the new rails run in the cloud, Carlos's landing zones, network/security baselines, and well-architected reviews are relevant to the resilience and availability targets. Consult on the platform/hosting and non-functional requirements.

### Anika Sharma — Head of Data Architecture
Payments generate transaction data needing reconciliation, lineage, and reporting — and PSD2 carries data-sharing/transparency dimensions. Anika governs data models, pipelines, and lineage. Involve her where the initiative touches reconciliation data, reporting, and data governance.

---

## Also pull in (referenced but no profile file available)
These names appear in the reporting lines of the people above and are likely relevant; confirm and engage them directly:

- **Maria Oliveira & Jonas Bakker** — direct reports of Aisha Khan; the delivery/engineering capacity inside the payments tribe.
- **Hannah Schulz** — functional report of Bram Hendriks within the payments domain.
- **Mark van Dijk** — functional leader / chief-architect line above the architects (Bram, Ahmed, Carlos, Anika report to him functionally); needed for architecture sign-off and cross-domain alignment.
- **Miguel Santos** — functional leader for payments architecture and line manager for integration; relevant to architecture governance.
- **Jeroen Meijer** — Aisha's line manager; relevant for delivery prioritisation and funding.
- **Sanne Vermeulen / Daan Verhoeven** — Charlotte's management chain on the compliance/governance side; relevant for formal compliance sign-off.

---

## Suggested alignment sequence
1. **Bram Hendriks** — agree the target architecture and the instant-payments/PSD2 approach.
2. **Aisha Khan** — translate into a delivery roadmap against the PSD2 deadline.
3. **Charlotte Dubois** — lock the compliance and audit requirements early.
4. **Ahmed Benali** — design the integration/event backbone for the new rails.
5. **Carlos Mendes & Anika Sharma** — confirm hosting/resilience and data/reconciliation needs.
6. Bring in the wider chain (Mark van Dijk, Miguel Santos, Jeroen Meijer, plus the compliance management line) for governance sign-off and funding.
