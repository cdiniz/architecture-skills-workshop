# Who should be in the room — instant-payments processing flow & integration

**Read of the issue:** A hands-on technical design session to work out the instant-payments processing flow and how it integrates with the bank's existing systems. This is a **design / working session** — the room should be the people who will *make and live with* the technical decision (domain, integration, and payments-delivery makers), not senior leaders. Relevance gets people onto the longlist; altitude decides who actually belongs, so "Head of" / functional-leader types are biased down unless the design hinges on their expertise.

**Assumptions I'm making** (I'd normally ask these as check questions, but this run is non-interactive):
- **Meeting type = design/working session** — taken directly from "hands-on technical design session." This is the single biggest driver of the roster.
- **Regulated/customer payment data is in scope** (instant payments inherently carry it), so compliance has a stake — but at design altitude that's a *consulted* concern, not a seat that drives the agenda.
- **The integration is with our own internal systems** (core banking, event backbone, APIs), not a one-off external rail, so integration architecture matters more than cloud/landing-zone work at this stage.

If any of these is wrong — especially if this is actually a steering/sign-off session rather than working design — the altitude flips and the leaders below would come *in* rather than being represented.

---

### Bram Hendriks — Domain Architect, Payments · relevance 9/10
**Remit + concern, dead centre.** He defines payments architecture standards and governs payment-processing patterns, and his stated concerns explicitly name **instant payments**, **resilience under high transaction volumes**, **event-driven processing**, and **aligning payments modernization with core banking and integration standards** — which is precisely this session. He's the right altitude for a design session: a domain architect doing the technical shaping, not a "Head of." This is the seat the meeting is built around. *Ask him:* the target processing pattern and how it reconciles against core banking.

### Ahmed Benali — Integration Architect · relevance 9/10
**Remit, dead centre on the "integrates with our systems" half.** He designs integration patterns, governs API contracts, and drives the event backbone — and his concerns (point-to-point sprawl, brittle batch interfaces, event-driven integration, managed API gateway) are exactly the failure modes a real-time payments flow has to avoid. Instant payments is event-driven and latency-sensitive, so the integration design *is* half the problem. Maker altitude, perfect fit. *Ask him:* how the flow rides the event backbone and which API contracts the surrounding systems expose.

### Aisha Khan — Tribe Lead, Payments · relevance 7/10
**Remit + concern, delivery lens.** She owns payments delivery and worries about **throughput, resilience, time-to-market, legacy rail dependencies, and the operational risk of high-volume processing** — all of which the processing flow has to survive in production. A tribe lead is at the right working altitude for a design session (she'll have to build and run this), and she represents the hands-on payments engineers under her ([[stakeholder-maria-oliveira]], [[stakeholder-jonas-bakker]]) who have no entries of their own. *Ask her:* what the current rails/legacy dependencies will tolerate and where the delivery risk sits.

### Charlotte Dubois — Compliance Officer, Architecture · relevance 5/10
**Concern, as a guardrail not a driver.** Instant payments is heavily regulated (PSD2, instant-payments rules, audit trails), and her remit is reviewing architecture decisions for regulatory compliance and keeping audit trails / exception handling intact. In a *design* session she's a consulted voice to keep the flow inside the rails, not someone shaping the technical pattern — invite her for the compliance-touchpoint part, or capture constraints from her ahead of time rather than holding her in the room throughout. *Ask her:* the must-not-break regulatory and audit constraints on the flow.

---

### Boundary notes

**Deliberately left out**
- **Carlos Mendes — Cloud Architect (relevance ~3 for this session).** Real-time payments will eventually need landing-zone, network, and resilience decisions, but his concerns (cost control, cloud sprawl, IaC blueprints) are a *build/deploy-time* layer, not the processing-flow-and-integration design itself. Bring him in once the flow is sketched and infrastructure shaping starts.
- **Anika Sharma — Head of Data Architecture (relevance ~3 for this session).** Reconciliation/lineage data will matter, and she'd be relevant if the session pivots to data products or the data model. But she's a "Head of" — too senior for a hands-on design session — and data isn't the core of *this* flow. Consult if a reconciliation-data design strand opens up; otherwise her standards are represented through Bram's "strong reconciliation patterns" remit.

**Represented by their stream**
- **Payments engineers (e.g. [[stakeholder-maria-oliveira]], [[stakeholder-jonas-bakker]], [[stakeholder-hannah-schulz]])** — no wiki entries, and at design altitude **Aisha Khan** (their tribe lead) stands in for the payments delivery line. If the design gets deep enough to need a specific implementer's knowledge, pull the relevant named engineer in directly.

**Referenced but not in the wiki** (linked only as `[[wiki-links]]`, no entry — so not scored; adding their entries would let me place them properly):
- **[[stakeholder-mark-van-dijk]]** — functional leader across the architecture discipline (Bram, Ahmed, Carlos, Anika all dotted-line to him). Likely the design-authority / sign-off chain above this session; not needed in the room for working design, but the place escalation goes.
- **[[stakeholder-miguel-santos]]** — Ahmed's line manager and Bram's functional leader; sits over the integration/payments-architecture line. Relevant to escalation, not to the working session.
- **[[stakeholder-jeroen-meijer]]** — Aisha's line manager (payments delivery chain). Would matter for committing the tribe's time, i.e. a tactical/planning conversation, not this design session.
- **[[stakeholder-sanne-vermeulen]]** / **[[stakeholder-daan-verhoeven]]** — Charlotte's line and functional leaders (compliance/governance chain); the sign-off escalation if a regulatory exception arises.

If any of my assumptions above are off — particularly the meeting-type call — tell me and I'll re-size the room (a steering/sign-off framing would pull the "Head of" and functional-leader names *into* the list and push the makers down).
