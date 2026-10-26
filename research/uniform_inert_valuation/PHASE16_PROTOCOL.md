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

## Execution (2026-10-24)

`ClassNumberInertBridge.lean` compiles the full targeted composition:
`smallPrimeNormLifting_of_classNumber_one` transports the Phase 11
residue map through the Phase 15 maximal-order equivalence, invokes
Phase 10's principal-kernel norm theorem, expands the generator in
the integral basis, and proves its principal norm nonnegative using
`4N=(2x+y)²+Dy²`. Thus absolute norm `p` is exactly norm `p`.
`smallPrime_nonsquare_of_classNumber_one` and
`rectangularTraceGram_valuation_of_classNumber_one` propagate the
strict local conclusion to the actual integer Gram with Ender's full
exponent. `fifteen_classNumber_ne_one` uses the registered
`D=15,p=3` root obstruction to ensure the global hypothesis was not
dropped. The first control script required an explicit concrete
field-positivity instance; this was repaired.

This does not prove Ender's chosen-radius cell count in Lean, his
analytic comparison, numerical certificate interpretation, or the
end-to-end class-number classification. The theorem is for the
squarefree `D≡3 (mod 4)` field chart and strict odd-prime range;
no even-discriminant case or endpoint equality is inferred.
