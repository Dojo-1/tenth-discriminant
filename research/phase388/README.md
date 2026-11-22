# Phase388 — Exact source-level identification of the nine fourth-jet traces

**22 November 2026 · AI-assisted mathematical derivation and two independent exact arithmetic implementations · research draft.**

## Verdict

For the **original** D=403, p=3, rho=40, R=100, S=J=4, Q=219 ordinary-Z/held-W trace-Gram source, the nine extra fourth-derivative directions are exactly the nine-dimensional Phase284 first-Bockstein/Frobenius **fourth-jet function space**. This is a finite source-typed equality of trace subspaces. It is **not** an equality of the original nine Phase284 rows with lower-null rows, not a universal theorem in D, not an additive Smith valuation, and not a new discriminant bound.

## Frozen definitions

Let beta²=-D, z=x+y beta, and W=conj(z) held fixed under all ordinary Z derivatives. For 0<=r<100, 0<=s<4, put

\[
k(r,s)=\min(\lfloor r/3\rfloor,3-s),\quad
F_{r,s,j}(z)=3^{-k(r,s)}\partial_Z^j
\left[Z^{r-3k(r,s)}W^s(Z^3-W)^{k(r,s)}\right]_{Z=z,W=\bar z}
\]

for j=0,1,2,3. Source divisibility making these integral is the earlier Frobenius-jet theorem. The actual ellipse has exactly 219 integer pairs, with y∈{-1,0,1}. Every one of the 27 source classes (x mod9, y mod9∈{8,0,1}) occurs. The Phase386 congruence formula proves that reduced normalized jets only depend on these source classes.

Define the exact 400-by-216 matrix A over F3, including BOTH source integer-pair output channels for all four ordinary jets. Write A_low for its j=0,1,2 columns and A_3 for j=3. Let

\[
K_3=\{c^\top A_3:c\in\mathbb F_3^{400},\quad c^\top A_{\rm low}=0\}.
\]

Two independent exact finite-field elimination directions find rank(A_low)=81, rank(A)=90, hence dim(K_3)=9.

## Explicit nine sparse source rows

Write F_(r,s) for the complete four-jet normalized original row with label (r,s), and work with coefficients mod3, where minus is coefficient 2. Set

\[
\begin{aligned}
N_0 &= F_{3,0}-F_{9,0}-F_{21,2}+F_{33,0},\\
N_1 &= F_{2,3}-F_{3,0}-F_{6,3}+F_{9,0}-F_{10,3}+F_{12,3},\\
N_2 &= F_{3,3}-F_{4,0}-F_{7,3}+F_{10,0}-F_{11,3}+F_{13,3},\\
N_3 &= -F_{0,3}+F_{2,1}-F_{4,3}+F_{6,3}-F_{15,2}+F_{27,0},\\
N_4 &= F_{0,2}-F_{1,3}-F_{5,3}+F_{7,3}-F_{16,2}+F_{28,0},\\
N_5 &= F_{1,2}-F_{2,3}-F_{6,3}+F_{8,3}-F_{17,2}+F_{29,0},\\
N_6 &= F_{2,2}-F_{3,3}-F_{7,3}+F_{9,3}-F_{18,2}+F_{30,0},\\
N_7 &= F_{0,3}-F_{4,3}-F_{8,3}+F_{10,3}-F_{19,2}+F_{31,0},\\
N_8 &= F_{1,3}-F_{5,3}-F_{9,3}+F_{11,3}-F_{20,2}+F_{32,0}.
\end{aligned}
\]

The exact finite calculation establishes on EVERY original Q point

\[
(N_i)_{j}(z)=0\pmod3\quad(j=0,1,2),
\]
and
\[
(N_0)_3(z)=2(1-z^8),\qquad
(N_i)_3(z)=z^{i-1}\quad(1\le i\le8).
\]

These nine fourth-jet functions are linearly independent: over F9, z^9=z, the degree-at-most-eight polynomial evaluation map is injective on all nine field elements, and 2(1-X^8),1,X,...,X^7 is an invertible change of basis from 1,X,...,X^8. All nine field residues are represented among Q mod9. The Phase284 fourth-jet functions B_a(z)=2z^a (0<=a<=8) span the SAME polynomial-function space. Because N_i have zero lower jets and span nine dimensions while K_3 has dimension nine, we have the exact finite statement

\[
\boxed{K_3=\operatorname{span}_{\mathbb F_3}\{(2z^a)_{z\in Q\bmod9}:0\le a\le8\}.}
\]

## Source-matched controls and hostile counterexamples

The independent direct integer-pair original derivative and the separate factored Frobenius-jet evaluation were matched on all 219 source points, all 9 witnesses, and all four ordinary derivative orders. Both source coordinate channels were retained. Independently calculated row and column ranks give A_low rank81 and A rank90. Original Phase284's nine SOURCE ROWS have lower-jet rank9: they are NOT themselves lower-null. Removing all nine source rows from A reduces total rank only 90→89, rather than 90→81. Thus NO nine new independent valuation factors follow.

The frozen sparse N_i fail to annihilate the lower jets on a y=2 mod9 sample outside the original ellipse. They also fail on the same y=1 source residue for D=19 (D mod9=1) and D=283 (D mod9=4); all are inert at p3, so inertness by itself is insufficient for these FIXED sparse identities. The positive certificate is tied to D=403 mod9=7 and the actual three vertical source residue classes. Generalization is **H**, not proved.

The code is [jet3_bockstein_bridge.py](jet3_bockstein_bridge.py), using two different source jet implementations from Phase386. Earlier Phase284 source code is [frobenius_overlap.py](../phase284/frobenius_overlap.py). This is a new exact finite identification relative to the prior nine-dimensional rank observation, not an independently human-reviewed mathematical theorem.

## Evidence and decision gates

- **P (finite algebraic):** the degree-eight polynomial basis and the rank-nullity implication conditional on the exact finite matrix results.
- **M:** bounded exact integer checks, independent direct ordinary-jet oracle, two elimination directions, original Q source support and explicit hostile mutations.
- **A:** existing Frobenius integrality and field/Gram source interpretation; no new field-to-class-number transfer.
- **H:** pinned Lean formalization of the 27 finite residue-case identities and the 81/90 rank factorization; algebraic generalization across other D mod9 and supports.
- **R:** interpreting matching dimension alone as a proof of equality, identifying original Phase284 rows directly with lower-null rows, adding nine valuation units, or claiming an improved unconditional field bound.

**Next bounded proof:** formalize the nine original-source lower-jet-null identities in Lean without Hasse derivatives, compile a finite matrix rank factorization with exact source coordinates, and require one wrong-support mutation to fail. Keep the original independent human issue #50 open; leave Masullo/Hecke, conductor and Selberg-Ihara claims unchanged.

## Fixed 81-by-81 lower-jet minor: a more transparent proof of rank 81

The actual 27 mod9 source classes are stable under conjugation: 9 classes with y=0 are fixed, while the 18 classes with y=1 or 8 form 9 conjugate pairs. Every original normalized source-jet value commutes with conjugation (it is built from integer polynomials, the original held-W convention and division by a scalar 3^k). Hence for each j=0,1,2 the 54 scalar source columns carry at most 9+2*9=27 independent scalar degrees of freedom. This yields the source-typed upper bound rank(A_low)<=81 with no Gaussian elimination.

The independent script [lowjet_minor_certificate.py](lowjet_minor_certificate.py) freezes **81 row labels** (first 51 row-major labels plus an explicitly listed sparse continuation), and freezes **81 scalar columns** (one coordinate from each y=0 class, both coordinates from each y=1 class, for every j<3). It checks the conjugation identities over all 400 source rows, then computes the 81x81 modular determinant using a separate exact elimination procedure. The result is

\[
\det(M_{81\times81})\equiv 1\pmod3.
\]

Thus rank(A_low)>=81 by an explicit unimodular minor and rank(A_low)<=81 by conjugation; **rank(A_low)=81 follows without the whole-matrix rank algorithm**. This is a finite computation plus elementary conjugation proof, and has not been translated into pinned Lean. Full rank(A)=90 still uses two independent exact finite Gaussian elimination implementations, and is not claimed to follow purely from the conjugation upper bound.

This fixed-minor artifact makes the finite lower-jet endpoint more auditable and is an additional negative control against accidentally dropping the imaginary source channel or swapping W-held ordinary derivatives for Hasse jets.


## Universal S=4 translation identity: algebraic upper bound 90

There is a genuinely SOURCE-LEVEL theorem behind the finite data. Fix **any** quadratic integer-pair source A_D with D≡1 mod3 (so the p3 source reduction is the inert field F9). Keep p=3, S=4 and arbitrary original legal r,s; hence k(r,s)<=3. For any integer source z and t∈{0,1,2}, let z_t=z+3t (which shifts both Z and its held value W by 3 in the sample, though differentiation still holds W constant). Then **for every original normalized ordinary jet row**:

\[
\boxed{F_{r,s,3}(z_t)-F_{r,s,3}(z_0)
=t\,\sum_{u=0}^{2}F_{r,s,0}(z_u)\pmod3.}
\]

**Proof in standard characteristic-3 differential algebra.** Put q=(Z^3-W)/3 at the integral source points. Its evaluation is integral by inert Frobenius. For ordinary Z differentiation of the normalized polynomials introduce the formal derivation δ on F3[Z,W,q] with

\[
\delta Z=1,\qquad \delta W=0,\qquad \delta q=Z^2.
\]

Then δ²q=2Z and δ³q=2. In characteristic 3, δ³ is itself a derivation (the middle binomial coefficients 3 choose 1 and 3 choose 2 vanish). It kills Z and W and sends q to 2, so **δ³=2∂/∂q** on this polynomial algebra. The original normal row is Z^a W^s q^k, with k<=3, and the δ^j evaluations reproduce the original normalized **ordinary** source jets for j<=3.

Under a source shift z→z+3t, Z,W are unchanged modulo3 but the integral Frobenius quotient satisfies q(z+3t)≡q(z)-t (mod3). Write the fixed-base normal value as a degree-at-most-three polynomial g(q)=a0+a1 q+a2 q²+a3 q³ over F9. Direct arithmetic in F3 gives

\[
\sum_{u=0}^{2}g(q-u)=2a_2,\qquad
2[g'(q-t)-g'(q)]=-t a_2=t(2a_2),
\]

which proves the claimed identity. This proof is **NOT** a universal S theorem: the degree bound k<=3 is essential. At S=5, k=4 the identity is false, explicitly at D403, r12,s0,z=0; that negative control is in [jet3_translation_identity.py](jet3_translation_identity.py).

### Finite geometry yields the full rank upper without a 400x216 rank oracle

The actual D403 source has all three x-lifts modulo9 for each base z∈F9, with y=0,±1. By the translation identity, every fourth-jet column over a lifted x is a linear combination of **one fourth-jet base column** and three zeroth-jet columns. Conjugation further reduces the fourth-jet base columns to 9 scalar degrees of freedom. Since the lower three jets have at most 81 scalar degrees, the full original A has rank <=81+9=**90** by source algebra alone.

The fixed 81x81 lower-jet unit minor proves lower rank=81. The nine explicitly constructed lower-null N_i and elementary polynomial-root independence prove the relative fourth-jet rank is at least9. Hence **rank A=90** algebraically, conditioned only on the finitely verified nine source row identities, the original quadratic source definitions, and the stated field/conjugation arithmetic. No black-box 400x216 elimination is needed for the *upper* bound.

Finally, the independent [compact_90_factorization.py](compact_90_factorization.py) fixes 90 geometrically chosen scalar source columns (81 lower + 9 fourth representatives) and 90 original row labels. Its 90x90 minor has determinant **2 modulo3**. It constructs coefficients expressing ALL 216 original columns in those 90 generators and verifies every resulting entry across all 400 rows. Each column requires at most four nonzero source-basis coefficients. This is a full exact finite matrix factorization certificate, distinct from the periodicity-based 130-row upper bound in Phase387.

**Evidence boundaries:** P-paper for the δ³ and source-shift identity with k<=3; M for six-source-parameter exact tests and the full source factorization; H for a pinned Lean formalization and the source-to-number-field semantic review. Neither the rank90 nor the nine Phase284 functions produce any separately creditable p-adic Smith valuation: the earlier Phase387 overlap correction still applies.
