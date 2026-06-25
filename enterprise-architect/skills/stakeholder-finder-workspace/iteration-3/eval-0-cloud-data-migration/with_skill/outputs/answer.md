# Who to talk to before committing to the analytics data-platform cloud migration

**The issue, in my words:** You're scoping a migration of the analytics data platform off on-prem into the cloud — moving the data warehouse from AWS to Azure — and some of the data in scope is **customer financial data**. You want to know whose input or sign-off you need *before committing*.

**Meeting type I'm sizing the room for:** a **strategic / steering scoping conversation** — a "do we commit, and on what conditions" decision-point, not yet the technical design session. "Before we commit" tells me you want the people who set direction, own the relevant standards, and hold sign-off — especially where regulated customer data and a cloud-provider change raise compliance and architecture-governance questions. I'm therefore biasing toward discipline leads and owners of standards, not hands-on engineers.

**Assumptions I'm making (and what I'd otherwise have asked):**
- **Regulated/customer financial data is in scope** — you said so, so compliance and data architecture are firmly pulled in.
- **This is a decision-to-commit, not the build.** If you actually meant a technical design session, the roster shifts toward the hands-on cloud/data/integration architects (see "Deliberately left out") — I'd have asked which.
- **It's the analytics warehouse moving, not the payments or core transactional estate.** I'd have asked which domain's systems are affected; the payments people are included only at the awareness/concern altitude, not as owners.
- **It's a standalone scoping effort** unless it sits under a wider transformation programme — I'd have asked, because a programme would pull in its sponsor and leads.

A note on the data: only **6 people** have full stakeholder entries I can actually assess. Several structurally important people (functional leaders, the escalation/sign-off chain) appear only as wiki-links with no entry — I've surfaced them, unscored, in the boundary notes, because for a "before we commit" decision they're often exactly the altitude you need.

---

## Stakeholders to consult, highest relevance first

### Anika Sharma — Head of Data Architecture · relevance 9/10
**Remit + concern.** This migration *is* her remit: she "defines data architecture standards, governs pipelines and models, and ensures alignment with data governance and platform strategy," and explicitly owns "scalability and performance of the data platform." Moving the analytics warehouse to a different cloud is a platform-strategy and data-governance decision that sits squarely with her — and her stated concern about "lack of lineage visibility" is exactly what's at risk when customer financial data crosses platforms. She's at the right altitude for a commit decision (a "Head of"). **Align with her on:** target-state data architecture on Azure, lineage/governance continuity for the financial data, and whether the move fits the platform strategy.

### Charlotte Dubois — Compliance Officer, Architecture · relevance 9/10
**Concern + remit.** Customer financial data plus a change of cloud provider is precisely her territory: she "reviews architecture decisions for regulatory compliance and ensures audit trails and exception handling are maintained," and worries about "undocumented exceptions" and "divergence from approved standards." A cross-cloud migration of regulated data is the kind of decision that needs a compliance read *before* commitment, not after. **Align with her on:** data residency / cross-border transfer, regulatory approval, and getting the decision and any exceptions documented for audit.

### Carlos Mendes — Cloud Architect · relevance 7/10
**Remit + concern.** He "designs and governs cloud landing zones, IaC modules, and well-architected reviews across workloads" — an AWS-to-Azure move lands directly on the landing-zone and security-baseline work he owns, and his concerns (cost control, "consistent network and security baselines," avoiding cloud sprawl) are first-order questions for whether this commitment is sound. He's more hands-on than the others here, so for a pure steering conversation he's slightly below the leads — but a cloud *provider switch* genuinely hinges on his expertise, so he belongs in this room. **Align with him on:** Azure landing-zone readiness, security baseline for financial data, and a realistic cost/effort read to inform the commit.

### Ahmed Benali — Integration Architect · relevance 6/10
**Remit + concern.** An analytics warehouse rarely moves alone — the pipelines and interfaces feeding it have to follow. Ahmed "designs integration patterns, governs API contracts," and worries about "brittle batch interfaces" and "point-to-point sprawl," which is exactly the integration risk a warehouse migration exposes. Consult him to pressure-test feasibility and scope the integration impact before you commit; he's not the decision owner. **Align with him on:** which feeds/contracts break or need rework, and the migration sequencing implications.

### Bram Hendriks — Domain Architect, Payments · relevance 5/10
**Concern (awareness).** Included only because you flagged **customer financial data**: if any of that originates from or reconciles against the payments domain, Bram — who owns payments architecture and worries about "regulatory change" and "strong reconciliation patterns" — has a stake in how that data is handled and where it lands. He's a should-be-aware consultee, not an owner, and only if payments data is actually in scope. **Ask him:** whether any in-scope financial data touches payments, and any reconciliation/regulatory constraints that follow it.

---

## Boundary notes

**Deliberately left out**
- **Aisha Khan (Tribe Lead — Payments)** — payments *delivery*, one altitude below Bram and focused on throughput/time-to-market. For a commit-level decision the payments concern is represented by Bram; she'd matter at delivery-planning time, not now. (See also "represented by their stream".)
- **The hands-on / design-session crowd in general** — if this were the technical *design* session rather than a commit decision, Carlos and Ahmed would rise to the top and you'd add the working-level data/cloud engineers. At "should we commit" altitude they're consulted for feasibility, not running the room.

**Represented by their stream**
- **Aisha Khan is represented by Bram Hendriks** for the payments line in this strategic conversation — same functional chain (Aisha's functional leader is Bram), and Bram speaks to the architecture/regulatory concern at the right altitude. Pull Aisha in directly only if delivery sequencing of payments-owned data becomes the topic.

**Referenced but not in the wiki (no entry — unscored, but likely the sign-off / escalation chain you'll need for a commit)**
- **Mark van Dijk** — functional (dotted-line) leader of Anika, Carlos, Ahmed *and* Bram; he's the architecture-discipline leader the whole technical roster rolls up to. For a "before we commit" decision he's very plausibly the architecture sign-off / escalation point. No entry exists, so I can't assess his remit or score him — **add his entry and I can place him properly.**
- **Daan Verhoeven** — Charlotte's functional (dotted-line) leader; likely the head of the compliance/governance discipline, i.e. where compliance sign-off escalates. Same caveat — no entry to assess.
- **Fatima el-Youssef** — Anika's line manager (and, interestingly, a functional report of Anika's), sitting in the data leadership chain; a candidate budget/direction owner for the data platform.
- **Yasmine Haddad** — Carlos's line manager, in the cloud/infrastructure leadership chain; plausibly owns the cloud-platform direction and cost envelope a provider switch commits you to.
- **Sanne Vermeulen** — Charlotte's line manager, in the compliance reporting chain.

For a genuine commit decision, the sign-off altitude almost certainly lives in **Mark van Dijk** (architecture) and **Daan Verhoeven** (compliance), with **Yasmine Haddad** / **Fatima el-Youssef** as the likely platform/budget owners. I've kept them unscored because their remits aren't recorded — **creating their entries and re-running would let me tell you which of them actually holds the pen.**
