# Steering Session: Payments Platform Modernisation — Strategy & Investment Case

**Question:** We're holding a steering session to set the multi-year strategy and the investment case for modernising our payments platform. Who should be in the room?

This is a strategy + investment steering session, not a delivery stand-up. The room needs the people who own the payments architecture and roadmap, the cross-cutting architecture functions the modernisation will depend on (integration, data, cloud), and the compliance/regulatory voice that has to sign off the direction. Below are the relevant people from the available stakeholder profiles.

## Recommended attendees

### Core — payments ownership (must attend)

**Bram Hendriks — Domain Architect, Payments**
Owns payments architecture standards, payment processing patterns, and regulatory/resilience requirements. He is already advocating a unified payments platform, event-driven processing, and strong reconciliation. He is the natural architectural owner of the modernisation direction and should help frame the target state and investment case.

**Aisha Khan — Tribe Lead, Payments**
Owns payments delivery, throughput, resilience, and time-to-market for new payment products, and aligns the tribe roadmap with payments architecture and regulatory deadlines. She brings the delivery-capacity, legacy-rail-dependency, and operational-risk realities that the multi-year roadmap and investment case must reflect. Functionally aligned to Bram, so the architecture/delivery view stays joined up.

### Cross-cutting architecture (should attend — modernisation depends on them)

**Ahmed Benali — Integration Architect**
Payments modernisation hinges on integration: API contracts, the event backbone, and replacing brittle batch interfaces. Ahmed governs exactly these. His event-driven and API-first direction aligns with Bram's unified-platform vision, and integration is a major cost/effort driver in the investment case.

**Anika Sharma — Head of Data Architecture**
Payments generate high-value data (reconciliation, lineage, reporting, fraud/AML inputs). Anika owns data architecture standards, pipelines, models, and governance. Multi-year strategy and investment should account for data products and platform scalability tied to payments.

**Carlos Mendes — Cloud Architect**
A multi-year modernisation almost certainly involves cloud platform choices, landing zones, and cost control — a core input to the investment case. Carlos governs landing zones, IaC, and well-architected reviews, and brings cost and security-baseline discipline to the numbers.

### Compliance / regulatory (should attend — sign-off on direction)

**Charlotte Dubois — Compliance Officer, Architecture**
Payments is heavily regulated (PSD2, instant payments). Charlotte reviews architecture decisions for regulatory compliance and ensures audit trails and exception handling. Her presence keeps the strategy defensible to regulators and auditors from the outset rather than as an afterthought.

## Notable gaps to fill before/at the session

The available profiles reference several senior people who are not yet documented but are clearly relevant to a steering session of this seniority. You will likely also want some of these in the room (or represented) as decision-makers and budget owners:

- **Mark van Dijk** — functional/line leader across multiple architects (incl. Bram); appears to be a senior architecture leader. A multi-year strategy session needs this level of authority.
- **Miguel Santos** — functional leader for integration/payments architecture; senior architecture decision-maker.
- **Jeroen Meijer** — Aisha's line manager (likely tribe/area lead for payments) — owns delivery capacity and budget.
- **Daan Verhoeven** / **Sanne Vermeulen** — compliance/governance leadership behind Charlotte.

These individuals do not have stakeholder profiles in the current dataset, so their exact roles are inferred from relationship links. Confirm and add them to the invite as the sponsoring/decision-making layer, since a steering session setting multi-year strategy and an investment case needs an accountable budget owner and senior architecture authority in the room.

## Summary of the room

| Attendee | Role | Why they are in the room |
|---|---|---|
| Bram Hendriks | Domain Architect, Payments | Owns payments target architecture and modernisation vision |
| Aisha Khan | Tribe Lead, Payments | Delivery roadmap, capacity, operational risk, regulatory deadlines |
| Ahmed Benali | Integration Architect | API/event backbone — a key modernisation enabler and cost driver |
| Anika Sharma | Head of Data Architecture | Payments data, lineage, governance, platform scalability |
| Carlos Mendes | Cloud Architect | Cloud platform choices and cost — core to the investment case |
| Charlotte Dubois | Compliance Officer, Architecture | Regulatory/audit sign-off on the strategy |
| (To confirm) Senior sponsor/budget owner | e.g. Mark van Dijk / Miguel Santos / Jeroen Meijer | Authority and funding decision on a multi-year investment case |
