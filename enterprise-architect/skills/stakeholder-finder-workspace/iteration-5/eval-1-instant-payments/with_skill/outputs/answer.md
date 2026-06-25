# Stakeholders to align with — SEPA instant payments / PSD2 modernisation

**Issue (my read):** You want to modernise the payment rails to support SEPA instant payments, with PSD2 regulatory deadlines as the forcing function. This is a payments-domain change with a hard compliance driver and a cross-cutting integration angle (instant rails touch the event backbone and core banking).

**Meeting type I'm sizing for:** A **tactical alignment session** — turning the modernisation intent into a plan, sequencing the work against the PSD2 deadlines, and lining up architecture + delivery + compliance sign-off. The word "align" plus a regulatory deadline points at planning/coordination, not a hands-on design session. Because deliverability and a regulatory clock are both in play, I'm using the **inclusive room-breadth mode** — I keep a delivery-feasibility voice and the compliance voice in the room rather than collapsing everything to a single leader.

**Assumptions I'd otherwise have checked with you:**
- *Is this a technical design session or a planning/alignment one?* I assumed **tactical alignment**. If it's actually a hands-on design session, the architects stay but the tribe/delivery and compliance leads drop out, and you'd add engineers.
- *Tight leadership room, or keep delivery-feasibility and compliance voices?* I assumed **inclusive**, because PSD2 deadlines make "can we actually hit the date, and does it pass compliance" central. A bare "set our payments strategy" would lean tight, with the Domain Architect representing the line.

## Stakeholders

| Stakeholder | Role | Why relevant | Score |
|-------------|------|--------------|-------|
| Bram Hendriks | Domain Architect — Payments | **Remit + concern, both squarely on target.** Owns payments architecture standards and payment-processing patterns; his stated concerns name *"regulatory change (PSD2, instant payments)"* and *"fragmented payment rails"* explicitly, and he promotes a unified payments platform and event-driven processing. This is his decision to shape and sign off — the central architecture voice for the room. | 10/10 |
| Aisha Khan | Tribe Lead — Payments | **Remit + structural, the delivery-feasibility voice.** Her remit is ensuring payments delivery complies with architecture and regulatory standards and aligns to the unified payments platform; she explicitly worries about *"legacy rail dependencies"* and aligns the tribe roadmap to *"regulatory deadlines"*. Kept in under inclusive mode — she answers "can we build this by the PSD2 date" in a way Bram can't fully stand in for. (In a tight strategy room she'd be represented by Bram.) Align on roadmap sequencing and rail-dependency risk. | 8/10 |
| Charlotte Dubois | Compliance Officer — Architecture | **Concern/remit, the PSD2 sign-off lens.** Reviews architecture decisions for regulatory compliance and owns audit trails and exception handling. PSD2 is the deadline driving the whole effort, so her review and sign-off path needs to be in the plan from the start, not bolted on. Align on what evidence/audit trail the PSD2 changes must produce and where exceptions get logged. | 8/10 |
| Ahmed Benali | Integration Architect | **Remit/concern, cross-cutting.** Governs API contracts and drives the event backbone; SEPA instant payments is real-time, event-driven integration touching that backbone, and his concerns (point-to-point sprawl, brittle batch interfaces) are exactly what instant rails must avoid. Consult so the instant-payment flows ride the managed event backbone rather than new point-to-point links. | 7/10 |

## Boundary notes

- **Deliberately left out — profiled but not ranked:**
  - *Carlos Mendes (Cloud Architect)* — relevant at build time for landing zones/IaC if instant payments needs new infra, but not for a tactical alignment on rails and deadlines. Bring him in once you're designing the runtime.
  - *Anika Sharma (Head of Data Architecture)* — payments data/lineage could surface later (reconciliation, reporting), but no remit or concern of hers points at payment rails or PSD2; too tangential for this room.

- **Represented by their stream / mode note:** I kept Aisha (Tribe Lead) in under **inclusive** mode for delivery feasibility. If you actually want a **tight** leadership-only room, drop Aisha — *the Domain Architect (Bram) represents the payments line, including delivery* — and say so and I'll re-cut. Aisha's direct reports (Maria Oliveira, Jonas Bakker) are the same payments stream one level down and are represented by Aisha; not in the room.

- **Referenced but not in the wiki (no entry — unscored, follow-ups):** Several names appear only as `[[wiki-links]]` and have no stakeholder entry, so I can't assess their remit/concerns and won't score them — but they look like the missing sign-off/escalation chain a PSD2 programme needs:
  - **[[stakeholder-mark-van-dijk]]** — Bram's line manager and the functional leader across the architecture group; likely the architecture escalation/sign-off point for a payments-platform mandate.
  - **[[stakeholder-miguel-santos]]** — Bram's functional leader and Ahmed's line manager; sits over the integration line that instant payments depends on.
  - **[[stakeholder-jeroen-meijer]]** — Aisha's line manager; the delivery-leadership owner who'd commit the payments tribe's capacity to the deadline.
  - **[[stakeholder-sanne-vermeulen]]** / **[[stakeholder-daan-verhoeven]]** — Charlotte's line manager and compliance functional leader; the regulatory sign-off chain above her for PSD2.

  These are leads to follow up, not stakeholders I can place. If you add their entries I can score them and tell you which belong in a strategic/steering version of this room (where this escalation chain is usually exactly the altitude you need).
