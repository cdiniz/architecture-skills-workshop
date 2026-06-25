# Who should be in the room — Payments platform modernisation: strategy + investment case

**Issue, as I read it:** A steering session to set the **multi-year strategy** for modernising the payments platform **and** make the **investment case** for it. This is a **strategic / steering session** — about direction, mandate, budget, and sign-off, not technical design or delivery planning.

**Room-breadth call (inclusive):** A pure "set the strategy" steering session leans *tight* (leadership-only — the most senior person in each line represents their reports). But you've explicitly added **"the investment case for modernising."** That is a deliverability-and-cost question, so I'm using the **inclusive** mode: I keep one delivery-feasibility voice in the room — the person who can answer "can we actually build this, and what will it cost / how long" — even though it sits in the same line as the payments architect. If you actually want a tight leadership-only room, say so and I'll drop that voice to "represented by" (it's a one-line switch, flagged below).

**Assumptions I'm making (and what I'd otherwise have asked):**
- I'd normally ask **"tight leadership room, or keep a delivery-feasibility voice?"** — given the investment-case framing I've assumed **inclusive**.
- I've assumed the modernisation is **bank-wide payments** (rails, instant payments, PSD2, resilience), not a narrow sub-component, so data and integration get a strategic seat as the discipline owners they touch.
- A genuine steering session needs **budget-holding / sponsor-level leaders** to set mandate and sign off the investment. The wiki has **no entries** for those people — they appear only as `[[wiki-links]]`. I've surfaced them in the gap note; they are very likely the most important attendees, but I can't score them without entries.

A heavy caveat on this dataset: of everyone referenced, only **six** people have actual stakeholder entries, and most of them sit at **architect / discipline** altitude rather than executive altitude. The true steering-committee leaders (CTO-equivalent, domain head's manager, programme sponsor, head of risk/compliance) are all **unprofiled links**. So the ranked list below is "the most senior assessable people," and the gap note is where the real sign-off chain lives.

---

## Stakeholders to have in the room (ranked)

### Bram Hendriks — Domain Architect, Payments · relevance 9/10
The single most central **assessable** person. **Remit:** he owns payments architecture standards, payment-processing patterns, and the regulatory/resilience requirements — and his entry explicitly advocates **"a unified payments platform"** and aligning "payments modernization with core banking and integration standards." That is precisely this session's subject. At strategy altitude he's the right level (domain owner, functional leader of the payments tribe), and in the inclusive room he carries both the architecture direction and — through his functional reports — the delivery line. *Ask him to bring the target-state payments architecture and the modernisation roadmap that the investment case will fund.*

### Aisha Khan — Tribe Lead, Payments · relevance 7/10
The **delivery-feasibility voice** I'm keeping because of the investment-case framing. **Remit:** she ensures payments delivery aligns with the **"unified payments platform strategy"** and is accountable for throughput, resilience, time-to-market, and **legacy rail dependencies / operational risk of high-volume processing** — exactly the "can we build this, and what does it really cost in effort and risk" input a multi-year investment case rests on. She's a different remit (delivery) from Bram (architecture), so she's a genuinely separate stream, not a duplicate — but they're in the same line (she's his functional report and reports to Jeroen Meijer). **In a *tight* leadership-only room she'd be "represented by" Bram and drop out**; I've kept her in because you asked for the investment case. Score is 7, not higher, because at pure-direction altitude she'd be too junior.

### Anika Sharma — Head of Data Architecture · relevance 6/10
**Remit + altitude fit.** "Head of" puts her at the right strategic altitude, and payments modernisation is data-heavy — reconciliation, lineage, reusable data products, and the scalability of the data platform under high transaction volume all fall in her remit. She advocates standardized models and governance, which a multi-year payments platform will lean on. She's the **single voice for the data discipline** (she represents Lotte Peters and her other functional reports — don't also invite them). *Consult on whether the data architecture can support the target payments platform and what data-side investment it implies.*

### Ahmed Benali — Integration Architect · relevance 6/10
**Remit + concern.** Bram's own entry names "integration standards" as a key alignment for payments modernisation, and Ahmed owns exactly that: API contracts, the event backbone, and killing point-to-point sprawl / brittle batch interfaces. A multi-year payments platform is an integration programme as much as a payments one. He's at architect (not "Head of") altitude, so for a pure-direction room he'd be borderline — but as the **discipline owner for integration** he's the one voice for that stream and his input shapes the investment case (the event-driven backbone is a cost line). *Consult on the integration target state and its build cost.*

### Charlotte Dubois — Compliance Officer, Architecture · relevance 6/10
**Concern / sign-off lens.** Payments is one of the most regulated domains (PSD2, instant payments, audit trails), and a multi-year strategy locks in compliance posture for years. Her remit — reviewing architecture decisions for regulatory compliance, audit trails, and exception handling — is a distinct stream that none of the architects substitute for. She belongs in a steering room precisely because direction-setting is when compliance constraints are cheapest to bake in. *Ask her what regulatory commitments the strategy must hold to and what the compliance review path for the investment looks like.* (Note: her true sign-off authority sits with her managers Sanne Vermeulen / Daan Verhoeven — see gap note.)

---

## Boundary notes

**Deliberately left out**
- **Carlos Mendes — Cloud Architect (not ranked).** Genuinely relevant when the platform is *built* (landing zones, cost control, IaC, well-architected reviews), and cloud cost is part of any investment case — but for a *strategy/steering* session he's a build-time specialist whose cost input is better fed in *through* the roadmap than by attending in person. Add him if the steering session is specifically about a cloud-vs-on-prem platform bet, where his "cost control / avoid sprawl" lens becomes first-order.

**Represented by their stream**
- **Aisha Khan is the one I'd collapse first if you want a tight room** — in leadership-only mode, **Bram Hendriks represents the payments delivery line** and Aisha moves to "represented by." I've kept her in because of the investment-case framing (inclusive mode). One-line switch.
- **Maria Oliveira, Jonas Bakker, Hannah Schulz** (payments tribe members, links only) — working-level; represented by Aisha / Bram. Not steering-room altitude regardless of mode.
- **Lotte Peters** and Anika's other functional reports (David Cohen, Eva Timmermans, Robin Janssen, Floor van der Berg) — **represented by Anika** for the data discipline.

**Referenced but not in the wiki (no entry — unscored, but likely your most important attendees)**
A steering session that sets multi-year strategy and approves investment needs budget-holders and sponsors. These people appear only as `[[wiki-links]]` — I can see their *position* but not their remit or concerns, so I can't score them. Adding their entries and re-running would let me place them properly. The ones whose position makes them likely steering-room members:
- **[[mark-van-dijk]]** — Bram's line manager and the **functional leader of the architecture community** (functional leader to Ahmed, Anika, Carlos). Almost certainly the **chief/lead architect** — the natural chair/sign-off for an architecture strategy and investment case. Probably the single most important missing name.
- **[[miguel-santos]]** — Ahmed's line manager and Bram's functional leader; senior architecture leadership, plausible steering member.
- **[[jeroen-meijer]]** — Aisha's line manager; the **delivery/tribe leadership** owner for payments — likely holds the delivery budget the investment case funds.
- **[[daan-verhoeven]]** and **[[sanne-vermeulen]]** — Charlotte's functional leader and line manager; the **compliance/risk sign-off chain** a regulated payments strategy needs.
- **[[fatima-el-youssef]]** — Anika's line manager (and, oddly, also her functional report) — senior data leadership; relevant if the data-platform investment is material.

I'd flag **mark-van-dijk** and **jeroen-meijer** (architecture mandate + delivery budget) as the two missing names I'd most want profiled before finalising this room.
