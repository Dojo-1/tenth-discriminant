# Phase377 — Root audit reconciliation, not whitelist bypass

**21 November 2026 · Research-only preregistration.**

Parent is Phase376 [PR #286](https://github.com/Dojo-1/tenth-discriminant/pull/286),
head \`94ba275e932d257fa7162a39c6ed15588d0e517b\`.

## Actual observed obstruction

Phase375 [root workflow #44822330911](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44822330911)
FAILED after compilation, at \`lean/audit.py\` \`project_coverage\`,
reporting \`UNAUDITED_PROJECT_MODULES\` Phase371–375.
The script has **NO permitted-module allowlist**: it recursively traverses
\`import TenthDiscriminant.*\` from \`lean/TenthDiscriminant.lean\`, requires
all project files reachable, scans every module for forbidden proof escapes,
then executes \`lake env lean Audit.lean\` (which runs
\`#audit_namespace TenthDiscriminant\`) and executable negative controls.

The earlier account described an "allowlist" as shorthand. That was
imprecise. The gate is **project-root import graph reachability**.
Repair it by adding real root imports of exactly
\`Phase371CausalReceipt\`, \`Phase372ExecutionAttempts\`,
\`Phase373ClockAuthoritySquare\`, \`Phase374ManifestRefinement\`,
\`Phase375PolicyTransport\`, and \`Phase376IndependentWitness\`.
Do not modify the audit logic, permitted axioms, negative controls,
pinned compiler, Mathlib revision, field source or original Gram.

## Preregistered hypothesis

Adding all six explicit imports to the root (rather than exempting them)
will remove \`UNAUDITED_PROJECT_MODULES\`. The complete CI may then
expose further independent failures; those must not be renamed "success".

### Gates in increasing scope

1. **Static root coverage**: \`project_coverage\` reports the full module
   set, exactly matches an independently coded DFS import parser on the same
   repository, and all six are explicitly imported once.
2. **Negative controls**: remove fixture B from synthetic import root,
   add a cyclic import, add a missing C file, and introduce a source-level
   \`sorry\`; original audit must reject the intended false worlds.
3. **Unchanged source**: Phase365 textual integer-Gram source anchors
   must pass (only a consistency test, not a mathematical proof).
4. **Pinned full Lean build**: real root \`lake build\` must succeed.
5. **Environment-level proof audit**: unmodified \`lean/audit.py\` must
   report \`IMPORT_COVERAGE_OK\` and \`AUDIT_OK TenthDiscriminant:\`;
   only \`propext\`, \`Classical.choice\`, \`Quot.sound\` may occur in
   transitive dependencies; every source-level escape stays prohibited.
6. **False strengthening rejection**: existing
   \`lean/negative_controls.py\` must reject each known-false arithmetic
   and proof-audit null without an unrelated setup/type error.
7. **External semantic review**: separately reconstruct original
   integer trace-Gram → maximal order → class number. This is OUTSIDE
   Phase377 and remains open in issue #50.

A passing focused preflight is insufficient for a root proof-audit pass.
A green full-root CI proves only that all encoded project declarations
compile and meet its static/environment audit policies, not that the
number-theoretic theorem states a justified 301^4 bound about actual fields.

## Matched controls, corrections, and stop rule

Matched baseline: the exact Phase376 parent with focused
[CI #44900790848](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44900790848)
green and root proof audit pending/failed. No differences in theorem content.

Representation attack: reorder import statements while preserving
reachability; this should not alter the coverage set. This phase does not
claim that root proof time, memory or CI availability are performance data.

**Kill:** missing modules, any new forbidden axiom/escape, broken known-false
controls, unverified head, or partial CI. Stop and preserve the failing run;
do not demote the gate, invent a new ontology, or merge.

**Promotion:** Only after exact-head comprehensive root CI success AND
inspection of the actual logs can root-import closure be marked P
(relative to the Lean audit model). Internal source semantics, PKI and
number-field conclusions remain H. PR stays draft until external review.
No merge authorized.

## Corrected claim ledger

- Phase371–376 individual focused Lean proofs: P relative to formal encoding;
  not enough to satisfy the root.
- Phase375 comprehensive project certification: **R** for failed attempt
  #44822330911 (unreachable modules).
- Phase377 root coverage: H until exact-head root run.
- Historical fast/meso mismatch: [R]_transport still preserved.
- Independent approver/key custody: [R]_attr still open.
- Quadratic field 301^4 result: [R]_sem still open.
- Genuine bandit yield: [R]_emp unmeasured.

## Reproduce

\`\`\`sh
python3 scripts/phase365_lean_anchor_guard.py
python3 -m unittest discover -s research/phase377 -p 'test_*.py' -v
cd lean
lake build
python3 audit.py
python3 negative_controls.py
\`\`\`

The last three commands are the authoritative full-root acceptance sequence
and are already required by the existing \`.github/workflows/lean.yml\`.
