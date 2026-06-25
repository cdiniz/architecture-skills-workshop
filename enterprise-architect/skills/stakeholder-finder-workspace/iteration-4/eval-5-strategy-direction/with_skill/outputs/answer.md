# Who should be in the room — Payments strategy steering session

**Issue, as I read it:** a leadership steering session to set the multi-year direction, priorities, and mandate for payments — *strategic direction only*, explicitly **not** a delivery-planning or costing exercise.

**Meeting type I'm sizing the room for:** **strategic / steering session.** That sets the altitude high — I'm biasing toward leaders who set direction, hold the budget, and sign off, and letting working-level specialists be *represented by their leader* rather than sitting in the room.

**Room-breadth mode I used: tight (leadership-only).** The framing is deliberately direction-and-mandate, with delivery and cost explicitly out of scope. Under the skill's room-breadth toggle, a bare "set the strategic direction" with no "can we build it / what will it cost" signal leans tight — the most senior person in each line represents everyone below them, including different-remit reports. If you actually want a deliverability/feasibility voice in the room after all, say so and I'll switch to inclusive mode (that mainly brings the Payments Tribe Lead back in — see "Represented by their stream").

**Assumptions I'm making (and what I'd otherwise have asked):**
- I'd normally check **meeting type** first; your wording ("set multi-year direction and priorities… strategic direction and mandate, not a delivery or costing exercise") settles it as strategic — no need to ask.
- I'd ask **tight vs inclusive room**; the explicit "not a delivery or costing exercise" makes tight the right default.
- I'd ask whether **regulatory direction** (PSD2, instant payments) is in scope for the mandate. I'm assuming yes — it's intrinsic to a multi-year payments direction — so I've surfaced the compliance lens. If compliance is genuinely out of scope, drop that name.

A hard constraint shapes this answer: **only 6 of the ~23 people in the wiki have actual entries.** The most senior payments leadership — the people a steering session is really *for* — appear only as `[[wiki-links]]` with no profile. I can't score them, but they're exactly the altitude this meeting needs, so they're called out prominently in the gap note below. **Please read that section — it likely contains the real chairs of this session.**

---

## Stakeholders to consider (ranked, profiled people only)

### Bram Hendriks — Domain Architect, Payments · relevance 8/10
**Remit + structural.** Bram owns payments architecture standards and is the named functional leader of the whole payments architecture line. His entry's concerns are precisely strategic-direction material: a *unified payments platform*, regulatory change (PSD2, instant payments), resilience under volume, and aligning payments modernization with core banking and integration. For a multi-year direction-setting session he is the single most relevant *profiled* voice — he carries the technical north-star and, in tight mode, represents the delivery line below him (the Payments Tribe). Ask him to frame the target-state payments platform and the regulatory horizon the mandate has to clear.

### Charlotte Dubois — Compliance Officer, Architecture · relevance 6/10
**Concern (lens).** A multi-year payments mandate is shaped by where regulation is heading (PSD2, instant payments, audit/exception standards). Charlotte's lens — keeping architecture decisions inside regulatory and internal-compliance bounds — is a direction-shaping constraint, not a delivery detail, so it belongs in a *strategy* room even though she doesn't own payments. Score reflects "should be consulted," not "owns it." Ask her which regulatory commitments are non-negotiable for the multi-year plan. *(Drop if you've scoped compliance out of this session.)*

### Ahmed Benali — Integration Architect · relevance 5/10
**Concern + structural.** Payments strategy leans heavily on integration direction — Bram's own concern explicitly names aligning payments with *integration standards* and event-driven processing, which is Ahmed's remit (API-first contracts, the event backbone). He's relevant as the integration lens on the payments target state. He sits one notch below leadership altitude for a steering room, so 5/10: consult him on the integration direction, but he's arguably *represented* by the architecture leadership chain (see gap note) rather than a required seat.

---

## Boundary notes

**Deliberately left out (profiled people I considered but didn't rank):**
- **Anika Sharma — Head of Data Architecture.** Genuinely senior and relevant to a data-strategy session, but payments direction touches her remit only indirectly (reporting/lineage). Marginal for *this* mandate; invite only if data-product strategy is explicitly part of the payments direction.
- **Carlos Mendes — Cloud Architect.** Cloud landing zones and cost control are a build/run concern. Relevant when payments platform *delivery* and *cost* are on the table — which you've explicitly excluded. Not for a pure direction session.

**Represented by their stream (one voice per chain):**
- **Aisha Khan — Tribe Lead, Payments** is omitted from the tight room. She's the delivery/feasibility voice for payments (throughput, time-to-market, legacy-rail risk) and sits under Bram functionally — in tight leadership-only mode, **Bram Hendriks represents the payments line**, including her delivery view. *This is the one seat that the room-breadth toggle flips:* if you want a feasibility/"can we actually build this multi-year" voice, switch to inclusive mode and Aisha comes back in (~6/10).

**Referenced but not in the wiki — the leadership/sign-off chain this session is actually for (no entries, so unscored):**
These appear only as `[[wiki-links]]`. I can see their *position* but not their remit or concerns, so I can't rank them — but for a strategy/steering session they are almost certainly the senior decision-makers and budget-holders who should chair or attend:
- **[[mark-van-dijk]]** — functional leader across the architecture practice (functional/line leader to Bram, Ahmed, Anika, Carlos). Looks like the top architecture authority — a natural owner of cross-domain strategic direction and sign-off.
- **[[miguel-santos]]** — Bram's dotted-line functional leader and Ahmed's line manager; sits senior in the integration/architecture chain. Plausible co-owner of architecture direction.
- **[[jeroen-meijer]]** — Aisha's line manager; the payments *delivery/business* leadership line. Likely a budget/mandate holder for payments — strong candidate for a steering seat.
- **[[daan-verhoeven]]** / **[[sanne-vermeulen]]** — the compliance leadership chain above Charlotte; relevant if the multi-year mandate needs senior compliance/regulatory sign-off.
- **[[yasmine-haddad]]** — cloud/platform leadership (Carlos's manager); relevant only if platform/infra strategy is in scope.

**Recommendation:** before convening, add wiki entries for **Mark van Dijk, Miguel Santos, and Jeroen Meijer** in particular and re-run — a payments *steering* session is defined by exactly these leaders, and right now they're the gap. The three profiled people above are the right architectural substance for the room, but they are not, on their own, a leadership steering committee.
