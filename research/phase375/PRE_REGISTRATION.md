# Phase375 — Versioned policy transport and irreversible issuance history

**20 November 2026 · Research draft.** Parent: Phase374 PR #284 at
\`2d855c09bb4c48065261615554d78b560cd75fed\`.
Preserve the original integer trace-Gram source; no public main merge.

## Frozen question

When a research policy changes version, which authorizations survive explicitly
certified transport? Do not infer that a successful GitHub execution, a future
manifest permission, or a signature from a test-owned key retroactively
authorized the original task.

## Two typed policy dimensions

1. A scheduling permission depends on the arm, native-clock intersection,
   research tier, budget, human opt-in, contrast opt-in, and manifest version.
2. The arm's **meaning** consists of source, scope, Worldlet, execution
   authority, purpose, transport/remainder, hyperedge and native clock.
   Preserve these dimensions separately rather than reducing them to a score.
   A different cost is an explicit resource change, not hidden semantic
   equality: it must be signed with both old/new values and remain affordable
   under both versions.

Version identity in Phase374 is Git blob SHA-1 over exact manifest bytes;
the Python Phase375 prototype separately binds each policy to canonical JSON
SHA-256 and a strictly increasing **locally declared** version ordinal. No
cryptographic correspondence of these hashes or provenance of the declared
version number is proven.

## Lean theorem targets

Define typed \`ArmMeaning\`, \`Policy\`, \`FrozenPermit p\`,
\`MigrationEdge p q\` and \`TransportedView p q\`. An edge requires the old
permission, new permission, semantic equality, different symbolic issuer
and approver and an increasing version label.

Prove that transported evidence retains its ORIGINAL issuing policy,
that lawful edges compose under stated premises, and counterexamples to:
(a) retroactive \`fast\` source authorization after a newer permissive policy;
(b) migration through a changed original/D203 source;
(c) newly allowed target implying already-issued origin.

These are conditional finite/state-level statements, NOT Ed25519 verification.

## Python and Prolog falsification

The Python \`Snapshot\` is immutable serialized manifest bytes plus a SHA-256
digest. \`PolicyMigrationGate\` rejects an unregistered or originally ineligible
task, stale/changed policy identity, cost over budget, scope/source/native
clock/Worldlet/authority drift, same-issuer approval, altered Ed25519 signed
claim, unsigned/wrong-signer/replayed migrations and new policy permission
used to launder a historical fast-clock source task.

The key pairs in tests are SYNTHETIC. \`register_origin\` and
\`register_snapshot\` are untrusted local inputs. No authenticated GitHub
comment fetcher, real signer, trusted clock or independently controlled
policy authority is implemented. The Python gate does NOT consume the
Phase373 task into production: it tests policy migration permission only.

GNU Prolog enumerates separate hypothetical policy worlds (source/scope/
executor/native-clock/cost changes). These are finite countermodels,
not proof that a real external principal approved a migration.

## Kill conditions

- A new permission must never rewrite an old disallowed issuance.
- Target authorization without original authorization must be rejected.
- Permission must be checked in BOTH policy versions.
- A semantic change without a separately typed mapping and remainder cannot
  be called exact transport. This phase deliberately requires exact meaning.
- No issuer may approve its own migration merely by renaming its identity.
  Separate public-key custody remains an unverified external requirement.
- A migration must not promote mathematical status or borrow authority from
  the Phase306 D203 Worldlet.
- Independently reported GitHub CI success does not establish authenticated
  issuance, revocation handling or the 301^4 source-to-field theorem.

## Evidence floor

- P: Phase374 960-case finite Lean/Python policy certificate, relative to
  that encoding and frozen manifest.
- H: Phase375 until exact-head kernel compilation.
- M: synthetic Python/Prolog bounded tests only upon actual passing CI.
- [R]_transport: historical Phase371 fast/meso mismatch remains retained.
- [R]_attr: authenticated external policy version/issuance/signer identity.
- [R]_sem: original Gram → field arithmetic and 301^4 / Siegel-zero claims
  remain open in issue #50.
- [R]_formal: no verified extraction proving Python implements Lean at all
  inputs; Phase375 tests are a bounded implementation check.
- [R]_emp: no measured bandit allocation advantage.

## Reproduction

\`\`\`sh
python3 scripts/phase365_lean_anchor_guard.py
python3 -m pip install cryptography==46.0.4
python3 -m unittest discover -s research/phase375 -p 'test_*.py' -v
gprolog --consult-file research/phase375/version_counterworlds.pl --query-goal phase375_main
cd lean
lake build TenthDiscriminant.Phase375PolicyTransport
\`\`\`

All results must refer to the SAME exact commit, and the Lean
\`#print axioms\` output must be inspected before labeling any theorem P.
