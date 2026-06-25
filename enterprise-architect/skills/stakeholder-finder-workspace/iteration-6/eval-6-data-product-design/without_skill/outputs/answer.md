# Who should be in the room — Regulatory Risk-Reporting Data Product design session

This is a **hands-on design session** with three explicit dimensions: the **data model**, **how it's built**, and **how it's governed**. The right room is small and made of the people who actually do the work in each stream — one voice per stream — plus the governance and regulatory-fit voices the design must satisfy. Avoid filling the room with the management chain above each maker; bring the practice lead *or* the maker, not the whole ladder.

## Core attendees (the working room)

| Person | Role | Why they're in the room |
|---|---|---|
| **Eva Timmermans** | Data Architect — Risk | The **maker of the data model** for this exact product. She does the hands-on modelling of risk data definitions and regulatory reporting fields. This session is, at its core, her design work. |
| **Lotte Peters** | Lead Data Architect | Owns the **canonical model and modelling standards** and reviews Eva's designs. Ensures the risk-reporting model fits the canonical model rather than diverging. The practice-lead voice on the data-model stream. |
| **Sofia Costa** | Data Engineer — Platform | The **maker on the build stream** — hands-on pipelines, ingestion, transformation, data-quality at ingest. "How it's built" is her keyboard. |
| **David Cohen** | Data Engineering Lead | Owns **build-and-run**: pipeline reliability, platform scaling/cost, buildability and operability. Answers whether the design can actually be stood up and run. The build-stream lead voice. |
| **Floor van der Berg** | Data Governance Lead | The **governance voice the design must satisfy** — data ownership, classification, lineage policy, and stewardship of regulatory data definitions. "How it's governed" is her remit. |
| **Charlotte Dubois** | Compliance Officer — Architecture | Because this is **regulatory** reporting: she ensures the design meets regulatory/internal compliance, with audit trails and documented exceptions. Keeps the regulatory-fit requirement honest at design time. |

## Notes on the two streams that have a lead + a maker

For both the **data model** and the **build** streams, I've included both the maker and the lead because a hands-on design session benefits from the person at the keyboard *and* the person who owns the standards/operability they must conform to:

- **Data model:** Eva (maker) + Lotte (standards/review).
- **Build:** Sofia (maker) + David (operability/lead).

If the room must be kept tight to one voice per stream, drop to **Eva** and **David** plus **Floor** and **Charlotte** — but for a genuine working design session, having the makers (Eva, Sofia) present is the point.

## Optional — bring in only if scope demands

| Person | Role | When to pull them in |
|---|---|---|
| **Anika Sharma** | Head of Data Architecture | If the product sets a new pattern/standard or there's cross-tribe reuse to enforce. Otherwise she's represented by Lotte and Floor and is above the altitude of a hands-on session. |
| **Ahmed Benali** | Integration Architect | If the build needs source-system integration / event-backbone or API contracts to feed the product. Pull in for the ingestion-design portion only. |

## Deliberately NOT in the room

- **Fatima El-Youssef (CDO)** — board/portfolio altitude. She sets mandate and answers to regulators, but does not shape individual data models. Wrong altitude for a hands-on design session; brief her on the outcome instead.
- **Payments people (Aisha Khan, Bram Hendriks, etc.)** — wrong domain. This is a risk/regulatory data product, not payments.
- **Carlos Mendes (Cloud Architect)** — only if the product needs a new landing zone / infra design; not a default for a data-model-and-governance session.

## One-line summary

Core room: **Eva Timmermans** + **Lotte Peters** (data model), **Sofia Costa** + **David Cohen** (how it's built), **Floor van der Berg** (governance), and **Charlotte Dubois** (regulatory compliance). Keep the CDO and other domains out of the working session and brief them on the outcome.
