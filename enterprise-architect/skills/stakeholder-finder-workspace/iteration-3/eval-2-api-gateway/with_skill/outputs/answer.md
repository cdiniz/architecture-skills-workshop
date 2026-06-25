# Who to talk to: standardising cross-domain integration (API gateway + event backbone, retiring point-to-point batch)

**Issue, in my words:** You want to standardise how domains integrate by introducing two shared platform capabilities — a managed API gateway and a shared event backbone — and decommissioning the sprawl of point-to-point batch interfaces. This is a cross-cutting architecture initiative that needs both technical design and cross-domain buy-in/mandate.

**Meeting type I'm sizing for:** This reads as a **strategic / steering session** first — you're "proposing" a direction that affects every domain and involves retiring existing interfaces, which needs a mandate, prioritisation, and sign-off before design work. So I bias toward leads and functional owners who can commit a domain or set a standard, and I represent working-level specialists by their leader rather than stacking the chain. Where useful, I flag who you'd pull into the **follow-on design session**.

**What I'd have asked (assumptions stated, since this is non-interactive):**
- *Is this a one-off proposal or part of a standing transformation programme?* — Assumed a standing standardisation initiative across domains.
- *Is regulated / customer or payments data flowing over these batch interfaces being retired?* — Assumed **yes**, given a financial-services org with a payments domain; that pulls in compliance and the payments line.
- *Strategic mandate-setting or already-mandated design session?* — Assumed **strategic/steering** (you're still "proposing").

---

### Ahmed Benali — Integration Architect · relevance 10/10
The owner. His remit is literally *"Designs integration patterns, governs API contracts, and drives adoption of the event backbone,"* and his stated concerns are *"point-to-point sprawl, inconsistent API contracts, and brittle batch interfaces"* — he already advocates *"a managed API gateway and event backbone."* This is his initiative in all but name (remit + concern). He's the one person who is central to both the strategy room and the eventual design room. Align with him first; he likely has the technical proposal already.

### Bram Hendriks — Domain Architect, Payments · relevance 8/10
Strongest domain stakeholder for a cross-domain integration standard. Remit: *"Aligning payments modernization with core banking and integration standards is key,"* and he promotes *"event-driven processing"* — so a shared event backbone directly intersects his architecture (remit + concern). Payments is also where retiring batch interfaces carries the most risk (reconciliation, instant payments). For a strategic session he's the right altitude to commit the payments domain and represents the payments delivery line beneath him.

### Anika Sharma — Head of Data Architecture · relevance 8/10
Retiring point-to-point batch interfaces is squarely a data-flow change — those batch jobs move data between domains. Her concerns are *"fragmented pipelines, inconsistent data models, and lack of lineage visibility,"* and she promotes *"reusable data products and standardized models"* (concern + remit). Moving from batch to an event backbone changes pipelines and lineage, so she needs to be at the table to align the event model with data governance. As a "Head of" she's the right altitude for a strategic room and represents her data architects (e.g. her direct report) rather than each attending.

### Charlotte Dubois — Compliance Officer, Architecture · relevance 6/10
Decommissioning interfaces and standing up a new gateway/backbone is exactly the kind of change her remit covers: *"Reviews architecture decisions for regulatory compliance and ensures audit trails and exception handling are maintained,"* with concerns about *"undocumented exceptions, gaps in audit trails, and divergence from approved standards"* (remit + concern). If regulated/payments data flows over the batch interfaces being retired, she needs to confirm audit-trail and exception handling survive the migration. Consult her on the proposal; she doesn't need to be in every design detail.

### Aisha Khan — Tribe Lead, Payments · relevance 5/10
Relevant because retiring batch interfaces and adopting the event backbone lands as delivery work on her tribe — her concerns include *"legacy rail dependencies"* and *"throughput, resilience, and time-to-market"* (concern + structural). For a **strategic** session she's largely **represented by Bram** (her functional leader / the payments architecture voice). I'd surface her into the **tactical/delivery planning** session, where committing the payments tribe and sequencing the batch retirement actually happens — there she'd be a 7–8.

---

### Boundary notes

**Deliberately left out**
- **Carlos Mendes — Cloud Architect.** A managed API gateway and event backbone will run somewhere (landing zones, IaC), so he's genuinely relevant *at build/design time* — but for a strategic proposal about integration standards he's not yet needed. Bring him into the design session when you're deciding how the gateway/backbone is hosted and operated.

**Represented by their stream**
- **Aisha Khan (Tribe Lead, Payments)** is represented by **Bram Hendriks** for this strategic session — same payments line, and the architecture voice is the right altitude to set direction. Reverse this for delivery planning, where Aisha is the one who commits the tribe.
- **Anika Sharma's data architects** (her direct report and functional reports) are represented by Anika for a strategic room; pull the relevant data architect into design only if the event-schema work needs hands-on data modelling.

**Referenced but not in the wiki (no entry — unscored, follow up)**
These appear only as `[[wiki-links]]` in the entries above, so I can place them structurally but can't read a remit/concern — I won't score them. They're likely your escalation/sign-off chain for a cross-domain mandate, which is exactly what a strategic session needs:
- **Mark van Dijk** — the *functional leader* (dotted line) for Ahmed (Integration Architect), Anika (Data Architecture), and Carlos (Cloud), and line manager of Bram. He sits across the whole architecture discipline, so a cross-domain integration *standard* almost certainly needs his mandate or sign-off. **Strongest missing name** — add his entry and I can place him properly (probably top-tier for this strategic room).
- **Miguel Santos** — Ahmed's line manager and Bram's functional leader; plausibly the integration/engineering leadership Ahmed escalates through. Worth identifying as a likely sponsor.
- **Daan Verhoeven / Sanne Vermeulen** — Charlotte's functional leader and line manager; the governance/compliance leadership who would own sign-off if the batch-retirement touches regulated data.
- **Fatima el-Youssef** — Anika's manager (and oddly listed as one of her functional reports); senior data leadership worth confirming.

Adding entries for **Mark van Dijk** and **Miguel Santos** in particular would let me rank the people who can actually *mandate* this standard across domains — right now I can see the doers and domain owners clearly, but the cross-domain sign-off chain is inferred from links rather than read.
