# The Tenth Discriminant

*Arithmetic against geometry, with one integer determinant in the middle.*

Can arithmetic force an integer to be **larger** than geometry allows it to be?

That is the guiding question of this AI-assisted investigation, begun in response to [Terence Tao's experimental tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/). The difficult part is not making a number smaller. It is showing that the arithmetic lower bound and geometric upper bound genuinely constrain **the same integer**, with the same polynomial jets, integral lattice, sampling set and field assumptions.

The repository combines number theory, exact computation, integral linear algebra, real geometry and Lean 4. It also records failed approaches. A failed transport, a lost prime factor or an incorrect normalization is useful evidence—not something to hide behind a more impressive-looking theorem.

## Where the formal work stands

**Strongest integrated Lean theorem — 3 November 2026.** For every totally complex quadratic number field $K$ of class number one, the encoded and checked theorem concludes that the **actual absolute field discriminant**, not the auxiliary trace-Gram determinant, satisfies

```math
|\mathrm{disc}(K)|<323^4=10{,}884{,}540{,}241.
```

The declaration [Threshold323.totallyComplex_degree_two_classNumber_one_discriminant_bound_323](lean/TenthDiscriminant/ActualField323.lean) was integrated by [PR #123](https://github.com/Dojo-1/tenth-discriminant/pull/123) at [commit dc7e19eb](https://github.com/Dojo-1/tenth-discriminant/commit/dc7e19ebefe2aecb0f2644b2ccd2b42203200a55), after **25/25** exact-head checks passed (including the full-root source, Lean, negative-control and security checks). The earlier $328^4$, $327^4$ and $324^4$ theorems remain separately auditable historical milestones.

**Next candidate — not an integrated field theorem.** [Phase200 / Issue #121](https://github.com/Dojo-1/tenth-discriminant/issues/121) studies fourth root $322$. The sound scalar, original thin-ellipse geometry, original primes 3/5 valuation gain, and the **same-original-Gram arithmetic lower** have passed their focused Lean checks. The sharpened [original analytic upper](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41717275582) is separately under verification; the full [322 field return](https://github.com/Dojo-1/tenth-discriminant/blob/research/phase200-same-gram-field322/lean/TenthDiscriminant/ActualField322.lean) remains a research target. Do not promote it from a rational separator or from an isolated lemma.

**External numerical perspective.** [twinheterodox v0.7.0](https://github.com/twinheterodox/tenth-discriminant/tree/v0.7.0/versions/v7) reports the much stronger cutoff $q<570$, with finite completion; other routes on [rStation](https://rstation.ai/problems/tenth_discriminant) reach smaller cutoffs still. Our present numerical bound is **not competitive** with those. The possible value of comparing the approaches lies in their source constructions, exactly which determinant is controlled, and their machine-checking assumptions—not in treating unlike rank arguments or numerical gaps as interchangeable. See [source-aware comparison](METHOD_COMPARISON_CURRENT.md) and the [frozen external bridge contract](https://github.com/Dojo-1/tenth-discriminant/blob/research/phase200-same-gram-field322/research/bridges/EXTERNAL_DETERMINANT_ALIGNMENT_20261103.md).

**The boundary matters.** Lean checks formal statements relative to definitions, imports and permitted axioms; it cannot substitute for an independent mathematician reconstructing the maximal-order-to-inertness bridge, integral ordinary jets, positivity, Hadamard upper, scalar gap, and field interpretation. That review is still explicitly open in [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50). No new nine-field classification, independent referee endorsement, or novelty priority is claimed.

Earlier checked endpoints—$324^4$, $327^4$, $328^4$, $331^4$, $375^4$, $377^4$, [41,006,250,000](research/thin_integrated/HUMAN_GUIDE_CURRENT.md), and [approximately 47 billion](research/tight_radial_v1/HUMAN_RECONSTRUCTION.md)—remain historical. Proposed five-billion and alternative-support arguments are **not** established field bounds.

## The one integer that matters

Take the original rectangular monomials $Z^rW^s$. Their ordinary $Z$-derivatives, **holding $W$ fixed**, are

```math
\partial_Z^j(Z^rW^s)=
\begin{cases}
(r)_{\underline{j}}\,Z^{r-j}W^s, & 0\le j\le r,\\
0, & j>r.
\end{cases}
```

Evaluating these jets at the original integer-pair observations $Q$ produces an integer matrix $E_Q$. The original trace pairing supplies the positive diagonal channel metric $B_Q$, with weights $2$ and $2D$ in the corresponding channels. Together they define

```math
G_Q=E_QB_QE_Q^{\mathsf T},
\qquad
\Delta_Q=\det G_Q>0.
```

The determinant $\Delta_Q$ is an **auxiliary integer**, *not* the number field's discriminant. It is the meeting place of two arguments:

- **Arithmetic:** guarded inert-prime and binary divisibility force $\Delta_Q$ to have sufficient prime factors.
- **Geometry:** the original ordinary-jet Hadamard bound constrains the size of that very same $\Delta_Q$.

Changing $Q$, the derivative convention, the lattice or the trace metric can change the problem. A prettier estimate for a *different* Gram is not a proof about the original one.

```mermaid
flowchart LR
    K["Imaginary quadratic field and class number 1"] --> Q["Original integer observations and ordinary jets"]
    Q --> G["ONE integer trace Gram"]
    G --> P["Inert primes: arithmetic lower bound"]
    G --> A["Real geometry: analytic upper bound"]
    P --> C{"Both bounds on the same determinant?"}
    A --> C
    C --> X["Contradiction at the stated threshold"]
    X --> F["Return to the actual field discriminant"]
```

## How the integrated 323⁴ argument closes

The positive original thin-ellipse ordinary-$Z$-jet trace Gram is established by [SourceGeometry323](lean/TenthDiscriminant/SourceGeometry323.lean) and [SourcePositivity323](lean/TenthDiscriminant/SourcePositivity323.lean). The [odd-prime lower](lean/TenthDiscriminant/Lower323.lean) retains the original $R=\lfloor D/4\rfloor$, $S=\lfloor R/25\rfloor$, primes $3$ and $5$, and their proven $0.0895$ floor-ratio recovery; [SourceOddBinary323](lean/TenthDiscriminant/SourceOddBinary323.lean) includes the original binary factor **once**. [ThinUpper323](lean/TenthDiscriminant/ThinUpper323.lean) bounds that same integer Gram analytically, using the padded ellipse **only for its cardinality majorant**. [ActualField323](lean/TenthDiscriminant/ActualField323.lean) connects the contradiction to the maximal-order quadratic field and the actual discriminant.

For $D\ge323^4$, the source-matched estimates assert

```math
\frac{999997}{1000000}\log D-\frac{57205}{10000}+\frac14\log 2
\;\le\;\frac{\log\det G_D}{R^2S}
\;\le\;\frac45\log D-\frac{1851}{2000}.
```

The finite-series certificates give $\log D\ge231104/10000$ and $\log2\ge6931/10000$ at the threshold; their exact rational separating margin is $178543/625000000>0$. These are constraints on **one unchanged positive integer determinant**. The margin is not a measure of how close the result is to the best external analytic cutoff, nor evidence of independent semantic review.

Historical [328⁴ endpoint](lean/TenthDiscriminant/ActualField328.lean), [327⁴ endpoint](lean/TenthDiscriminant/ActualField327.lean) and [324⁴ endpoint](lean/TenthDiscriminant/ActualField324.lean) remain available with their original CI evidence. The source-to-source review in [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) is still open.

## What the different investigations establish

| Thread | What survives scrutiny | Where to inspect |
| --- | --- | --- |
| **Arithmetic (Phases162–166)** | Lean-checked divisibility and logarithmic lemmas for the original ordinary-jet Gram, with one binary factor and an odd-only prime product. | [Binary divisor](lean/TenthDiscriminant/BinaryNullTraceGram.lean) · [binary normalization](research/thin_integrated/PHASE165_EXACT_BINARY_NORMALIZATION.md) · [same-Gram log guide](research/thin_integrated/PHASE166_SAME_GRAM_LOG.md) |
| **Integrated field bound (Phase199)** | Encoded strict $323^4$ actual-field endpoint, with 25/25 whole-root checks; independent semantic review remains open. Earlier $324^4$, $327^4$ and $328^4$ are historical. | [323 source](lean/TenthDiscriminant/ActualField323.lean) · [PR #123](https://github.com/Dojo-1/tenth-discriminant/pull/123) |
| **Original-prime recovery (Phases190–200)** | Original primes 3 and 5: $0.0895$ floor-ratio gain integrated for the 323 theorem; $0.0901$ is a separately focused-Lean-checked 322 source gain, not yet an integrated 322 field result. | [Integrated floor-ratio lemma](lean/TenthDiscriminant/RecoveryGainFloorRatio.lean) · [322 source bridge](https://github.com/Dojo-1/tenth-discriminant/blob/research/phase200-original-prime-gain322/lean/TenthDiscriminant/Phase200PrimeRecovery322.lean) |
| **322 research target (Phase200)** | Scalar, source geometry and original-Gram arithmetic lower are focused-Lean-checked; same-Gram analytic upper, full field return and whole-root integration remain separate obligations. | [Issue #121](https://github.com/Dojo-1/tenth-discriminant/issues/121) · [322 research branch](https://github.com/Dojo-1/tenth-discriminant/tree/research/phase200-same-gram-field322) |
| **Characteristic observations (Phase158)** | Exact finite rank, coefficient-obstruction and $2$-adic capacity experiments; no uniform new field cutoff. | [Dossier](research/reverse_determinant/PHASE158_CHARACTERISTIC_JETS.md) · [verifier](research/reverse_determinant/phase158_characteristic_jets.py) |
| **Support and arithmetic gluing (Phases142, 159–160)** | Exact finite examples separating full rank, integral image, Smith data and Gram volume. A smaller support need not yield a smaller determinant bound. | [Phase142](research/ellipsoid_trimming/PHASE142_LEVERAGE_AND_UNISOLVENCE.md) · [Phase159](research/reverse_determinant/PHASE159_OBSERVATION_CONTINUUM.md) · [Phase160](research/reverse_determinant/PHASE160_ARITHMETIC_NEURITES.md) |
| **Symmetry (Phase161)** | Source-preserving conjugation and related finite controls; removing a symmetric observation is not automatically safe. | [Human guide](research/reverse_determinant/PHASE161_SYMMETRY_GUIDE.md) · [Lean](lean/TenthDiscriminant/ObservationConjugation.lean) |
| **Normalized 2-adic filtration (Phase181; bounded pilot)** | After the existing Phase162 row factors are removed, exact Smith barcodes distinguish two D=163 supports having the same first mod-2 nullity. No production-uniform gain or new field cutoff is proved. | [Finite pilot and explanation](research/reverse_determinant/PHASE181_NORMALIZED_BINARY_FILTRATION.md) · [open target #99](https://github.com/Dojo-1/tenth-discriminant/issues/99) |
| **Transport coherence (Phase179)** | The formal determinant-one rational shear preserves volume but not the anchored integral lattice. | [merged PR #98](https://github.com/Dojo-1/tenth-discriminant/pull/98) · [Lean](lean/TenthDiscriminant/TransportCoherence.lean) |

One exact arithmetic example behind the current transport study is worth keeping in sight:

```math
H=\begin{pmatrix}1&\frac12\\0&1\end{pmatrix},
\qquad
G_0=\begin{pmatrix}4&0\\0&4\end{pmatrix},
\qquad
HG_0H^{\mathsf T}
=\begin{pmatrix}5&2\\2&4\end{pmatrix}.
```

The two integral Grams have equal determinant $16$, yet not the same integral congruence class. The obstruction is concentrated at the prime $2$ *relative to the fixed lattice reference*. Transport the reference lattice as well, and the semantic question changes. This counterexample is not a new discriminant bound and not a theorem of intrinsic computational hardness. The formalization is integrated in [PR #98](https://github.com/Dojo-1/tenth-discriminant/pull/98); [PR #104](https://github.com/Dojo-1/tenth-discriminant/pull/104) adds finite fixed-versus-moving extraction controls.

For the dated, detailed research record—including unsuccessful attempts—see [RESEARCH_NOW.md](RESEARCH_NOW.md), the [reverse-determinant research index](research/reverse_determinant/README.md), and the [prior-art ledger](PRIOR_ART.md). The [earlier long README is archived](research/archive/ROOT_README_BEFORE_PHASE158_2026-11-01.md).

## Reproduce, inspect, challenge

The repository pins **Lean 4.19.0** and **Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`**. To build and audit the formal library:

```sh
cd lean
lake exe cache get
python3 verify_sources.py
lake build
python3 audit.py
python3 negative_controls.py
```

For one bounded exact finite experiment, from the repository root:

```sh
python3 -m pip install sympy==1.14.0 mpmath
python3 research/reverse_determinant/phase158_characteristic_jets.py
python3 research/reverse_determinant/phase181_normalized_binary_filtration.py
python3 research/reverse_determinant/phase181_thin_support_pilot.py
```

For the documentation's math/Markdown sanity check:

```sh
python3 scripts/check_readme_math.py README.md
python3 scripts/check_human_math.py
```

A successful finite test is evidence about the tested instances. A successful Lean build is evidence about the *encoded theorem*. Neither is an independent external review of the whole intended argument. If you find a missing hypothesis, wrong field identification, false lemma, normalization mismatch or counterexample, please include the exact claim and a reproducible witness. [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) and [the source-to-source transport review](https://github.com/Dojo-1/tenth-discriminant/issues/51) are natural starting points.

## Attribution and context

The challenge and its [adelic-determinant context](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/) are due to **Terence Tao**. The derivative-determinant approach is credited to **Ben Green**; **Roelof van Dijk** and **Kyle Pratt** contributed distinct related methods discussed in Tao's thread. Related arguments and formalizations by **twinheterodox, Peter Murphy, Antoine Olivier**, and others include stronger bounds. The citations neither imply collaboration nor endorsement; see [PRIOR_ART.md](PRIOR_ART.md) and [METHOD_COMPARISON_CURRENT.md](METHOD_COMPARISON_CURRENT.md).

The question behind our characteristic-support experiments was inspired by **Miguel N. Walsh's** work on the polynomial method, not presented as a theorem he proved about our construction. See [Walsh's ICM survey](https://www.mathunion.org/fileadmin/ICM/Proceedings/uploads/ICM-2018-vol2-ver1-eb.pdf), [the inverse sieve problem](https://doi.org/10.1215/00127094-1645788), and [the polynomial method over varieties](https://doi.org/10.1007/s00222-020-00975-6).

Research direction: **Jesús Vilela Jato (Dojo-1)**, with substantial AI assistance for exploration, code, Lean, explanatory writing and checking. The AI systems are not independent referees. Our aim is not to turn machine-generated polish into borrowed authority, but to leave every mathematical claim open to reconstruction and correction.

*Documentation convention:* use inline $x$-style math and fenced `math` blocks for displayed formulae. Do not place mathematical expressions inside code spans or split a single-dollar expression across multiple lines. The sanity checks catch common markup failures, **not** mathematical mistakes or every possible MathJax rendering defect.
