# Phase158 — Characteristic sets for original ordinary jets

*1 November 2026 · canonical \`main\`. A finite, independently reconstructible calculation, not a new field-discriminant bound.*

The earlier radius work implicitly treated the whole ellipse as if every observation were necessary. Miguel N. Walsh's discussion of **characteristic subsets** invites a different question: which smaller sample set forces the same restricted polynomial to vanish? The conceptual inspiration is from Walsh; the statements below are elementary, domain-specific Hermite interpolation and coefficient linear algebra. **Neither the \`p\`-root theorem nor the coefficient-obstruction formula is attributed as a theorem of Walsh.** No new mathematical priority, collaboration or endorsement by him is claimed.

The original integer Gram stays unchanged **in its definition**: for each newly selected support \`Q\`, we independently evaluate the exact ordinary \`∂Z^j\` jets of \`Z^rW^s\`, holding \`W\` fixed, with original real/imaginary channels and weights \`2, 2D\`. A smaller \`Q\` creates a *different integer determinant*, not a passive gauge of the old one. Its arithmetic lower and real upper must both be reconstructed for that same \`G_Q\`.

## Frobenius and the correct rank problem

Let \`p\` be an odd prime with \`-D\` nonsquare modulo \`p\`, \`R=p-1\`, and \`1≤S=J≤R\`. The coefficient space of the original rectangular observables embeds along the characteristic-\`p\` Frobenius graph:
$$
V_{R,S}=\operatorname{span}_{\mathbb F_{p^2}}
  \{T^{r+ps}:0\le r<p-1,\ 0\le s<S\}.
$$
It consists of exactly those polynomials of degree at most \`pS-2\` whose coefficients in degrees \`kp-1\` (\`1≤k≤S-1\`) vanish. This is a **codimension \`S-1\`** subspace of all polynomials up to that degree, not an entire polynomial ring.

For \`j<S<p\`, the original partial-\`Z\` jet agrees with \`j!\` times the Taylor coefficient on the graph at a root \`a\`, because \`(a+h)^p=a^p+h^p\`, and \`h^p\` vanishes in the length-\`S\` quotient. The factorials are units at **this witness prime**. They are *not* units at all smaller primes that contribute to the integer Gram's divisibility.

A real-axis integer node contributes one residue root; a nonreal node plus its conjugate contributes two. The invertible real/imaginary-to-conjugate channel map requires \`p\` odd and inert, and all chosen residues distinct.

**Elementary p-root sufficiency [P-paper].** If the selected \`Q\` supplies \`p\` distinct conjugate-closed residue roots, the original \`RS\times(2S|Q|)\` integer evaluation has full row rank modulo \`p\`: a nonzero \`F\in V\` vanishing to order \`S\` at \`p\` distinct roots would have degree at least \`pS\`, contrary to \`deg F≤pS-2\`. Consequently its *original* positive-trace Gram is positive definite over the reals. This theorem is not yet Lean-formalized.

**Orbit-selecting p roots [P-paper].** If \`Q_full\` is a \`y≥0\` representative set for a conjugation-stable disk, contains at least one real node, has no mod-\`p\` collisions, and has \`N_full≥p\` effective residue roots, an exactly \`p\`-root conjugation-closed subset exists. Let \`k=min(n_nonreal,(p-1)/2)\`; retain \`k\` nonreal nodes and \`p-2k\` real nodes. Because \`N_full=n_real+2n_nonreal≥p\`, the latter number is positive, odd, and no larger than \`n_real\`. Selecting near the center is an implementation heuristic, not part of the rank proof. In Phase157 \`N_full>p\` is established at paper level by a disk-area bound, so this reduces the required support **without increasing its radius**.

## One fewer root produces a small, exact obstruction

Assume \`S≥2\` and precisely \`p-1\` distinct conjugate-closed residue roots \`A\`. Set their **monic annihilator**
$$
g_A(T)=\prod_{a\in A}(T-a)\in\mathbb F_p[T],
\qquad \deg g_A=p-1.
$$
A polynomial \`F\in V_{p-1,S}\` vanishes to order \`S\` at all roots of \`A\` iff \`F=g_A^S H\` with \`deg H≤S-2\` and the \`S-1\` forbidden coefficients vanish. Writing \`H(T)=\sum_{j=0}^{S-2}h_jT^j\`, this condition is exactly
$$
\boxed{
\mathcal O_{kj}=[T^{kp-1-j}]\,g_A(T)^S,\quad
1\le k\le S-1,\ 0\le j\le S-2.
}
$$
Therefore
$$
\boxed{\operatorname{rank}_{\mathbb F_p}E_A=RS
\iff \det\mathcal O\ne0.}
$$
This is an **exact equivalence** for these stated original-jet hypotheses, not a numerical approximation, but the general proof is still paper-level and should be checked independently. It shrinks an \`RS\`-row rank question to an \`(S-1)\times(S-1)\` obstruction. At the proposed multi-billion parameters, \`S-1\` remains enormous; no claim of a cheap production-time algorithm follows.

**Counterworld [M, exact].** At \`p=5,D=2,S=2\`, take two real nodes \`0,2\` and a nonreal conjugate pair with \`(x,y)=(0,1)\`. Then
$$
g(T)=T(T-2)(T^2+2)\in\mathbb F_5[T],
\quad [T^4]g(T)^2=0.
$$
The \`1\times1\` obstruction vanishes and the actual original ordinary-jet matrix has rank **7, not 8**. Thus \`p-1\` roots are **not a universal interpolation guarantee**. Real-axis multiplicative-group examples may succeed but need radius comparable to \`p\`, far larger than our intended \`O(D^{3/4})\` support.

## Exact D=163 observations [M]

With \`p=31,R=30,S=J=5\`, the complete radius-13 disk has 27 real-axis roots and five nonreal conjugate pairs, or **37 effective roots**. The deterministic center-first characteristic selection keeps 21 real roots and all five nonreal pairs: **26 integer nodes and exactly 31 effective roots**. Both the original integer-channel modular evaluator and the independent polynomial-quotient remainder model give rank **150/150**. Its original-jet raw Hadamard diagonal product strictly decreases relative to the full radius-13 support, and the compulsory \`2\`-primary factorial capacity goes from **310 to 430**. This is stronger certification of a *different, smaller Gram*, not determinant equality across supports.

The earlier **30-root** radius/cardinality frontier is also recovered via the obstruction:
| Radius | Integer nodes | Effective roots | Original rank | \`det \mathcal O\pmod{31}\` |
| ---: | ---: | ---: | ---: | ---: |
| 13 | 25 | 30 | 150/150 | 29 |
| 14 | 19 | 30 | 150/150 | 23 |
| 15 | 15 | 30 | 150/150 | 8 |

For the radius-13 support, the exact obstruction is
$$
\mathcal O=\begin{pmatrix}
0&4&26&23\\29&19&21&5\\2&14&9&14\\16&12&0&14
\end{pmatrix}\pmod{31},\quad\det\mathcal O=29.
$$
Its nonvanishing is separately matched to both original source rank and polynomial-quotient rank. Neither the finite \`p-1\` success nor the quotient oracle establishes an all-discriminant assertion.

## Where this meets our 2-primary arithmetic

For an **unweighted** characteristic support with exactly \`p\` effective scalar channels at each derivative order, \`m=(p-1)S\` rows, and **odd D**, each original nonzero trace weight has \`v_2=1\`. Cauchy–Binet's cheapest-column divisor is now an exact **capacity floor**, not an observed full determinant valuation:
$$
\boxed{
\beta_2^{\rm cap}
=(p-1)S+
2\left[p\sum_{j=0}^{S-2}v_2(j!)
      +(p-S)v_2((S-1)!)\right].
}
$$
Here \`p\` channels are taken at each order \`j<S-1\`, and \`p-S\` at the final order; this calculation uses no probabilistic model and no factorial rescaling of the integer determinant. The existing odd-prime lower product and this independent prime-2 divisor may be combined because they are coprime **only when both apply to this same new \`G_Q\`**.

At the sampled \`D=5,000,000,003\` with a genuine prime **parameter** \`p=1,041,666,709\` (not an assertion of class number one), the current Phase157 normalized \`L,U\` formulas give an improved pilot margin when replacing the earlier conservative upper capacity by this exact \`p\`-root capacity. A positive sample is not a universal 5-billion field bound. Indeed, the Phase157 field implication still awaits the uniform Frobenius-to-PosDef Lean bridge, the integral Cauchy–Binet/odd-mass combination, all-\`D\` scalar inequalities and independent review.

## Where the ideas come from

- **Tao's challenge**: [Terence Tao, experimental tenth-discriminant challenge (20 October 2026)](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/). The original derivative Gram and finite-field ideas in this area have important antecedents in **Ben Green**, **Roelof van Dijk**, **Kyle Pratt**, and challenge contributions including **twinheterodox**, **Peter Murphy**, **Antoine Olivier** and others, recorded with boundaries in [the prior-art ledger](../../PRIOR_ART.md) and [the source-aware comparison](../../METHOD_COMPARISON_CURRENT.md). No external endorsement is implied.
- **Miguel N. Walsh**, [*Characteristic subsets and the polynomial method*](https://www.mathunion.org/fileadmin/ICM/Proceedings/uploads/ICM-2018-vol2-ver1-eb.pdf), ICM 2018, vol. II, pp. 485–504: conceptual inspiration for demanding a smaller set that preserves polynomial vanishing constraints; **not a theorem imported into the present Gram**.
- **Miguel N. Walsh**, [*The inverse sieve problem in high dimensions*](https://doi.org/10.1215/00127094-1645788), *Duke Mathematical Journal* **161** (2012), 2001–2022: background on residue sparsity and forcing algebraic structure; not an inverse-sieve statement about our particular ellipse.
- **Miguel N. Walsh**, [*The polynomial method over varieties*](https://doi.org/10.1007/s00222-020-00975-6), *Inventiones mathematicae* **222** (2020), 469–512: context for restricting polynomial questions to the actual underlying algebraic variety; our Frobenius-graph specialization is separately derived.
- Root-counting with multiplicity, Hermite interpolation, Cauchy–Binet and factorial valuations are **classical**. The worked matrix, support-selection experiment and current proof targets were generated in the author's AI-assisted research process and are not independently refereed. We claim no globally novel theorem or permission from any cited mathematician.

**Reproduce:** \`python3 research/reverse_determinant/phase158_characteristic_jets.py\` on the pinned finite workflow with SymPy 1.14.0 and mpmath. It tests the original source evaluation and an independent quotient calculation, three exact characteristic obstructions, one falsifying counterworld, the radius/2-adic capacity trade-off and a high-precision *parameter-only* normalized budget probe. All claims stronger than these finite checks remain explicit [H].
