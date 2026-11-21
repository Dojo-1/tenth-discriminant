# Phase380 - Every line, one proof boundary

**21 November 2026 (Europe/Madrid). AI-assisted research memorandum. Research draft, not peer reviewed.**

Primary objective: Terence Tao's 20 October 2026 tenth-discriminant / Siegel-zero challenge. Carry the Tenth Discriminant original trace-Gram, Alpöge RH/Dirichlet GRH reconstruction, Masullo's Hecke spectral approach, Discriminant-Conductor-Zero Atlas, and Selberg-Ihara in parallel, **without identifying different zeta functions, determinant sources, zero-free assumptions, or forms of evidence**. All original Lean modules, source metrics, filed PRs and external review issue #50 remain unchanged.

## I. A genuinely stronger *conditional* comparison; not a new unconditional result

### Assumption with precise quantifiers

Let **ZF(33/64)** assert that for every negative fundamental discriminant `D`, the corresponding primitive quadratic Dirichlet `L(s,chi_D)` has **no real zeros in** `(33/64,1)`. The confirmed external Dirichlet-GRH theorem implies this because `33/64 > 1/2`, with the principal `s=1` exception automatically excluded. This is a **strictly stronger assumption than ZF(7/8)** used in Phase379; compare these as distinct inputs, not as numerical proof improvements under the same assumptions.

### Proposition (written conditional argument, standard analytic inputs)

If ZF(33/64) holds, **every imaginary quadratic field of class number one has absolute fundamental field discriminant at most 199**. The proof is short conditional on standard Epstein-zeta expansion, quadratic Dedekind factorization, Hasse/eta/Beta identities, the Dirichlet class-number formula, and the Bessel bound.

For `D=-d<0`, `d>=200`, and `h(D)=1`, the number of units is 2. With `a=sqrt(d)/2` and the appropriate integer-basis parity `b in {0,1}`, the principal norm is

`Q(m,n)=(m+bn/2)^2+a^2 n^2`.

The principal-ideal Dirichlet series, continued from `Re(s)>1`, has at `1/2<s<1` the standard Poisson expansion

`zeta_K(s)=zeta(2s)+B(s-1/2,1/2) a^(1-2s) zeta(2s-1)+E_b(s,a)`,

where

`E_b(s,a)=(4 pi^s/Gamma(s))*a^(1/2-s)*sum_{n,k>=1} n^(1/2-s) k^(s-1/2) cos(pi*b*n*k) K_{s-1/2}(2*pi*a*n*k)`.

At `s=33/64` this becomes

`zeta_K(33/64)=zeta(33/32)-B(1/64,1/2)*(4/d)^(1/64)*abs(zeta(1/32))+E_b`.

The self-contained `zero_free_33_64_certificate.py` verifies with **rational/integer comparisons only**

* `zeta(33/32)-B(1/64,1/2)*(4/d)^(1/64)*abs(zeta(1/32)) - |E_b| > 0.0015792412454... > 1/1000` for all `d>=200`;
* `|E_b| < 24*r/(1-r)^2 < 1/1,000,000` with `r=exp(-2*pi*a)<10^-8`;
* the main term at `d=199` has a **negative** certified upper bound, so this particular sign gate must not claim `d<=198`.

**Directional audit / correction before publication:** the first draft reversed which endpoint of the bracket for `2^(1/32)` enters the **lower** enclosure of `zeta(33/32)`. Because `r -> 1 - 1/r` increases for `r>1`, the lower bound is `eta33_lo/(1-1/r_hi)`; the upper bound uses `eta33_hi/(1-1/r_lo)`. The earlier quotient was *not* a certified lower bound, even though its sign happened to agree. After correction, the exact positive margin is `0.001579241245461...` (strictly greater than `1/1000`). This correction is recorded as R for the earlier local enclosure, not concealed by the surviving claim.

Exact envelopes come from Hasse's convergent eta representation (72 terms with a bounded tail), splitting the Euler Beta integral at 1/2 (72 terms with positive and bounded coefficients), and integer-power brackets for the 32nd and 64th roots. **The script does not prove** Epstein/Poisson continuation, the class-number identities, analytic inequalities for Gamma and Bessel, or the externally verified ZF assumption. Its Python float printouts are presentations of exact Fraction comparisons, **not acceptance calculations**.

Since `zeta(s)<0` on `(0,1)`, positivity of `zeta_K(33/64)=zeta(33/64)*L(33/64,chi_D)` forces `L(33/64,chi_D)<0`. Since `L(1,chi_D)>0` by the quadratic class-number formula, some real `beta in (33/64,1)` is a zero, contradicting ZF(33/64). Therefore `d<200`, i.e. `d<=199`. The reverse implication is invalid.

The finite certificate tests all **62 negative fundamental discriminants with `d<=199`** by the two Phase378 arithmetic algorithms (primitive reduced positive-definite binary quadratic forms and independent quadratic-character class-number summation), agreeing at every entry and leaving exactly `3,4,7,8,11,19,43,67,163`. This is reproducible classical arithmetic, *not* a new classification theorem or a Heegner-based premise.

**Comparison guard:** Phase379's `ZF(7/8) => d<=652` is a weaker-hypothesis, weaker-numerical-cutoff line. Phase380's `ZF(33/64) => d<=199` uses a stronger external input. Tao's original arithmetic-determinant challenge emphasizes the **mechanism** and its conditions, not cherry-picking one scalar bound across unmatched inputs. Existing non-zero-free determinant approaches in his public comments already give sharper numerical cutoffs than the 322^4 project; track sources separately.

## II. Original trace-Gram: an exact radical obstruction, independent of the bound

Let `E` be an integral `r x m` ordinary-Z-jet evaluation matrix, with real and imaginary coefficient channels, and diagonal trace metric `B` with weights `2` and `2D`. The **same** source Gram is `G=E B E^T`.

**Elementary theorem (any field `F`, `B` symmetric nondegenerate, `E` full row rank):** `G` is nonsingular **iff** the row space `W` of `E` has `W intersect W^perp_B = {0}`. Proof: the adjoint of the restricted pairing on `W` has Gram `EBE^T` under the independent row basis of `E`. Its kernel is exactly the radical of the restricted pairing. Over `R` with positive definite `B`, radical vanishes. Over a finite field, isotropic vectors make the radical nontrivial even when `E` has full row rank. The baby counterworld `E=[1,2], B=I_2` over `F_5` gives `rank(E)=1` and `G=[1+4]=[0]`.

`gram_radical_adversarial.py` additionally **reconstructs from the original integer pairs** (not copied matrices) the `D=3, rho=2, R=S=J=2` old-control Gram:

```
G=[[22,0,0,64],
   [0,64,-8,0],
   [0,-8,86,0],
   [64,0,0,296]],  det G=13,143,040.
```

At `p=5`, the original `E` has full row rank 4, while `rank(G)=3`. This is a counterexample **only** to the illegal finite-field inference `full rank(E mod p) -> det(G) nonzero mod p`; it does **not** challenge the original large-D inert-prime divisibility theorem or indicate that the source field-return is false. An integral unimodular row-frame transformation `U` preserves the exact determinant through `G'=UGU^T` and preserves radical dimension mod 5. A lossy observation projection does not.

**Unresolved:** the project's `322^4` theorem exists in Lean relative to its definitions, but external issue #50's exact source-to-number-field meaning remains separate. `301^4/302^4` research branches and Phase377 root-import audit remain drafts. The elementary radical theorem should become a source-typed Lean guard before any cross-project determinant comparison.

## III. Masullo: two false appendix identities and a *new* sampling proof obligation

The 940-page user-supplied PDF *The Music of the Primes* has exact counterexamples at Appendix C, pp.697-698:

- Lemma C.3.4.1(2): `sum_e |<Te,e>|` is **not** orthonormal-basis independent (`T=diag(1,-1)`, standard basis sum 2, 45-degree rotated basis sum 0).
- Lemma C.3.4.4(2): `||AT||_1=||TA||_1` for all bounded `A` and trace-class `T` is **false** (`T=E11, A=E12`: left 0, right 1). Correct separate inequalities and trace cyclicity remain valid.

**New, source-local proof gap:** p.453 infers convergence of a zero-indexed Schwartz sample sum by saying it is comparable to an `L^1` integral. Schwartz decay alone does not yield a uniform sampling-to-`L^1` bound. For a nonempty discrete sample set and a smooth compact bump `f_eps` of value 1 at one sample, support width `2 eps`, `sum |f_eps(gamma)|>=1` while `int |f_eps| <= 2 eps ->0`. The finite counterworld is in `spectral_sampling_and_positivity.py`. This refutes the **bare sampling comparison**, not the actual zero sum's convergence.

**Possible repair:** prove an actual zero-counting bound, for each needed character/vertical line and **uniformly across the character family** or with a conductor-weighted summability condition. If the zero counting measure obeys `N(R)<=C(1+R)^A` for a fixed component, a Schwartz seminorm `sup_t (1+|t|)^B |f(t)|` with `B>A` controls the discrete sum via dyadic shells. It is not generally controlled by `||f||_{L^1}` alone. The manuscript's p.453 proof refers to other estimates; trace their exact hypotheses before declaring the result invalid. The p.501-502 uses of C.3.4.4 appear to need correct **separate** left multiplication convergence, not its false equality, so the local error may be repairable. Chapter 13 p.522 still explicitly leaves the claimed general Hecke-GRH final theorem statement and positivity bridge unfinished in the uploaded draft.

**Stop:** neither invoke Masullo's broad GRH assertion as a premise nor claim to have disproved the full trace formula by a local counterexample.

## IV. Conductor-zero: source-aware Euler corrections form a genuine cocycle

For a primitive real quadratic character `chi_D` of modulus `|D|`, order conductor `f` corresponds here to an **induced Dirichlet modulus** `M=|D| f^2`. A chain `f|g|h` gives `M|N|K`. The exact source-level correction of `L(s,chi_N)` relative to `L(s,chi_M)` is

`F_(M,N)(s)=prod_(p|N) (1-chi_M(p)*p^(-s))`.

Primes already dividing `M` contribute neutral factors because `chi_M(p)=0`. For `Re(s)>0`, every correction is a holomorphic unit. Crucially,

`F_(M,K)=F_(M,N)*F_(N,K)`

holds **for genuine induced characters**. It can fail if one incorrectly reuses the primitive character at every step. At `D=-4` and `f=1,g=3,h=9`, the moduli are `4,36,324`. At `s=1`, the correct corrections are `4/3`, `1`, `4/3`. Reusing primitive `chi_-4(3)=-1` in the middle would falsely give `4/3` instead of `1` for the second leg.

`conductor_cocycle_finite.py` checks **132** exact `f|g` corrections and **304** `f|g|h` cocycles for `D=-4,-8`, `1<=f,g,h<=20` with rational arithmetic. This supplies finite corroboration but does not replace the Mathlib `LFunction_changeLevel` analytic theorem or an unbuilt Lean T11.1-T11.4 source bridge. Zero multiplicities are preserved when the correction is an analytic unit; the imaginary-axis boundary can introduce zeros.

## V. Selberg-Ihara: the correct operator positivity certificate

For a finite connected `(q+1)`-regular graph, remove the trivial adjacency eigenspaces `+-(q+1)` as applicable. On the nontrivial invariant real subspace `H_nt`, the regular-Ihara/Ramanujan condition is **equivalent** to nonnegativity of the self-adjoint quadratic form

`B_q=4q I - (A|H_nt)^2`.

Proof: by the spectral theorem, its eigenvalues are `4q-lambda^2`, nonnegative precisely when `|lambda|<=2 sqrt(q)` for every nontrivial adjacency eigenvalue. This is a *global positive-semidefinite* test, not a trace-average or selected minor. In an invertible frame, transport the quadratic form by congruence `B' = U^T B U`; its inertia is preserved (Sylvester), unlike an arbitrary lossy observation.

`q=3, A=diag(4,0)` gives `B=diag(-4,12)` and `tr B=8>0` even though `B` is **not** PSD. Two violations `A=diag(4,4)` give `det B=16>0` though `B` remains negative definite. Thus scalar trace positivity or determinant positivity cannot replace a full test-family positivity certificate. These toy spectral matrices are **not claimed as adjacency spectra of the earlier actual graph witness**; that graph's valid off-circle poles remain established through its separate exact characteristic polynomial.

For compact Selberg zeta, small Laplace eigenvalues `0<lambda<1/4` are a different real-zero obstruction, not something a Dirichlet GRH theorem eliminates.

## VI. Source verification and independent gates

- Original [Alpöge `Statements.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/6b1e1b8e9d683841024757f158fda63a32bbeae7/src/Statements.lean) includes `DirichletLNonvanishingRightOfHalf`, with explicit principal pole guard `chi != 1 or s != 1`. At real `s=33/64`, this guard is discharged by `s!=1`. Original [Main.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/6b1e1b8e9d683841024757f158fda63a32bbeae7/src/Main.lean) supplies this theorem as `LFunction_ne_zero_of_half_lt_re := allChi`.
- The [Lean and Mathlib community statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) reports independent verification of the *actual* RH proof, not our arithmetic corollary, the 301^4 branch, Hecke GRH, or Selberg-Ihara.
- This Phase380 session had no local Lean or GNU Prolog executable, so **no new kernel or Prolog claim** is made. Finite integer/rational/Python checks above ran locally on the dated sources. Follow with source-level Lean formalization or independent human audit for the analytic bridges.

### State / bounded next gates

| Line | Current narrow result | Missing decisive bridge |
|---|---|---|
| Tao / conditional | Exact rational `ZF(33/64) => d<=199` (external analytic identities) | Lean formalization and independent check of Epstein normalization and hypotheses |
| Original trace Gram | Fully reconstructed small original source and Gram radical obstruction | Source-to-field independent review #50; no hidden rank/Gram promotion |
| Alpöge | Pinned exact Dirichlet nonvanishing theorem, externally checked | Match fundamental quadratic character with Mathlib, class-number formula |
| Masullo | Two exact false operator lemmas; discrete sampling-vs-L1 proof gap | Locate full zero-count seminorm and test-family density before Hecke GRH |
| Conductor-Zero | Source-correct correction cocycle, 132+304 finite exact checks | Actual Mathlib source-modulus theorem and analytic orders in Lean |
| Selberg-Ihara | PSD spectral certificate and finite false-scalar controls | Source-typed Bass/Ihara theorem and Selberg-geodesic operator bridge |

No draft is merged. Preserve all negative results, exact source wording, zero-free assumption strengths and author/AI contributions. The next priority is a **real analytic or semantic source bridge**, not another unsupported ontology or bound comparison.
