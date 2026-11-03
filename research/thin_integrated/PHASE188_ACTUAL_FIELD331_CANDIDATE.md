# Phase188 — a candidate actual-field endpoint, contingent on two source bridges

*3 November 2026 · explicitly a theorem target, not an accepted numerical bound.*

The temptation after seeing the scalar contradiction at $331^4$ is to report a new field bound. That would skip the most demanding part of the argument: showing that the analytic upper and arithmetic lower constrain **one and the same positive integer**. This phase keeps that obligation visible rather than treating a scalar mismatch as a theorem about an unrelated determinant.

## Original source and what is not being changed

Fix the original $Q_D$ thin ellipse, $R=\lfloor D/4\rfloor$, $S=\lfloor R/25\rfloor$, and original integer ordinary-$Z$-jets of $Z^r W^s$ with $W$ held fixed. With the original trace-channel weights $2,2D$, form

~~~math
E_D=E_{Q_D},\qquad
B_D=\mathrm{diag}(2,2D,\ldots),\qquad
G_D=E_D B_D E_D^{\mathsf T}.
~~~

This $G_D$ is an **auxiliary integer trace Gram**, not the number-field discriminant. The existing odd/even maximal-order chart and arbitrary quadratic-field equivalence are the bridge to the final invariant. No new prime, weighted source, alternative support or equality of padded and thin Gram determinants is introduced.

## The intended contradiction

The original odd squarefree class-number-one hypothesis, if it persisted for $D\ge331^4$, would imply, using **the same** $G_D$:

~~~math
\frac{999997}{1000000}\log D-\frac{5739}{1000}
+\frac14\log 2
\;\le\;
\frac{\log\det G_D}{R^2S}
\;\le\;
\frac45\log D-\frac{1849}{2000}.
~~~

The sound Phase183 logarithm enclosure and old lower bound for $\log2$ make these expressions strictly disjoint when $D\ge331^4$. The conservative positive gap at the floor is **0.000305376**; this is far less forgiving than the earlier 375 comparison.

The intended [ActualField331.lean](../../lean/TenthDiscriminant/ActualField331.lean) does not repeat the whole determinant proof. It imports the separately verifiable bridge declarations:

- **Phase183 / Phase184:** original interpolation and positive original thin Gram.
- **Phase185:** recovered original odd-prime mass at the 331 domain.
- **Phase186:** original same-Gram lower with the existing binary divisor counted **once**.
- **Phase187:** original same-Gram normalized analytic upper with the inherited Hadamard/radial saving.
- **Phase183 scalar:** exact logarithmic non-overlap, without the false extra $0.098$ reserve.

Only when the above imports are compiled and their audit accepted can the odd contradiction be carried through the pre-existing even-parity chart and arbitrary totally complex quadratic-field equivalence to the **actual** absolute field discriminant. The numeric target is $331^4=12{,}003{,}612{,}721$.

## Evidence and stop rules

- **P:** the merged $375^4$ actual-field Lean theorem on main, and the earlier isolated 331 scalar/geometry/positivity/odd-source components within their stated domains.
- **H:** the Phase186/187 conjunction and this Phase188 field theorem until exact-head Lean and full source/axiom/negative-control tests pass.
- **A:** any existing permitted axioms in the imported library remain subject to explicit audit; zero Lean admissions alone are insufficient.
- **R:** treating the abstract scalar separator or a normalized residual from a changed reference lattice as an actual-field proof.

**Kill conditions:** if either original-Gram bound fails at the 331 domain, if the stricter scalar margin is eaten by an altered analytic error, if the proof imports an unproved 375-domain theorem as if it held at 331, or if the maximal-order field transport changes the claim, leave this branch unmerged. Never promote the numeric endpoint merely because the source has a theorem-shaped declaration.

The independently reconstructed mathematical argument remains an external requirement tracked by [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50). A successful Lean build validates the precise encoded declarations relative to permitted assumptions; it is not peer review, priority, or a new classification.
