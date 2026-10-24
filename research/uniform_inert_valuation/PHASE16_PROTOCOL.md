# Phase 16 preregistration: class number one to local inertness

Date: 2026-10-24. Base: draft PR #28 head `cf1c9db`, pinned CI
`40043319145` and CodeQL passed. This protocol precedes proof edits.

## Exact target

For squarefree `D ≡ 3 (mod 4)` and odd prime `p`, prove in Lean that
class number one of the actual field from Phase 15 implies
`SmallPrimeNormLifting D p`. Compose:

1. a root of `X²+D` mod `p` gives the Phase 11 quotient of the
   explicit order;
2. the Phase 15 ring equivalence transports it to `𝓞_K`;
3. Phase 10 gives a principal element with absolute norm `p`;
4. the Phase 15 norm formula and positivity of the imaginary
   quadratic form turn absolute norm into exact norm `p`;
5. Phase 9 then excludes strict small roots and supplies the
   nonsquare guard for the actual integer Gram valuation.

The complete target is the class-number-to-local valuation implication,
not merely another conditional norm lemma. Do not infer Ender's
analytic cutoff or a class-number classification from this local
implication without the area/analytic/finite chain.

## Controls and failure boundary

`D=15,p=3` has a residue root and fails unconditional norm lifting.
The theorem must therefore retain class number one; it should imply
`classNumber(K_15) ≠ 1`, or otherwise make the attempted unconditional
specialization fail. Preserve any failed proof or false strengthening.
The strict endpoint `p<(D+1)/4` is inherited unchanged; equality is
not asserted. Run targeted Lean, full pinned build, source
correspondence, compiled dependency audit and negative controls on
the proof head. Update human documentation; keep PR draft/unmerged.
