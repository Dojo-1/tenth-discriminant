# Phase149 — Positivity-first prime mass on the same ordinary-jet Gram

**Scope:** a narrowly typed Lean refactoring of the already established arithmetic lower bound, continuing Phases144–148 on the **single canonical branch `main`**. It neither changes the observation matrix nor proves a smaller discriminant cutoff. The exact current compile and axiom-audit status must be determined from the new commit's CI, not from a previous receipt.

The frozen mathematical object is the **original ordinary \(\partial_Z^j\) jet** observation matrix \(E_Q(D)\), differentiated with \(W\) held fixed, on the same integer support \(Q\). Its positive trace metric \(B_Q\) gives \(G_Q=E_QB_QE_Q^\mathsf T\). The existing [`RadialCutoff.lean`](../../lean/TenthDiscriminant/RadialCutoff.lean) wrapper previously used the sufficient guard
\[
2(R-1)+(S-1)<|Q|
\]
to obtain \(0<\det G_Q\) and then applied the independent arbitrary-\(Q\) inert-prime divisibility theorem. This guard is **not** a necessary rank characterization; the matched finite Phase144 and Phase147 studies give explicit counterexamples to necessity.

## Minimal theorem interface

The new declaration `RadialCutoff.prime_mass_log_lower_of_det_pos` states, in the original types and under all the original field hypotheses,
\[
\boxed{\quad
0<\det G_Q\ \Longrightarrow\
\mathrm{exactOddPrimeMass}(R,S)\le \log(\det G_Q).
\quad}
\]
Its full assumptions still include \(D>0\), \(R,S\ge1\), \(D\bmod4=3\), squarefree \(D\), the specified quadratic-order class-number-one hypothesis, and the inert-prime range cutoff \(R<(D+1)/4\). These are **not** waived by positivity. The determinant on both sides remains precisely that of `integerRectangularTraceGram Q D S R S`, and no differently sampled or differently normalized Gram is substituted.

The proof body is the previous `prime_mass_log_lower` proof **unchanged except for the source of positivity**: its local `hz : 0 < z` now comes from the direct hypothesis `hdet`. Inert-prime valuation, prime-power product, cast to reals and logarithmic inequality are unchanged. The original `prime_mass_log_lower` declaration remains a thin wrapper, obtaining `hdet` from `integer_det_positive` under the old strict cardinality guard. Consequently old callers preserve their assumptions and the old field endpoint is not strengthened by fiat.

**Evidence governance:** if exact-head Lean CI plus allowed-axiom and negative controls pass, the *encoded positivity-first implication* is formally checked [P-formal]. Its applicability to any new production support remains [H] until an independent **uniform** positivity certificate for that same \(E_{Q(D)}\) is proved. Finite HNF certificates at \(D=13,\dots,25\) are [M] and cannot serve as a uniform field-level lemma; even a finite image equality does not transfer prime lower bounds between two different Gram integers.

## The remaining theorem bridge

One might derive positivity from a directly certified full-row-rank original observation matrix:
\[
x^{\mathsf T}G_Qx
= (E_Q^{\mathsf T}x)^{\mathsf T}B_Q(E_Q^{\mathsf T}x)>0
\quad(x\ne0),
\]
provided \(D>0\), the original \(B_Q\) is positive and \(E_Q\) has full real row rank. This is classical linear algebra **at paper level**, not a Lean theorem already constructed here. An integral Hermite certificate gives such rank **only for its finite frozen parameter**, not for all production \(D\).

Even a future uniform positivity theorem would not alone prove a sharper field-discriminant cutoff. It must be coupled with a uniform inverse-Gram-free analytic upper for \(\det G_{Q(D)}\), compatible with prime, ellipse, squarefree, and logarithm guards in the **same** argument. Any attempted shortcut that substitutes an \(\Omega_D\) bound into a new \(Q(D)\) without rebuilding the two sides must be retired.

**Reproduction:** run the repository [Lean workflow](../../.github/workflows/lean.yml) on the exact commit of this refactor, including source correspondence, entire library, allowed axioms and negative controls. Read original [Phase144–148 index](README.md) and the external semantic-review obligations [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50), [#51](https://github.com/Dojo-1/tenth-discriminant/issues/51). No PR #61/#62 merge or stronger actual-field claim is implied.
