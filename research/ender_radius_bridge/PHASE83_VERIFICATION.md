# Phase83: closed weighted-kernel estimate

**Accepted locally, standalone.** `ClosedKernel.closed_count_kernel`
replaces the finite kernel by an explicit formula, and
`closed_actual_gram_budget` composes it with the original derivative Gram.
The [human guide](CLOSED_KERNEL_GUIDE.md) explains the exact affine identity,
separate constant payment and conservative harmonic estimate.

Base: `a4a6fe1b32dbc8bf182e160155c0bec6e69ba0ae`.
Registration: `0c8c592385f54b3e8e4d4eb7030ee2a5bf7feef0`, before source/execution.
No production mathematical file, root import, tool, certificate, pin or CI
gate changed. This source imports frozen root82 plus pinned harmonic bounds.

| Invocation | Exit | Seconds | Result |
|---|---:|---:|---|
| First | 1 | 50.0273877 | Count-majorant division normalization failed; audit and transitive check rejected sorryAx. |
| Second | 0 | 48.7966777 | All statements, composition, controls and checks passed. |

Total98.8240654seconds; each cap600seconds/8192MB, cumulative cap1200.
No internal/outer resource stop. The sole repair inserts
`simp only [div_eq_mul_inv] at hs ⊢` before the existing `nlinarith`.
All11public theorem statements,2definitions, other proof bodies,
controls and reporting are byte-identical across attempts. No target
rerun after acceptance. The first failure remains in the8-file raw archive.

The full standalone invocation from `lean/` was:

```sh
lake env lean -j 1 ../research/ender_radius_bridge/Phase83ClosedKernel.lean
```

It includes the namespace audit (28logical declarations/26theorems,
0runtime-only), four controls and fresh transitive inspection of the final
composed root. The closure visits57,618declarations and excludes the same
34 named h1/older-cutoff/classification/finite-answer inputs as82.
Root axioms are exactly propext, Classical.choice, Quot.sound. Controls
check L=3, zero slope, a constant count's exact payment, and nonnegativity
of the closed endpoint. Warnings about unused nonnegativity guards on
that last control are retained; no linter suppression was added.

Lean4.19.0 and Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b remain pinned.
[Manifest](PHASE83_RESULTS.json), [raw evidence](PHASE83_RAW.zip),
[registration](PHASE83_PROTOCOL.md). Verify saved evidence from the root:

```sh
python research/ender_radius_bridge/verify_phase83_results.py
```

The verifier also checks the frozen integrated82 evidence. It does not
rerun Lean. The earlier input-cap discrepancy stays recorded there.
No new whole-library/root CI run was registered for this standalone cycle;
82's 5058/4285/16993 audit remains its own historical result. There is no
external exact-head CI or independent human review for83.

The effective closed estimate now depends explicitly on actual M(K).
Its transport to D, even-chart/field transport and numerical strict
cutoff remain open. No new numerical range, optimality or full
classification is claimed. README remains61lines.
