# Stakeholders for SEPA Instant Payments / PSD2 Modernisation

**The issue, in one line:** You're modernising the payment rails to support SEPA instant (real-time, high-availability) payments while meeting incoming PSD2 regulatory deadlines — a payments-domain architecture change with a hard regulatory driver, resilience/throughput implications, and integration/compliance ripple effects.

**Check questions I'd normally ask (assumed here, since this is non-interactive):**
- *Is this a standalone modernisation or part of the standing "unified payments platform" programme?* — I'm **assuming it's part of the unified payments platform strategy**, since that programme is named across the payments entries and instant payments/PSD2 sit squarely inside it.
- *Does the work involve new external connectivity / API exposure (PSD2 open-banking APIs, third-party access)?* — I'm **assuming yes** (PSD2 strongly implies open-banking API obligations), which pulls in integration.
- *Is customer or transaction data being newly processed, moved, or re-platformed?* — I'm **assuming the data architecture impact is modest** (rails/processing change rather than a data re-platform), so I've ranked the data role lower. Tell me if a data migration is in scope and I'll re-weight.

---

## Ranked stakeholders

### Bram Hendriks — Domain Architect, Payments · relevance 10/10
The central owner. His remit is *defining payments architecture standards, governing payment processing patterns, and ensuring regulatory and resilience requirements are met* — exactly this work. His stated concerns name the issue almost verbatim: *"regulatory change (PSD2, instant payments), and resilience under high transaction volumes,"* and he promotes *a unified payments platform and event-driven processing*. Nothing should proceed without his sign-off on the target architecture. **Align with him first** on the target rails design and how it fits the unified payments platform.

### Aisha Khan — Tribe Lead, Payments · relevance 9/10
Owns delivery. Her remit is ensuring *payments delivery complies with architecture and regulatory standards and aligns with the unified payments platform strategy*, and she explicitly *aligns the tribe's roadmap with the payments architecture and regulatory deadlines* — i.e. the PSD2 deadlines are hers to hit. Her concerns (legacy rail dependencies, operational risk of high-volume processing, time-to-market) are precisely the delivery risks of instant payments. Remit + concern, both lighting up. **Align on roadmap, sequencing, and which legacy rails get cut over.**

### Charlotte Dubois — Compliance Officer, Architecture · relevance 8/10
PSD2 is a regulatory deadline, so compliance sign-off is on the critical path. Her remit is *reviewing architecture decisions for regulatory compliance and ensuring audit trails and exception handling are maintained*; her concerns about *gaps in audit trails and divergence from approved standards* map directly onto PSD2's audit/SCA obligations. Remit-driven. **Engage early** so compliance checks are embedded in the design rather than discovered at review.

### Ahmed Benali — Integration Architect · relevance 7/10
Relevant on the assumption that PSD2 brings open-banking APIs and that instant payments need event-driven rails. His remit covers *governing API contracts and driving adoption of the event backbone*, and he advocates *API-first contracts and event-driven integration* — the same pattern Bram wants for payments. Concern + structural overlap with the payments architecture. **Consult on API contracts and the event backbone** for real-time processing. (Drop to ~4 if no new external/API surface is involved.)

---

## Boundary notes

**Deliberately left out**
- **Anika Sharma — Head of Data Architecture (≈4/10).** Genuinely relevant only if a data migration or new regulated-data flow is in scope; under my assumption that this is a rails/processing change rather than a data re-platform, her input is secondary. Pull her in if transaction-data lineage or platform scalability becomes part of the work.
- **Carlos Mendes — Cloud Architect.** Matters at build/run time (landing zones, resilience infrastructure for high-availability instant payments) but not for the architecture-and-alignment decision you're scoping now. Bring him in once the target design implies new cloud workloads.

**Referenced but not in the wiki (no entry — not scored, follow-ups)**
These appear only as `[[wiki-links]]` in the entries above, so I can place them structurally but can't assess their remit/concerns. They look like the sign-off / escalation chain for payments and compliance:
- **[[stakeholder-mark-van-dijk]]** — Bram's line manager and the functional leader for several architects; appears to sit at the head of the architecture function. Likely an architecture sign-off / escalation point.
- **[[stakeholder-miguel-santos]]** — Bram's dotted-line functional leader (and Ahmed's line manager); plausibly the integration/architecture leadership link.
- **[[stakeholder-jeroen-meijer]]** — Aisha's line manager; likely the payments delivery/business escalation point for roadmap and deadline commitments.
- **[[stakeholder-sanne-vermeulen]]** and **[[stakeholder-daan-verhoeven]]** — Charlotte's line manager and functional (compliance) leader respectively; the likely compliance escalation/sign-off chain for a regulatory deadline like PSD2.
- **[[stakeholder-maria-oliveira]]**, **[[stakeholder-jonas-bakker]]**, **[[stakeholder-hannah-schulz]]** — payments tribe/domain reports under Aisha and Bram; probable hands-on delivery contributors.

Adding entries for these (especially Mark van Dijk, Jeroen Meijer, and the compliance chain) would let me score the sign-off/escalation layer properly — worth doing before you lock the alignment list.
