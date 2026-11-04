# Phase204 — two typed directions beyond the residue field

**4 November 2026 · preregistered before code:** [Track A #136](https://github.com/Dojo-1/tenth-discriminant/issues/136), [Track B #137](https://github.com/Dojo-1/tenth-discriminant/issues/137). Frozen source: [IntegerTraceGram.lean](../../lean/TenthDiscriminant/IntegerTraceGram.lean) on the integrated [322⁴ theorem](https://github.com/Dojo-1/tenth-discriminant/pull/126), with stacked Phase202–203 source modules unchanged. This is an AI-authored research record requiring independent mathematical review, **not** an external validation or a stronger field cutoff.

## A — a filtration of the *same* integer Gram by ordinary jet depth

Fix \(\mathbb Z[\sqrt{-D}]\), original finite integer-pair support Q, fixed rectangular row labels \((r,s)\) and ordinary derivative \(\partial_Z^j(Z^r W^s)\) with W held fixed. The exact source formula is
\[
e_{r,s;j}(z)=
\begin{cases}
j!\binom rj\, z^{r-j}\bar z^{s},&j\le r\\
0,&j>r.
\end{cases}
\]
Its paired integral trace is \(2(a a'+D b b')\) when the two jets are written \((a,b)\), \((a',b')\). Let \(G_J\) denote the original integer trace Gram using all depths \(0\le j<J\), with **unchanged** Q,D,R,S. The depth increment satisfies
\[
\boxed{\Delta_jG=G_{j+1}-G_j\in 2(j!)^2\operatorname{Mat}_{RS}(\mathbb Z).}
\]
Thus for \(a\le J\):
\[
\boxed{G_J\equiv G_a\pmod{2(a!)^2}}\quad
\text{entrywise}.
\]
This is **P (straight source algebra)**: the chosen order is closed under multiplication, every ordinary j-jet contains j!, and the trace is bilinear. Mathlib already has \`Nat.descFactorial_eq_factorial_mul_choose\` (known prior algebra); the new [Lean source module](../../lean/TenthDiscriminant/JetFactorialFiltration.lean) is a proof **candidate** until scoped compilation and the unmodified root audit pass.

For odd primes p and J≥p, \(G_J\equiv G_p\pmod{p^2}\). In characteristic 2, the extra trace-2 factor gives \(G_J\equiv G_2\pmod 8\). These relations retain matrix entries, not just one determinant; however \(\det G_J\equiv \det G_p\pmod{p^2}\) is only congruence, **not** a new lower bound on \(v_p(\det G_J)\) when its reduction vanishes. In particular this does not improve the original prime-power certificate of the integrated 322⁴ theorem.

**Predeclared exact tests** in [ordinary_jet_filtration.py](ordinary_jet_filtration.py): (p,D)=(3,7),(5,3), Q={(0,0),(1,0),(1,1)}, R=p+2,S=2,J=p+2. A one-point witness Q={(0,0)}, row (r,s)=(p,0), j=p has \(\Delta_pG_{rr}=2(p!)^2\), with \(v_p=2\) exactly for p=3 and5. The wrong Hasse/divided derivative gives 2, not a multiple of p²; this is a **negative semantic control**. At p2 the sharp j2 trace contribution is 8 (valuation 3). All computations are exact integers. **M only after an actual run/CI receipt.**

## B — a true anchored lift, and a full-tube impossibility

For split p7 and the original selected order D=215, the reduced value/first-derivative Hermite rotation is
\[
U_7=H_7^{-1}\bigl(\oplus_{a\in\mathbb F_7} R\bigr)H_7,\quad
R(v,d)=(d,-v).
\]
Its carrier is **the 14-dimensional first-jet polynomial space over \(\mathbb F_7\)**, not the original number field, and the same W-frozen derivative is used.

Over \(A=\mathbb Z/49\mathbb Z\), fix *one section* consisting of representatives \(a=0,\ldots,6\). Their pairwise differences are units in A. Therefore the 14×14 confluent Hermite matrix \(H_{49}\) is invertible over A and
\[
U_{49}=H_{49}^{-1}(\oplus R)H_{49}
\]
is a valid anchored rotation: \(U_{49}^2=-I\), \(\det U_{49}=1\), and \(U_{49}\bmod7=U_7\). It rotates value/first-derivative data at the chosen seven nodes.

But **no polynomial linear operator on the same source can rotate the two ordinary jets at EVERY element of A**. Apply any putative operator to the constant polynomial f=1 and write its output h. It would require
\[
h(0)=h(7)=0,\qquad h'(0)=-1\pmod{49}.
\]
Every polynomial over A obeys the Taylor congruence
\[
h(7)-h(0)\equiv7h'(0)\equiv-7\not\equiv0\pmod{49},
\]
a contradiction. This is **P (two-point proof)** independent of polynomial degree; it refutes *universal exact value/derivative rotation*, not every possible isometry at prime-power level.

The [exact p49 harness](anchor_vs_tube_p49.py) preregistered in #137 checks \(U_{49}\) at all seven anchors, entrywise reduction to the explicit prior U7, and the sharp constant-polynomial failure \(h(7)=42\pmod{49}\). The correct lifted order root is \(\sqrt{-215}\equiv\pm31\pmod{49}\), **not** \(\pm3\), which applies only mod7.

An actual thickened jet family can vary between points \(a\) and \(a+7\lambda\), but that change is not an isometry simply by inheritance from the residue field. The first derivative changes by a term involving second derivatives; it must be carried explicitly as a typed transport remainder. No decorative cross-prime manifold or putative automatic integral isometry is asserted.

## Where the lines intersect, and where they do not

Track A explains the **p-adic filtration of ordinary derivative contributions** to the full integer trace Gram. Track B explains why its residue-field Hermite rotation cannot act uniformly across all \(\bmod p^2\) evaluation points even though an anchored lift exists. These statements are mutually consistent: the \(j\ge p\) columns vanish modulo \(p^2\) as Gram *contributions*, but individual high-jet values may survive modulo \(p^2\) and matter at higher precision.

| Claim | Evidence state | Promotion gate |
|---|---|---|
| Source factorial jet and Gram depth congruence | **P paper** | Lean source import, scoped and whole-root audit |
| p3/p5 sharpness and Hasse replacement counterworld | **M pending CI** | Exact script on PR head |
| Anchored U49 and reduction to U7 | **P via CRT / M pending CI** | Confluent Vandermonde unit-pivot test and 7 anchor evaluations |
| Universal exact U49 across full residue tubes | **R (refuted)** | Polynomial Taylor contradiction at 0 and7 |
| New p-adic valuation gain for original production det | **H / unestablished** | Same integer determinant, source-aware p-adic Smith/exterior-minor and matched analytic upper |
| External selected minor equals our Gram | **R (invalid identification)** | Need a separate source-preserving typed comparison; none produced |

**Stop:** No merge, field-cutoff announcement, p-adic sheaf/connection upgrade, or genuine novelty claim from finite controls alone. The original local inertness hypotheses and full-root sources stay unchanged. The independent human-semantic-review [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) stays open.
