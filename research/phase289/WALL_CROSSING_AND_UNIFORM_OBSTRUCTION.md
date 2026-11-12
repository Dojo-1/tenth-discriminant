# Phase289 — wall crossing, exact normalized-gain collapse and typed moving frame

**Post-result synthesis, 12 November 2026.** Phase289-A original D283/D403 source, independent held-out D563, and post-result D563 transverse-layer ablation all passed their focused CI. The precise geometry of the change is now known. These are AI-authored mathematical derivations and bounded executable experiments, NOT independent human review, a new uniform theorem or a class-number-field cutoff.

## The wall where the support changes

The **ORIGINAL** complete centered ellipse is
`Q_D(rho)={(x,y) in Z²: x²+D y² <= rho²}`.
The allowed transverse y-layers are `|y| <= floor(rho/sqrt(D))`. A new pair of layers appears precisely when `rho² >= k² D`. At the three frozen original sources:

| D | rho | floor(rho/sqrt(D)) | exact counts by layer | total Q |
|---|---:|---:|---|---:|
| 283 | 31 | 1 | y0:63; each y+/-1:53 | 169 |
| 403 | 40 | 1 | y0:81; each y+/-1:69 | 219 |
| 563 | 51 | 2 | y0:103; each y+/-1:91; each y+/-2:37 | 359 |

The D563 5-layer original source has 700 polynomial rows and 359 observations. The **counterfactual** 3-layer source Q3 has 285 observations, still passes the ORIGINAL row-interpolation sufficient guard `285>2(R-1)+(S-1)=282`, and keeps *all 700 original polynomial rows, j=0..4 ordinary derivatives, original 2/2D trace metric and the same 36 quartet partition*. Q3 is a DIFFERENT finite source and may NOT replace the original Q359 in the number-field theorem.

## Exact intervention and quantitative statement

The preregistered holdout [CI #43247424896](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43247424896) found ORIGINAL D563 `K_full=179` and 36 strict quartets; approximate incremental gain \(L_{full}/(R²S)\approx0.001386825\).

The *post-heldout* preregistered ablation [CI #43248582258](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43248582258) found THREE-LAYER D563 `K_three=2138`, also 36 strict quartets, approximate incremental gain 0.0152484655. Original five-layer and ablated three-layer Gram matrices differ **exactly** by the positive-semidefinite trace Gram of the deleted 74 y=+/-2 observations, checked on a frozen quartet; the matrix identity holds for all original rows by the definition of E and B. There is no theorem that adding a positive-semidefinite observation block must increase or decrease a RATIO of Fischer block products.

Let `V_pair(Q)` be the old Phase206 matched two-fiber product and `V_four(Q)` the new nested four-fiber product evaluated on the SAME Q. The integer dyadic rule already checks for EACH strict quartet:
`2^k < (detA detB)/detG4 <= 2^(k+1)`.
Multiplying disjoint quartet ratios gives
`2^K < V_pair(Q)/V_four(Q) <= 2^(K+N_strict)`.
Hence the **actual supported ratio of gains** at D563 obeys the exact, floating-point-free inequality

`[V_pair(Q_three)/V_four(Q_three)] /
 [V_pair(Q_full)/V_four(Q_full)]
 > 2^(2138-(179+36)) = 2^1923.`

This is a **strong source-intervention observation**, NOT a claim that the determinants of the two DIFFERENT sources have any p-local transport equivalence.

For the ORIGINAL D563 source itself, its normalized extra analytic saving satisfies
`L_full/(R²S) <=215 ln2/98000 <215/98000 <43/10000`.
Thus the historical proposal that **this particular four-fiber incremental construction** always yields normalized saving >=0.0043 is **REFUTED** by a valid larger original source. No similar statement about other analytic constructions, or the actual field discriminant theorem, is refuted by this one experiment.

## Source-covariant wall-crossing algebra [P-paper]

Fix D,R,S,J and any centrally symmetric finite supports `Q_minus subset Q_plus`, with added points \(\Delta Q=Q_+\setminus Q_-\). Keep the same original row module and ordinary-jet metric. Then

\[
G_+ = G_- + \Delta G,\qquad
\Delta G = E_{\Delta Q} B_{\Delta Q} E_{\Delta Q}^{T}\succeq0.
\]

If both G_- and G_+ are positive definite, the discrete "transport" along a support wall has a precise determinant update
\[
\log\det G_+ - \log\det G_-
 = \log\det\big(I+G_-^{-1/2}\Delta G G_-^{-1/2}\big)\ge0.
\]
But for the new four-block ratio the wall increment is a **signed difference of three nonnegative updates**:
\[
\Delta L_{\cal B}
=\log\frac{\det A_+}{\det A_-}
 +\log\frac{\det B_+}{\det B_-}
 -\log\frac{\det G_{4,+}}{\det G_{4,-}} .
\]
Its sign is NOT determined by Loewner monotonicity. The **exact** ablation exhibits a large negative total increment when the y=+/-2 source layers are added. Each added pair of layers is itself Noether-inversion invariant, so central parity remains an exact symmetry across the wall, but the canonical-correlation spectrum can change sharply.

This is a **discrete support wall crossing**, not smooth adiabatic evolution of a constant-rank observation bundle. Phase287's real positive-gapped rotating Hamiltonian and Phase288's fixed integer row lattice remain distinct; no p-adic Smith transport through a changed support is claimed.

## A hard asymptotic obstruction

For the ORIGINAL production source, \(\rho_D\sim(11/25)D^{3/4}\) while \(R\sim D/4\), \(S\sim D/100\). Consequently
\[
\left\lfloor\rho_D/\sqrt D\right\rfloor
\sim (11/25)D^{1/4}\to\infty.
\]
A family restricted to a FIXED number \(2m+1\) of y-layers has at most \((2m+1)(2\rho_D+1)=O_m(D^{3/4})\) points, whereas the existing source rank/interpolation guard requires \(2(R-1)+(S-1)=\Theta(D)\). Hence **a fixed three-layer ablation cannot satisfy that sufficient guard in the production limit**. The strong observed Q3 correlation cannot simply be imported into the original field theorem.

The next real theorem target must bound the **signed Schur mode-flow contribution of every newly entering transverse layer**, ideally by an explicit moment/slice kernel, while preserving the full source and the original local arithmetic once. Without that, the apparent constant-gain pattern from two fixed-stratum examples was an epistemic failure of extrapolation.

**Evidence:** [P-paper] wall-crossing identities from Gram decomposition/Schur; [M] three exact finite original-source cases and one controlled ablation; [R] normalized >=0.0043 quartet-only uniform gain; [H] many-layer uniform spectral theorem and any actual field cutoff improvement. Independent peer/source-to-field review #50 remains open.
