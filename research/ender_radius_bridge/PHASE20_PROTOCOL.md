# Phase 20 preregistration: the production Hadamard upper formula

Date: 2026-10-24. Base: draft PR #28 head `f7fe3cf`; pinned Lean CI
`40075949893` and CodeQL passed. This protocol precedes proof edits.

## Exact target

Relate the *actual* rectangular trace-Gram diagonal product to the
unchanged `tools/green_h1_ellipse.py:upper_B(R,S,J,n,B)` on its `R>B`
branch. Formalize that branch's exact real expression, including

`RS log(2nJ) + 2 log(B) [S R(R-1)/2 + R S(S-1)/2]`

and its exact derivative correction

`2 S(J-1) [R log(R/B)-R+B+log(R/B)]`.

Assume explicitly `B>=1`, `R>B`, `J>=1`, positive row dimensions,
all sample norms `<=B`, and `card P<=n`. Prove
`log(prod_i G_ii) <= upper_B` for the unchanged Gram, preferably with
strict inequality when warranted. Do not replace ordinary derivatives,
the factor-two trace, the row grid, or the production expression. The
finite prime-mass lower side from Phase 19 is already checked.

The sample-count upper estimate used by Ender's interval program,
`card(ellipsePairs D rho) <= pi*rho^2/sqrt(D)+2rho+M` with
`M=2 floor(rho/sqrt(D))+1`, is a *separate* still-open geometric arrow.
The final instantiated interval theorem must not be claimed until it and
the certificate interpretation are checked.

## Proof route and adversarial controls

Use the checked exact diagonal moment identity. Bound each ordinary
derivative by its falling factorial, `B^(r+s-j)`, then convert the
derivative correction to `max(0,log(r/B))`. Sum over the rectangular
grid. For `R>B`, justify the discrete correction using monotonicity
and a real integral (or another exact inequality); never replace it by
the larger `R log(R/B)` unless a renewed numerical campaign proves it
sufficient. Check `r=0`, `j>r`, `B=1`, and the empty/zero diagonal
obstruction when `n=0` or `J=0`; those guards cannot disappear.

If the full production inequality does not close, retain only checked
lemmas that are genuine subclaims of it, log the first precise obstruction,
and leave `upper_B` unverified in Lean. No `sorry`, new axioms, or
unproved numerical premise. Run targeted Lean, the full pinned build,
source correspondence, compiled dependency audit and negative controls
on the proof head. Preserve this draft PR and do not merge.
