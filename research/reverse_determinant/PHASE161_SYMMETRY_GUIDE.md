# Phase161 — Symmetry is useful when it preserves the observation

The Tenth Discriminant argument compares two inequalities for **one integer**: the determinant of the Gram of original ordinary \(Z\)-jets of \(Z^rW^s\), with \(W\) held fixed. Our integral coordinates are \(x+y\sqrt{-D}\), and the original trace weights are \(2,2D\). Symmetry is not permission to substitute Hasse jets, change the weight, move outside the allowed ellipse, or import the prime-mass lower bound for a different Gram.

**The decision.** Keep the elementary exact actions and the parity-resolved rank test; retire automatic rank claims and untested Spin/intermanifold extensions. The [graveyard](../graveyard/PHASE161_DEFERRED_LIFTS.md) states precisely why. The [small Lean file](../../lean/TenthDiscriminant/ObservationConjugation.lean) only proves what its title says. The [finite source test](phase161_symmetry_controls.py) checks the other observations without claiming a universal theorem.

## What moves, and what remains the same?

Write \(E_Q\) for the integer channel matrix, \(B_Q\) for the *unchanged* diagonal trace metric and \(G_Q=E_QB_QE_Q^{\mathsf T}\). On a node \(q=(x,y)\):

| Action | Original jets and Gram | Scope |
| --- | --- | --- |
| Conjugate \(c(x,y)=(x,-y)\) | Real channels unchanged; imaginary channels negate. Thus \(G_{cQ}=G_Q\). | **Lean target** in `ObservationConjugation.lean`; original trace metric |
| Invert \(i(x,y)=(-x,-y)\) | On row \((r,s)\), the sign is \((-1)^{r+s-j}\) in derivative order \(j\). Writing \(P_{r,s}=(-1)^{r+s}\), \(G_{iQ}=PG_QP\). | Source-level exact identity, Phase145 parity is already in Lean |
| Translate \(t_a(x,y)=(x+a,y)\), \(a\in\mathbb Z\) | The existing integral binomial row frame \(T_a\) gives \(G_{t_aQ}=T_aG_QT_a^{\mathsf T}\), \(\det T_a=1\). | Established at paper/source level in [Phase146](PHASE146_TRANSLATION_NEWTON.md); translated points may leave the production ellipse |

These identities preserve the determinant (when defined), but **do not say** that two differently sampled supports have the same determinant. Nor do they prove a new field cutoff.

For an action stabilizing the support, the action on the column lattice \(L_Q=\operatorname{im}_{\mathbb Z}E_Q\) may be nontrivial on the quotient \(C_Q=\mathbb Z^{RS}/L_Q\). For \(D=3,R=S=J=2,Q=\{(0,3)\}\), the four source columns are

\[
E_Q=\begin{pmatrix}
1&0&0&0\\
0&-3&0&0\\
0&3&1&0\\
27&0&0&-3
\end{pmatrix}.
\]

Here \(P=\operatorname{diag}(1,-1,-1,1)\) preserves the Gram and the lattice, while \(C_Q\cong(\mathbb Z/3)^2\); it negates one torsion generator and fixes another. A determinant or list of Smith factors alone would miss this stabilizer action. This is an **exact finite** example, not evidence of a new holonomy or number-field inequality.

## One useful parity reduction of the characteristic-rank test

There is a clean combinatorial lemma behind symmetry-preserving characteristic sampling. Assume an odd inert witness prime \(p\), \(R=p-1\), \(S<p\), a centered conjugation/negation-stable disk whose distinct residue roots include \(0,\pm1\), with at least \(p\) roots and the noncollision condition \(2\rho<p\).

The roots come in symmetry orbits of sizes \(1\) (the origin), \(2\) and \(4\). Let their counts be \(1,a,b\), with \(a\ge1\). Since \(1+2a+4b\ge p\), choose \(a'\le a\), \(b'\le b\) with \(a'+2b'=(p-1)/2\). The origin and those orbits give exactly **\(p\)** roots, still symmetry-stable and inside the old radius. The established [Phase158](PHASE158_CHARACTERISTIC_JETS.md) multiplicity argument then certifies full rank of the **original ordinary-jet** matrix. This is a paper derivation, **not** a new Lean theorem.

If one removes the origin, the remaining \(p-1\) roots occur in opposite pairs. Their annihilator is even: \(g(T)=h(T^2)\). The existing Phase158 obstruction

\[
O_{k,j}=[T^{kp-1-j}]\,g(T)^S,\qquad
1\le k\le S-1,\quad 0\le j\le S-2
\]

has zero entries when \(k-1-j\) is odd. Reordering by parity makes \(O\) block diagonal. **Both block determinants must still be nonzero** to preserve full rank.

The exact source checks distinguish both outcomes:

| Example | Before deleting 0 | After deleting 0 | Meaning |
| --- | --- | --- | --- |
| \(D=163,p=31,S=5\) | rank 150 | rank 150; parity-block determinants 2 and 17 mod 31 | A successful conditional reduction |
| \(D=3,p=11,S=3\) | rank 30 | rank 29; \(O=\operatorname{diag}(0,3)\) mod 11 | A symmetric counterexample, even with \(D\equiv3\bmod4\) |

The \(D=3\) case is **not** an admissible production witness-prime instance for a discriminant cutoff. It disproves only the mistaken claim that symmetry itself makes the origin removable.

## Why the integral parity seam survives

Phase145 has already shown that a real block decomposition need not be an integral lattice decomposition. For a \(P\)-stable lattice \(L\), the seam

\[
\Gamma_L=L/(L^+\oplus L^-)
\]

is killed by 2. It must not be erased by switching to a real even/odd basis. In the original \(D=19\) finite case the seam was \((\mathbb Z/2)^8\), and a later \(2^{10}\) lattice-index jump was **not** caused by changing this seam. These controls are retained, not reinvented as Phase161 proofs.

**Verification boundary.** The conjugation lemmas are compiled only after a fresh Lean CI receipt on their exact head. The finite source tests do not establish a uniform \(p-1\)-root theorem, any extra \(2\)-adic divisor, an admissible lower/upper budget, or a stronger field statement. The accepted \(47\)-billion actual-field theorem remains unchanged; the \(5\)-billion proposal remains open.

**Attribution.** The Phase158 characteristic-subset direction was inspired by Miguel N. Walsh; the original polynomial/Gram framework and challenge have important predecessors in the work of Green, van Dijk, Pratt, Tao and other participants. The involution and coefficient-parity calculations are classical algebraic specializations, not claims of new priority.
