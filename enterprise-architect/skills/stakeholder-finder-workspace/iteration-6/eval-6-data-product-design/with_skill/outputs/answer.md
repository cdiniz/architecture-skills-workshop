# Who should be in the room — regulatory risk-reporting data product design session

**Issue, in my words:** You're standing up a new data product for regulatory risk reporting and running a hands-on design session to nail three things — the **data model**, **how it's built**, and **how it's governed**.

**Meeting type I'm sizing for:** a **design / working session** — making and living with the technical decision, not a strategy or steering session. That biases the room toward the makers and the discipline ICs, and trims the "Head of / Chief" leadership off the top of each chain (they're represented by their stream, not in the room).

**Assumptions I'm making** (this run is non-interactive — these are what I'd have asked):
- The product is genuinely in the **risk / regulatory** domain (the brief says so), so I'm pulling in the Risk data architect and the regulatory-compliance lens rather than a generic data product.
- "How it's governed" means **data governance** (ownership, classification, lineage, regulatory definitions) **and** the **regulatory-compliance / audit** angle — for a regulator-facing product both matter, and they're distinct remits, so each gets a seat.
- It's a working session, so I keep the hands-on makers and drop the leadership layers above them to one represented voice per chain.

The three focuses map cleanly onto three distinct streams plus a compliance voice: **data model → Eva**, **how it's built → Sofia**, **how it's governed → Floor**, **regulator-facing review → Charlotte**.

## The room

| Stakeholder | Role | Stream | Why relevant | Score |
|-------------|------|--------|--------------|-------|
| Eva Timmermans | Data Architect — Risk | data-modelling | **Remit, exact match.** She is hands-on on the data model for **risk / regulatory** products specifically — "mapping regulatory reporting fields… making sure the model is correct and queryable." This is the "nail the data model" seat at design altitude. Her lead (Lotte) and Head (Anika) are the same modelling stream, one and two rungs up — represented by Eva for a working session. | 10/10 |
| Sofia Costa | Data Engineer — Platform | data-engineering | **Remit, "how it's built".** She's at the keyboard building and running the pipelines that populate data products — ingestion, transformation, data quality. The maker of the engineering stream; the right altitude for a design session. Her lead David is the same stream one rung up — represented by Sofia. | 9/10 |
| Floor van der Berg | Data Governance Lead | governance | **Remit, "how it's governed".** Owns data ownership, classification, lineage policy, and stewardship of **regulatory data definitions** — explicitly the governance voice a regulatory/risk data product has to satisfy. Distinct remit from modelling and engineering, so a separate seat. She's an IC-level lead, so altitude fits the working session. | 9/10 |
| Charlotte Dubois | Compliance Officer — Architecture | compliance | **Concern, regulator-facing.** Reviews architecture decisions for **regulatory compliance** and owns audit trails / exception handling — directly in play for a regulatory risk-reporting product. Distinct from Floor's data-governance remit (compliance/audit vs ownership/lineage). No reports, so right altitude for a design session; bring her in so the design is defensible to the regulator from the start. | 7/10 |

## Boundary notes

**Represented by their stream** (collapsed to one voice — reversible if you want them back):
- **Lotte Peters** (Lead Data Architect) and **Anika Sharma** (Head of Data Architecture) — same data-modelling chain as Eva (Anika → Lotte → Eva), same concern. Eva is the maker; she carries the modelling line. Pull Lotte in only if you want practice-level model-standards sign-off live in the room.
- **David Cohen** (Data Engineering Lead) — same data-engineering chain as Sofia (David → Sofia), same build-and-run concern. Sofia is the maker for a working session; David's "is this buildable and operable / what effort" lens is the same stream one rung up. Add David if the session needs to weigh build effort and operability decisions, not just do the work.

**Deliberately left out:**
- **Fatima El-Youssef** (Chief Data Officer) — too senior for a hands-on design session; she sets mandate, investment, and the regulatory-data-risk posture. She'd be the headline seat for a *strategy / steering* session on this, but here she's represented by her data office (Anika/Floor's streams).
- **Ahmed Benali** (Integration Architect) — relevant if/when the risk product needs to source data over the event backbone or expose APIs, but the brief is data model / build / govern, not integration patterns. Easy add the moment integration enters scope.
- **Carlos Mendes** (Cloud Architect) — relevant at platform/landing-zone build time, not for nailing the model and governance in this design session.
- **Payments people** (Bram Hendriks, Aisha Khan, Maria Oliveira, Jonas Bakker, Hannah Schulz) — different domain (payments), no stake in a risk-reporting data product.

**Referenced but not in the wiki** (named only as `[[wiki-links]]`, no entry — not scored; adding their entries would let me place them properly):
- **[[stakeholder-mark-van-dijk]]** — functional leader (dotted line) for the architecture discipline across data, integration, payments, and cloud. Likely the chief-architect-level escalation/standards owner; would matter for sign-off, not for a hands-on design session.
- **[[stakeholder-sanne-vermeulen]]** and **[[stakeholder-daan-verhoeven]]** — Charlotte's line manager and compliance functional leader; the regulatory-compliance escalation chain above her.
- **[[stakeholder-miguel-santos]]** and **[[stakeholder-yasmine-haddad]]** — managers in the integration / cloud lines; only relevant if those streams enter scope.

If you'd told me this was a **strategy / steering** session instead, the room would flip toward the leaders — Fatima (CDO) as the headline, with Anika and Floor representing their streams — rather than the makers above.
