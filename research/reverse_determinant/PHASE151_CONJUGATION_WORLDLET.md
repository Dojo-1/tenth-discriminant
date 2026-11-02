# Phase151 — Conjugation Worldlets: integral sheaf descent, metric breathing, and a typed two-primary seam

**31 October 2026 · canonical branch `main`.** [P-paper] the algebraic equivariance, orbit reconstruction, PSD inequalities and inverse-free spectral bounds below follow from original ordinary-jet definitions and standard linear algebra, not new general mathematical theory. [M] bounded exact checks for D=17,19,21,23,43; source-matched GitHub CI pending at this commit. [H] uniform support localization, phase transport, and production field bound. [S] polycosmic terminology describes an explicitly typed architecture, not quantum hardware, general intelligence, or a new physical law. No new number-field cutoff, Lean theorem, PCB or accelerator result.

## The carrier: an equivariant jet local system, not one Euclidean scalar

Let `D>0`, `1≤S≤R`, `J>0`, `m=RS`, and `Q⊂Z²` finite and closed under **conjugation** `c(x,y)=(x,-y)`. The actual ordinary jets in [`IntegerTraceGram.lean`](../../lean/TenthDiscriminant/IntegerTraceGram.lean) use

\[
f_{r,s,j}(q)=(r)_{\underline j}z^{r-j}\bar z^s,\quad
z=x+y\sqrt{-D},\quad j\le r;
\qquad f=0\text{ for }j>r.
\]

The metric pairing is **exactly** `2*(re·re + D*im·im)`, and `E_q∈Z^{m×2J}` contains the paired real/imaginary coordinate columns. Set
\[
C_J=\operatorname{diag}(1,-1,\ldots,1,-1),\quad
B_J=\operatorname{diag}(2,2D,\ldots,2,2D).
\]

The original integer-pair multiplication is conjugation-equivariant, so **for every** q,
\[
\boxed{E_{c(q)}=E_qC_J,\quad C_J^2=I,\quad C_JB_JC_J^T=B_J.}
\]
The sample action groupoid `Q//C₂` with fiber `Z^{2J}` and transition `C_J` is an *actual* finite equivariant local system. The real-axis fixed nodes obey the stabilizer condition: imaginary columns vanish there. No sheaf cohomology or stack equivalence is being asserted beyond this finite descent datum.

Select one representative from each conjugation orbit, `Q⁺={q∈Q:y≥0}`; let `w(q)=1` for y=0 and `w(q)=2` for y>0. Because `C_J` is an **integral unimodular** matrix,
\[
\boxed{\operatorname{im}_{\mathbb Z}E_Q=\operatorname{im}_{\mathbb Z}E_{Q^+}.}
\]
The image equality commutes with extension of scalars to every `Z_p`; full-image Smith invariants and p-adic image defects do not change. This does **not** assert equality of determinants of the *unweighted* Grams. The exact original Gram instead descends as a weighted orbit sum:
\[
\boxed{G_Q=\sum_{q∈Q^+}w(q)\,E_q B_J E_q^T.}
\]
This is the zero-loss orbit **holoportation** contract: preserve representative coordinates, multiplicities and sign of the imaginary channel, and the ordered original integer observation matrix can be reconstructed exactly. Preserving merely the Gram loses ordered observation/provenance information and is not exact inverse transport.

## Three different worlds of the same arithmetic object

- **Integral Worldlet:** `M_Q=im_Z E_Q`, its Hermite basis and the integer cokernel; transport by signed unimodular `C_J`. Proof of equality is **integral**, not just rank over Q.
- **p-adic Worldlets:** `M_Q⊗Z_p`, relative finite cokernels and Smith/Fitting invariants. Exact orbit descent commutes with each scalar extension. A p-adic image invariant is not itself an invariant of the new unweighted Gram determinant.
- **Archimedean Worldlet:** the positive definite cone `SPD_m`, with `G_real` from fixed points and `H=\sum_{q∈Q⁺,y>0} E_qB_JE_q^T`. Then
  \[
  G_Q=G_{\mathrm{real}}+2H,\quad
  U:=G_{Q^+}=G_{\mathrm{real}}+H,\quad
  0\preceq H\preceq U,\quad U\preceq G_Q\preceq2U.
  \]
  If U is SPD, the eigenvalues `λ_i` of `U^{-1/2}HU^{-1/2}` belong to [0,1] and
  \[
  \log\frac{\det G_Q}{\det U}=\sum_i\log(1+\lambda_i)
  \in[0,\operatorname{rank}(H)\log2].
  \]
  The diagonal Hadamard majorant of U is no greater than that of G_Q; it is an **inverse-free** upper bound on the *same U*. Since rank(H)≤m, the maximum gain from conjugate deletion is `O(RS)`, not the needed leading `O(R²S)` radius-scale effect. Do not market this descent alone as an improved discriminant cutoff.

These are *plural* geometries with a **typed common origin** in the same original jets, not an asserted metric isometry among p-adic and real worlds.

## The commuting Klein square — and the refused false quotient

Antipodal reflection `a(x,y)=(-x,-y)` is a **different** involution. In row `(r,s)`, put `P_(r,s)=(-1)^(r+s)`, and in derivative-channel block put `L_J=diag((-1)^j,(-1)^j)_(j=0..J-1)`. Then
\[
E_{a(q)}=P\,E_qL_J,\quad E_{c(q)}=E_qC_J,\qquad C_JL_J=L_JC_J.
\]
Thus `a∘c=c∘a`: the finite group of sample symmetries is Klein's `C₂×C₂`, with a commuting *2-cell* on jet data. For a support invariant under both involutions, the full original Gram commutes with P; its y≥0 descent also commutes with P. The measured test verifies the exact identities rowwise for all nodes.

**Kill condition / counterexample:** One must **not** quotient by antipodal reflection as if it acted only by signed coordinate columns. With `R=2,S=J=1` and two real-axis nodes x=±1, their real column matrix is `[[1,1],[1,-1]]`, rank 2. Keeping a single antipodal representative makes rank 1. Conjugation descent is safe; arbitrary antipodal deletion is not.

## A genuine two-primary remainder from a bad Fourier lift

Over `C`, the two-character `C₂` Fourier matrix is unitary after normalization. Over `Z`, the unnormalized sum/difference matrix `[[1,1],[1,-1]]` has determinant `-2`, not ±1. Therefore even/odd **Fourier combinations** of conjugate observation columns create factors `2 E_q`, and the integral image can shrink.

The exact [verifier](phase151_conjugation_descent.py) reconstructs this *different* lattice and its relative Smith factors. For D17, D19, D21 and D23 at rho5, R8,S=J4, the naive Fourier sum/difference has
\[
M_{\mathrm{integral\ orbit}}/M_{\mathrm{naive\ Fourier}}
\cong(\mathbb Z/2)^{16};
\]
at D43 (all samples real), the quotient is trivial. This is a nontrivial **[R]_transport** of the unnormalized character construction, **not** an intrinsic failure of the correct orbit-representative descent. It is distinct from Phase145's parity-gluing group, which lives in a different module and grading. No inference about quantum hardware is made.

## Finite exact measurements [M]

Original `R=8,S=J=4,rho=5`, source-matched `D=19` jets and independently parameterized evaluators:

| D | Original points | Orbit reps | rank(H) | log det gain unweighted | raw Hadamard log gain | Naive Fourier relative index |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 17 | 21 | 16 | 32 | 11.400760909294 | 10.561240279068 | 65536 |
| 19 | 21 | 16 | 32 | 11.564317661066 | 12.771522698291 | 65536 |
| 21 | 21 | 16 | 32 | 11.750775706856 | 14.705004794656 | 65536 |
| 23 | 17 | 14 | 24 | 9.960781482704 | 12.484605537151 | 65536 |
| 43 | 11 | 11 | 0 | 0 | 0 | 1 |

All matrix operations, Gram comparisons, HNF/Smith and orbit reconstruction are exact arbitrary-precision integers; logarithms are **display only**. At D19 the weighted quotient reduces distinct original-node jet evaluations from 21 to 16 (5/21 ≈23.8%) while yielding the **identical** Gram. This is an operator-count saving, **not** measured latency or power improvement. With unweighted reps the Gram changes, while the integer observation image and its p-adic completions are unchanged. All D values here are algebraic **matrix controls**, not claimed class-number-one field instances: the original `R=8,D=19` violates the production `R<(D+1)/4` guard.

## Hamiltonian / adiabatic / holographic interfaces (typed, not ornamental)

For the positive Grams define an independent archimedean **breathing** path `G(t)=U+tH` for 0≤t≤1. Unlike an invented quantum mechanism, the variation has exact derivatives
\[
\frac{d}{dt}\log\det G(t)=\mathrm{tr}(G(t)^{-1}H)\ge0,\qquad
\frac{d^2}{dt^2}\log\det G(t)
=-\mathrm{tr}((G(t)^{-1}H)^2)\le0.
\]
Slow scheduling `t=t(\tau)` obeys the non-spectral-gap engineering bound
\[
\left\|G^{-1/2}\frac{dG}{d\tau}G^{-1/2}\right\|_{\mathrm{op}}
\le\left|\frac{dt}{d\tau}\right|
\]
because `0≤H≤U≤G(t)`. This is an *adiabatic-inspired relative-rate control*, **not** a quantum adiabatic theorem or measured global holonomy.

One possible genuine Hamiltonian lift lives on the cotangent bundle `T*SPD_m` with canonical symplectic form and geodesic kinetic energy `H_geo(G,Π)=½ tr(GΠGΠ)`. It is a separate, testable real dynamical system: one must specify the controlled coupling from orbit-weight updates to this flow before invoking any conserved Hamiltonian or a transport holonomy. The scalar log determinant alone cannot establish an n-cosmo advantage.

In the **Omni-Mobius Edge Fabric** interpretation, the candidate operator is `OrbitFold<D,R,S,J>`: input oriented integer-pair nodes, stabilizer, conjugation sign and multiplicity; output exact signed integer jet blocks and optionally an orbit-weighted Gram accumulator. CPU golden vectors are the exact big-integer matrices above. A Rust/FPGA implementation must specify fixed/variable width, checked overflow, metric scaling, provenance, clock, and a matched no-fold baseline before claiming speed/power benefits. No PCB or RTL is authorized or implied.

## How this meets the discriminant target — and where it stops

The original per-node Frobenius row factor from [`RectangularGramFactor.lean`](../../lean/TenthDiscriminant/RectangularGramFactor.lean) applies to **each** retained observation. Thus under all the strict class-number-one, inert-prime and range hypotheses, the positive Gram on `Q⁺` can enter the Phase149 positivity-first prime-mass theorem as a *new same-object witness*. Its positivity follows from the full Gram's positive rank and the proven exact image equality. However the Phase149 Lean refactor **does not yet have a completed exact-head Lean receipt**; this remains a source-level proof plan until freshly compiled. Nor does the radius shrink. Since the largest possible conjugate-fold log saving is `RS log2`, this operation alone cannot provide a leading-order `R²S` improvement.

Future [H] is **two simultaneous transports**: orbit quotient without losing integral arithmetic, and arithmetic-adaptive radius localization with independent analytic bounds. A higher-dimensional, Hamiltonian or sheaf interpretation is admissible only if it adds a measurable invariant, reconstruction guarantee, or falsifier beyond this classical controlled baseline. Retain the antipodal and bad-Fourier counterworlds.
