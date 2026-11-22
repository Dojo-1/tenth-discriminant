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
