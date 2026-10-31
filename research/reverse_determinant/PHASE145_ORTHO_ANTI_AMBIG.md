# Phase145 — Ortho / Anti / Ambig: two 360° circuits through the original ordinary-jet Gram

31 October 2026. [M] Reproduced finite **exact-integer** experiment in D=19, rho=5, R=8, S=J=4 original ordinary Z-jets with W fixed, real/imaginary integer channels, and original trace weights 2 and 38. [P-paper] Classical lattice, Schur-complement and closure identities below, **not Lean checked**. [H] Uniform production extension, adiabatic transport and measured global holonomy **not established**. Existing PRs #61/#62 and numerical cutoff proofs are untouched.

The [Phase145 executable](phase145_ortho_anti_ambig.py) imports the original [Phase140 ordinary-jet source](../ellipsoid_trimming/phase140_exact_trim.py), the [Phase144 HNF/Smith verifier](phase144_verifier.py) and the [six-point exact minimum witness](phase144_minimum_support.py), without modifying their definitions. The original universe is $\Omega=\{(x,y)\in\mathbb Z^2:x^2+19y^2\le25\}$, 21 points; $E_Q$ has 32 rows and $8|Q|$ integer columns, and $G_Q=E_Q B_Q E_Q^\mathsf T$ with $B_Q=\mathrm{diag}(2,38,\ldots)$.

**Pre-registration and negative controls.** Ask whether (i) parity-metric coupling can vary inside one integral column-image stratum; (ii) the exceptional 17-point index change is due to altered parity gluing or changes *inside* the pure parity sublattices; (iii) a closed two-parameter metric circuit may have noncommuting SPD tangents even when the determinant returns. Tests: mirror Q, antipodal completion, full-ellipse symmetry, equal-tangent commutation null, independent modulo-2/gluing-index calculations, exact HNF closure, and a modular commutator witness. Retire new-gluing as the cause if Gamma is unchanged; retire nonflat tangent claim if the commutator vanishes. This is not a complexity or number-field theorem.

## Ortho and anti: exact parity of the original jets

On row $(r,s)$ define the integer involution $P_{(r,s),(r,s)}=(-1)^{r+s}$, $P^2=I$. For every point $q$, ordinary derivative slot $j$ and real/imaginary channel $c$,

$$E_{-q}^{(j,c)}=(-1)^j P E_q^{(j,c)}.$$

The verifier tests this entrywise across all 21 points, 4 derivative slots and both channels. Therefore $G_{-Q}=P G_QP$. In the 16+16 parity row ordering write $G=\begin{pmatrix}A&C\\C^\mathsf T&D\end{pmatrix}$; its **parity pinching** $G_{\rm ortho}=(G+PGP)/2=\mathrm{diag}(A,D)$ has

$$\chi_{\rm anti}(G)=\log\frac{\det A\det D}{\det G}
=-\log\det(I-D^{-1/2}C^\mathsf TA^{-1}CD^{-1/2})\ge0.$$

This is a standard positive-Schur-complement consequence. Pinching is **not** the same as actually adding antipodal observations.

Finite [M] results, natural logarithms displayed approximately:

| Support | Cardinality | log det G | chi anti |
|---|---:|---:|---:|
| Q6 = {(-2,-1),(-1,-1),(-1,0),(0,-1),(0,0),(1,-1)} | 6 | 424.342642241362 | 19.995899166040 |
| -Q6, exactly reflected | 6 | 424.342642241362 | 19.995899166040 |
| Q6 union (-Q6), actual completion | 11 | 465.111990597164 | 0 |
| Full ellipse Omega | 21 | 530.285191201861 | 0 |

The cross-parity block flips sign under reflection and vanishes for antipodally symmetric sets. Every listed set has the **same full integral column image**, certified by HNF inclusion. Since completion changes cardinality, do not interpret the log-det difference as solely a change in chi.

## Ambig: exactly typed 2-primary lattice seam

For a full-rank P-stable free integer column image $M\subseteq\mathbb Z^{32}$, let $M^\pm=\{x\in M:Px=\pm x\}$ and $\Gamma_M=M/(M^+\oplus M^-)$. Map $x\in M$ to $(I+P)x\bmod 2M$. The kernel is exactly $M^+\oplus M^-$: if $(I+P)x=2y$ for $y\in M$, applying $P$ yields $Py=y$ and $x-y\in M^-$. Thus

$$\boxed{\Gamma_M\simeq\operatorname{im}_{\mathbb F_2}(I+\overline P\mid M/2M),\qquad |\Gamma_M|=2^{\operatorname{rank}_{\mathbb F_2}(I+\overline P)}.}$$

Let $H$ be a column-Hermite basis of $M$. In these integral coordinates $T=H^{-1}PH$ is the correct parity action, not the ambient diagonal matrix reduced modulo two. Independently let $a_\pm$ be the indices of the coordinate projections $\pi_\pm(M)\subseteq\mathbb Z^{16}$. Exact lattice algebra yields $[\mathbb Z^{32}:M]=a_+a_-|\Gamma_M|$. Both are tested.

Measured [M]:
- For M_full = M_Q6: Gamma = (Z/2)^8 (order 256), a+ = 330225942528, a- = 990677827584.
- For the exceptional symmetric M_17 after removing all four (±1,±1): Gamma **still** (Z/2)^8, a+ = 10567230160896 = 32 × a+_full, a- = 31701690482688 = 32 × a-_full.
- The relative quotient of M_full/M_17 has the inherited Smith factors (Z/2)^6 ⊕ (Z/4)^2, order 2^10. Here the pure parity indices grow by 32 and 32, while the gluing group **does not change**.

**Correction [R]**: the earlier possibility that this observed 2^10 jump represents **new parity gluing** is false in the frozen example. All index growth is already accounted for inside the two pure parity sublattices. Gamma is nontrivial, but unchanged.

## Up and down: closure is not inversion

For Q subset Omega, define Phi(Q) = im_Z E_Q, Psi(M) = {q in Omega : im_Z E_{ {q} } subset M}. Then Phi(Q) subset M iff Q subset Psi(M), so c=Psi Phi is a closure operation, not an inverse. Exact membership tests show c(Q6)=Omega (21/21), while for Q17=Omega minus the four (±1,±1) points, c(Q17)=Q17 (17/21). The same 32-dimensional integral image can admit many different minimal or redundant supports.

## Moving moving frame: a scalar 360° and a nonflat tangent plane

Choose G0=G_Q6, A1=G_{ {(5,0)} }, A2=G_{ {(1,1)} }. All are original integer Grams; A1,A2 are positive semidefinite and G(u,v)=G0+uA1+vA2 is SPD for 0<=u,v<=1. The log-det values at (0,0),(1,0),(0,1),(1,1) are respectively

$$424.342642241362,\quad459.304536926256,\quad429.549512681400,\quad463.997126309078.$$

Traversing the boundary in order (0,0) → (1,0) → (1,1) → (0,1) → (0,0) gives an exact zero integral of d log det G. This scalar fact is independent of the path; it is **not** evidence of a novel transport effect.

For the specified *affine-invariant Riemannian metric* on SPD(32), curvature of the plane formed by the two symmetric tangents depends on the normalized commutator. It vanishes iff

$$A_1G_0^{-1}A_2-A_2G_0^{-1}A_1=0.$$

An exact witness excludes that identity: det G0 ≡ 74 (mod 101), so reduction of G0 inverse is legal, and the commutator has entry (0,1) ≡ 44 (mod 101), with 982 nonzero entries. With the matched null A1=A2 the commutator is exactly zero. This certifies **local nonflatness of the specified SPD connection**, not a numerically computed parallel-transport holonomy around the square. Any whitening/moving frame must transport the grading and integer lattice data; a real whitening operation does not preserve their arithmetic meaning.

## Research boundary and next discriminator

The actual surviving structure is threefold: integral-image preservation, parity-metric coupling and curvature under a *chosen* SPD connection. They are not equivalent invariants. The anti coupling is not a guaranteed field-bound saving; parity gluing did not explain the observed 2^10 transition; local tangent curvature is not global holonomy or physics.

Next [H]: repeat with at least one independently controlled nearby D and a small family of image-preserving supports, keeping original ordinary derivatives and equal computational budgets, then seek a uniform bound linking support selection and primitive metric factor. A separate [H] experiment may compute genuine affine-invariant parallel transport around the square versus the flat-connection null. Retire production relevance if a putative uniform family loses image rank, requires an inverse of the unknown production Gram, or its claimed gain disappears against the certified analytic upper.

**Reproduce:** run python3 research/reverse_determinant/phase145_ortho_anti_ambig.py with SymPy 1.14. Exact integer/HNF/Smith and finite-field claims were checked locally; logarithms are display-only approximations. No new PR, no merge, and no new field discriminant claim.
