# 0001. Tokenise card PANs via a third-party vault instead of storing raw PANs

- Status: Proposed
- Date: 2026-06-23
- Deciders: [OPEN QUESTION: who is taking part in this decision? Payments platform team and architecture review are assumed but not confirmed]
- Decision owner: [OPEN QUESTION: name the accountable individual or role for this decision]
- Regulatory scope: PCI DSS (card data in scope). [NEEDS COMPLIANCE/RISK REVIEW: confirm whether GDPR/data-protection and any local payments regulation also apply, and whether this changes the platform's PCI DSS assessment level (e.g. SAQ type / Report on Compliance scope)]

## Context

The payments platform currently stores raw card Primary Account Numbers (PANs)
directly in the payments database. Storing raw PANs puts the database — and every
system, backup, and person with access to it — inside the PCI DSS cardholder data
environment (CDE), which carries a heavy compliance, security, and audit burden.

We want to remove raw PANs from our own systems by tokenising card data through a
third-party vault. After this change the application only ever sees tokens; the
real PAN is held by the vault provider and never lands in our database.

[ASSUMPTION: the driver is to reduce PCI DSS scope, lower the risk of a PAN
breach, and simplify the cardholder data environment. Confirm the primary driver
and any deadline.]

## Decision

We will stop storing raw card PANs in the payments database and instead tokenise
card data through a third-party tokenisation vault. The application and payments
database will store and operate on **tokens only**; the underlying PAN will be
held by the vault, which returns it (or uses it directly) only when a payment must
be processed.

[DECISION PENDING: selection of the specific vault provider — this ADR records the
decision to tokenise via a third party, not which vendor. Capture the chosen
provider in a follow-up ADR or by refining this one.]

## Options considered

- **Option A — Tokenise via a third-party vault (chosen).** The application
  exchanges PANs for tokens at capture time and only ever handles tokens
  thereafter; the vault holds the PAN.
  - Pros: removes raw PANs from our database and most of our systems; substantially
    reduces PCI DSS scope; the vendor carries the storage/security burden for PANs.
  - Cons: introduces a third-party dependency and concentration/lock-in risk;
    detokenisation latency and availability now depend on the vendor; token format
    and integration constraints; cost of the service.
  - Key risk/compliance implication: shifts cardholder-data storage to a vendor,
    which must itself be PCI DSS compliant and covered by appropriate contractual
    and oversight controls. [NEEDS COMPLIANCE/RISK REVIEW: vendor PCI DSS
    attestation (AOC) and outsourcing/third-party due diligence]

- **Option B — Keep storing raw PANs, harden in place.** Continue storing PANs in
  the payments database with encryption, tightened access controls, and tokenised
  internal references.
  - Pros: no new vendor dependency; full control of the data.
  - Cons: the database stays in full PCI DSS scope; we retain the breach risk and
    the cost of protecting PANs ourselves; does not meaningfully reduce audit
    burden.
  - Key risk/compliance implication: maximum PCI DSS scope and PAN-breach exposure
    remain with us.

- **Option C — Build our own internal token vault.** Run an in-house vault that
  isolates PAN storage to a small, dedicated component.
  - Pros: reduces scope of the broader platform; no external PAN-storage vendor.
  - Cons: we still store and must secure PANs ourselves; the vault remains fully in
    PCI DSS scope; significant build and ongoing assurance cost.
  - Key risk/compliance implication: retains PAN-storage obligations in-house.

## Regulatory & compliance impact

- **PCI DSS:** Card PANs are cardholder data and are in scope of PCI DSS. Removing
  raw PANs from the payments database is expected to reduce the systems within the
  CDE and therefore the assessment burden. [NEEDS COMPLIANCE/RISK REVIEW: confirm
  the resulting PCI DSS scope reduction, the applicable validation level
  (SAQ A / SAQ A-EP / SAQ D or RoC), and that tokens as implemented are not
  themselves rendered in scope (e.g. tokens must not be reversible without the
  vault)].
- **Data classification & privacy:** PAN is sensitive card data; depending on
  jurisdiction it may also be personal data. [NEEDS COMPLIANCE/RISK REVIEW:
  confirm data classification and whether data-protection law (e.g. GDPR or local
  equivalent) applies, and whether a DPIA is required].
- **Retention:** Tokenisation changes what we retain (tokens vs PANs). [OPEN
  QUESTION: what are the retention rules for tokens, and does removing PANs affect
  any records-retention obligation?]

## Risk assessment

- **Security risk (reduced):** Removing raw PANs from our database materially
  reduces the impact of a breach of our own systems, since they would no longer
  hold usable card numbers.
- **Third-party / concentration risk (introduced):** Card data availability now
  depends on a single external vault provider; an outage or vendor failure could
  block payment processing. See Security & resilience.
- **Operational risk (introduced):** New integration, token lifecycle, and
  migration of existing stored PANs into tokens.
- **Qualitative rating and risk owner:** [NEEDS COMPLIANCE/RISK REVIEW: assign a
  qualitative risk rating and a named risk owner; record residual risk accepted].
- **Migration of existing data:** [OPEN QUESTION: how will the PANs already stored
  in the payments database be migrated to tokens and then securely destroyed, and
  who signs off that destruction?]

## Security & resilience

- **Threat surface:** Reduced for our database (no usable PANs at rest), but a new
  trust boundary and integration with the vault is introduced; secure the
  tokenise/detokenise API calls and credentials.
- **Encryption & key management:** PAN encryption/key management for stored card
  data shifts to the vault provider. [NEEDS COMPLIANCE/RISK REVIEW: confirm the
  provider's key management and how our API credentials/secrets to the vault are
  stored and rotated].
- **Authentication/authorisation & segregation of duties:** [OPEN QUESTION: how is
  access to detokenisation controlled and segregated, and which roles may invoke
  it?]
- **Resilience (RTO/RPO, DR, availability):** Payment processing that needs the
  PAN now depends on vault availability. [NEEDS COMPLIANCE/RISK REVIEW: vendor SLA,
  failover behaviour, and impact on platform RTO/RPO if the vault is unavailable].
- **Data residency & sovereignty:** PANs will be stored/processed by the vendor.
  [OPEN QUESTION: where does the vault store and process card data, and are there
  cross-border transfer constraints to satisfy?]

## Consequences

- **Easier:** Smaller PCI DSS footprint and audit scope; reduced consequence of a
  breach of our own systems; the vendor carries PAN-storage security.
- **Harder / trade-offs:** A new critical third-party dependency for payment
  processing; integration, token lifecycle, and credential management work; a
  one-off migration of existing PANs to tokens followed by secure destruction.
- **Reversibility / exit:** Reverting to in-house PAN storage, or moving to another
  vault, would require re-acquiring or re-tokenising card data. [OPEN QUESTION:
  what is the vendor exit / portability plan if we need to leave the provider?]

## Approvals

This ADR is `Proposed`. Before it can move to `Accepted`, it needs sign-off from
the relevant functions. [NEEDS COMPLIANCE/RISK REVIEW: confirm the required
approvers — typically the Architecture Review Board, CISO/security, the
compliance/PCI function, and risk — and record their decisions here. None of
these approvers were named in the request, so do not treat any approval as given.]

## References

- [OPEN QUESTION: link the chosen vault provider's PCI DSS Attestation of
  Compliance (AOC) once a provider is selected]
- [OPEN QUESTION: link any threat model, DPIA, and the risk-register entry for
  this decision]
- Related ADRs: none yet (this is the first ADR in `docs/adr`).
