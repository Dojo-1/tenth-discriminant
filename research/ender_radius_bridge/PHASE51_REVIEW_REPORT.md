Phase51 first returned review — bounded, read-only

Target: `69010f4e5d2e0adc44c70932d20583e669b7b7c2`.
Observed working HEAD: `7e6cd1ce5e7641746509ed0587180dd93e4cfbe5`.

The tracked Lean sources, root import, dependency declaration and toolchain match the frozen target: the corresponding `git diff --exit-code 69010f4... -- ...` returned zero with no differences. HEAD adds only the review protocol, brief and task state. There is an untracked `lean/lake-manifest.json`; it is not mathematical source. The inspected Mathlib checkout is at the declared revision `c44e0c8ee63ca166450922a373c7409c5d26b00b`, and the inspected dependency files have no reported changes.

Dispatch marker supplied: `2026-10-25T19:44:52Z`. Final read-only inspection timestamp: `2026-10-25T19:47:16.4020468Z`. No edits, builds, experiments, delegation, external posting or CI operations were performed.

No contradiction established in these bounded checks of the new mathematical statements. One SLOPPY documentation finding follows. This is not exhaustive verification of the inherited proof.

Finding: SLOPPY — degree two has more than the single advertised use

Evidence:

- `research/ender_radius_bridge/CONJUGATION_BRIDGE_GUIDE.md:9–11` says degree two is used at “one specific field-theoretic step: identifying the fixed field with Q.”
- `lean/TenthDiscriminant/ImaginaryQuadraticRepresentation.lean:27–37` also installs the quadratic-extension instance before transporting conjugation.
- The invoked Mathlib theorem, `lean/.lake/packages/mathlib/Mathlib/NumberTheory/NumberField/Embeddings.lean:213–222`, requires `IsGalois`.
- Quadratic normality is supplied by `Mathlib/FieldTheory/Normal/Basic.lean:286–293`; quadratic Galoisness, with separability, by `Mathlib/FieldTheory/Galois/Basic.lean:521–526`.
- The quadratic hypothesis is separately used to obtain exactly two automorphisms at `ImaginaryQuadraticRepresentation.lean:15–20`.

Trigger and consequence: retaining total complexity while dropping degree two does not supply the normality/Galois premise used by this conjugation-construction route. Total complexity alone does not assert that an embedded field is stable under complex conjugation. Thus the guide’s “one specific step” wording compresses away a necessary earlier dependency.

This does not invalidate the exported theorem: its degree-two hypothesis is present and used correctly. The documentation should distinguish obtaining conjugation through quadratic Galoisness from showing that invariance under that conjugation means rationality. No proof repair is indicated by this finding.

1. Conjugation and rationality — RE-DERIVED

`ImaginaryQuadraticRepresentation.lean:22–53` constructs conjugation as follows. Degree two gives a quadratic extension of Q; characteristic zero supplies separability, hence Galoisness. An embedding and its complex conjugate agree on Q, so the embedding theorem produces an automorphism `sigma` satisfying
`phi(sigma x) = conjugate(phi x)`.

If `sigma` were the identity, the embedding would be real, contradicting total complexity (`:40–46`). Applying the displayed identity twice and using injectivity proves involutivity (`:47–53`).

The projector laws at `:55–71` have the correct dimension-independent types: `sigma` is a rational algebra automorphism, and involutivity is an explicit premise. These laws do not require degree two. Division by two is legitimate in a number field. They are not laws for an arbitrary set-theoretic involution.

For rationality, the proof does not merely assume that one involution has rational fixed field. It establishes that the entire automorphism group consists of identity and `sigma` (`:91–94`). Consequently `u²` is fixed by every automorphism (`:95–101`), and Galois fixed-field theory identifies that whole-group fixed field with Q (`:102–107`). The invoked Mathlib equivalence explicitly has this meaning at `Mathlib/FieldTheory/Galois/Basic.lean:482–487`.

The higher-degree failure is concrete: in `Q(i,√2)`, complex conjugation negates `u=i(1+√2)`, but
`u²=−3−2√2` is not rational. The projector laws still hold; the two-element whole-group argument does not.

Limit: standard embedding existence, separability and Galois theory were source-traced at their interfaces rather than re-proved from foundations.

2. Normalization and transport — SOURCE-TRACED, with the new normalization algebra re-derived

The strict sign step is sound. Nonidentity supplies an `x` with `sigma x≠x`; therefore `u=(x−sigma x)/2` is nonzero (`ImaginaryQuadraticRepresentation.lean:80–90`). Its complex image is nonzero, anti-invariance forces zero real part, and its imaginary part is nonzero. Thus its square is strictly negative, not merely nonpositive (`:108–134`).

The denominator clearing at `:139–177` uses:

- `A=q.num.natAbs>0`, with the positive numerator identified correctly;
- `B=q.den>0`;
- `q=A/B`;
- `B²q=AB=N`;
- `z=Bu`, giving `z²=−N`;
- `N=b²d`, with both `b,d` positive and `d` squarefree;
- `a=z/b`, giving `a²=−d`.

The Mathlib factorization theorem returns exactly these positivity and factorization premises (`Mathlib/Data/Nat/Squarefree.lean:302–303`). The proof explicitly establishes the nonzero denominator in K before the final division (`:173–176`). No class-number assumption constructs the generator.

`QuadraticGeneratorBridge.lean:16–37` sends the quotient root to the supplied root by an algebra homomorphism. Its injectivity comes from the field structure, and equality of the two finite rational dimensions gives surjectivity. No surjectivity or field isomorphism is assumed.

Actual class-number-one transport passes through the maximal integer rings and principality:
`QuadraticChartEquivalence.lean:96–104`. This is sufficient for the actual class-number-one predicate; it does not redefine class number using the chosen order.

Actual discriminant transport uses `NumberField.discr_eq_discr_of_algEquiv` at `QuadraticGeneratorBridge.lean:69`. Mathlib defines that discriminant using a basis of the ring of integers and transports its integral basis (`Mathlib/NumberTheory/NumberField/Discriminant/Defs.lean:33–52`). It is therefore the field discriminant, not the discriminant of `X²+d` or a possibly nonmaximal order.

The final theorem at `ImaginaryQuadraticRepresentation.lean:205–211` exposes only the stated field, total-complexity, degree and class-number hypotheses. Its root and squarefree representative are obtained internally. These new wrapper bodies contain no finite answer-list premise or circular classification input.

Limit: I traced the calls to the inherited 100-billion results at `TunedAnalyticCutoff.lean:213–241`; I did not reconstruct their complete analytic proof or exhaustively traverse their transitive dependency closures. Those inherited obligations remain CANNOT-VERIFY in this review.

3. Sign sectors and sample symmetry — RE-DERIVED

For an active ordinary derivative,
`derivativeRow(r,s,j,−z)=(-1)^(r−j+s) derivativeRow(r,s,j,z)`.
The definition keeps the conjugate factor fixed during differentiation (`TraceGram.lean:15–17`); the new proof implements precisely this convention (`CentralSymmetry.lean:10–17`).

When both derivatives are active, the product sign exponent is
`r+s+t+u−2j`, so opposite total-degree parity negates the pairing. The proof guards both natural subtractions by `j≤r` and `j≤t`; otherwise the product is zero (`:19–37`).

The integer pairing remains `2(ax bx+D ay by)` (`IntegerTraceGram.lean:75–81`). The new proof transports this same pairing through evaluation (`CentralSymmetry.lean:43–54`). No factor two is removed.

For each derivative order, negation bijects the original finite sample set and negates the summand. Therefore the sum equals its own negative and is zero in Z (`:58–83`). This handles the origin, arbitrary J including zero, zero derivatives, and empty samples without extra exclusions.

The generic exported theorem is specifically about finite sets of integer pairs. For `D>0`, the existing cast theorem identifies it with the original real Gram on distinct evaluated samples (`IntegerTraceGram.lean:95–110`). The ellipse instance has the required positive-D guard (`CentralSymmetry.lean:85–95`).

The singleton control is correct: with sample `(1,0)`, `D=J=1`, rows `(0,0)` and `(1,0)` both evaluate to one at derivative order zero, producing the nonzero entry two (`:98–101`).

Simultaneous negation changes signs without exchanging row labels or Z/W. It therefore preserves every rectangular row set, including thin rectangles.

Limit: no arbitrary-complex-sample public symmetry theorem or determinant-factorization API is exported here.

4. Arithmetic compatibility and guards — RE-DERIVED, with row-action identity SOURCE-TRACED

The actual coefficient matrix sums
`(-1)^t choose(k,t)` into original column `(r−pt)S+(s+t)`
(`RectangularBasisMatrix.lean:15–27`). Its exponent is
`k=min(floor(r/p),S−1−s)`
(`RectangularValuation.lean:17–24`).

On the active range, `pt≤r` and `s+t<S` are proved explicitly (`RectangularBasisMatrix.lean:30–49`). Thus natural subtraction represents genuine subtraction and the target remains inside the original rectangle. `RectangularRowAction.lean:82–94` recovers the actual quotient/remainder labels. The auxiliary `min` in the total finite-index function disappears on active terms.

For odd p, the degree change is `(1−p)t`, which is even. `ParityCompatibility.lean:18–49` uses the guarded bounds to establish zero coefficients across opposite parities before deriving commutation. Primality is unnecessary for this structural theorem; positive odd p is its actual guard.

Both concrete equations use the identical `rectangularSignMatrix R S` definition (`:9–16`, `:66–83`): the original Gram and the explicit arithmetic matrix commute with the same diagonal integer operator.

For `p=2,R=3,S=2`, row four is `(2,0)`, `k=1`, and its expansion is `Z²−W`. Column one is `(0,1)`, so its coefficient is −1 and the parities differ, exactly as asserted at `:85–89`.

If either rectangle dimension is zero, `Fin(R*S)` is empty. The statements are vacuous matrix identities; they do not require interpreting a nonexistent row label.

The integral sector interpretation is valid because the sign operator is explicitly diagonal in an integer coordinate basis. The rational expressions `(I±C)/2` simply select coordinates and preserve this lattice; no general lattice-divisibility assertion is needed.

The reached row-action theorem identifies this actual matrix with ordinary jets (`RectangularRowAction.lean:163–185`), rather than substituting a matrix sharing only its determinant.

Limit: inherited jet-power divisibility, unimodularity and Gram-factor constructions were not exhaustively re-proved.

5. Public claim boundaries — SOURCE-TRACED

The inspected current README introduction, STATUS Phase47–50 entries, and FORMALIZATION introduction match the exported hypotheses and conclusions. The one documentation dependency issue is recorded above.

The guides correctly separate structural consequences from exported APIs:

- Central-symmetry grouping gives block diagonal structure, without claiming an exported determinant-product theorem (`CENTRAL_SYMMETRY_GUIDE.md:28–31`).
- Compatibility of the transformed Gram is identified as a linear-algebra consequence (`PARITY_COMPATIBILITY_GUIDE.md:54–56`).
- Neither block structure nor commutation supplies an additional valuation or strict Hadamard saving (`CENTRAL_SYMMETRY_GUIDE.md:45–50`; `PARITY_COMPATIBILITY_GUIDE.md:60–64`).
- The normalization exports existence rather than a computational uniqueness API and does not identify every residue Frobenius with global conjugation (`CONJUGATION_BRIDGE_GUIDE.md:54–56,73–76`).

The current text distinguishes the earlier reviewed cutoff from the subsequently added representation modules (`lean/FORMALIZATION.md:45–52`). Historical weaker frontiers are explicitly retained as history. I found no current announcement of full general classification, an improved cutoff from symmetry, novelty, optimality, or independent human review.

CANNOT-VERIFY: numerical build timings, declaration counts, compiled input/axiom inventories, historical CI successes and the eventual outcome of CI `40227162534` were not independently validated. I observed no eventual CI result and make no assertion about it.

Scope conclusion

No FATAL or GAP finding was established in the four new modules. The SLOPPY finding affects the explanation of degree-two dependencies, not the public theorem’s assumptions or conclusion.

This report is one fresh-context AI source review. It establishes neither human independence nor model-family independence, full classification, exhaustive inherited proof verification, improved quantitative estimates, or publication readiness.
