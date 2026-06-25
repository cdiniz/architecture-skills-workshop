# Who to talk to before committing to the analytics data platform cloud migration

**The issue, in one line:** You're moving the analytics **data warehouse** off on-prem into the cloud — a **cloud-to-cloud re-platforming (AWS → Azure)** — and **customer financial data** is in scope, which makes this both a data-architecture decision and a regulatory/compliance one.

**Assumptions I'm making** (non-interactive run — normally I'd confirm these with you first):
- **Regulated, customer financial data is in scope** → this firmly pulls in data architecture and compliance. (Would have asked: exactly which datasets / what residency or cross-border constraints apply?)
- This is an **analytics / data-warehouse** migration, not a payments or core-banking system move, so I'm weighting the data-platform people above the payments-domain people. (Would have asked: is this a one-off or part of a standing transformation/cloud programme, and does any payments data flow through this warehouse?)
- "AWS to Azure" means you already have a cloud footprint and this is a **target-platform change**, so cloud landing-zone and security baselines matter at design time but aren't the gating sign-off for the *decision*. (Would have asked: is the AWS→Azure direction already mandated, or still open?)

---

## Stakeholders to consult, highest relevance first

### Anika Sharma — Head of Data Architecture · relevance 9/10
Central on **remit**: she "defines data architecture standards, governs pipelines and models, and ensures alignment with data governance and platform strategy" — an analytics data-warehouse migration sits squarely inside that accountability. Her stated concerns (fragmented pipelines, inconsistent models, lineage visibility, and "scalability and performance of the data platform") are exactly the risks a warehouse re-platform creates. This decision should not proceed without her sign-off. Ask her: target data model and lineage strategy on Azure, and how governance is preserved through the cut-over.

### Charlotte Dubois — Compliance Officer, Architecture · relevance 8/10
Strong on **concern** and effectively a sign-off gate given customer financial data is moving. Her remit is to "review architecture decisions for regulatory compliance and ensure audit trails and exception handling are maintained," and her concerns are "gaps in audit trails" and "divergence from approved standards." Moving regulated customer financial data between clouds raises data-residency, cross-border-transfer, and audit-trail questions you want surfaced *before* you commit, not after. Ask her: residency/cross-border constraints on this data and what compliance evidence the decision needs.

### Carlos Mendes — Cloud Architect · relevance 7/10
Relevant on **remit** for the *how* and *where*: he "designs and governs cloud landing zones, IaC modules, and well-architected reviews across workloads," and worries about "consistent network and security baselines" and cost control. Since the target is Azure, the warehouse must land inside a compliant landing zone with the right security baseline — and his cost-control lens matters for a warehouse's storage/compute footprint. He's more design-time than decision-gating, but consult him early so the AWS→Azure target is feasible and not a sprawl/cost surprise. Ask him: is there an approved Azure landing zone for regulated data, and what the security baseline requires.

### Ahmed Benali — Integration Architect · relevance 6/10
Relevant on **remit/concern**: he "designs integration patterns" and his concerns include "brittle batch interfaces" and "point-to-point sprawl." A warehouse rarely moves alone — the pipelines, feeds, and downstream consumers that read from it have to be re-pointed at Azure. He'll care about how data flows in and out during and after the migration. Consult him on the integration/feed re-wiring and any event-backbone implications, especially to avoid a brittle batch cut-over.

---

## Boundary notes

### Deliberately left out
- **Aisha Khan (Tribe Lead — Payments)** and **Bram Hendriks (Domain Architect — Payments)** — both are squarely payments-domain. Under my assumption that this is an *analytics* warehouse migration and not a payments-system move, they're not core. **Reconsider them if** payments transaction data flows through this warehouse or if the regulated "customer financial data" originates in the payments domain — in that case Bram (architecture standards, regulatory/resilience) would jump to a consult and Aisha to an awareness contact.

### Referenced but not in the wiki (no entry — not scored)
These names appear only as `[[wiki-links]]` in the entries above, so I can place them structurally but can't assess their remit/concerns. They're likely where escalation and sign-off live — adding their entries and re-running would let me rank them properly:
- **[[stakeholder-mark-van-dijk]]** — the recurring **functional leader (dotted line)** above Anika, Ahmed, Carlos and the payments domain architect. Looks like the lead architect / architecture function head — a probable escalation and standards-sign-off point for a cross-cutting platform decision like this.
- **[[stakeholder-fatima-el-youssef]]** — Anika's **line manager** (and a functional report of hers). Sits in the data leadership chain above Head of Data Architecture; plausible budget/strategy owner for the data platform.
- **[[stakeholder-sanne-vermeulen]]** and **[[stakeholder-daan-verhoeven]]** — Charlotte's **line manager** and **functional leader** respectively. The compliance/governance escalation chain — relevant if the regulated-data aspect needs formal compliance sign-off above Charlotte.
- **[[stakeholder-yasmine-haddad]]** — Carlos's **line manager**; likely cloud/platform leadership, a possible owner of the AWS→Azure direction itself.
- **[[stakeholder-lotte-peters]]** — Anika's **direct report**; potentially a hands-on data architect who'd do the detailed migration design work, but unscored without an entry.

*If you can confirm whether payments data is in scope and whether this migration is part of a standing programme, I can tighten this list — particularly whether the payments architects and any programme sponsor belong in the room.*
