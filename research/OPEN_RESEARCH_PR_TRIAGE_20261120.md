# Open research PR triage — 20 November 2026

**Snapshot only.** Query GitHub for live check and merge status. There were 18 open PRs when this table was assembled; none is approved for automatic mainline promotion. Distinguish proof compilation from research lineage, source semantics and external review.

## Publication and source-to-field gate

| PR | Research | Triage |
| --- | --- | --- |
| [#268](https://github.com/Dojo-1/tenth-discriminant/pull/268) | Phase360 unified original-Gram 302^4 arithmetic + analytic + field theorem | Draft: fresh exact-head combined-root Lean and source-fidelity audit; then **research-parent only**. Independent issue #50 still open |
| [#232](https://github.com/Dojo-1/tenth-discriminant/pull/232) | Phase350 307^4 complete-root audit and 54 former unaudited modules | Exact-head Lean checked, but underlying field semantics still need human review; avoid propagating to main |
| [#223](https://github.com/Dojo-1/tenth-discriminant/pull/223) | Historical Phase346–349 307^4 stack | **Lean failed** at the last inspected head. Historical/superseded by Phase350 check; do not merge before repair/lineage reconciliation |

## Conductor, kernel and transport experiments

| PRs | Research | Why retained open |
| --- | --- | --- |
| [#229](https://github.com/Dojo-1/tenth-discriminant/pull/229) | E24–E27 integral frame transport and nested partial inverses | Base **main**: require an explicit research-only retarget/review; no implicit public claims |
| [#230](https://github.com/Dojo-1/tenth-discriminant/pull/230), [#231](https://github.com/Dojo-1/tenth-discriminant/pull/231) | E28/E29 residue frames and graded reconstruction | Stacked research parents; inspect source-kernel vs target-cokernel semantics and root closure |
| [#233](https://github.com/Dojo-1/tenth-discriminant/pull/233), [#234](https://github.com/Dojo-1/tenth-discriminant/pull/234) | E30 finite-depth kernel transition variants | Parallel child branches; reconcile duplicated E30 naming and counterexamples before consolidating |
| [#238](https://github.com/Dojo-1/tenth-discriminant/pull/238) | E33 conductor source-kernel versus target-cokernel sequence | Research-only algebraic semantics; not an arithmetic prime factor of original Gram |
| [#246](https://github.com/Dojo-1/tenth-discriminant/pull/246) | E41 all-depth conductor-kernel projection cancellation | Separate from nonzero finite-level kernels and from full original source arithmetic |

## Genuine original-Gram divisibility and derivative clocks

| PRs | Research | Review frontier |
| --- | --- | --- |
| [#239](https://github.com/Dojo-1/tenth-discriminant/pull/239), [#240](https://github.com/Dojo-1/tenth-discriminant/pull/240), [#241](https://github.com/Dojo-1/tenth-discriminant/pull/241) | E34–E36 original integer-Gram p² factor, ordinary-jet row certificate, unimodular moving frame | Check exact integral row transformation on the **complete original** thin ellipse before interpreting a small example as a uniform field-bound gain |
| [#242](https://github.com/Dojo-1/tenth-discriminant/pull/242), [#247](https://github.com/Dojo-1/tenth-discriminant/pull/247) | E37/E42 general integral Gram factor theorem and maximal-minor inheritance | Respect theorem hypothesis of actual original source evaluation and matrix factor, not ambient conductor loss |
| [#243](https://github.com/Dojo-1/tenth-discriminant/pull/243), [#245](https://github.com/Dojo-1/tenth-discriminant/pull/245) | E38/E40 bounded exact ordinary-jet valuation clock tests | Finite-oracle M vs Lean P distinguished; not a new asymptotic p-factor |
| [#252](https://github.com/Dojo-1/tenth-discriminant/pull/252) | E39 complete two-real-point Gram separation | Patch also touches E41 and an oracle; source-clean integration recommended instead of merging incidental changes |

## Integrated controls this round (do not reopen without new evidence)

- [#235](https://github.com/Dojo-1/tenth-discriminant/pull/235) E31 original-Gram counterexample: ambient conductor kernel does **not** imply 5 | det.
- [#237](https://github.com/Dojo-1/tenth-discriminant/pull/237) E32 nonreduced source versus reduced split target.
- [#250](https://github.com/Dojo-1/tenth-discriminant/pull/250) E37 legitimate unimodular certificate and universal impossible-source obstruction.
- [#251](https://github.com/Dojo-1/tenth-discriminant/pull/251) E38 every finite kernel nonzero but compatible integer-representative kernel thread zero.
- [#264](https://github.com/Dojo-1/tenth-discriminant/pull/264) E46 consolidated observer family; historical conflicting E42 PR #254 closed as superseded.
- [#265](https://github.com/Dojo-1/tenth-discriminant/pull/265), [#267](https://github.com/Dojo-1/tenth-discriminant/pull/267) Phase358 and Phase359 302^4 upper/actual field research results; **not public main or externally refereed**.

## Merge discipline

1. **No bulk-merge** based on CI color alone. Inspect exact-head successful Lean, allowed transitive axioms, source math and negative controls.
2. For overlapping ancestor/child branches after a squash merge, create a **source-clean consolidation** and re-run CI at its new head; do not force-conflict-merges or duplicate source modules.
3. No public-main promotion of a stronger actual-field discriminant claim until independent mathematical review #50, reproducibility, and source-to-field verification are settled.
4. Archive rather than delete falsification evidence. A failed or superseded proof is research provenance, not waste.
