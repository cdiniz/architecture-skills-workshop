# Who should be in the room — Payments platform modernisation (steering session)

**The issue, in my words:** You're setting the *multi-year strategy* and the *investment case* for modernising the payments platform — direction, mandate, and money, not the technical design.

**Meeting type I'm sizing for:** **Strategic / steering session.** Your wording ("steering session", "multi-year strategy", "investment case") settles this — I don't need to ask. That altitude biases the room toward people who set direction, own the payments mandate, and can speak to (or sign off) the spend, and pushes hands-on/design specialists down to "represented by their leader".

**Assumptions I'd otherwise have check-questioned:**
- I'm treating this as a leadership/budget conversation, so I'm surfacing the *senior* end of each payments stream and leaving the makers out (they're represented). If you actually want a mixed working+steering room, pull Ahmed Benali up from the boundary note.
- I'm assuming the strategy is firm-wide for payments (rails, resilience, regulatory roadmap), so compliance belongs in the room. If the session is purely financial/portfolio with compliance handled separately, drop Charlotte to a pre-read.

A real caveat up front: this wiki has only **six profiled people**, and the actual budget-holders / sign-off chain for a strategy session of this size appear only as `[[wiki-links]]` with no entries. The scored list below is the right *content* of the room from the people I can assess; the **"Referenced but not in the wiki"** note is where the people who'd typically *chair and fund* this session sit — read both together.

---

### Bram Hendriks — Domain Architect, Payments · relevance 9/10
**Remit + concern, and the right altitude for this room.** His remit is, almost word for word, the subject of the meeting: "Defines payments architecture standards... promotes **a unified payments platform**, event-driven processing." His stated concerns — fragmented rails, regulatory change (PSD2, instant payments), resilience under volume, and "aligning payments modernization with core banking and integration standards" — *are* the modernisation thesis. He's the person who owns the architectural shape of the multi-year strategy and whose case underpins the investment ask. For a steering session he's the central voice and represents the payments architecture stream below him.

### Aisha Khan — Tribe Lead, Payments · relevance 8/10
**Remit + structural, and the deliverability reality of the investment case.** Her remit explicitly aligns the tribe's roadmap "with the **unified payments platform strategy**" and regulatory deadlines; her concerns (throughput, resilience, time-to-market, legacy rail dependencies, operational risk of high-volume processing) are exactly what turns a strategy slide into a credible multi-year plan and cost. She's functionally led by Bram, but architecture-strategy vs delivery-feasibility are *genuinely different remits*, so she belongs in her own right — she's the one who can say what's actually buildable and over what horizon. Slightly below Bram only because a top-of-house steering session leans architecture/strategy over delivery execution; if the session is as much "can we deliver this and what will it cost" as "what should we build", she's a 9.

### Charlotte Dubois — Compliance Officer, Architecture · relevance 7/10
**Concern, and a sign-off lens a payments investment case can't skip.** Payments modernisation is regulator-shaped (PSD2, instant payments, audit trails, reconciliation), and her remit is reviewing architecture decisions for regulatory compliance and keeping audit trails and exception handling intact. A multi-year strategy that hasn't been pressure-tested for compliance is an investment case with a hidden liability. She's a different stream from architecture and delivery, so she's additive, not a duplicate. Ask her: which regulatory deadlines (and which way the rules are moving) must the multi-year roadmap be sequenced around.

### Ahmed Benali — Integration Architect · relevance 5/10
**Concern, but altitude pulls him down for *this* meeting.** Payments modernisation leans heavily on his world — the event backbone, API-first contracts, killing point-to-point sprawl — and Bram's own strategy names "integration standards" as a dependency. But Ahmed is a hands-on/design-altitude specialist; in a steering session about direction and money he's **represented by Bram**, who carries the integration dependency into the room. Include him only if the strategy genuinely hinges on an integration-platform decision (e.g. committing multi-year to the event backbone) — then he moves up. Otherwise he's a design-session invite, not a steering one.

---

**Boundary notes**

- **Deliberately left out — Carlos Mendes (Cloud Architect):** relevant when you're *building* (landing zones, IaC, cost control), but a strategy/steering session on payments direction and investment doesn't turn on cloud build-time choices. Bring him in once the strategy lands and you're sizing the platform build.
- **Deliberately left out / marginal — Anika Sharma (Head of Data Architecture):** payments modernisation touches data (reconciliation, data products, lineage), and she's senior enough for a strategy room — but data architecture is adjacent to *setting payments strategy*, not central to it. Worth a heads-up or a pre-read so the payments data implications are represented; only a seat if the strategy explicitly hinges on a payments-data platform decision.
- **Represented by their stream:** Maria Oliveira and Jonas Bakker (Aisha's direct reports) and Hannah Schulz (in Bram's functional line) are the working level — **represented by Aisha and Bram** for a steering session; they're design/delivery altitude, not strategy. Ahmed Benali stands in for the integration team. Surface them directly only if you want makers in the room.
- **Referenced but not in the wiki (no entry — unscored, but this is where your steering chair and budget sign-off likely sit):** A steering session for multi-year strategy and an investment case needs the people who hold the mandate and the money, and they appear here only as links:
  - **Mark van Dijk** — functional leader of the architects (Bram, Ahmed, Anika, Carlos all dotted-line to him); reads as the head/chief architect who would own and sign off the multi-year architecture strategy. Almost certainly chairs or co-owns this room.
  - **Miguel Santos** — line manager of integration/payments architecture (manages Ahmed; functional leader for Bram). Plausible delivery/engineering leadership voice on the investment case.
  - **Jeroen Meijer** — Aisha's line manager; the management chain above the payments tribe, i.e. where delivery budget and headcount commitments live.
  - **Fatima el-Youssef** — Anika's manager (data leadership) — relevant only if data sits in the payments strategy scope.
  - **Daan Verhoeven / Sanne Vermeulen** — Charlotte's functional and line chain (compliance/governance leadership) — the level that would give regulatory sign-off on the strategy.

  I can't score these — there's no entry stating their remit or concerns, so any score would be invented. But for a steering session they're likely the most important attendees of all. **Next step:** add wiki entries for Mark van Dijk (priority — the probable strategy/sign-off owner) and the relevant management chain, then re-run and I'll place them properly in the ranked room.
