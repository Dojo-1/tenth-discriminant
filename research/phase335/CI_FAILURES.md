# Phase335 — exact-head failure and correction ledger

## 16 November 2026: first exact-head verification

- Head SHA: `7f58c62c7bb89b83f51249d24f990be9cab6d5c3`.
- GitHub Actions: [run 43955279131](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43955279131).
- Exact source-jet Python controls: **PASS**, including D=3,7,163 and the sharp binary negative control.
- Lean compilation: **FAIL** at Phase335JetFiltration.lean lines 153 and 159.
- Diagnostic: `failed to synthesize Decidable ¬pairDvd 4 (originalHOrdinaryJet 3 ... (1, 0))` when `by decide` was used directly with the unexpanded custom Prop `pairDvd`.
- The general `odd_jet_filtration_equivalence`, `maximal_jet_two_step_to_source` and `sourceHJet_zero_divisible_by_four` declarations compiled and printed only standard logical axioms; the failing two negative-control declarations temporarily reported `sorryAx`, therefore **the whole file is not a checked proof at this head**.

### Controlled repair

Compute the original ordinary-jet *pair* as `(2,0)` with `decide` (decidable pair equality), rewrite the target, then discharge `¬ pairDvd 4 (2,0)` with `norm_num [pairDvd]`. This does not alter the source, derivative, modulus, theorem statements, ring, Gram, test or workflow.

**Promotion rule:** repeat exact-head CI including full source-jet integer tests, Lean module build and axiom inspection. Retain this failed receipt.

## Second verification — mathematical file compiled; workflow shell failure

- Source head: `760bbde1b459cb1f669b562b80700f5807c1a184`.
- [Run 43955819231](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43955819231) failed at the final axiom-inspection step.
- Original source-jet finite tests: **PASS**.
- Lean compilation of `Phase335JetFiltration`: **PASS**; all printed Phase335 theorem dependencies at build time were among `propext`, `Classical.choice`, `Quot.sound`, with no `sorryAx`.
- Failure source: GitHub workflow generated a `printf '%s\\n' \\` command with doubled trailing shell backslashes. The shell consequently tried to run the Lean `import TenthDiscriminant.Phase335JetFiltration` line as a command (`command not found`, exit 127).
- Correction: replace the generated-shell `printf` command with a simple quoted heredoc that writes the *same* Lean inspection statements; retain the theorem statements and all mathematical checks unchanged.
