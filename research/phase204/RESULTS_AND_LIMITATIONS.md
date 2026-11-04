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
This is **P (straight source algebra)**: the chosen order is closed under multiplication, every ordinary j-jet contains j!, and the trace is bilinear. More strongly, the repository's already-integrated [JetPrecisionBridge.lean](../../lean/TenthDiscriminant/JetPrecisionBridge.lean) **Lean-proves** `integerDerivativeRow_eq_factorial_hasse` for this exact integer source. Phase204 must reuse that lemma, not claim the factorial separation as newly formalized mathematics. The new [Lean source module](../../lean/TenthDiscriminant/JetFactorialFiltration.lean) now imports it and targets only the additional trace-pairing factor and Gram-depth increment; both remain **candidates** until a successful exact-head scoped build and unchanged root audit.

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

## Further registered junction: Smith filtrations and two-sided tube transport

**Registered prospectively in comments on #136 and #137**, before implementing [truncated_smith_profiles.py](truncated_smith_profiles.py) and [two_sided_tube_transport.py](two_sided_tube_transport.py). Their compiled/executed status must be checked on the **latest** PR head, not inferred from an older CI receipt.

**A2: not merely one determinant.** If two integral \(n\times n\) matrices agree modulo \(p^e\), their presentations over \(\mathbb Z/p^e\) agree. By uniqueness of Smith normal form over this principal ideal ring, the entire *multiset* of truncated invariant-factor valuations \(\{\min(v_p(d_i),e)\}_{i=1}^n\) agrees, with \(v_p(0)=\infty\). The source factorial congruence therefore freezes the truncated Smith profile of \(G_J\) at depth \(a\) for every \(e\le v_p(2(a!)^2)\). This is classical module algebra [P paper] and a genuinely vector-valued local constraint, **not** a new lower bound on the full determinant valuation. A deterministic modular-unit-pivot elimination test over \(\mathbb Z/p^2\) compares source \(G_p\) and \(G_{p+2}\), checks row shear/transpose invariance, and rejects the false "same det ⇒ same local profile" using diag(1,25) versus diag(5,5).

**B2: changing the question from rotation to transport.** The failure of a universal *two-jet rotation* over a residue tube does not prohibit transport of a deeper ordinary jet tower. For any integer-pair source monomial \(Z^rW^s\), let
\[
e_{r,s;j}(Z,W)=\partial_Z^j(Z^rW^s),\quad 0\le j<p,\qquad
\delta=p\lambda\in\mathbb Z/p^2.
\]
If a source point's **real integer-pair coordinate** is shifted by \(\delta\), both \(Z\) and its conjugate variable \(W\) shift by that same \(\delta\). Ordinary polynomial Taylor expansion gives, *modulo \(p^2\)*,
\[
\boxed{e_{r,s;j}(Z+\delta,W+\delta)=
e_{r,s;j}(Z,W)+\delta e_{r,s;j+1}(Z,W)+
\delta s\,e_{r,s-1;j}(Z,W).}
\]
For \(j=p-1\), the otherwise missing \(e_{r,s;p}\) has coefficient divisible by \(p!\), so \(\delta e_{r,s;p}=0\bmod p^2\). The \(s=0\) term is defined as zero. This is a **two-sided unipotent transport**: an ordinary jet-depth shift and a distinct \(W\)-row lowering operation. The two actions compose by addition of the infinitesimal shifts because products of two shifts vanish modulo \(p^2\). It preserves the original integer-pair derivative *type* but is not an isometry or a Gram-determinant equality for changed observation supports.

The [exact source test](two_sided_tube_transport.py) freezes \((p,D)=(3,7),(5,3),(7,215)\), \(R=p+2,S=3,J=p\), source points \((0,0),(1,0),(1,1)\), and shifts \(\delta=p,2p\). It compares both integer-pair coordinates entry by entry against direct translated evaluations and verifies composition. **Negative:** when \(J=2<p=7\), \(f(Z)=Z^2\) has the same first two ordinary jets at zero as the zero polynomial, yet after shifting \(Z\mapsto Z+7\) its first derivative is \(14\ne0\bmod49\); no autonomous *two-jet* transport can recover the shifted derivative from those data. Higher ordinary jet depth resolves precisely this information loss in the thicker fibre.

The two directions meet in a **filtered higher-jet module with a typed, unipotent transport**. This is actual algebra, not a claim that finite and Archimedean fibres are isomorphic. In particular the transport does not imply that a split-prime isometry extends to the inert small-prime divisor or that the original integer Gram determinant improves its certified lower exponent. That remains a separate, falsifiable research target [H].

## An explicit junction with already-existing Phase146 translation (source audit correction)

**Prior art within this repository is decisive.** [Phase146 translation/Newton](../reverse_determinant/PHASE146_TRANSLATION_NEWTON.md), written 31 October 2026, already derives the *exact* source-matched unitriangular integer row action \(T_a\), with
\[
E_{Q+(a,0)}=T_aE_Q,\quad G_{Q+(a,0)}=T_aG_QT_a^T,\quad
T_aT_b=T_{a+b},\quad\det T_a=1.
\]
It also tracks the potential **non-invariance of the integral column image** and a typed boundary defect, and a rational centering method for analytic upper bounds. None of those original results is attributed to Phase204. [CoordinateTranslation.lean](../../lean/TenthDiscriminant/CoordinateTranslation.lean) already addresses typed translations and a distinct imaginary-axis counterexample. The new conjunction below is a specialized, lower-precision synthesis of Phase146 and the factorial filtration, not a novel exact translation theorem.

Let \(N=\Gamma_1\) be the integer row operator, indexed by the original \((r,s)\) rows, with \(N_{(r,s),(r-1,s)}=r\), \(N_{(r,s),(r,s-1)}=s\). For \(\delta=p\lambda\) the Phase146 matrix reduces to \(T_\delta=I+\delta N\bmod p^2\). Since the original depth tail \(G_J-G_p\) is divisible by \(p^2\) when \(J\ge p\), the unchanged source obeys
\[
\boxed{G_{J,Q+(\delta,0)}\equiv
G_{p,Q}+\delta(NG_{p,Q}+G_{p,Q}N^T)\pmod{p^2}.}
\]
**Proof [P paper]:** multiply the exact Phase146 Gram congruence, discard the \(p^2\)-divisible factorial tail, and expand \(T_\delta\) mod \(p^2\). Translation of ONE point instead of ALL of Q is NOT covered; the real point shift changes both Z and its conjugate W, whereas W is held fixed only during differentiation.

[Exact regression](source_translation_junction.py) reconstructs both channels of the original source and tests the exact integral row action and Gram pullback, \(T_\delta T_{-\delta}=I\), the \(p^2\) first-variation identity and preservation of the complete truncated Smith profile for \((p,D,R,S,J)=(3,7,5,2,5),(5,3,7,2,7),(7,215,9,3,9)\), at \(\delta=p,2p\). A partial-support shift and an incorrect W-fixed *point motion* are the matched negative controls. The first run was also checked by a separate local implementation before committing this script. **Evidence is finite M pending a current-head GitHub CI receipt.**

### The first nonzero associated-graded layer, rather than a false valuation gain

For odd p, let
\[
H_{p,J}(Q):=\frac{G_{J,Q}-G_{p,Q}}{p^2}\pmod p.
\]
The quotient is an **integral matrix before reduction**. Write \(e^{[j]}_{r,s}(z)=\binom rj z^{r-j}\bar z^s\) for a divided/Hasse **coordinate used only to describe the quotient**; \(G^{[j]}\) is the original trace pairing applied to this one-depth coordinate matrix. Because the actual ordinary source jet equals \(j!e^{[j]}\), it follows for every \(J\ge p\) that
\[
\boxed{H_{p,J}(Q)=\sum_{j=p}^{J-1}
\left(\frac{j!}{p}\right)^2 G^{[j]}_Q \pmod p.}
\]
This is an associated-graded **identity**, not replacement of the jets used in the original \(G\) or a license to drop factorial valuations. Moreover Phase146 gives \(H_{p,J}(Q+(p\lambda,0))=H_{p,J}(Q)\) over \(\mathbb F_p\) for every integer \(\lambda\): the tail changes by congruence under \(T_{p\lambda}\equiv I\pmod p\). Its entries can be nonzero, so \(G_J-G_p\) need not vanish modulo \(p^3\).

The [registered regression](graded_padic_layers.py) tests \(p=3,5,7\) with the original integer-pair source. At the frozen \(Q\) and \((R,S,J)=(p+2,2,p+2)\), the numbers of nonzero entries of \(H\) are 9, 11, 11 respectively. The sharp single-node \(r=j=p\) diagonal has graded residue \(2\bmod p\). These are finite M; source algebra is paper P.

### Integral divided powers, not illicit modular factorial inversion

Write the **already-known** Phase146 translation matrix by its integral binomial coefficients:
\[
T_a=\sum_{k\ge0}a^k\Gamma_k,\quad
(\Gamma_k)_{(r,s),(u,v)}=
\mathbf1_{\substack{u\le r,v\le s\\r+s-u-v=k}}
\binom ru\binom sv.
\]
Then \(\Gamma_0=I\), \(\Gamma_1=N\), \(\Gamma_1^2=2\Gamma_2\) exactly **over the integers**. For \(a=p\lambda\):
\[
\boxed{T_a\equiv I+a\Gamma_1+a^2\Gamma_2\pmod{p^3}.}
\]
Unlike a casual "\(N^2/2\)" formula, \(\Gamma_2\) is an integral matrix even at \(p=2\), where division by 2 is not an operation on \(\mathbb Z/8\mathbb Z\). In the row \(Z^2\), the \(a=2\) second-order coefficient is exactly \(4\pmod8\), so the first-order approximation fails.

The [second registered exact test](graded_padic_layers.py) verifies the entire row-matrix expansion, \(\Gamma_1^2=2\Gamma_2\), direct original ordinary-jet evaluation for translated supports, and exact full integral Gram congruence at \(p=2,3,5\). This is **not** a new translation theorem and **not** a p-adic isometry between unrelated arithmetic fibres.

**Remaining hard obstruction:** neither the preserved Smith profiles nor the nonzero graded tail supplies a stronger *production* Gram determinant divisor. The shifted support is a distinct ellipse; its exact determinant equality under integer real-axis translation is a gauge identity, already known in Phase146. Any arithmetic gain must instead obtain a stronger local exponent for the SAME fixed original determinant, paired with a matched Archimedean bound. Human semantic review [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) remains open.

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
