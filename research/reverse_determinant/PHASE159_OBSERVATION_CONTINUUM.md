# Phase159 — Observation continua, lattice transport, and deletion obstructions

*1 November 2026; exact source basis: main commit \`d1af5bac2ca51e4066eebd01831ccc82fbfe5c4a\` (Phase158). The exact tests below are independently executable finite experiments, **not** a stronger field theorem.*

Rather than treating every observation set as an unrelated Gram, we can regard the source ordinary-jet matrices as configurations of one observation system. This is useful only if real continuity and finite-prime arithmetic remain separately legible.

## The source object, no substitution

The original integer pair is \`x+y sqrt(-D)\`. For rows \`(r,s)\`, ordinary partial \`Z\` jets of \`Z^r W^s\` hold \`W\` fixed. The effective integer channel columns of \`E_Q\` have positive diagonal metric \`B_Q=diag(2,2D)\` for nonreal points and a single nonzero real channel with weight 2 at a real-axis point. Deleting the identically zero imaginary columns on the real axis changes neither the trace Gram nor its determinant.

\[
G_Q=E_QB_QE_Q^{\mathsf T}.
\]
A new support defines a **new** integer Gram. Original-vs-Hasse jet substitution is not allowed at small primes. The metric must not be replaced by the trace form of a half-integral field basis. The [source-matched Python verifier](phase159_observation_continuum.py) checks the old Phase147 evaluator including these weights.

## The continuous real fiber and its limitation [P-paper]

For the full collection of real observation channels \(a_i\) and positive source weights \(b_i\), define
\[
G(z)=\sum_i z_i b_i a_i a_i^{\mathsf T},\qquad 0\le z_i\le1.
\]
Integral support indicators \(z_i\in\{0,1\}\) recover the original Grams. For \(Q'\subseteq Q\) full rank, \(G_Q-G_{Q'}\succeq0\), so \(0<\det G_{Q'}\le\det G_Q\). The interpolation \((1-t)G_{Q'}+tG_Q\) remains positive definite. Its logarithmic derivative is \(\mathrm{tr}(G(t)^{-1}(G_Q-G_{Q'}))\ge0\). The conclusion requires **independent diagonal channel weights**; a general cross-coupled positive metric does not allow the same sub-Gram ordering simply by dropping blocks.

Let \(L_Q=E_Q\mathbb Z^{N_Q}\), \(d_Q=[\mathbb Z^{RS}:L_Q]\), and \(H_Q=\det G_Q/d_Q^2\). If \(E_Q\) has full integral row rank and \(B_Q\) is positive integral then \(H_Q\in\mathbb Z_{>0}\) by factoring \(E_Q=B_Q^{\rm lattice}C_Q\) through a basis of its column lattice. Here \(B_Q^{\rm lattice}\) is a basis matrix, **not** the trace metric. For nested full-rank supports, \(d_Q\mid d_{Q'}\) and \(H_{Q'}\le H_Q\), because
\[
\log(H_Q/H_{Q'})=\log(\det G_Q/\det G_{Q'})+2\log(d_{Q'}/d_Q).
\]
This is a monotonic **real size** statement, not a divisibility statement about \(H_Q/H_{Q'}\), or a monotonicity statement about \(v_q(\det G_Q)\).

The multivariate unweighted observation polynomial
\[
P_E(z)=\det(E\,\mathrm{diag}(z)\,E^{\mathsf T})
=\sum_{|I|=RS}(\det E_I)^2\prod_{i\in I}z_i
\]
encodes every maximal minor. Over any field \(K\), if \(E=[E_0\ E_1]\) has full row rank, then the order in \(t\) of the **formal multivariate** polynomial \(P_E(z_0,tz_1)\) equals \(RS-\operatorname{rank}_K E_0\). The separate \(z_i\) prevent monomial cancellation. Crucially, this is the *unweighted* rank polynomial: the physical trace weights are all even and can annihilate the weighted determinant polynomial modulo two. Likewise setting all \(z_i=1\) before reduction modulo a prime can cause coefficient cancellation.

## One prime, one missing root [P-paper and M]

For odd inert witness prime \(p\) and \(2\le S<p\), our Frobenius section space has basis \(T^{r+ps}\), \(0\le r<p-1,\ 0\le s<S\). For \(p-1\) conjugate-stable roots \(A\) with \(g_A(T)=\prod_{a\in A}(T-a)\), rank is equivalent to
\[
\det O_A\ne0\pmod p,\qquad
(O_A)_{k,j}=[T^{kp-1-j}]g_A(T)^S,\quad
1\le k\le S-1,\ 0\le j\le S-2.
\]
It is **not** universally true that deleting a real root from a full-rank \(p\)-root support preserves rank.

A successful constructive but noncompetitive-radius control is \(A=\mathbb F_p^\times\), \(g_A=T^{p-1}-1\); then
\[
(O_A)_{k,j}=\mathbf 1_{j=k-1}(-1)^{S-k}\binom Sk
\]
and all diagonal terms are nonzero for \(S<p\). For \(p=31,S=5\), \(\det O=20\bmod31\).

The source-matched D163, p31, R30, S5 characteristic selection has 26 integer nodes / 31 residue roots. **Every one of its 21 possible real-root deletions** yields a nonzero \(\det O\bmod31\), retaining rank 150 with 25 nodes / 30 roots. The compulsory 2-adic factorial capacity rises from **310** (complete radius-13 disk) to **430** (31 roots) to **450** (all these 30-root supports). These are *floors*, not actual determinant valuations.

Two counterworlds have been independently calculated using the original ordinary-jet evaluator and the separate coefficient obstruction: at \(p=7,D=1,S=3,\rho=3\), support \(\{(0,0),(0,1),(0,2),(2,2)\}\) has full rank 18, but deletion of its sole real root gives rank 17, with \(O=\left(\begin{smallmatrix}1&4\\4&2\end{smallmatrix}\right)\bmod7\) singular. At \(p=11,D=3,S=3,\rho=5\), the support \(\{(-5,0),(-4,1),(-3,1),(-2,1),(-1,1),(3,2)\}\) has rank 30; deletion of \((-5,0)\) gives rank 29. Both obey \(2\rho<p\) and inertness. The second also satisfies \(D\equiv3\bmod4\), but is not a production large-\(D\) field theorem.

## Actual q-adic valuation is a fourth observable [M]

The second [exact modular verifier](phase159_padic_gram.py) reconstructs the **same weighted integer Gram**, then performs 2-adic Smith-style elimination modulo both \(2^{64}\) and \(2^{128}\). Every invariant exponent is strictly less than 64 and the two computations agree; thus the valuation sums are exact for these finite cases.

| D163 support | factorial capacity floor | exact \(v_2(\det G)\) |
|---|---:|---:|
| 31 roots, 26 nodes | 430 | 3187 |
| remove center \((0,0)\), 30 roots | 450 | 3200 |
| remove outer \((10,0)\), 30 roots | 450 | 3176 |

The real determinant decreases under either deletion, the compulsory factorial divisor increases, **yet the actual 2-adic valuation moves in opposite directions**. There is no general monotonicity of \(v_2(\det G_Q)\) under deleting observations.

A small exact trace-Gram countercontrol at D3,R2,S2 uses \(Q_0=\{(0,2)\}\subset Q_1=\{(0,2),(0,1)\}\). The determinants are respectively 2304 and 53280; lattice indices 4 and 1; residual integers \(H=144\) and \(53280\). The minimum 2-adic Cauchy–Binet term valuation for \(Q_1\) is 4, but \(v_2(\det G_{Q_1})=5\): the lowest-valuation terms sum to zero modulo 2. Hence the capacity floor need not be sharp even at fixed support.

The factorial lower bound, lattice index and actual Gram valuation are different invariants and cannot be conflated. Existing inert-prime mass from the class-number-one argument may involve determinant divisibility not reducible to the column lattice index alone.

## Proof obligations, no premature cutoff

The existing [\`prime_mass_log_lower_of_det_pos\`](../../lean/TenthDiscriminant/RadialCutoff.lean) already accepts arbitrary Q **conditional on positivity** and the class-number-one, squarefree, congruence and prime-range hypotheses. The Phase159 proof path is therefore to formalize the Frobenius \(p\)-root rank-to-positivity bridge on the **same original Gram**, the factorial Cauchy–Binet divisor, its coprime conjunction with *existing* odd-prime mass, and a uniform same-support analytic upper. A \(p-1\)-root optimization is conditional and needs a **uniform obstruction nonvanishing certificate** for a competitive-radius support family; finite successes are not enough.

The formally recorded actual-field bound remains **47 billion**, with independent semantic reconstruction open. The **5-billion** endpoint is a candidate only. Phase159 itself adds no Lean theorem, does not verify a new field cutoff, and must not treat a cancelled Lean workflow as successful.

## Attribution

The tenth-discriminant investigation responds to [Terence Tao's challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/), including antecedents by Ben Green, Roelof van Dijk and Kyle Pratt, with other challenge contributors recorded in [prior art](../../PRIOR_ART.md). [Miguel N. Walsh's ICM 2018 lecture](https://www.mathunion.org/fileadmin/ICM/Proceedings/uploads/ICM-2018-vol2-ver1-eb.pdf) motivates characteristic subsets, but does not assert this specific jet or obstruction theorem. Cauchy–Binet, confluent Vandermonde, the matrix-determinant lemma and Hermite interpolation are classical. The finite combinatorial organization relates to **arithmetic matroids** (Michele D'Adderio and Luca Moci), **valuated matroids** (Andreas Dress and Walter Wenzel), and determinantal-stability literature (Julius Borcea, Petter Brändén and Thomas Liggett); no direct application of their theorems to our field cutoff is asserted. These experiments were developed in Jesús Vilela Jato's Dojo-1 AI-assisted research programme; model-generated self-tests are not independent mathematical refereeing.

Reproduce the bounded Python checks with SymPy 1.14.0:
\`\`\`sh
python3 research/reverse_determinant/phase159_observation_continuum.py
python3 research/reverse_determinant/phase159_padic_gram.py
\`\`\`
