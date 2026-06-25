# Who to talk to: standardising cross-domain integration (managed API gateway + shared event backbone, retiring point-to-point batch)

**The issue, in one line:** You want to standardise how domains integrate — introduce a managed API gateway and a shared event backbone as the sanctioned integration mechanisms, and decommission the sprawl of point-to-point batch interfaces. This is a cross-domain architecture-standards play with an ownership question (who governs the gateway and backbone), a per-domain migration impact (each domain's batch interfaces have to be retired safely), and a governance/compliance angle (retiring interfaces and routing through a gateway changes audit trails and approved patterns).

**Assumptions I'm making** (non-interactive run — these are what I'd normally check with you first):
- This is a **standing, cross-domain integration standardisation initiative**, not a one-off interface swap. If it's actually scoped to a single domain, the list narrows to that domain's architect/tribe.
- **Payments is the most material domain** in scope — it's the only domain with named architecture/tribe representation in this dataset, and batch-rail dependencies are exactly where its risk sits. If a different domain is the primary target, swap in that domain's architect/tribe lead (none others are present in this dataset — see the gap note).
- Retiring batch interfaces touches **regulated data flows and audit trails**, which is why I've pulled in compliance.

What I'd have asked: (1) Is this a programme-level mandate or a single-domain change? (2) Which domains' batch interfaces are first to retire? (3) Is regulated/customer data carried over those interfaces?

---

## Stakeholders, highest relevance first

### Ahmed Benali — Integration Architect · relevance 10/10
The owner. His remit is *"Designs integration patterns, governs API contracts, and drives adoption of the event backbone"* — this proposal **is** his remit. His stated concerns are an exact match: *"point-to-point sprawl, inconsistent API contracts, and brittle batch interfaces"*, and he *"promotes API-first contracts, event-driven integration, and a managed API gateway and event backbone."* All three axes light up. This is the person who should be drafting/co-owning the proposal — start here. Align on: target-state pattern catalogue, gateway/backbone ownership model, and the batch-retirement sequencing.

### Mark van Dijk — Chief/Lead Architect (functional leader for the architecture community) · relevance 8/10
**Structural axis.** Ahmed's dotted-line functional leader, and the functional leader for Carlos (Cloud), Anika (Data) and the Payments domain chain. A cross-domain *standard* needs sign-off from the head of the architecture function — he's the one who can mandate the gateway/backbone as the org-wide pattern and arbitrate between domains. (Entry not in this dataset; identified via the `[[stakeholder-mark-van-dijk]]` links — confirm his exact title.) Align on: endorsing the standard and the deprecation policy for point-to-point batch.

### Bram Hendriks — Domain Architect, Payments · relevance 8/10
**Remit + concern.** Owns payments architecture standards and explicitly works on *"Aligning payments modernization with core banking and integration standards"* — your standard has to land in his domain. His concerns include *"fragmented payment rails"* and he *"promotes ... event-driven processing"*, so the event backbone is directly in his interest; but *"resilience under high transaction volumes"* means he'll scrutinise routing payments through a shared gateway and retiring batch rails. He's the key domain reviewer and a likely early adopter. Align on: which payments batch interfaces can be retired, and resilience/SLA requirements for the gateway and backbone.

### Charlotte Dubois — Compliance Officer, Architecture · relevance 7/10
**Concern axis.** Retiring interfaces and re-routing flows through a gateway changes how data movement is evidenced. Her concerns are *"undocumented exceptions, gaps in audit trails, and divergence from approved standards"* — all three are in play when you decommission point-to-point batch and adopt a new sanctioned pattern. Bring her in to embed the new standard into the architecture review process and to ensure batch-retirement keeps audit trails intact. Consult, don't necessarily co-own.

### Aisha Khan — Tribe Lead, Payments · relevance 6/10
**Structural + concern.** She runs delivery for the payments tribe and owns *"legacy rail dependencies and the operational risk of high-volume processing"* — retiring batch interfaces is delivery work and operational risk that lands on her tribe. She also cares about *"time-to-market"*, so she'll want migration sequenced so it doesn't stall the roadmap. Consult on feasibility and timeline of actually decommissioning the interfaces her teams run.

### Anika Sharma — Head of Data Architecture · relevance 6/10
**Concern axis.** Point-to-point batch interfaces are very often data pipelines. Her concerns — *"fragmented pipelines, inconsistent data models, and lack of lineage visibility"* — overlap directly with replacing batch transfers with an event backbone, and she *"promotes reusable data products and standardized models."* The event backbone is also a data-contract surface. Consult so the backbone's event schemas align with her data standards and lineage requirements; the boundary between "integration event" and "data product" needs agreeing with her.

---

## Deliberately left out (so the boundary is legible)

- **Carlos Mendes — Cloud Architect (≈4, omitted):** A managed API gateway and event backbone will run on cloud landing zones, so he's relevant *once you're implementing* (network/security baselines, IaC modules). But the question here is whose input/sign-off the *standardisation decision* needs, and that's an integration-pattern decision, not a landing-zone one. Bring him in at build time, not for the proposal.
- **The line managers behind the dotted-line links** (Miguel Santos, Jeroen Meijer, Yasmine Haddad, Fatima el-Youssef, etc.): referenced via wiki-links but **not present as entries in this dataset**, so I can't read their remit/concerns. Mark van Dijk is included because the functional-leadership chain makes his sign-off structurally necessary; the others I've left out rather than guess.

## Gap worth flagging
This dataset only contains architecture/compliance roles and a single represented domain (**Payments**). A genuinely *cross-domain* integration standard needs the architect or tribe lead of **every** affected domain in the room — and no domain other than Payments appears here. Either those people live outside this dataset, or there's a real coverage gap: identify and add the equivalent domain architects (the people Ahmed must drive adoption *with*) before you treat this shortlist as complete.
