# Who to talk to: Standardising cross-domain integration (API gateway + event backbone, retiring point-to-point batch)

Your proposal has three load-bearing parts: (1) a **managed API gateway**, (2) a **shared event backbone**, and (3) **retiring point-to-point batch interfaces**. Below are the stakeholders to engage, grouped by why they matter, drawn from the stakeholder profiles available.

## Start here — your natural sponsor and co-author

### Ahmed Benali — Integration Architect
**This is your single most important contact.** His remit is literally *"Designs integration patterns, governs API contracts, and drives adoption of the event backbone."* His recorded concerns are **point-to-point sprawl, inconsistent API contracts, and brittle batch interfaces** — and he already promotes **API-first contracts, event-driven integration, and a managed API gateway and event backbone.**

Your proposal is, almost word-for-word, Ahmed's agenda. Treat him as your co-author and primary ally. Get alignment with him before taking this anywhere else.
- Reports to: **Miguel Santos** (line manager)
- Functional leader: **Mark van Dijk**

## Decision-makers / sponsors to secure (escalation path)

These two sit above the integration architecture function and are the route to a mandate for a cross-domain standard.

### Mark van Dijk — Functional leader for architecture
He is the functional leader (dotted-line) for Ahmed Benali, Carlos Mendes, and Anika Sharma, and the line manager for the Payments Domain Architect (Bram Hendriks). He sits across the architecture community, so a cross-domain integration standard needs his backing. *(No standalone profile available — inferred from the relationship graph; confirm his exact title.)*

### Miguel Santos — Ahmed's line manager
Miguel is Ahmed's line manager and is the functional leader for the Payments domain architecture. He is a key sponsor for giving the integration standard organisational weight. *(No standalone profile available — inferred from relationships; confirm title.)*

## Domain owners whose interfaces you'll change

A cross-domain standard only works if the domains buy in. These are the people whose point-to-point batch interfaces you want to retire and who must adopt the gateway/backbone.

### Bram Hendriks — Domain Architect, Payments
High-priority stakeholder. He promotes a **unified payments platform, event-driven processing, and strong reconciliation patterns**, and explicitly cares about *"aligning payments modernization with core banking and integration standards."* He is a natural ally for the event backbone — but he'll scrutinise resilience under high transaction volumes and reconciliation when retiring batch interfaces. Engage early.

### Aisha Khan — Tribe Lead, Payments
Owns payments **delivery** (throughput, resilience, time-to-market) and has **legacy rail dependencies**. If batch interfaces feed payment processing, she owns the operational risk of changing them and the delivery roadmap to do so. Bring her in on sequencing and migration impact.

> Note: Payments is the only domain with profiles available. Other domains (e.g. lending, core banking) will have equivalent domain architects / tribe leads you should identify and engage the same way — the data here doesn't cover them.

## Data architecture — batch retirement is largely a data-flow change

### Anika Sharma — Head of Data Architecture
Important. Point-to-point batch interfaces are often **data pipelines**, and her concerns are exactly *"fragmented pipelines, inconsistent data models, and lack of lineage visibility."* She promotes **reusable data products and standardized models** — well aligned with your event backbone, but she'll want lineage, data contracts, and governance preserved as you move from batch to events. Co-design the event schemas / data contracts with her team.

## Cloud platform — where the gateway and backbone will run

### Carlos Mendes — Cloud Architect
A managed API gateway and an event backbone are platform capabilities that live in his **landing zones**. His concerns — **consistent network/security baselines, cost control, avoiding cloud sprawl** — apply directly to standing up shared gateway/backbone infrastructure. Engage him on hosting, IaC modules, and well-architected review.

## Governance & compliance — to make the standard stick (and pass audit)

### Charlotte Dubois — Compliance Officer, Architecture
Engage once the proposal firms up. Retiring established (batch) interfaces and mandating a new standard creates exactly what she watches for: **undocumented exceptions, gaps in audit trails, and divergence from approved standards.** She can help embed the new integration standard into the architecture review process so adoption is enforceable — and ensure batch-to-event migrations keep their audit trails (relevant for payments).

## Suggested sequence

1. **Ahmed Benali** — align on the proposal; make him co-owner.
2. **Mark van Dijk / Miguel Santos** — secure sponsorship and a mandate for a cross-domain standard.
3. **Bram Hendriks + Aisha Khan** — first domain (Payments); strongest natural allies and highest-risk interfaces.
4. **Anika Sharma** — data contracts, lineage, and pipeline/batch migration.
5. **Carlos Mendes** — platform hosting for gateway + backbone.
6. **Charlotte Dubois** — bake the standard and exception handling into governance.

## Caveats on the data
- Only six stakeholder profiles were available (Ahmed Benali, Aisha Khan, Anika Sharma, Bram Hendriks, Carlos Mendes, Charlotte Dubois).
- **Mark van Dijk** and **Miguel Santos** are referenced as leaders but have no profiles — their roles are inferred from the reporting graph; confirm titles before escalating.
- Domains other than Payments aren't represented in the data, but a cross-domain standard will need their architects/tribe leads too — identify them separately.
