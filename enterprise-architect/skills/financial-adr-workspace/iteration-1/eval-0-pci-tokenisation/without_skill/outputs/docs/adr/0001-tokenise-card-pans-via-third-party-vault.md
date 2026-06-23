# 1. Tokenise Card PANs via a Third-Party Vault

- Status: Proposed
- Date: 2026-06-23
- Deciders: Payments Platform Team, Security / Compliance
- Tags: payments, security, pci-dss, tokenisation

## Context

Our payments platform currently stores raw card Primary Account Numbers (PANs) directly in the payments database. This means cardholder data lives inside our own systems, which has significant consequences:

- **PCI DSS scope.** Because we store, process and transmit raw PANs, large parts of our infrastructure (the payments database, the application servers that touch it, backups, logs, and supporting network segments) fall within PCI DSS scope. This makes audits expensive, slow, and high-risk.
- **Breach exposure.** A compromise of the payments database would directly expose usable card numbers, creating major financial, regulatory, and reputational liability.
- **Operational burden.** Encryption-at-rest, key management/rotation, access controls, and audit logging around the PAN data all have to be built, maintained, and proven to auditors by us.

We want to reduce our PCI DSS scope and breach exposure by ensuring the application **never persists or even sees raw PANs**. The proposal is to adopt **tokenisation through a third-party PCI-compliant vault**: card numbers are exchanged for non-sensitive tokens, and only those tokens are stored in and handled by our systems.

## Decision

We will **stop storing raw card PANs in the payments database** and switch to **tokenisation provided by a third-party vault**.

Key points of the decision:

1. **Tokens only in our systems.** The payments database and application will store and operate on opaque tokens, never raw PANs. The token is meaningless outside the vault and cannot be reversed to a PAN without the vault.
2. **Card capture bypasses our backend.** Card data is captured and sent directly to the vault (e.g. via hosted fields / a client-side SDK or a redirect), so raw PANs do not transit or land on our application servers. Our backend receives a token in return.
3. **Operations use tokens.** Subsequent operations (charges, refunds, recurring/repeat payments, settlement, reconciliation) are performed by passing the token to the vault/processor, which detokenises internally to reach the card networks.
4. **The vault is the system of record for card data.** The third party holds and secures the actual PANs and is responsible for the corresponding PCI DSS obligations on that data.
5. **Migration of existing PANs.** Existing stored PANs will be migrated into the vault (bulk import / tokenisation), the returned tokens stored against the corresponding records, and the raw PANs then securely purged from our database and backups.

## Consequences

### Positive

- **Reduced PCI DSS scope.** With no raw PANs stored or transiting our systems, the bulk of our environment can move toward a far smaller assessment footprint (e.g. SAQ A / A-EP style scope rather than full SAQ D), lowering audit cost and effort.
- **Reduced breach impact.** A compromise of our payments database yields only tokens, which are not usable card data. This materially lowers financial and reputational risk.
- **Less security plumbing to own.** Card-at-rest encryption, key rotation, and the heaviest cardholder-data controls become the vault provider's responsibility rather than ours.
- **Clean abstraction.** The application deals with stable tokens, which can simplify storage and reuse for recurring payments.

### Negative / Trade-offs

- **Third-party dependency.** We take a hard dependency on the vault provider for availability, latency, and correctness of payment operations. Their outage becomes our outage; their SLAs become our limits.
- **Vendor lock-in.** Tokens are typically provider-specific. Migrating providers later requires a re-tokenisation/migration exercise and provider cooperation.
- **Integration changes.** Front-end card capture, backend payment flows, refunds, and reconciliation all need to be reworked to use hosted capture and token-based calls.
- **Migration risk.** The one-off migration of existing PANs and their secure deletion is a sensitive, carefully-controlled operation that must be auditable and irreversible once complete.
- **Cost.** The vault/tokenisation service carries per-transaction or subscription fees, and there is engineering cost to integrate and migrate.
- **Residual scope.** The card-capture path (hosted fields / redirect integration) and the integration points with the vault remain in PCI scope and must still be assessed; scope is reduced, not eliminated.

### Follow-ups

- Select and contract a PCI DSS Level 1 compliant tokenisation vault provider; obtain their Attestation of Compliance (AoC) and responsibility matrix.
- Design and validate the card-capture integration (hosted fields vs. redirect) to keep PANs off our servers.
- Plan and execute the migration: bulk tokenisation of existing PANs, token backfill, then verified secure purge of raw PANs from the database and all backups.
- Re-baseline our PCI DSS assessment (SAQ type / scope) with our QSA following the change.
- Update incident response, data-retention, and logging policies to reflect tokens-only storage.
