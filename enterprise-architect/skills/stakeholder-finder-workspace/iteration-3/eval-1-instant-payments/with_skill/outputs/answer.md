# Stakeholders for SEPA Instant Payments / PSD2 modernisation

**The issue:** You want to modernise the payment rails to support SEPA instant payments, with PSD2 regulatory deadlines forcing the timeline. This is a payments-domain modernisation that is simultaneously an architecture decision (new rails, integration patterns) and a compliance-driven programme (PSD2 deadlines).

**Meeting type I'm sizing the room for:** "Who do I need to **align** with" reads to me as a **strategic / steering alignment** — agreeing the direction, the mandate, and who owns the regulatory commitment — rather than a hands-on design session. I've biased the roster toward people who own the decision and its sign-off, and toward one voice per stream.

**Assumptions I'm making (and what I'd otherwise have asked):**
- I'm treating this as a **strategy/alignment** conversation, not a technical design session. *I'd have asked: is this to set direction and secure sign-off, or to actually design the rails?* If it's the latter, the altitude shifts down (Aisha and Ahmed rise, a "Head of" drops out) — I flag that per person below.
- I'm assuming **regulated customer payment data is in scope** (it always is for PSD2/SEPA), which is why Compliance is on the list.
- I'm assuming this is an **enterprise-level rail change**, not a one-off project, so the payments domain architect — not just the delivery tribe — is central.

---

### Bram Hendriks — Domain Architect, Payments · relevance 10/10
Squarely **remit**: his entry literally names "regulatory change (PSD2, instant payments)" and "fragmented payment rails" as core concerns, and he owns payments architecture standards and processing patterns. He is the one person whose accountability is this exact issue, and he promotes a "unified payments platform" — which is what modernising the rails amounts to. He's the right altitude for an alignment conversation: senior enough to set direction, close enough to own the technical shape. **Align with him first** on the target rail architecture and how it maps to the PSD2 deadlines.

### Charlotte Dubois — Compliance Officer, Architecture · relevance 8/10
**Remit + concern**: PSD2 is a regulatory mandate, and she reviews architecture decisions for regulatory compliance and owns audit trails and exception handling. Modernising rails under a regulatory deadline is precisely where her sign-off matters — you need her to confirm the approach evidences PSD2 compliance and doesn't create undocumented exceptions. Bring her in early so compliance shapes the design rather than blocking it at the end.

### Ahmed Benali — Integration Architect · relevance 7/10
**Remit + concern**: SEPA instant payments are an integration problem as much as a payments one — real-time messaging, API contracts, and the event backbone he governs. His stated concerns (point-to-point sprawl, brittle batch interfaces, event-driven integration) are exactly the patterns instant payments force you to fix; legacy rails are typically batch, and "instant" means event-driven. Align with him on how the new rails plug into the API gateway and event backbone. *(In a design session he'd rise toward 9.)*

### Aisha Khan — Tribe Lead, Payments · relevance 6/10
**Remit + structural**: she delivers payments and her remit explicitly aligns the tribe's roadmap "with the payments architecture and regulatory deadlines"; her concerns name "legacy rail dependencies" directly. She owns whether this is deliverable and on what timeline. For a *strategic* alignment she is partly **represented by Bram** (he is her functional leader for the payments architecture line), so I've scored her below him — but she's the right person the moment the conversation turns to sequencing, team commitment, and time-to-market, so I'd keep her in the loop. *(For a tactical/delivery-planning meeting she rises to 8–9.)*

---

**Boundary notes**

- **Deliberately left out — Anika Sharma (Head of Data Architecture):** payments modernisation touches reconciliation and transaction data, but her remit (data pipelines, models, lineage) isn't central to the rails or the PSD2 deadline. Worth a heads-up if the rail change reshapes the payments data model, not a core alignment partner.
- **Deliberately left out — Carlos Mendes (Cloud Architect):** relevant at build time (landing zones, IaC for the new rail workloads), not for a direction-and-mandate alignment. Pull him in once the architecture is agreed and it's about where/how it runs.
- **Represented by their stream — Aisha Khan via Bram Hendriks** for the *strategic* framing of this question: Bram is her functional leader for payments architecture and stands in for the payments line when setting direction. Reverse this if the meeting is really about delivery planning, where Aisha leads.
- **Referenced but not in the wiki (no entry — unscored, follow-up leads):**
  - **[[mark-van-dijk]]** — functional leader of the architects (Bram's line manager and the architecture functional lead across the org). Looks like the chief/lead architect and a likely **sign-off / escalation point** for a cross-domain rail change. For a strategy meeting this is probably the altitude you ultimately need — add his entry to place him properly.
  - **[[daan-verhoeven]]** — Charlotte's functional (dotted-line) compliance leader; likely the senior compliance owner who carries the **PSD2 regulatory accountability**. The natural escalation point above Charlotte for the deadline commitment.
  - **[[miguel-santos]]** — Ahmed's line manager and Bram's functional leader; appears to sit over the payments/integration domain and could be a delivery or domain sponsor.
  - **[[jeroen-meijer]]** — Aisha's line manager (payments delivery line); a likely budget/resourcing owner for the tribe.
  - None of these have stakeholder entries, so I can't read their actual remit or concerns and haven't scored them. They're exactly the senior sign-off / escalation chain a strategic alignment usually needs — **adding their entries and re-running would let me place them in the ranked list.**

**Gap to note:** no one in the wiki holds an explicit **payments product / business-owner** role (the revenue/customer-proposition side of SEPA instant payments). If a business sponsor owns the "why now" and the budget, they're missing from this dataset and worth identifying outside it.
