# Stakeholders to align with — SEPA Instant Payments / PSD2 modernisation

**Issue (my read):** You're modernising the payment rails to support SEPA Instant Credit Transfer, against a hard regulatory clock (PSD2 deadlines). This is squarely a payments-domain initiative with a heavy regulatory dimension, touching architecture standards, delivery throughput, integration with core banking, and audit/compliance evidence.

**Check questions I'd normally ask (assumptions made instead, since this run is non-interactive):**
- *Is this a standing transformation programme or a one-off project?* — I assume it ties into the existing **unified payments platform strategy** that the payments entries reference, so I'm pulling in the payments domain leadership, not just a delivery squad.
- *Does it involve cross-border / customer payment data movement or new cloud workloads?* — I assume standard customer payment data is in scope but no novel data-residency or greenfield cloud build, which keeps Data Architecture and Cloud Architecture marginal rather than central (noted below).
- *Who holds the formal regulatory sign-off?* — I assume PSD2/instant-payments compliance must be evidenced through the architecture review process, so the Compliance Officer is in scope.

---

## Shortlist (ordered by relevance)

### Bram Hendriks — Domain Architect, Payments · relevance 10/10
The single most central person. **Remit:** defines payments architecture standards and *"ensures regulatory and resilience requirements are met."* **Concern:** his entry names this initiative almost verbatim — *"regulatory change (PSD2, instant payments), and resilience under high transaction volumes,"* and he promotes *"a unified payments platform, event-driven processing, and strong reconciliation patterns"* while *"aligning payments modernization with core banking and integration standards."* He should own the target architecture. Align with him first on the rails design, the instant-payments processing pattern, and the PSD2 conformance approach.

### Aisha Khan — Tribe Lead, Payments · relevance 9/10
Owns delivery. **Remit:** *"ensures payments delivery complies with architecture and regulatory standards and aligns with the unified payments platform strategy."* **Concern:** throughput, resilience, time-to-market, *"legacy rail dependencies and the operational risk of high-volume processing,"* and she explicitly *"aligns the tribe's roadmap with the payments architecture and regulatory deadlines"* — i.e. the PSD2 clock is her problem to schedule against. **Structural:** she sits under Bram functionally, so she and Bram are the architecture-plus-delivery pair you need together. Align on roadmap, sequencing against the deadline, and migrating off legacy rails.

### Charlotte Dubois — Compliance Officer, Architecture · relevance 8/10
The regulatory deadline makes her a sign-off gate, not an optional consult. **Remit:** *"reviews architecture decisions for regulatory compliance and ensures audit trails and exception handling are maintained."* **Concern:** undocumented exceptions, gaps in audit trails, divergence from approved standards. For a PSD2-driven change you'll need her to confirm the design is compliant and that the decision is evidenced for auditors/regulators. Bring her in early so compliance isn't a late blocker; align on what audit trail and approval evidence the new rails must produce.

### Ahmed Benali — Integration Architect · relevance 7/10
Instant payments are an event-driven, contract-heavy integration problem, and Bram's own target ("event-driven processing", integration standards) runs straight through Ahmed's remit. **Remit:** governs API contracts and drives the event backbone. **Concern:** point-to-point sprawl, inconsistent API contracts, brittle batch interfaces — exactly the failure modes when bolting real-time rails onto legacy systems. Consult on the API-first contracts and event backbone the instant-payments flows will ride on.

---

## Deliberately left out (boundary of the shortlist)

- **Anika Sharma (Head of Data Architecture)** — relevant only if the programme introduces new payment-data pipelines, lineage, or reporting obligations. Under my assumption of a rails/processing change rather than a data-platform change, she's marginal (3/10). Pull her in if reconciliation/reporting data models become part of scope.
- **Carlos Mendes (Cloud Architect)** — relevant only if instant payments require new cloud landing zones or capacity/resilience infrastructure work. No cloud build is implied, so marginal (2–3/10). Worth a heads-up if the high-volume resilience requirement drives new infrastructure.

## Gaps worth flagging

The entries repeatedly link to people who **have no stakeholder entry in the wiki yet** — notably **Mark van Dijk** (functional leader / enterprise-architecture lead across several of these roles), **Miguel Santos**, **Jeroen Meijer** (Aisha's line manager), and the governance line behind Charlotte (**Sanne Vermeulen**, **Daan Verhoeven**). For an initiative with regulatory sign-off and cross-domain architecture impact, the **enterprise/chief architect (Mark van Dijk)** and the **governance lead** would normally belong on this list, and Aisha's business line manager would matter for funding/priority. I can't score them because their entries don't exist — that absence is itself worth noting: if you need escalation or programme-level sign-off, those are the people to add once their wiki entries are populated.
