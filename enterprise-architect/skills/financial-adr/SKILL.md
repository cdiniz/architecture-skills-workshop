---
name: financial-adr
description: Generate an Architecture Decision Record (ADR) for a regulated financial institution — one that captures not just the technical choice but the regulatory, compliance, risk, security, data-residency, resilience, and audit dimensions that a bank, insurer, payments firm, or asset manager must evidence. Use whenever the user wants to document an architecture decision in a financial-services or regulated context, record a decision that touches customer data, payments, trading, lending, or core banking, needs an auditable decision with sign-off and risk assessment, or says things like "write an ADR for our new payments service", "document this decision for the regulator/auditors", "we need a decision record with the compliance impact", "capture why we chose this with the risk trade-offs". Prefer this over a generic ADR whenever the system handles money, regulated data, or sits in scope of a financial regulator.
---

# Generate a Financial-Institution ADR

An ADR in a regulated financial institution does everything a normal ADR does —
records one decision, its context, the options weighed, and the consequences —
but it must **also stand up as audit evidence**. Regulators, internal audit, and
risk functions read these records to confirm that a decision was made
deliberately, that the relevant risks were considered, and that the right people
approved it. So the bar is higher: the rationale must be explicit, the
compliance and risk impact must be assessed (even if the assessment is "no
impact, because…"), and the record must be traceable and immutable.

The job of this skill is to produce that record without inventing facts. Where a
regulatory or risk dimension wasn't discussed, **say so explicitly** rather than
guessing — an ADR that fabricates a compliance assessment is worse than one that
flags the gap, because it gives false assurance to the people relying on it.

## Workflow

1. **Locate where ADRs live and match the convention.** Look for an existing
   `docs/adr/`, `docs/decisions/`, `architecture/decisions/`, or `adr/`
   directory and reuse its numbering and filename style (e.g.
   `0042-adopt-tokenisation-for-pan.md`). If none exists, ask the user where
   ADRs should live before creating a directory. Use the next sequential,
   zero-padded number.

2. **Gather the decision and its context** from the conversation, or ask. You
   need the technical decision, the forces driving it, the options considered,
   the chosen option, and the consequences — the normal ADR content.

3. **Assess the regulated dimensions.** This is what makes the record fit for a
   financial institution. Work through the checklist below and fill in each
   relevant section. For any dimension that genuinely doesn't apply, state that
   briefly and why — don't silently drop it, because a reviewer can't tell the
   difference between "considered and not applicable" and "forgotten".

4. **Do not fabricate.** If a control, regulation, approval, or risk rating
   wasn't established in the conversation, mark it with an uncertainty marker
   (see below) instead of asserting it. Naming a specific regulation, a control
   ID, or a risk owner that the user never mentioned is a hallucination that can
   mislead an auditor.

5. **Write the ADR** using the template, save it, and tell the user which
   regulated dimensions still need input from compliance, risk, or security
   before the record can move from `Proposed` to `Accepted`.

## Regulated dimensions to assess

Treat these as prompts to think through, not boxes to pad. Include a section
only when it carries real information; for the rest, a one-line "not applicable
because…" is enough.

- **Data classification & privacy** — Does the decision touch PII, customer
  financial data, card data (PCI DSS), or special-category data? What is the
  data classification, and what handling/encryption/retention follows from it?
- **Applicable regulation** — Which regimes are in scope (e.g. PCI DSS, SOX,
  GDPR/data protection, PSD2/Open Banking, MiFID II, Basel/CRR, DORA, AML/KYC,
  records-retention rules)? Name only the ones actually relevant; mark the rest
  as needing confirmation if unsure.
- **Risk assessment** — Operational, security, financial, concentration, and
  conduct risk introduced or reduced. Give a qualitative rating and name the
  risk owner if known.
- **Security** — Threat surface changes, authentication/authorisation,
  encryption in transit and at rest, key management, secrets handling, and
  segregation of duties.
- **Resilience & continuity** — Impact on availability, RTO/RPO, failover,
  disaster recovery, and operational resilience obligations (important under
  regimes like DORA).
- **Third-party & concentration risk** — New vendors, cloud providers, or
  outsourcing arrangements, and any supplier-exit / lock-in considerations.
- **Data residency & sovereignty** — Where data is stored and processed, and any
  cross-border transfer constraints.
- **Audit & traceability** — How the decision and its operation will be
  evidenced (logging, immutability, change records).
- **Approvals & sign-off** — Who must approve (architecture review board, CISO,
  DPO, risk committee) before the decision is `Accepted`.

## Uncertainty markers

Use these inline so reviewers can see exactly what is settled and what is not:

- `[OPEN QUESTION: …]` — something that must be answered before acceptance.
- `[DECISION PENDING: …]` — a sub-decision deferred to another owner/forum.
- `[ASSUMPTION: …]` — a stated assumption the decision rests on.
- `[NEEDS COMPLIANCE/RISK REVIEW: …]` — a regulated dimension requiring
  confirmation from the relevant function.

## Template

ALWAYS produce this structure (omit a regulated subsection only with an explicit
"not applicable" note):

```markdown
# NNNN. <Short title of the decision>

- Status: Proposed
- Date: <YYYY-MM-DD>
- Deciders: <people/roles involved>
- Decision owner: <accountable individual or role>
- Regulatory scope: <regimes in scope, or "none identified — [NEEDS COMPLIANCE/RISK REVIEW]">

## Context

<The business and technical forces. Why must this be decided now? What customer,
product, or regulatory driver is behind it?>

## Decision

<The change, in active voice: "We will ...">

## Options considered

- **Option A** — <summary; pros; cons; key risk/compliance implication>
- **Option B** — <summary; pros; cons; key risk/compliance implication>

## Regulatory & compliance impact

<Applicable regulation and what it requires of this decision. Data classification
and privacy impact. Mark gaps with [NEEDS COMPLIANCE/RISK REVIEW: …].>

## Risk assessment

<Operational / security / financial / conduct risks introduced or mitigated, a
qualitative rating, and the risk owner. Note residual risk accepted.>

## Security & resilience

<Security controls affected; encryption and key management; availability,
RTO/RPO, DR, and operational-resilience impact; data residency.>

## Consequences

<What becomes easier or harder. Trade-offs accepted, follow-up work, and new
risks introduced. Include reversibility / exit considerations.>

## Approvals

<Forums/roles that must sign off before this moves to Accepted — e.g.
Architecture Review Board, CISO, DPO, Risk Committee. Record decision once given.>

## References

<Links to the spec, threat model, DPIA, risk register entry, related ADRs.>
```

## Notes

- One decision per record; keep it readable in a single sitting.
- Status values: `Proposed`, `Accepted`, `Superseded by NNNN`, `Deprecated`.
  ADRs are immutable once `Accepted` — supersede with a new record rather than
  rewriting history, because the audit trail depends on it.
- If a Data Protection Impact Assessment (DPIA) or threat model is implied by the
  decision, link it rather than reproducing it here.
