# Who to talk to: standardising cross-domain integration (managed API gateway + shared event backbone, retiring point-to-point batch)

**The issue, in one line:** You want to standardise how domains integrate by introducing a managed API gateway and a shared event backbone as the org-wide pattern, and decommission a sprawl of point-to-point batch interfaces — a cross-cutting integration-architecture decision with adoption, governance, and per-domain migration implications.

**Assumptions I'm making** (this run is non-interactive, so I'm stating rather than asking). I'd normally have asked: (1) *Which domains' batch interfaces are in scope first?* — I'm assuming this is org-wide standardisation, with Payments as a likely early/high-impact domain given its volume and rail dependencies; (2) *Does the data flowing over these interfaces include regulated/customer data and is the change in scope of compliance/audit sign-off?* — I'm assuming yes, since cross-domain integration in a bank typically carries regulated data and an architecture decision of this size needs a compliance review; (3) *Is this a standing transformation/standards initiative or a one-off?* — I'm treating it as a standards-setting initiative, which pulls in the functional architecture leadership chain. If any of these is wrong, redirect me and the shortlist shifts.

---

### Ahmed Benali — Integration Architect · relevance 10/10
He **owns** this exactly. His remit is literally "designs integration patterns, governs API contracts, and drives adoption of the event backbone," and his stated concerns are "point-to-point sprawl, inconsistent API contracts, and brittle batch interfaces" — he already "promotes API-first contracts, event-driven integration, and a managed API gateway and event backbone." This is his proposal's natural home on all three axes (remit, concern, structural). He should lead the design and be your first conversation; align on the target pattern, the gateway/backbone reference architecture, and the batch-retirement sequencing.

### Anika Sharma — Head of Data Architecture · relevance 8/10
Retiring point-to-point batch interfaces hits her **remit and concerns** directly. Many batch interfaces *are* data pipelines; her concerns are "fragmented pipelines, inconsistent data models, and lack of lineage visibility," and she "promotes reusable data products and standardized models." Moving from batch to an event backbone changes how data flows, lineage, and models are governed across domains — she governs that. Align on how the event backbone carries data products, lineage/governance over event streams, and which batch data flows convert versus stay. She also functionally connects to a wide data-engineering group, so she's a route to the people who actually build the affected pipelines.

### Bram Hendriks — Domain Architect, Payments · relevance 8/10
Payments is where this standardisation will bite hardest, and he owns its architecture. His remit governs "payment processing patterns," and his concerns include "fragmented payment rails" and "aligning payments modernization with core banking and **integration standards**" — he already "promotes ... event-driven processing." He's both a strong adopter and a domain whose batch interfaces (reconciliation, rails) need careful, resilience-aware migration. Use him as the proving-ground domain architect; align on which payments batch interfaces can move to events without breaking reconciliation and high-volume resilience.

### Aisha Khan — Tribe Lead, Payments · relevance 6/10
Structural/delivery axis. She doesn't own integration standards, but her tribe builds and runs the payments systems whose batch interfaces you want to retire, and her concerns are "throughput, resilience, and time-to-market" plus "legacy rail dependencies and the operational risk of high-volume processing." Retiring batch interfaces is delivery work and operational risk her tribe absorbs. Consult her on migration sequencing, cutover risk, and roadmap capacity — she's where the change lands operationally even though the decision isn't hers.

### Charlotte Dubois — Compliance Officer, Architecture · relevance 6/10
Concern/governance axis. A cross-domain change to how data moves between systems, plus decommissioning interfaces, is exactly the kind of decision she screens: her concerns are "undocumented exceptions, gaps in audit trails, and divergence from approved standards," and she "embeds compliance checks into the architecture review process." Bring her in early so the gateway/backbone pattern and the batch-retirement plan carry the audit trail and approvals — and so the new standard becomes the approved baseline rather than an exception. (Weight this higher if regulated/customer data flows over the interfaces, per my assumption above.)

---

### Deliberately left out
- **Carlos Mendes — Cloud Architect.** Relevant at *build/run* time — a managed gateway and event backbone will need landing zones, network/security baselines, and IaC, which is his remit. But that's an implementation concern that follows the decision, not an input to *whether/how* to standardise. Pull him in once the pattern is agreed; he's not needed to scope the decision itself.

### Referenced but not in the wiki (no entry — not scored)
These names appear only as `[[wiki-links]]` in the entries above. They look structurally important (this is where the sign-off / escalation chain lives), but I can't read their remit or concerns, so I won't score them. Adding their entries would let me place them properly.
- **Mark van Dijk** — functional (dotted-line) leader for the Integration, Data, and Cloud architects (Ahmed, Anika, Carlos), and line manager of Bram. Looks like the head of the architecture function — the most likely owner of cross-domain architecture *standards* and therefore a probable sign-off for making this the org-wide pattern. **Highest-priority gap to fill.**
- **Miguel Santos** — Ahmed's line manager and functional leader for the Payments domain architect (Bram). Plausibly head of integration/architecture delivery; likely matters for resourcing and mandating adoption.
- **Daan Verhoeven** — Charlotte's functional leader (compliance/governance). Probable escalation point if the new standard needs formal governance/compliance endorsement.
- **Jeroen Meijer** — Aisha's line manager (Payments delivery leadership); relevant for delivery capacity and roadmap trade-offs if Payments is the pilot domain.
- Others linked but more peripheral here: *Fatima el-Youssef, Yasmine Haddad, Sanne Vermeulen* (managers up the chains), and the data-engineering functional reports under Anika (*Lotte Peters, David Cohen, Eva Timmermans, Robin Janssen, Floor van der Berg*) who'd be the hands-on builders if specific batch pipelines are converted.

**Gap in the roster worth flagging:** no one in the wiki holds an explicit *enterprise/security or platform-operations* remit for an API gateway as a runtime platform (auth, rate-limiting, runtime ownership). If that role exists, it belongs in this conversation; if it doesn't, that's a real ownership gap for a managed gateway.
