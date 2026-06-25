# Who should be in the room — Payments platform modernisation (steering / strategy)

**Read of the issue:** A steering session to set the **multi-year strategy** and the **investment case** for modernising the payments platform. This is a **strategic / steering session** — direction, mandate, budget and sign-off — so I'm biasing the room toward senior leaders and one voice per stream, not the working-level makers.

**Room-breadth mode used: INCLUSIVE (feasibility-aware).** The framing explicitly carries an *investment case* ("what will it cost / can we actually deliver this"), not just direction-setting. Per the skill, an investment-case signal leans inclusive, so I keep a delivery-feasibility second voice (the Payments Tribe Lead) in the room alongside the domain architect, rather than collapsing her fully. If you actually want a **tight leadership-only** room (direction and money only), drop Aisha Khan — Bram Hendriks would then carry the payments line — and that's a one-line change.

**Assumptions I made (and what I'd otherwise have asked):**
- I'd normally check the **meeting type** — here the wording ("steering session", "set the multi-year strategy and the investment case") makes it unambiguously strategic, so I inferred it rather than asking.
- I'd ask **tight vs inclusive room**; I inferred inclusive from the investment-case wording (see above).
- I assumed regulatory exposure is in scope (PSD2 / instant payments are inherent to a payments platform), which keeps a compliance voice on the longlist — though at strategy altitude she is borderline (see "Deliberately left out").
- Note on data quality: only **6** people have actual stakeholder entries. Several of the most senior, sign-off-level people for a session like this exist **only as wiki-links with no entry** — they're the part of the room I can flag but not score (see "Referenced but not in the wiki"). That gap matters most precisely for a steering session.

## Recommended room

| Stakeholder | Role | Why relevant | Score |
|-------------|------|--------------|-------|
| Bram Hendriks | Domain Architect — Payments | **Remit + concern, dead centre.** Owns payments architecture standards and explicitly promotes "a unified payments platform" while managing "fragmented payment rails, regulatory change (PSD2, instant payments), and resilience under high transaction volumes" — this strategy *is* his remit. At strategy altitude he is the single architectural voice for the payments line and represents the tribe/working level below him. Align on: target-state architecture and the multi-year sequencing that underpins the investment case. | 9/10 |
| Aisha Khan | Tribe Lead — Payments | **Structural + delivery-feasibility voice (inclusive mode).** Her remit aligns the tribe roadmap "with the unified payments platform strategy" and she owns "throughput, resilience, time-to-market… legacy rail dependencies." Kept in because the investment case needs a "can we actually build this, and at what cost / over what horizon" voice that the domain architect can't fully stand in for. In a tight room she'd be *represented by* Bram. Align on: delivery feasibility, team capacity, and cost/effort to migrate off legacy rails. | 7/10 |
| Ahmed Benali | Integration Architect | **Concern overlap, strategy-relevant.** Payments modernisation hinges on the event backbone and API contracts he governs; his stated concerns (point-to-point sprawl, brittle batch interfaces, API-first and event-driven integration) are load-bearing for the target platform. He's a discipline voice rather than a leader, so borderline for a steering room — include him as the integration-strategy input if the platform's integration backbone is a strategic pillar; otherwise his functional leader (Miguel Santos) would represent the integration line. | 6/10 |

## Boundary notes

**Deliberately left out (profiled, not ranked):**
- **Anika Sharma (Head of Data Architecture)** — relevant if data products / reconciliation data are a strategic pillar, but the payments strategy as framed is platform/rails/integration-led; she'd be consulted, not core, and is better pulled in once data is named as a workstream. Surface her if the investment case includes a data-platform component.
- **Carlos Mendes (Cloud Architect)** — cloud landing zones and cost control matter at *build* time; for a direction-and-investment steering session he is too working-level and is represented by his manager (Yasmine Haddad) if cloud spend is a strategic line item.
- **Charlotte Dubois (Compliance Officer — Architecture)** — payments is regulation-heavy (PSD2, instant payments), so compliance has a genuine stake, but her remit is reviewing *decisions* and audit trails, which is an execution-altitude concern. For a strategy session the regulatory mandate is better carried by the compliance *leadership* line (Daan Verhoeven / Sanne Vermeulen, neither profiled). Bring Charlotte in once the strategy turns into specific decisions to review.

**Represented by their stream:**
- The working-level payments engineers **Maria Oliveira** and **Jonas Bakker** (wiki-links under Aisha) are represented by Aisha Khan / Bram Hendriks — no makers in a steering room.
- In **tight** mode, **Aisha Khan** is represented by **Bram Hendriks** (one voice for the payments line). I kept her in because of the inclusive/investment-case framing.

**Referenced but not in the wiki (no entry — cannot score; this is the gap that matters most for a steering session):**
- **[[stakeholder-mark-van-dijk]]** — functional leader of the architecture discipline (line manager of Bram; functional leader of Ahmed, Anika, Carlos). Almost certainly the **most senior architecture sign-off** for a multi-year platform strategy. For a steering session this is likely *the* person who should chair or sponsor. Add their entry to place them properly.
- **[[stakeholder-miguel-santos]]** — functional leader for the integration/payments-architecture line (Bram's functional leader; Ahmed's line manager). Plausible owner of the architecture mandate and a key sign-off voice. Unscored only because there's no entry.
- **[[stakeholder-jeroen-meijer]]** — Aisha's line manager, i.e. the **delivery/tribe leadership** above the payments tribe. The natural owner of the *delivery* side of the investment case (capacity, funding of teams). Strong steering-room candidate once profiled.
- **[[stakeholder-yasmine-haddad]]** — Carlos's manager, likely Head of Cloud/Platform; relevant if cloud/platform spend is a strategic pillar of the investment case.
- **[[stakeholder-daan-verhoeven]]** / **[[stakeholder-sanne-vermeulen]]** — the compliance leadership chain above Charlotte; the right altitude to carry the regulatory mandate into a strategy room (vs. Charlotte at execution level).
- **[[stakeholder-fatima-el-youssef]]** — Anika's manager; relevant only if data becomes a named strategic workstream.

**Biggest caveat:** the people who most belong in a *steering / investment* room — the architecture, delivery and compliance **leaders who hold mandate and budget** — are exactly the ones with no wiki entry. The profiled six are mostly discipline/working altitude. I'd recommend creating entries for at least **Mark van Dijk, Jeroen Meijer and Miguel Santos** and re-running, since for a strategy session they likely outrank everyone scored above.
