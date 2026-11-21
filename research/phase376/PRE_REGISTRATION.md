# Phase376 — independent public-key witness and revocation-time semantics

**21 November 2026 · Research-only preregistration. Parent:** Phase375 draft PR #285,
frozen head \`e2ea3fa36f3f6ba1824f1d38d04747f2c4d46626\`.
No change to the original Phase367 integer trace-Gram source.
No public-main merge or field-claim promotion.

## Honest starting point

Phase375's FOCUSED Lean/Python/Prolog workflow #44822289151 succeeded
(30 Python tests and 17 GNU Prolog counterworlds). Its separate broad
root workflow #44822330911 **FAILED** at \`UNAUDITED_PROJECT_MODULES\`:
Phase371–375 modules were not on the project's full-root dependency
audit allowlist. That root failure is neither fixed nor bypassed by this
PR; all new Lean results remain focused research-branch P only once
their exact-head kernel/axiom gates pass. Do not claim root certification.

## Distinct questions (do not conflate)

1. Was the original task eligible under the *original* policy? (Phase375)
2. Did an alleged issuer sign an origin-record envelope using an
   authorized, independently enrolled public key? (new bound fixture)
3. Did a *different public key*, authorized for policy migration,
   sign the new policy transition? Different actor names alone are not
   evidence of different principals.
4. Had either key been revoked at the current decision time?
5. Did a distinct governance public key sign a revocation effective
   NOW, rather than backdating or falsifying a past acceptance?
6. Is the *historical accepted record* preserved, without permitting
   a second approval after revocation?

A signed envelope proves possession of its private key **given** a trusted
public-key registry. It does NOT prove signer independence, meaningful
identity, trusted timestamps, mathematical correctness or institutional
review by itself.

## Frozen formal hypotheses

Lean module \`Phase376IndependentWitness.lean\` defines \`Credential\`,
\`ActiveAt c t\`, \`AuthorizedAt issuer approver tick\`,
\`RevocationWitness\` for an independent guardian, and
\`WitnessedMigration p q\` retaining Phase375's original permit.

\[
\operatorname{ActiveAt}(k,t)\iff
t\ge \operatorname{registeredAt}(k)\;\land\;
\forall r,\ \operatorname{revokedAt}(k)=r\Rightarrow t<r.
\]

Under *symbolically supplied* revocation state and clock, prove:
- A key with cutoff r cannot grant NEW authority at any t≥r.
- Different actor aliases with the SAME public-key fingerprint
  cannot construct an independent-approval witness.
- A revoked issuer or approver cannot authorize a fresh migration.
- A historical acceptance retains its old policy permission even
  after a later registry change; no historical signature is silently
  converted into a new authorization.
- A registry clock rollback is rejected under an assumed monotone
  watermark.
- Positive control: an example credential is active at t=6 and
  inactive at t=7 if revoked at t=7.

This is NOT an Ed25519 proof, a universally trusted time source or
a theorem about live PKI.

## Runtime protocol and bounded falsifiers

\`revocation_gate.py\` uses real Ed25519 verification from a pinned
\`cryptography\` release but uses **locally generated fixture keys**:
issuer, approver and independent revocation guardian.
A \`SignedOrigin\` must verify BEFORE the Phase375
\`register_origin\` eligibility gate. \`SignedMigration\` must pass
both live issuer/approver status AND the inherited Phase375 signed
version/source/scope/clock/budget/replay checks. A guardian may revoke
another key effective at the currently observed registry tick, but may
not sign a backdated or future revocation. Clock rollback, duplicate
key aliases, new approvals after revocation, forged signatures, wrong
roles, changed phase/source, false historical fast tasks and self-
revocation are fail-closed.

**Temporal semantics chosen deliberately:** A valid accepted migration
remains in the historical record after revocation. Its validity as
historical evidence does not entitle anyone to a fresh approval. This
research fixture fails closed for new migrations if either the
historical issuer or the current approver is now revoked. That choice
is more restrictive than some production PKI policies, and cannot
establish whether a real signature was forged before compromise.

The registry is an **UNAUDITED LOCAL INPUT** and the integer tick is a
**CALLER-SUPPLIED LOCAL CLOCK**. No external root of trust, secure
enrollment, independent signer, live GitHub reader, revocation
transparency log, HSM, trusted monotonic time, certificate chain,
quorum, or real signer revocation exists here. The Python event list is
not independently append-only. Treat every successful test as bounded
implementation M, never production authority.

GNU Prolog enumerates 20 bounded symbolic cases to distinguish
historical acceptance, new admission, aliases and rollback. It does
not perform cryptography, clock authentication or field review.

## Stop / kill conditions

- A signer with a different *alias* but identical public key passes.
- Revoked issuer or approver can authorize a NEW migration at/after
  cutoff, or a backdated notice rewrites a historical acceptance.
- The same key can create a purportedly independent governance revocation.
- A task unauthorized under Phase374 becomes retroactively eligible
  after changing native clocks in a later policy.
- A source guard closure upgrades the 301^4 number-field claim.
- A focused CI build is misrepresented as full-root proof-audit acceptance.

## Evidence classification and next external gate

P: only exact-head Lean-checked symbolic statements once CI succeeds.
M: 32 synthetic Ed25519 Python tests and 20 finite Prolog tests,
if exact-head execution confirms.
H: trustworthy enrollment/identity, role separation in the real world,
external anchored revocation state, independent timestamps, durable event
lineage, empirical improvement of the research bandit.
[R]_formal: no Lean-to-Python extraction proof.
[R]_attr: no independent key custodian or signed external policy registry.
[R]_transport: Phase371 fast/meso authorization mismatch and live time mappings.
[R]_sem: independent quadratic field/maximal-order source-to-field review,
issue #50; no claimed 301^4 field theorem or Siegel-zero consequence.

The next deployment experiment must enroll issuer/approver/governor keys
outside the policy runtime, record verifiable revocation timestamps in
an append-only external system, and compare accepted/rejected live
migrations against a held-out oracle. Do NOT substitute our own synthetic
test keys for that external validation.
