# Phase62: checked prime-axis repair, conditional aggregate constant

**Standalone local PASS**, outside the production root and CI. Protocol
`10fca35` preceded source/execution, on a separate branch based at `b4cff27`.
No Phase61 source, budget, control or published CI was restarted or changed.

The fixed target comprises the actual binary-form axis identity, prime
factorization, finite prime-axis cardinal<=2, principal-axis emptiness,
conditional at-most-two-family accounting and the fixed D=12011 control.
All eight public theorem type prefixes and definitions are unchanged.

First build FAIL22.8003626s: a generic natural nonlinear tactic did not
prove natAbs(x)=1 from natAbs(x)^2=1. The audit rejected the incomplete
dependency; the full source/logs remain. One proof repair uses the existing
`Nat.pow_eq_one` lemma. Second build PASS22.7932198s. Total45.5935824s,
within3 builds/300seconds each/600seconds cumulative/8192MB; no stop or
reroll. Namespace audit18 logical/16 theorem/2 runtime declarations,
including generated/private logical declarations, allows only the standard
three axioms. The axis and conditional aggregate roots print only those.

`PHASE62_RAW.zip` contains8 exact raw files, read back against originals.
`verify_phase62_results.py` checks protocol ancestry, hashes, budgets,
unchanged statements, the exact one-line repair, audit output and unchanged
production proof files. It is an integrity check, not a Lean execution.

## What it proves and what it does not

Prime-axis symmetry gives at most two points per nonprincipal form;
the principal form contributes none. Thus h forms need at most2(h-1)
zero-row prime points, which is<=h for h<=2. The conditional finite-sum
lemma recovers the old h/4 allowance assuming the nonzero-row bounds and
four representations per counted prime. It does not establish either
input, identify forms with ideal classes, supply an excluded-prime B,
bound ramified primes, certify an old numerical campaign or lower a cutoff.
[Human proof and remaining paper geometry](TWO_CLASS_AXIS_GUIDE.md).
The Phase60 per-form counterexample remains valid and frozen.

## Reproduction

From repository root, pinned elan on PATH:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase62.ps1 build
python research/ender_radius_bridge/verify_phase62_results.py
```

The runner accounts for the saved attempts and caps future executions.
No additional build is needed merely to repeat this result. The local
Phase61 regression timeout remains INCOMPLETE even if a different remote
CI environment subsequently passes. No new reviewer or merge authorized.
