# Phase142 — observation leverage and a minimal exact rank witness

**31 October 2026. [P] classical Sylvester determinant identity; [M] exact finite source-matched D=19 experiment; [H] a new general unisolvence / production-size proof programme.** No improvement in the existing strict 47-billion actual-field theorem is asserted.

Our old experiment chose fewer nodes by shrinking an ellipse, leaving the familiar interpolation sufficient guard \(2(R-1)+(S-1)<|Q|\) untouched. That guard is not a necessity of the original ordinary-jet interpolation map. The new experiment directly separates rank from the sufficient count, with an *exact* full-rank witness at eight nodes.

## Frozen arithmetic and the small-leverage determinant

Let \(E_Q\) contain every original rectangular monomial \(Z^rW^s\), \(0\le r<R\), \(0\le s<S\), evaluated by every **ordinary** \(\partial_Z^j\), \(0\le j<J\), at each original lattice point; let \(B_Q=\operatorname{diag}(2,2D,\dots)\) and \(G_Q=E_QB_QE_Q^\top\).

For a single sample \(q\), collect its \(2J\) integer observation columns into \(E_q\), and let \(B_q\) be the corresponding positive diagonal block. The exact identity, for a positive-definite original \(G_Q\), is

\[
\frac{\det(G_{Q\setminus\{q\}})}{\det G_Q}
=\det\bigl(I_{2J}-B_q E_q^\top G_Q^{-1}E_q\bigr).
\tag{1}
\]

For a removed antipodal pair \(\{q,-q\}\), stack both blocks; the right-hand determinant has size \(4J\), independent of the number \(RS\) of polynomial rows. It is a standard determinant-lemma/Sylvester identity, **not a novel determinant theorem**.

Its spectral interpretation uses the *symmetric* positive semidefinite matrix \(B_q^{1/2} E_q^\top G_Q^{-1} E_q B_q^{1/2}\). The nonsymmetric \(B_q E_q^\top G_Q^{-1} E_q\) in (1) has the same nonzero eigenvalues by similarity, but its raw entries need not form a real symmetric matrix. With \(G_{Q\setminus q}\) positive definite, all relevant eigenvalues are strictly below one. At loss of rank, at least one reaches one and the determinant ratio becomes zero. Access to \(G_Q^{-1}\) is still an expensive **global** precondition, so the dimension reduction is not a free polynomial-time production solver.

The [exact Fraction-arithmetic verifier](phase142_leverage.py) reconstructs the unchanged \(D=19,\rho=5,R=8,S=J=4\) 21-node Gram, performs one 32×32 inverse and checks the 16×16 update against independent 32×32 Bareiss determinants:

| Removed antipodal pair | Exact determinant identity | Log determinant decrease |
|:--|:--:|--:|
| \(\pm(5,0)\) | verified | 17.618507018 |
| \(\pm(1,0)\) | verified | 2.156982103 |

These are distinct leverage effects under the same node-cardinality change; the source makes no universality claim. [Source-matched GitHub Actions run #41194111932](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41194111932) passed.

## A striking stronger *finite* rank witness

Use **only** the eight original real-axis lattice nodes

\[
Q_8=\{(-4,0),(-3,0),(-2,0),(-1,0),(1,0),(2,0),(3,0),(4,0)\}.
\]

The original finite guard is \(2(8-1)+(4-1)=17\), so \(17<8\) is **false**. Nonetheless, the complete original ordinary-jet evaluation matrix, restricted to its nonzero real coordinates, is square \(32\times32\) and has a nonzero exact integer determinant. On the real axis, the imaginary columns vanish; hence with \(M\) the real jet evaluation matrix,

\[
G_{Q_8}=2MM^\top,\qquad
\det G_{Q_8}=2^{32}(\det M)^2>0.
\tag{2}
\]

The exact test verified (2), positivity and divisibility by the **same** \(3^{38}\) factor, without appealing to the sufficient count lemma. This is a bounded result for \(D=19\); the formal source theorem only gives a one-way sufficient implication.

For seven distinct real nodes and \(J=S=4\), there are at most \(7J=28\) nonzero real observation columns for 32 polynomial rows, so \(\det G=0\). Thus the 8-versus-7 transition in this restricted original real-axis family is an exact *dimension boundary*, not chaos.

The verifier also tested a second set of eight distinct real nodes. In both cases,

\[
\frac{\det M}{\prod_{i<k}(x_k-x_i)^S}
=55\,306\,395\,648\,000 \quad(R=8,\ S=J=4).
\]

This constancy is explained by the general polynomial factorization below; a short **Fourier-root witness** also shows its constant is nonzero for every \(1\le S\le R\). The old claim that this nonvanishing was only a finite conjecture is therefore superseded by a paper proof, not yet by Lean. For \(S>R\), derivative columns with \(j\ge R\) vanish identically, giving a singular square evaluation matrix.

## A direct relation to the discriminant of the node polynomial

There is an elementary, higher-order identity behind the finite observations. Let \(x_1,\ldots,x_R\) be *variables*, and define the square \(RS\times RS\) matrix

\[
M_{(r,s),(i,j)}=(r)_{\underline j}\,x_i^{r+s-j},
\qquad 0\le r<R,\quad 0\le s,j<S,
\]

with entries zero when \(j>r\). This is exactly the **ordinary** \(Z\)-jet matrix at real nodes \(Z=W=x_i\); it is not the one-variable Hermite derivative *along* the diagonal.

**Paper-level factorization [P, short algebraic argument, not a Lean statement]:**

\[
\boxed{\det M=C_{R,S}\prod_{1\le i<k\le R}(x_k-x_i)^S}
\tag{3}
\]

for a constant \(C_{R,S}\in\mathbb Z\) depending on \(R,S\). To see this, assign each nonzero entry the homogeneous degree \(r+s-j\). Every determinant term has total degree

\[
\sum_{r,s}(r+s)-\sum_{i,j}j=S\binom R2.
\]

When \(x_i=x_k\), subtract the \(S\) corresponding derivative columns for nodes \(i\) and \(k\); each difference has the factor \(x_i-x_k\), so the determinant is divisible by \((x_i-x_k)^S\). Every distinct node-pair factor is irreducible in \(\mathbb Z[x_1,\ldots,x_R]\); their product has precisely the computed degree. The remaining polynomial must be an integer constant. The degree and divisibility argument alone does **not** establish nonvanishing; the next lemma supplies it.

**Nonvanishing lemma [P: elementary Fourier evaluation, paper proof, not Lean compiled].** For every pair of positive integers \(R,S\), \(C_{R,S}\ne0\) if and only if \(S\le R\).

To prove the nontrivial direction, evaluate the polynomial determinant at the complex \(R\)-th roots of unity, \(x_i=\zeta^i\), \(0\le i<R\), with \(\zeta=e^{2\pi i/R}\). This is only a witness that a polynomial is not identically zero: these complex test nodes are **not** substituted into the quadratic-field Gram, prime factors or sampling ellipse. Multiply each \((i,j)\) column by the nonzero scalar \(x_i^j\). The resulting \((r,s),(i,j)\) entry is \((r)_{\underline j}\zeta^{i(r+s)}\).

For each derivative slot \(j\), apply an invertible length-\(R\) discrete Fourier transform to its \(R\) node columns. The transformed \((r,s),(k,j)\) entry vanishes unless \(r+s\equiv k\pmod R\), in which case it is \(R(r)_{\underline j}\). Regroup rows and columns by their residue \(k\). If \(S\le R\), each \(k\) labels exactly \(S\) rows \((r_s,s)\) with

\[
r_s\equiv k-s\pmod R,\qquad 0\le r_s<R,\qquad 0\le s<S.
\]

The \(S\) values \(r_s\) are pairwise distinct. The resulting block is the **falling-factorial evaluation matrix**
\(\bigl[(r_s)_{\underline j}\bigr]_{s,j=0}^{S-1}\).
Because \((X)_{\underline j}\) is a monic polynomial of degree \(j\), its determinant is
\(\prod_{a<b}(r_b-r_a)\ne0\). Every transformed Fourier block is invertible; all column scalings and Fourier changes were invertible. Therefore \(\det M\ne0\) at this complex test configuration, so its universal polynomial constant \(C_{R,S}\) cannot vanish.

Conversely, if \(S>R\), every column with derivative order \(j=R\) is zero since \(r<R\), and \(\det M=0\) identically. This proves the full iff at **paper level**. It is a classical Fourier/Vandermonde mechanism, not a novelty claim.

**Corollary [P, paper]:** When \(1\le S\le R\), every set of **\(R\) distinct real nodes** has full row rank for the original \(J=S\) ordinary \(Z\)-jets, and its original real-axis trace Gram is positive. Distinctness is necessary for the square \(R\)-node matrix (identical nodes give repeated derivative columns). Thus, in this restricted real-axis setting, the exact criterion is \(S\le R\) plus distinctness—not the much larger generic sufficient count \(2(R-1)+(S-1)<|Q|\). This does **not** extend by assertion to arbitrary complex or two-dimensional node configurations.

The adversarial finite source now tests \(R=2,\ldots,6\), all \(1\le S\le\min(5,R+1)\), and two unequal node configurations per case. It finds \(C_{R,S}\neq0\) for the tested \(S\le R\), and \(C_{R,S}=0\) when \(S>R\). The latter has a general easy explanation: if \(S>R\), the \(j=R\) derivative columns vanish for every row. The stronger exponent \(S^2\), tempting from *one-variable confluent Vandermonde* determinants, is **false** here: at \(R=3,S=2\), \(\det M=8\), Vandermonde \(=2\), and \(16\nmid8\).

For any fixed \(R,S\) for which the constant is nonzero, a set of distinct real nodes has

\[
\det G=2^{RS}C_{R,S}^2
\left[\operatorname{Disc}\left(\prod_{i=1}^R(X-x_i)\right)\right]^S.
\tag{4}
\]

This is a precise bridge from an *ordinary-jet Gram determinant* to a **power of the discriminant of the sampling polynomial**. It is emphatically *not* the discriminant of the quadratic number field \(\mathbb Q(\sqrt{-D})\); the two arithmetic quantities govern different degenerations. The general nonvanishing argument is now given above at paper level. The next formalization target is a Lean proof of the Fourier-block unisolvence statement, or an equivalent elementary polynomial proof, with explicit ordinary-derivative conventions; classical confluent interpolation and determinant identities are prior art.

## Why this matters, and what remains open

The practical next question is not to discard the established interpolation criterion. It is to find a **new, stronger, simple-to-verify sufficient condition** in terms of selected node configurations and ordinary jets that can be proved uniformly on the compact integer ellipse.

A real-axis construction requiring \(R\) distinct real nodes has radius of order \(R\), which grows as \(D\), not \(D^{3/4}\), for the tuned production parameters. It is therefore **not** automatically an improvement of the production upper bound. The legitimate shape proposal is to distribute *unisolvent* nodes throughout the two-dimensional ellipse while retaining its cheap norm bound. Complex nodes provide two real coordinates per derivative order; selecting points can in principle approach a lower cardinality than a purely real-axis design. This is [H] until an exact uniform rank proof exists.

A small finite rank boundary, widely varying leverage, or a jagged chosen-radius plot does **not** prove NP-hardness or dynamical chaos. The D-optimal design literature supplies relevant classical determinant sensitivity and experimental-design machinery, but neither its terminology nor its complexity results should be silently transported to this particular structured interpolation problem. Any computational hardness assertion must specify the finite selection problem, its input encoding, the cost model, and a reduction or lower bound.

**Controls and promotion:** preserve the original 21-node baseline, exact antipodal matched cards, unchanged inert factor, all ordinary jets, negative seven-node rank case, differing 8-node placements, exact residual. [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) remains independent semantic reconstruction; [issue #51](https://github.com/Dojo-1/tenth-discriminant/issues/51) remains the global modular-rank versus same-Gram problem. A new 41.00625-billion endpoint must be proved in a separate Lean chain (see [draft PR #60](https://github.com/Dojo-1/tenth-discriminant/pull/60)); no such endpoint is asserted here.
