# Phase 9 preregistration: the small-prime norm-to-local guard

Date: 2026-10-23. Base: draft PR #27 head `e6241d1`, unmerged.
This protocol precedes all Phase 9 proof edits. It changes no saved
certificate, cutoff, sample set or numerical experiment.

## Exact bounded target

For `D : Nat` with `D % 4 = 3`, and an odd prime `p` strictly below
`(D+1)/4`, prove the following **conditional** bridge in Lean. Assume
that every root of `X²+D` in `ZMod p` yields integers `x,y` with
`principalNorm D x y = p`. Then no such root exists: a nonzero `y`
contradicts the existing norm lower bound, while `y=0` would make the
prime `p` an integer square. Translate absence of a root to the exact
`¬ IsSquare (-(D : ZMod p))` guard and compose with the Phase 8 theorem
to obtain the determinant power for the original integer Gram.

If the pinned Mathlib supports a clean polynomial statement, also prove
that this guard is equivalent to irreducibility of `X²+C D` over
`ZMod p`. Keep the norm-lifting premise visible in every public theorem.

## Falsifiers, limits and stop rule

Keep the strict endpoint: `D=163,p=41` is **not** covered; the norm
`principalNorm 163 0 1 = 41` is a boundary witness. Check a split
small-prime example fails the lifting premise rather than asserting a
false inertness conclusion. `D=19,p=3` is a positive local control.
Record proof-script failures and mathematical counterexamples. The
missing substantive theorem is that class-number one (for the *maximal*
order of fundamental discriminant `-D`) supplies the lifting premise
for all relevant odd roots, including ramified cases. Do not claim that
the conditional lemma proves it, or a cutoff/classification.

Run targeted Lean, full pinned build, source correspondence, compiled
dependency audit and inherited negative controls where feasible. Update
human guide and status with this exact boundary. Keep PR #27 draft;
never merge automatically.

## Execution record

`SmallPrimeBridge.lean` now proves the strict norm obstruction including
the rational (`y=0`) prime-square case, the exact polynomial
irreducibility/nonsquare equivalence, and the determinant consequence
by applying the existing Phase 8 theorem. The lifting hypothesis stays
syntactically visible. The `D=15,p=3` ramified small-prime control
proves this hypothesis cannot simply be omitted; `D=19,p=3` checks the
irreducible polynomial wording, and the pre-existing `D=163,p=41`
norm witness guards strictness at the endpoint.

First Lean attempt failed on `Int.natAbs` transport, `IsSquare`'s
equality orientation and the polynomial `C(-D)` rewrite. These were
proof-script normal-form errors, not counterexamples. The repaired
targeted file passes pinned Lean. Full build and pinned CI are reported
separately below rather than inferred from that targeted check.

Local checks: `lake env lean TenthDiscriminant/SmallPrimeBridge.lean`
passed; `lake build` completed all 6700 steps; `python
verify_sources.py` passed from `lean/` with its stated endpoint-only
scope. `git diff --check` passed. The first source-verifier invocation
from the repository root failed because that file lives in `lean/`;
the corrected invocation passed. Compiled dependency audit and inherited
negative controls await pinned Linux CI on the proof head.
