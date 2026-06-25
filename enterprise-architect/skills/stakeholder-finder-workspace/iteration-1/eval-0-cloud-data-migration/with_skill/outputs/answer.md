# Who to talk to before committing to the analytics data-platform cloud migration

**The issue, in one line:** You're scoping a lift of the analytics data warehouse off on-prem and across clouds (AWS → Azure), and some of the data in scope is **customer financial data** — so this is simultaneously a data-architecture move, a cloud landing-zone move, and a regulated-data / cross-border-transfer question.

**Assumptions I'm making** (this run is non-interactive, so I'm stating these rather than asking):
- "Customer financial data" means **regulated, in-scope-for-the-regulator** data — which is why compliance and data architecture are pulled in, not just the infra teams. *(I'd otherwise have asked: is the in-scope data actually regulated/PII, or aggregated and de-identified?)*
- This is a **standalone migration**, not a workstream inside a named standing transformation programme. *(I'd have asked: is this part of a broader cloud or data-platform programme? If so, that programme's people would join the list.)*
- The data being moved is the **analytics warehouse**, not the payments/transactional systems — so I've weighted the payments-domain people lower (they're affected as data *sources/consumers*, not owners of the warehouse).

A note on coverage: the wiki currently holds **only six stakeholder entries**. Several clearly relevant roles are referenced as `[[wiki-links]]` (line managers and functional leaders) but have **no entry of their own** — I've flagged those as gaps at the end rather than invent attributes for them.

---

## Stakeholders to consult, highest relevance first

### Anika Sharma — Head of Data Architecture · relevance 9/10
**Remit + concern.** This is squarely hers: she "defines data architecture standards, governs pipelines and models, and ensures alignment with data governance and platform strategy." Moving the analytics warehouse is exactly the kind of decision she must shape and effectively sign off. Her stated concerns — fragmented pipelines, inconsistent models, lack of **lineage visibility**, and **scalability and performance of the data platform** — all bite directly on a cross-cloud warehouse migration. **Talk to her first**; align on target data model, lineage continuity across the move, and platform performance/SLOs on Azure.

### Charlotte Dubois — Compliance Officer, Architecture · relevance 9/10
**Concern + remit (sign-off).** Because customer financial data is in scope, she's central, not advisory. She "reviews architecture decisions for regulatory compliance and ensures audit trails and exception handling are maintained," and worries about "undocumented exceptions" and "gaps in audit trails." A cross-cloud, on-prem-to-cloud move of regulated data raises data-residency, cross-border-transfer, and audit-trail questions she needs to bless **before** you commit. Ask her: what's the compliance position on hosting this data class in Azure, and what must be evidenced for the regulator/auditors.

### Carlos Mendes — Cloud Architect · relevance 8/10
**Remit.** The Azure destination is his territory: he "designs and governs cloud landing zones, IaC modules, and well-architected reviews across workloads." The warehouse needs to land in a compliant Azure landing zone with the right network/security baseline. His concerns — consistent security baselines, cost control, avoiding cloud sprawl — are exactly the ones an unplanned cross-cloud move trips over. Align on: target landing-zone blueprint, the well-architected review, and the AWS→Azure cost/egress picture.

### Ahmed Benali — Integration Architect · relevance 6/10
**Remit (data movement) + concern.** The warehouse doesn't move in isolation — its **feeds and consumers** do. Ahmed "designs integration patterns, governs API contracts, and drives adoption of the event backbone," and explicitly worries about "brittle batch interfaces" and "point-to-point sprawl." The pipelines feeding the warehouse and the downstream extracts are his contracts to keep intact across the move. Consult him on how ingestion and downstream integrations re-point to Azure without breaking.

### Bram Hendriks — Domain Architect, Payments · relevance 5/10
**Structural + concern (data owner).** Relevant if the "customer financial data" originates from or feeds the **payments domain** — likely, given that's where customer financial data lives. He owns payments architecture, governs "regulatory and resilience requirements," and cares about regulatory change and reconciliation. He's a **data-source/consumer stakeholder and a regulatory voice**, not an owner of the warehouse migration. Consult him to confirm which payments data is in scope and any reconciliation/residency constraints on it.

### Aisha Khan — Tribe Lead, Payments · relevance 4/10 (borderline — include only if payments data is in scope)
**Structural.** As delivery lead for payments, she'd care if her tribe's data is moving and there's a delivery/operational impact, and her remit explicitly includes "regulatory standards" and "regulatory deadlines." But she's a step removed from a warehouse migration she doesn't own. Loop her in for **awareness and timing** if payments-sourced data is confirmed in scope; otherwise omit.

---

## Deliberately left out (so the boundary is legible)

- **The line managers / functional leaders referenced but not in the wiki** — e.g. Anika's manager **Fatima el-Youssef**, the functional leader **Mark van Dijk** (architecture), Carlos's manager **Yasmine Haddad** (cloud), and Charlotte's chain **Sanne Vermeulen / Daan Verhoeven** (compliance/governance). On a regulated cross-cloud migration, the **governance / risk escalation chain** (Daan Verhoeven looks like the functional head of compliance, and Mark van Dijk the architecture leadership) is normally exactly who you'd want for sign-off — but **none of them has a stakeholder entry**, so I can't responsibly characterise their remit. **This is a real gap: the people most likely to hold formal escalation/sign-off authority aren't in the wiki yet.** Recommend creating entries for them and revisiting.

- **A dedicated Security / InfoSec architect and a Data Privacy / DPO role** — a regulated-data, cross-border cloud move would normally pull these in, but **no one in the repo holds those roles**. Carlos (security baselines) and Charlotte (regulatory/audit) partially cover the ground; the residual security-engineering and privacy-specific angles are uncovered.

**Start with Anika, Charlotte, and Carlos** — data architecture, compliance, and the Azure target — before you commit. Confirm the regulated-data scope with Bram, and the pipeline/integration impact with Ahmed.
