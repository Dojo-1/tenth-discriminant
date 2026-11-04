# Phase202 — arithmetic fibres, restricted radicals, and a source-typed Frobenius rank lift

**4 November 2026 | two tracks preregistered in [Issue #130](https://github.com/Dojo-1/tenth-discriminant/issues/130) BEFORE the first new experiment.** Source floor: the integrated \(322^4\) actual-field Lean theorem, [PR #126](https://github.com/Dojo-1/tenth-discriminant/pull/126), main commit \`f41ce45b\`. The separate [Phase201 PR #129](https://github.com/Dojo-1/tenth-discriminant/pull/129) is still a documentation draft. Human source-meaning review [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) stays open.

**Scope:** No stronger uniform cutoff, external determinant equality, remote collaborator validation, new Lean theorem or novelty claim. These are (i) standard algebra with proofs reconstructed on paper and (ii) deterministic exact finite tests. The code in this branch is unmerged and should receive its own run/CI receipt before any operational claim of remotely reproduced status.

## The one common integral source, not a fictitious common field

For fixed \(D,Q,R,S,J\), take the **original** ordinary-\(Z\) jets in [IntegerTraceGram.lean](../../lean/TenthDiscriminant/IntegerTraceGram.lean), holding \(W\) fixed:
\[
a_{r,s;j,z}+u\,b_{r,s;j,z}=\left.\partial_Z^j Z^rW^s\right|_{(z,\bar z)},
\qquad u^2=-D,\quad (a,b)\in\mathbb Z^2.
\]
Here \(\mathbb Z[u]\) is the selected integer-pair order; it is **not in general the maximal order**. Split each jet into two integral observation channels. Denote the resulting \(N\times2m\) integral matrix by \(E\), with \(N=RS\), \(m=J|Q|\). Let \(B=\mathrm{diag}(2,2D,\ldots,2,2D)\), indexed in the same \((j,z,a/b)\) order. The original integer trace Gram is
\[
G=EBE^{\mathsf T}\in \mathrm{Mat}_{N\times N}(\mathbb Z).
\]
Each matrix is *typed at the source*, not identified with another investigator's selected complex minor or with the field discriminant.

### Track A: base change and radical as the actual junction

**[P, standard algebra, proof on paper; Lean-source instantiation still H]** For **every commutative** \(\mathbb Z\)-algebra \(T\),
\[
G_T=E_TB_TE_T^{\mathsf T}.
\]
Reason: each matrix entry is a finite sum/product of integer coefficients, and any ring morphism preserves those operations. Equivalently, determinantal ideals \(I_k(E)\) and \(I_k(G)\) extend to their base-changed counterparts: \(I_k(E_T)=I_k(E)T\), similarly for \(G\). This is established Fitting/determinantal-ideal algebra, not a new result. See the [Stacks Project, Fitting ideals](https://stacks.math.columbia.edu/tag/07Z6), especially its base-change property.

**[P, elementary linear algebra, proof on paper; Lean-source instantiation still H]** Let \(k\) be a field of **any** characteristic, \(E\in k^{N\times M}\), \(B=B^{\mathsf T}\in k^{M\times M}\) (it may be degenerate), \(\iota=E^{\mathsf T}:k^N\to k^M\), and \(W=\operatorname{im}\iota\). Define
\[
\mathrm{Rad}_B(W)=W\cap W^{\perp_B},\qquad G=EBE^{\mathsf T}.
\]
There is a **short exact sequence**
\[
0\longrightarrow\ker E^{\mathsf T}
\longrightarrow\ker G
\xrightarrow{\ \iota\ }
\mathrm{Rad}_B(W)
\longrightarrow0.
\]
Indeed \(Gx=0\) iff \(\langle E^{\mathsf T}x,E^{\mathsf T}y\rangle_B=0\) for all \(y\); this is precisely \(E^{\mathsf T}x\in W\cap W^{\perp_B}\). Restricting \(\iota\) to \(\ker G\) is surjective onto the radical, with kernel \(\ker E^{\mathsf T}\). In particular:
\[
\boxed{\operatorname{rank}_k G
=\operatorname{rank}_k E-\dim_k\mathrm{Rad}_B(W).}
\]
This tells us *which* algebraic reason accounts for rank loss, not just whether a determinant vanished. When \(E^{\mathsf T}\) is injective the two kernels are isomorphic. No accidental demand that \(B\) be nondegenerate is needed.

**[M, independent exact finite source-typed test]** On the original ordinary-jet instance \(D=3,\rho=2,R=S=J=2\), 11 points, 22 complex columns, \(N=4\),
\[
G=\begin{pmatrix}
22&0&0&64\\0&64&-8&0\\0&-8&86&0\\64&0&0&296
\end{pmatrix},\quad \det G=13\,143\,040.
\]
Its integral determinantal divisors are \(d_k=(1,2,4,32,13143040)\), giving Smith factors \((2,2,8,410720)\). Thus the place-wise invariant profile is **not a scalar**: the valuations of the four Smith factors at \(2\) are \((1,1,3,5)\) and at \(5\) are \((0,0,0,1)\). At \(p=5\) the complex evaluation rank is 4, integer-channel rank 4, but trace-Gram rank **3**, with nonzero kernel vector \((0,1,3,0)\). At \(p=2\), the overall factor 2 makes \(G\bmod2=0\). At \(p=3\mid D\), the ambient metric degenerates, yet **this restricted Gram still has full rank 4 mod 3**. Therefore neither ambient degeneracy nor complex rank alone determines Gram rank.

A compact equal-determinant counterworld: \(\mathrm{diag}(1,25)\) and \(\mathrm{diag}(5,5)\) both have determinant 25 but ranks 1 and 0 modulo 5. Their \(I_1\) ideals and Smith profiles differ. This proves that the additional local data is not recoverable from the determinant alone; it does **not** yet show a better field cutoff.

### Track B: finite-field Frobenius rank without changing derivative types

**[P, mathematical lemma with explicit argument; Lean instantiation H]** Let \(p\) be an odd prime inert for \(\mathbb Q(\sqrt{-D})\) and let the reductions of points in \(Q\subset\mathbb Z[u]\) be distinct in \(\mathbb F_{p^2}\). Fix the rectangular \(R\times S\) ordinary-jet family and \(J\) derivative orders. If
\[
p\ge R,\quad 1\le J\le p,\quad
|Q|J>R-1+p(S-1),
\]
then its \(RS\)-row complex evaluation matrix is full row rank over \(\mathbb F_{p^2}\).

*Reason:* Frobenius gives \(\bar z=z^p\). The substitution \(F(Z,W)\mapsto F(Z,Z^p)\) is injective on the prescribed rectangular polynomials because the exponents \(r+ps\) are distinct when \(p\ge R\); its degree is at most \(R-1+p(S-1)\). If all ordinary jets vanished, each distinct reduced sample would be a root of multiplicity at least \(J\), since \(j!\ne0\) for \(j<J\le p\). Their total multiplicity would exceed the degree, impossible. A nonzero maximal minor mod \(p\) remains nonzero in characteristic zero, hence the **same** complex evaluation matrix has full row rank over \(\mathbb C\); then its original real trace Gram is positive definite.

**Important converse counterworld [P]:** If \(p<R\) and \(S\ge2\), \(Z^p-W\) is a nonzero row polynomial but all its ordinary \(Z\)-jets vanish at the Frobenius samples modulo \(p\), even if arbitrarily many samples are taken. This prevents a false universal full-rank statement.

**[M, preregistered positive experiment]** \(D=215\) is squarefree, \(R=p=53\), \(S=J=2\). Since \(-D\equiv-3\pmod{53}\) is a quadratic nonresidue, \(p=53\) is inert. For the explicitly **trimmed** radius \(\rho=16\), the selected integer-pair support contains exactly **59** points. We have \(2\rho=32<53\), hence distinct reduction, and \(nJ=118>105=(R-1)+p(S-1)\). Exact elimination gave:
\[
(\operatorname{rank}_{\mathbb F_{53^2}}A,\operatorname{rank}_{\mathbb F_{53}}E,\operatorname{rank}_{\mathbb F_{53}}G)
=(106,106,106).
\]
The old sufficient interpolation condition \(n>2(R-1)+(S-1)=105\) is **false** at the trimmed radius.

**[M, matched canonical-support control, added explicitly for source fidelity]** The Phase200 *canonical* \(D=215\) radius is instead \(\lceil (11/25)D^{3/4}\rceil=25\), not 16. Its support has **133** points, so the old count guard is true. It also satisfies \(2\rho=50<53\), and its exact rank triple is **again** \((106,106,106)\). Therefore the new positive test is a proof method on an **alternative support** where the old sufficient counting theorem fails, **not** a claim that the canonical production support was deficient. The two Gram determinants must not be identified.

**[M, preregistered hostile test]** With \(D=3,p=5,R=6,S=J=2,\rho=2\), the explicit row relation \(Z^5-W\) is zero in the modular evaluation array. Exact elimination returns complex row rank **11/12**, confirming the obstruction at \(p<R\).

### Why the two lines meet without collapsing

- At finite places the **typed** information is a filtration of determinantal ideals and, over residue fields, the rank/radical exact sequence. The Smith factors determine valuations of these ideals over \(\mathbb Z\). The ring \(\mathbb Z[u]\) should not be silently replaced by the maximal order, particularly at the index-two place \(p=2\).
- At infinity the real trace form becomes positive because of the complex embedding and ordinary positive Hermitian sum. **This positivity is not a statement about modular positive definiteness**; no such order is available in finite fields.
- A mathematically legitimate common junction is a **fixed nonzero integral minor at a fixed exterior degree**: its finite-prime divisibilities and Archimedean absolute size refer to *the same integer*, providing a possible higher-exterior-degree determinant sandwich. Whether arithmetic provides strong divisibility for all needed source minors, and geometry gives an upper for an actually nonzero one, is a new **H**. A scalar equality or a change of chart cannot discharge either condition.

## Post-registered extension — a finite-field rank reversal when support grows

**Evidence classification:** the p=7 effect was found in a *post hoc exploratory sweep* after preregistering [#130](https://github.com/Dojo-1/tenth-discriminant/issues/130). A targeted certificate check was preregistered separately in [#131](https://github.com/Dojo-1/tenth-discriminant/issues/131). Do not retrospectively describe the first observation as predicted. It is a finite counterexample and a test of transport semantics, not an improvement to the tenth-discriminant cutoff.

Keep \(D=215,R=53,S=J=2\) and the original derivative rows/trace metric, but compare \(Q_{16}\subset Q_{25}\). At the split prime \(p=7\), the trace weights are \(2,2D\equiv2,3\bmod7\), hence the ambient pairing is **nondegenerate**. Exact field elimination (cross-checked using a second SymPy DomainMatrix \(GF(7)\) implementation) gives

| Source support | \(|Q|\) | \(\operatorname{rank}E\bmod7\) | \(\operatorname{rank}G\bmod7\) | \(\dim\mathrm{Rad}_B(\mathrm{im}E^T)\) |
|---|---:|---:|---:|---:|
| Trimmed \(\rho=16\) | 59 | 28 | 28 | 0 |
| Canonical \(\rho=25\) | 133 | 28 | 26 | 2 |

**Exact rank lower witnesses:** the leading principal \(28\times28\) minor of \(G_{16}\) is \(4\bmod7\). The \(26\times26\) principal minor of \(G_{25}\) indexed by \(0,\ldots,23,25,27\) is \(2\bmod7\). The reproducible [certificate script](certify_mod7_rank_drop.py) constructs full independent nullspace bases of dimensions 78 and 80, verifies all basis vectors by direct modular matrix multiplication, and checks two explicit sparse vectors \(v_1,v_2\in\ker G_{25}\) whose images under \(E_{25}^T\) are independent, spanning the two-dimensional radical:
\[
\begin{aligned}
v_1&=3e_4+3e_7+2e_8+5e_{12}+5e_{15}+e_{16}+6e_{19}+2e_{20}+e_{24},\\
v_2&=5e_5+4e_6+2e_9+4e_{10}+6e_{14}+2e_{17}+3e_{18}+5e_{21}+3e_{22}+e_{26}.
\end{aligned}
\]
Indices use the source **zero-based** row order \(i=rS+s\); all coefficients are in \(\mathbb F_7\). Their images are nonzero and independent. A matched \(p=11\) control has \(\operatorname{rank}E=\operatorname{rank}G=44\) for both supports. This establishes a genuine local rank/radical change, **not** mere ambient metric degeneracy or loss of evaluation rank.

**A genuine typed moving-frame construction (local, not a universal manifold) [P conditional algebra + M inputs]:** Write \(\iota_{\rho}=E_\rho^{\mathsf T}:\mathbb F_7^{106}\to\mathbb F_7^{2J|Q_\rho|}\). Since \(Q_{16}\subset Q_{25}\), \(\ker\iota_{25}\subseteq\ker\iota_{16}\). Both maps have rank 28, so both kernels have dimension 78 and are **equal**, \(K\). This gives a **canonical** common quotient \(V=\mathbb F_7^{106}/K\), dimension 28, rather than arbitrarily identifying two different output spaces. Each \(G_\rho\) descends to a symmetric bilinear form \(\beta_\rho\) on \(V\). The same quotient thus carries \(\beta_{16}\) with zero radical and \(\beta_{25}\) with a two-dimensional radical. There is a structure-preserving map of the underlying quotient vector spaces, but **no isometry** of these two pairings via this canonical identification. The resulting form difference \(\beta_{25}-\beta_{16}\) is a well-defined typed transport remainder, not a cohomology class or a proof of novel holonomy. An exploratory exact computation also gives \(\operatorname{rank}_{\mathbb F_7}(G_{25}-G_{16})=28\); that number is secondary to the changed restricted-pairing type.

**Opposite Archimedean behaviour [P, simple quadratic-form identity]:** for the real embeddings, the difference
\[
G_{25}-G_{16}
=2\sum_{\substack{z\in Q_{25}\setminus Q_{16}\\0\le j<J}}
\operatorname{Re}\bigl(a_{z,j}a_{z,j}^{*}\bigr)
\succeq0,
\]
where \(a_{z,j}\) is the column of complex jet values over source rows. For every real vector \(x\), its quadratic form equals \(2\sum_{z,j}|\sum_r x_r a_{z,j,r}|^2\ge0\). Thus extending support is Loewner-monotone **at infinity**, while the Gram rank can *decrease* modulo 7, because no finite-field positivity order transports that inequality. No contradiction arises.

This is the cleanest current example of why **place-wise transport must retain the full pairing and its radical**, not just a common determinant or a slogan about moving manifolds. It also warns against calling a larger Q a universally better Gram for *arithmetic* purposes. The example varies Q and does **not** transfer to a bound on the fixed original Phase200 determinant.

Reproduce the targeted post-discovery check:
\`\`\`sh
python3 research/phase202/certify_mod7_rank_drop.py
\`\`\`

## Consequences, controls, and stop gates

| Claim | Status | Exact boundary |
|---|---|---|
| Source \(G=EBE^{\mathsf T}\) and matrix base-change identity | **P** (algebra, reconstructed) | Source-specific Lean theorem still to be coded and checked |
| Kernel/radical short exact sequence and rank formula | **P** (algebra, reconstructed) | True also with degenerate ambient pairing, any field characteristic |
| D=3 mod2/mod3/mod5 Smith and radical profile | **M** (finite exact) | Not a large-field discriminant argument |
| D=215 p=53 rank witness, trimmed/canonical support comparison | **M** (finite exact) | No class-number-one hypothesis and no substitution of full Gram |
| General inert prime rank lemma | **P** (paper-level argument) | Needs source-typed Lean proof before any formal-P claim |
| Uniform availability of \(p\ge R\) compatible with growing \(R(D)\), sampling budget and original Gram | **H** | Must be established under original field assumptions |
| A stronger field cutoff from local ideals/exterior degrees | **H** | Requires nonzero same-minor upper and arithmetic divisor lower; no numerical threshold advanced |
| Identifying external v7 selected minor with our Gram | **R** | Invalid; different \((Q,R,S,J)\) and matrix types |
| Inferring modular Gram invertibility solely from complex rank | **R** | D=3 mod5 counterexample |

**Cross-investigator scope:** [twinheterodox v0.7.0, derivative determinant §3](https://github.com/twinheterodox/tenth-discriminant/blob/v0.7.0/versions/v7/proof.tex) also uses ordinary jets and a Frobenius nonvanishing argument, but fixes \(R=p_0\), \(S=\lfloor3R/64\rfloor\), \(J=\lceil R/9\rceil\), and samples the **maximal-order lattice**. Our demonstration uses a selected integer-pair order, distinct dimensions and radius. The shared rank mechanism does not identify determinants or valuations, nor imply co-authorship or external peer review.

**Novelty scope:** base change/Fitting ideals, Smith filtration and the finite-field polynomial zero-multiplicity mechanism have well-established antecedents; no independent novelty claim is made. The programme-specific task is whether a *source-matched assembly* yields stronger constraints, and that remains unproved.

## Reproduce (no GPU, standard Python only)

\`\`\`sh
python3 research/phase202/placewise_jet_probe.py
python3 research/phase202/matched_canonical_support.py
\`\`\`

The first script executes the preregistered small-field/Smith controls, the \(D=215\) trimmed rank test and the \(p<R\) negative test. The second contrasts the canonical and trimmed \(D=215\) supports. No stochastic fitting, external imports or floating-point rank tests are used. Exact local computations were also run in an independent container session in this round; the new repository scripts themselves await an exact-head CI/replay receipt.

**Next specific proof obligations:** source-typed Lean \(G=EBE^\mathsf T\) entry and the kernel/radical exact sequence; a finite-field Frobenius interpolation rank lemma over the original integer order; a *matched-cost*, same-source exterior-minor test. If uniform prime supply or a strong source-minor divisor cannot be proved, keep the finite positivity result but retire any projected improved discriminant cutoff.