# Phase168 — Making the generic theorem mathematically inhabited

An implication can be Lean-checked yet tell us nothing new if its
hypotheses cannot occur. Phase166's thin-ellipse specialization assumed
a class-number-one imaginary quadratic field past the already excluded
41.00625-billion threshold. We therefore test its **generic** arbitrary
original observation-support theorem where the number field *does*
exist.

Take the imaginary quadratic field **Q(sqrt(-7))**. The repository
already [proves that its actual class number is one](../../lean/TenthDiscriminant/SmallPositiveClassNumber.lean).
The checked [odd-field equivalence](../../lean/TenthDiscriminant/QuadraticChartEquivalence.lean)
transports this statement to the right maximal-order quadratic chart
`QuadraticField ((7+1)/4)=QuadraticField 2`. This matters: silently
substituting the nonmaximal order Z[sqrt(-7)] would invalidate the
class-number argument.

Choose `R=S=J=1` and the original integer-pair observation
`Q={(0,0)}`. Direct arithmetic yields the original positive one-row
Gram `[2]`. Here `R=1<(7+1)/4=2`, `D=7` is squarefree and congruent to
3 modulo 4, the checked binary exponent equals one, and the odd
prime product below one is empty. The source logarithmic bound
specializes to the exact equality

```text
(binary exponent 1) * log(2) + (odd mass 0)  =  log(det [2]) = log(2).
```

The [new Lean module](../../lean/TenthDiscriminant/SevenActualFieldWitness.lean)
is designed to prove **all** these premises in the correct field,
invoke the *existing* Phase166 arbitrary-Q theorem, and separately
calculate the equality directly. Thus the generic theorem becomes a
real field/sampling example rather than an already excluded high-D
conditional. It still cannot improve any large-D discriminant bound.

**Verification gate:** source-typed focused pinned-Lean compilation,
whole-library import, permitted-axiom, negative and security checks.
Every new declaration is **H / CI pending** until passed. The direct
one-node and empty-support arithmetic checks were previously
Lean-checked in [Phase167](../../lean/TenthDiscriminant/OneNodeTraceControls.lean).
A numerical equality and correlated Lean encoding do not replace
independent semantic review ([issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50)).

**Kill condition:** if maximal-order class-number transport requires an
unstated assumption or if the real source Gram is not the declared
integer one, reject the attempted realization. Never repair it by
changing the field or Gram.
