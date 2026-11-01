# Phase152 — Frobenius graph, sheaved ordinary jets and a radius–support Pareto frontier

**1 November 2026 · canonical `main` only.** Evidence [P-paper]: exact elementary polynomial/finite-field and geometry lemmas below; *not yet Lean formalized*. [M]: original-jet source-matched exact modular tests at D=43 and D=163 and a hypothetical large-parameter geometry check. [H]: uniform production field cutoff. [R]: the implication that a sufficient degree bound is necessary, or that a smaller-radius alternative family already proves a stronger discriminant bound.

## The geometry we actually manipulate

Start on the **two-dimensional algebraic surface** `Spec k[Z,W]` and polynomial section space `V=span{Z^r W^s:0≤r<R,0≤s<S}` of dimension `RS`. Every observation is the original **ordinary partial-Z** directional jet `∂_Z^j`, **holding W fixed**, with `j<J`. The integer matrix `E_Q(D)` retains its usual paired real and imaginary channels and positive metric `B=diag(2,2D,...)`.

For an odd inert prime `p` in the imaginary quadratic order, reduction sends `z^p=\bar z` in the residue field `k≈F_(p²)`. The **Frobenius graph**
\[
\Gamma_p=\{(Z,W):W=Z^p\}
\]
gives the restriction homomorphism
\[
\phi_p: V\longrightarrow k[T],\quad Z^rW^s\mapsto T^{r+ps}.
\]

If `p≥R`, the exponents `r+ps` are all **different**. Hence `φ_p` is injective and every nonzero section maps to a nonzero polynomial of degree at most `(R−1)+p(S−1)`. If `J≤p`, its ordinary `j`-derivatives for `0≤j<J` agree with the pulled-back original ordinary `∂_Z^j` jets: `∂(T^p)=0` for `j<p`, and the falling factorials are unchanged modulo p.

Let `N_p(Q)` count all distinct residue roots represented by `z_q` **and** `\bar z_q` for selected integer-pair nodes `q=(x,y)`. Distinctness includes matching the two roots of each nonreal node. Over the quadratic residue field, an invertible change of channels converts the integer `(re,im)` columns into these two conjugate complex evaluation blocks; for real-axis points the imaginary channels vanish and contribute only one block.

**Theorem target [P-paper, elementary proof].**
For `p` odd inert, `1≤J≤p`, `1≤S≤R≤p`, and all conjugate residues distinct,
\[
\boxed{J N_p(Q)>(R-1)+p(S-1)
\quad\Longrightarrow\quad
\operatorname{rank}_{\mathbf F_p}E_Q(D)=RS.}
\]
Proof by contradiction: a nonzero row relation maps under `φ_p` to a nonzero `F(T)` of the displayed degree. Vanishing of all original paired ordinary jets forces every one of the `N_p` distinct roots to have multiplicity at least `J`. This contradicts the degree bound. Consequently `E_Q` has full characteristic-zero row rank and `G_Q=E_Q B E_Q^T` is positive definite for every `D>0`. This is **the same original integer Gram** whose inert-prime mass is studied in [Phase149](PHASE149_POSITIVITY_BRIDGE.md).

```mermaid
flowchart LR
   A["Original ordinary-Z jet bundle"] --> B["Frobenius graph W=Z^p"]
   B --> C["Sheaf restriction: r,s -> r+ps"]
   C --> D{"p >= R ?"}
   D -->|yes| E["Injective polynomial pullback"]
   E --> F["Conjugate residues and multiplicity J"]
   F --> G["RS independent rows: original Gram positive"]
   D -->|no| H["Kernel Z^p-W; divide/filter Frobenius"]
```

**Mandatory failure:** if `p<R` and `S≥2`, the nonzero section `Z^p−W` lies in the rectangle but maps to zero on `Γ_p`, and all its ordinary jets below order p vanish modulo p. The Phase152 verifier checks this **actual row relation** at D=43,p=7,R=8,S=2. Thus the clean no-collision proof cannot be silently used in the production R≈D/4 regime with only inert primes p<R.

## Coherent-sheaf factorization [P-paper] — where geometry enters the theorem

Over \`k≈F_(p²)\`, compactify to the **algebraic surface** \`X=P¹_Z×P¹_W\`, with section bundle \`L=O_X(R−1,S−1)\`. The Frobenius-graph embedding is \`i_p:P¹_T→X, T↦(T,T^p)\`. There is an exact, type-preserving bundle identity
\[
\boxed{i_p^*L=O_{P^1}((R-1)+p(S-1)).}
\]
This degree is *precisely* the maximum exponent in the polynomial proof. The composed jet-restriction map on global sections factors as
\[
H^0(X,L)\xrightarrow{i_p^*}H^0(P^1,O(d_p))
\xrightarrow{\mathrm{jet\,eval}}\bigoplus_{\xi\in\Xi}
   O(d_p)\otimes \mathcal O_{P^1,\xi}/\mathfrak m_\xi^{J},
\quad d_p=(R-1)+p(S-1).
\]
The first arrow is injective for \`R≤p\` by the distinct \`r+ps\` exponents. The kernel of the second arrow is
\[
H^0(P^1,O(d_p-J\sum_{\xi\in\Xi}[\xi]))=0
\quad\text{if }JN_p>d_p.
\]
Hence the full-rank criterion is an **actual sheaf-kernel vanishing theorem**, not an analogy with higher-dimensional geometry. In characteristic p, \`(T+t)^p=T^p+t^p\`; for \`J≤p\` the length-J directional jets pull back correctly because the normal (W) coordinate does not change to orders less than J. The factorization remains tied to original ordinary jets rather than silently changing to Hasse jets.

The failure at \`p<R\` is located in the **first** map: \`H⁰(X,I_(Γp)⊗L)\` contains the nonzero globalized section \`Z^p−W\` (when S≥2). This is the candidate entrypoint for a conormal/Rees filtration \`I^m/I^(m+1)\` and the larger divided-Frobenius geometry in the published 331 argument. Such a filtration needs a separate integral p-adic transport, so do not infer automatic equivalence of the rectangular and triangular determinants.

## Localized support existence under the class-number-one *hypothesis*

For `D≡3 mod4`, squarefree, `D≥10^6`, and the **hypothetical premise** `h(-D)=1`, every prime `p<(D+1)/4` is inert, by the standard norm-minimum obstruction. Put `m=(D+1)/4`. Bertrand gives an odd prime `m/2<p<m` (m≥6), hence an inert witness supplied by the same arithmetic assumption; no split-prime count above that inertness threshold is needed. Take `R=p−1`, `J=S`, `1≤S≤R`, and
\[
\delta=\frac12\sqrt{D+1},\qquad
\rho=\left\lceil\delta+\sqrt{\frac{p\sqrt D}{3}}\right\rceil.
\]
The rectangular integer lattice `Z+Z√(-D)` has covolume `√D` and covering radius `δ`. Voronoi-cell area comparison yields
\[
|\Omega_D(\rho)|\ge\frac{\pi(\rho-\delta)^2}{\sqrt D}>\!p,
\quad\Omega_D(\rho)=\{(x,y)\in\mathbb Z^2:x^2+Dy^2\le\rho^2\}.
\]
For `D≥10^6` the elementary inequalities `p>(D+1)/8` and `p<(D+1)/4` ensure `2ρ<p` and `ρ<0.31 D^{3/4}`. Thus the residues of *all* lattice nodes in the disk are distinct modulo `pO_D`: if `a-b∈pO_D` and `a≠b`, then `|a-b|≥p`.

Take one representative from each conjugate orbit, `Q^+=\{(x,y)\in\Omega:y≥0\}`. Its conjugate residue set has size `N_p(Q^+)=|\Omega|>p`. For `R=p−1`, the degree bound becomes `pS−2`, and `J N_p=S|\Omega|>pS−2`. Hence its original **unweighted** integer Gram is positive and the original inert-prime arithmetic lower theorem is in principle applicable **with its other assumptions intact**. This is a parameter-family **paper-level theorem**, not a new exclusion of large D; the hypothetical class-number premise is contradictory to the known classification, as is normal in a reductio proof of the challenge.

The new `R=p−1` is generally **not** the original tuned `R≈D/4`. This changes the polynomial dimension and prime-mass lower estimate. The radius bound alone **cannot** be inserted into the existing 41-billion comparison. An actual improvement needs a re-derived normalized analytic upper on this **same `G_(Q^+)`**, a re-evaluated lower for `R=p−1,S`, and an explicit inequality crossing.

## Exact geometry and its Pareto frontier at D=163 [M]

Take `p=31` (inert because `−163` is a nonsquare modulo 31), `R=30`, `S=J=5`, `m=RS=150`. The source-matched verifier uses the original integer-pair multiplication, ordinary falling factorials, and both real/imaginary columns; a separate Gaussian eliminator computes rank and square-minor determinants in `F_31`. **A real node provides at most five effective columns, a nonreal conjugate-orbit representative at most ten**. With `rho≤15<2√163`, only the rows `y=0,±1` can occur.

| Radius `rho` | Available nonreal conjugate orbits | Minimum nodes (exact) | Witness: nonreal x at y=1; real x at y=0 | Square-minor det mod 31 |
| ---: | ---: | ---: | --- | ---: |
| 12 or less | none (at most 25 real nodes at radius12) | impossible (rank≤125) | — | — |
| **13** | 5 | **25** | nonreal x=−2..2; real x=−10..9 | **29** |
| **14** | 11 | **19** | nonreal x=−5..5; real x=−4..3 | **22** |
| **15** | 15 | **15** | nonreal x=−7..7; no real nodes | **22** |

Counting gives the **global lower** `2k+l≥R=30` for `k` nonreal-orbit reps and `l` real nodes, hence `k+l≥30−k_max`, and always `k+l≥ceil(R/2)=15`. Every row above reaches its lower bound with a **nonzero square original-channel minor** mod31; the three minima are therefore exact for that integer radius. At radius 15 this achieves the global channel-count minimum **15 observations**. The simple degree-vs-multiplicity theorem itself needs 16 nodes here (`160>153`); the 15-node optimum has `150≤153` and is independently certified by determinant 22 mod31. **Do not credit the weaker universal theorem for the sharper finite instance.**

This provides a concrete *Pareto geometry*, rather than collapsing all structure into one scalar: minimal radius is 13, cardinality-minimal support is achieved at radius15, and `(rho,n)=(13,25),(14,19),(15,15)` are the exact frontier in the frozen integer-pair system.

**Same-object analytic tradeoff [M, exactly ordered].** For the three positive original Grams above, the exact integer raw Hadamard products \`U_Q=∏_(r,s)(G_Q)_(r,s),(r,s)\` satisfy **U_13<U_14<U_15**, although their numbers of observation nodes decrease 25→19→15. Displayed \`log U/(R²S)\`, with \`R²S=4500\`, is **2.965521603**, **3.024801260**, **3.079626430** respectively. The comparison uses integer products, with floats only for printing logs. Thus *support cardinality optimization and raw metric optimization point in opposite directions* in a matched original-jet example. This does not decide the best determinant itself or another integer-unimodular frame's upper.

## Arithmetic–analytic interface to Tao's actual goals

The proof of `prime_mass_log_lower_of_det_pos` in [RadialCutoff.lean](../../lean/TenthDiscriminant/RadialCutoff.lean) is preserved on current `main`; [whole-root Lean CI at commit 32850f81](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41246553130) completed successfully, superseding the **cancelled** older Phase149 commit run. It retains the original squarefree, odd-discriminant, class-number, and `R<(D+1)/4` guards. The present rank theorem supplies precisely its positive-Gram input conditionally, without introducing Hasse jets or cyclic coefficient-field extensions.

An inverse-Gram-free upper for the same positive Gram is immediately available from Hadamard:
\[
\log\det G_Q\le \sum_{r=0}^{R-1}\sum_{s=0}^{S-1}
\log\!\left[2|Q|\sum_{j=0}^{\min(r,S-1)}
(r)_{\underline j}^{2}\rho^{2(r+s-j)}\right].
\]
It is valid but likely too loose. A future sharp majorant should exploit the **Frobenius-adapted filtration** with an integer-unimodular monic row basis, rather than misleading factorial rescaling. It must preserve the same integer `det G_Q` and be compared to the same-`R,S,Q` prime mass.

The rival [D≤331 write-up](https://github.com/dualverse-ai/tenth_discriminant/tree/main/bound-331/latex) uses a different *triangular* polynomial space, larger auxiliary inert primes and **Hasse** derivatives in its rank/size comparison; those changes cannot be transplanted into this original rectangular ordinary-jet Gram without proving the bridge. Our low-prime no-collision witness uses only a prime already **guaranteed inert** by the hypothesis, but pays by choosing `R=p−1`. The professor explicitly welcomes different methods and transparently bounded negative results; this is compatible in research objective, **not yet an equivalent numerical field bound**.

**Next kill conditions:** (i) try to derive a same-Gram upper sharply enough that the lower-minus-upper gap actually increases; (ii) measure at fixed R,S/Q and a matched-radius baseline, not cross-parameter raw logs; (iii) if mass loss from reducing R cancels the radius gain, retire the numerical extrapolation while retaining the rank theorem; (iv) port the clean algebraic rank criterion to Lean with the exact original integer-pair model and independent human reconstruction; (v) distinguish sheaf Frobenius pullback from characteristic-zero equivalence, and test `p<R` collisions rather than adding hypercomplex terminology.
