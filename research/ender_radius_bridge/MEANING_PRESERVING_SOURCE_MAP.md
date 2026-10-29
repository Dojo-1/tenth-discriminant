# Meaning that survives transport

Current branch: [Phase128](PHASE128_VERIFICATION.md) integrates the accepted47.5-billion successor, arbitrary-field classification interface and radial laws. All local checks pass; publication is separate. [Short current account](STRUCTURAL_BRIDGE_CURRENT.md).

The map below is the historical PR42/Phase122 baseline. Its failed attempt
[remains unchanged](PHASE122_VERIFICATION.md); the successful successor is a separate registered cycle, not a retry of that stopped source.

## One integer and two inequalities

[RadialOperator](../../lean/TenthDiscriminant/RadialOperator.lean) proves
`gram_congruence`, `gram_det` and `integral_inverse`: integer frame change
H=TGT^t, detT=1, preserves the original integer determinant. `real_posDef`
keeps explicit radius-independent point-count/depth guards; `reduced_rank`
compares frames modulo each prime, not real rank with reduced rank.
`integer_bridge` retains oddness/nonsquare hypotheses for its valuation.

[RadialDetBound](../../lean/TenthDiscriminant/RadialDetBound.lean),
`production_normalized_upper`, bounds log(detG)/(R^2S) by 0.8 log D - 0.823.
[RadialCutoff](../../lean/TenthDiscriminant/RadialCutoff.lean),
`prime_mass_log_lower` and `recovered_mass_le_actual_log`, refer to THAT
integer. `recovered_normalized_lower` gives 0.999997 log D - 5.739.
The [human proof](FORTY_EIGHT_BILLION_GUIDE.md) explains their contradiction.
No improved inequality is inferred merely from determinant conservation.

## Classification: what exists and what needs composition

[ClassNumberClassification](../../lean/TenthDiscriminant/ClassNumberClassification.lean)
proves `imaginaryQuadratic_classNumber_one_iff` for positive squarefree d:
h(Q(sqrt(-d)))=1 iff d is in 1,2,3,7,11,19,43,67,163. Both directions use
actual class number. Its finite coverage depends on `phase36_all_fibers`,
not on finite sampling or a fresh shortened 48-billion certificate campaign.
Its discriminant-membership theorem concerns the same canonical fields.

[ImaginaryQuadraticRepresentation](../../lean/TenthDiscriminant/ImaginaryQuadraticRepresentation.lean),
`exists_squarefree_root_of_totallyComplex_degree_two`, supplies positive
squarefree d and a root in any totally complex degree2 number field K,
without a class-number premise. [QuadraticGeneratorBridge](../../lean/TenthDiscriminant/QuadraticGeneratorBridge.lean),
`imaginaryQuadraticEquivOfRoot`, constructs Q(sqrt(-d)) equivalent to K.
[QuadraticChartEquivalence](../../lean/TenthDiscriminant/QuadraticChartEquivalence.lean),
`classNumber_one_of_field_equiv`, carries h=1 in either direction by using
the equivalence or its inverse. Mathlib `NumberField.discr_eq_discr_of_algEquiv`
transports the actual signed discriminant, as used by the final 48-billion theorem.

A natural NEW API target is h(K)=1 iff there exist positive squarefree d
in the nine-element list and a rational algebra equivalence from the canonical
field to K. The existing ingredients suggest this composition; no new Lean
proof or independent semantic review of that statement is supplied here.
Uniqueness of the representative is a separate claim. A signed-discriminant
membership implication is weaker than a full iff and must be labelled so.

## Which operators already compose?

[PassiveTransport](../../lean/TenthDiscriminant/PassiveTransport.lean) has
`translate_zero`, `translate_add`, `translate_inverse` and `translate_map`.
These are actual bivariate polynomial laws over commutative rings; covariance
of ordinary jets is supplied separately. Reproving these is unnecessary.

RadialOperator supplies an adjugate inverse witness. Its present module does
NOT expose general `matrix(a)*matrix(b)=matrix(a+b)` or inverse=`matrix(-a)`.
The earlier finite checks do not prove these universal laws. A future bounded
proof can use the binomial row formula and coefficient convolution, including
empty rectangles. It must distinguish integer-linear action from multiplication
of polynomials: no ring automorphism, new prime exponent or curvature follows.

The determinant cannot detect every frame change around a loop. Track the
operator, jets and guards too. Literal translated samples with fixed observables
can change the determinant; passive translation moves both together.

## Next decisions

The fixed endpoint test stopped after one elaboration failure; its preserved
outcome does not replace 48 billion. Next choose classification composition or
radial action laws as a separately scoped proof cycle. Independent review of
new mathematics remains open; the older 50-billion review is not transferred.
