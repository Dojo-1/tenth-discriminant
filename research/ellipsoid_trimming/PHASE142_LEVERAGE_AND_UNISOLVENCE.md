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

This finite constancy suggests a **confluent diagonal Vandermonde theorem target**, not an established all-\(R,S\) formula. A counterworld is \(S>R\): derivative columns with \(j\ge R\) vanish identically, giving a singular square evaluation matrix.

## Why this matters, and what remains open

The practical next question is not to discard the established interpolation criterion. It is to find a **new, stronger, simple-to-verify sufficient condition** in terms of selected node configurations and ordinary jets that can be proved uniformly on the compact integer ellipse.

A real-axis construction requiring \(R\) distinct real nodes has radius of order \(R\), which grows as \(D\), not \(D^{3/4}\), for the tuned production parameters. It is therefore **not** automatically an improvement of the production upper bound. The legitimate shape proposal is to distribute *unisolvent* nodes throughout the two-dimensional ellipse while retaining its cheap norm bound. Complex nodes provide two real coordinates per derivative order; selecting points can in principle approach a lower cardinality than a purely real-axis design. This is [H] until an exact uniform rank proof exists.

A small finite rank boundary, widely varying leverage, or a jagged chosen-radius plot does **not** prove NP-hardness or dynamical chaos. The D-optimal design literature supplies relevant classical determinant sensitivity and experimental-design machinery, but neither its terminology nor its complexity results should be silently transported to this particular structured interpolation problem. Any computational hardness assertion must specify the finite selection problem, its input encoding, the cost model, and a reduction or lower bound.

**Controls and promotion:** preserve the original 21-node baseline, exact antipodal matched cards, unchanged inert factor, all ordinary jets, negative seven-node rank case, differing 8-node placements, exact residual. [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) remains independent semantic reconstruction; [issue #51](https://github.com/Dojo-1/tenth-discriminant/issues/51) remains the global modular-rank versus same-Gram problem. A new 41.00625-billion endpoint must be proved in a separate Lean chain (see [draft PR #60](https://github.com/Dojo-1/tenth-discriminant/pull/60)); no such endpoint is asserted here.
