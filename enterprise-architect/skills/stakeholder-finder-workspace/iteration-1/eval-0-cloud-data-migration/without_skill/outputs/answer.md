# Who to talk to before committing to the analytics data platform cloud migration

You're scoping a migration of the analytics data platform from on-prem to cloud, moving the data warehouse from AWS to Azure, and some of the data is customer financial data. That combination touches **data architecture, cloud landing zones, and regulatory compliance** most directly, with integration as a secondary concern.

Based on the stakeholder profiles available, here is who you should engage and why.

## Talk to first (core decision-makers)

### Anika Sharma — Head of Data Architecture
**Why she's essential:** This is her platform. She defines data architecture standards, governs pipelines and data models, and owns alignment with data governance and platform strategy. A warehouse migration goes to the heart of her remit.
- Her stated concerns map directly to migration risk: **fragmented pipelines, inconsistent data models, lack of lineage visibility, and the scalability/performance of the data platform.**
- She promotes reusable data products and standardized models and enforces governance with the tribes — so any re-platforming needs her buy-in to avoid creating new fragmentation.
- **Engage her on:** target data architecture on Azure, pipeline/lineage continuity through the migration, performance and scalability of the new warehouse, and governance.

### Carlos Mendes — Cloud Architect
**Why he's essential:** He designs and governs cloud landing zones, IaC modules, and well-architected reviews across workloads. Any move to Azure runs through him.
- His concerns are squarely relevant: **cost control, consistent network and security baselines, and avoiding cloud sprawl.**
- He'll want this done via reusable landing-zone blueprints and IaC, and put through a well-architected review before commitment.
- **Engage him on:** the Azure landing zone, network/security baseline for the warehouse, cost model (an AWS-to-Azure change has real cost and egress implications), and the well-architected review gate.

### Charlotte Dubois — Compliance Officer (Architecture)
**Why she's essential:** Customer financial data plus a change of cloud provider raises regulatory, data-residency, and audit questions. She reviews architecture decisions for regulatory compliance and ensures audit trails and exception handling are maintained.
- Her concerns are exactly the failure modes here: **undocumented exceptions, gaps in audit trails, and divergence from approved standards.**
- She embeds compliance checks into the architecture review process, so engaging her early keeps the decision auditable rather than retrofitting compliance later.
- **Engage her on:** regulatory treatment of customer financial data, data residency/sovereignty on Azure, audit trail continuity, and whether this needs a documented exception or sign-off.

## Talk to as a secondary stakeholder

### Ahmed Benali — Integration Architect
**Why he's relevant:** He governs integration patterns, API contracts, and the event backbone. The analytics platform almost certainly ingests from upstream systems, so re-pointing those feeds during the migration is integration work.
- His concerns — **point-to-point sprawl, inconsistent API contracts, and brittle batch interfaces** — are real risks when source feeds get re-wired to a new warehouse.
- **Engage him on:** how data lands in the warehouse, batch vs. event-driven ingestion, and keeping contracts stable through the cut-over.

## Worth noting / likely follow-ups

- **Anika reports to Fatima El-Youssef** and **Carlos reports to Yasmine Haddad** (and both have **Mark van Dijk** as functional/architecture leader). These leaders are referenced as Anika's and Carlos's managers but do not have profiles in the available data. Given the scope and the financial-data risk, **funding and final sign-off will likely sit at that leadership level**, so plan to escalate to them (via Anika and Carlos) once the technical and compliance shape is agreed.
- **Charlotte reports to Sanne Vermeulen** (governance) with **Daan Verhoeven** as functional leader. If a formal compliance exception or governance ruling is needed, expect Charlotte to route it upward there.
- The **Payments stakeholders (Aisha Khan, Bram Hendriks)** in the data set are not directly relevant unless the analytics platform consumes payments data specifically; if customer financial data includes payments/transaction data, loop Bram in on the data-source and regulatory side.

## Suggested sequence
1. **Anika + Carlos** together — agree the target data architecture and Azure landing-zone shape, and trigger a well-architected review.
2. **Charlotte** — early, to confirm regulatory/residency/audit constraints on customer financial data before the design hardens.
3. **Ahmed** — on ingestion and integration impact.
4. **Escalate to the architecture/owning leadership (Mark van Dijk, plus Fatima/Yasmine)** for the commit decision once technical feasibility and compliance are confirmed.

> Note: This analysis is drawn from the six stakeholder profiles available in the data set. Several referenced leaders (Mark van Dijk, Fatima El-Youssef, Yasmine Haddad, Sanne Vermeulen, Daan Verhoeven) do not have their own profiles, so their specific concerns are inferred from their roles only.
