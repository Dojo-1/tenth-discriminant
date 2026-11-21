# Phase379 / All research lines, one evidential standard

**21 November 2026. AI-assisted research dossier. DRAFT.**

**Primary problem:** Professor Terence Tao's [20 October 2026 experimental challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/): extract effective bounds for a hypothetical tenth imaginary quadratic class-number-one discriminant from proposed new zero-free/Siegel-zero arguments **without using Heegner's solution**, quantify constants, and optimize them where justified.

**Adjacent lines (not equivalent):** the existing original integer trace-Gram determinant argument, independently checked Alpoge RH/Dirichlet-GRH proof reconstruction, Masullo's adelic trace proposal, the discriminant-conductor-zero atlas, and Selberg-Ihara spectral analogues. Keep their formal targets separate.

## 0. Verdict and correction ledger

- **M (rationally certified):** a new *exact-arithmetic enclosure* of the already-known conditional `ZF(7/8) -> d<=652` route. The certificate itself uses no floats or third-party libraries. It proves `zeta_K(7/8) > 1/100000` for the classical principal Epstein expression under `h(K)=1`, `d>=654`, **conditional on** standard, unformalized analytic identities stated below. Both the external 7/8 zero exclusion and analytic continuation facts are not proved by Python.
- **P in ordinary mathematics, not locally Lean-checked:** the abstract analytic-unit lemma preserving zero multiplicity under nonvanishing finite Euler factors. This strengthens the atlas's pointwise zero-set transport semantically, without an asserted new Mathlib build.
- **R (two explicit counterexamples):** Masullo Appendix Lemma C.3.4.1(2) (absolute diagonal sum invariant under ONB) and Lemma C.3.4.4(2) (equality of left/right trace norms). Both false as written. Neither counterexample, by itself, refutes Masullo's entire trace-formula method.
- **P (elementary algebra) + M (known exact graph characteristic polynomial):** an Ihara pole off its critical circle has a well-defined log-radius displacement. The switched `K4,4` counterworld from the Selberg-Ihara repository disproves *universal* graph RH, not classical RH.
- **H:** open external mathematical validation for the source-to-field interpretation of the original `301^4` route. `322^4` and 301/302 branches are **different evidence and assumptions** from the analytic `652` bound.
- **A:** the 7/8 zero-free premise and imported Epstein/Poisson/Bessel/class-number formulas in the Python certificate; no hidden promotion to a new unconditional GRH proof.

There is no new *best bound*: published challenge participants already gave `d<=652` (and other methods report smaller upper bounds). The novelty here, if any, is the independently checkable finite *rational enclosure*, and that novelty has not been literature-refereed.

## 1. Exact rational 652 reconstruction

Let `D=-d<0` be a **negative fundamental discriminant** and assume `h(D)=1`, `d>=654`. Then the unit group is `{+-1}`. With `a=sqrt(d)/2`, the principal form is

`Q(m,n)=(m+b*n/2)^2+a^2*n^2` with `b=0` or `1` according to the parity chart.

The principal-ideal calculation and Poisson summation give, initially for `Re(s)>1` and then by analytic continuation for real `1/2<s<1`,

`zeta_K(s)=zeta(2s)+B(s-1/2,1/2)*a^(1-2s)*zeta(2s-1)+E_b(s,a)`.

At `s=7/8`, the Bessel remainder has the (external classical) exact form

`E_b=[4*pi^s/Gamma(s)]*a^(1/2-s)*sum_{n,k>=1} n^(1/2-s)*k^(s-1/2)*cos(pi*b*n*k)*K_(s-1/2)(2*pi*a*n*k)`.

Thus positivity follows if the positive `zeta(7/4)` term exceeds the negative beta-zeta term and the absolute remainder. The new script `research/phase379/tao_652_exact.py` checks this by **only exact `fractions.Fraction`, integer roots and finite sums**.

### Beta coefficient: rapidly convergent, rational tail

For `0<a,b<1`, splitting the beta integral at `1/2` and expanding both factors yields

`B(a,b)=2^(-a)*sum_{k>=0} (1-b)_k/(k! 2^k (a+k)) + 2^(-b)*sum_{k>=0} (1-a)_k/(k! 2^k (b+k))`.

The coefficients `(1-a)_k/k!` and `(1-b)_k/k!` lie in `[0,1]`. Truncating either sum before index `N` has **nonnegative tail at most** `2^(1-N)/(N+a)` or `2^(1-N)/(N+b)` respectively. The fractional radicals `2^(-3/8)` and `2^(-1/2)` are bracketed by exact integer-power comparisons. No gamma routine is used.

### Eta/zeta coefficient: rapidly convergent, rational tail

For `s>0` the Euler-transformed alternating eta sum is

`eta(s)=sum_{n>=0} 2^(-n-1)*sum_{k=0}^n (-1)^k*C(n,k)*(k+1)^(-s)`.

Its inner sum is nonnegative and at most one: by the gamma/Laplace integral it equals

`Gamma(s)^(-1)*int_0^infinity t^(s-1)*exp(-t)*(1-exp(-t))^n dt`.

Hence the whole tail after `N` indices lies in `[0,2^(-N)]`. We bracket each `(k+1)^(-3/4)` or `(-7/4)` by integer fourth-power inequalities, tracking alternating signs conservatively. The identities

`abs(zeta(3/4))=eta(3/4)/(2^(1/4)-1)` and `zeta(7/4)=eta(7/4)/(1-2^(-3/4))`

then give certified *rational* bounds, including denominators.

### Bessel tail and exact cutoff

For `0<nu<1/2`, `K_nu(x)<=K_(1/2)(x)=sqrt(pi/(2x))*exp(-x)` by the integral representation. For `d>=654`, `a>=12`. Basic bounds `3<pi<4`, `1/Gamma(7/8)<2` (from `Gamma(7/8)>int_0^1 exp(-t)dt>1/2`), and `n^(-7/8),k^(-1/8)<=1` give

`|E_b(7/8,a)| < 24*r/(1-r)^2`, `r=exp(-2*pi*a)`.

Since `2*pi*a>72>30` and `exp(30)>30^10/10!>10^8`, the script checks

`|E_b| < 24*10^8/(10^8-1)^2 < 1/10^6`.

Its exact-rational final computation yields the lower bound

`zeta_K(7/8) > 0.0000136727425... > 1/100000` for all `d>=654`.

This decimal is printed for convenience: the Python *acceptance gate* is an exact Fraction comparison against `1/100000`. The similarly checked upper bound of the Epstein **main term** at `d=653` is negative, a near-threshold control; it is not a purported class-number-one field with that discriminant.

As `zeta(7/8)<0`, `L(7/8,chi_D)<0`. Since `L(1,chi_D)>0` by the class-number formula, there would be a zero in `(7/8,1)`. That contradicts `ZF(7/8)`, proving `d<654`. Negative fundamental discriminants have `d` divisible by 4 or `d=3 mod 4`; thus neither 653 nor 654 is admissible, so `d<=652`.

The prior Phase378 script independently enumerates all 313 negative fundamental discriminants below 1024 by reduced primitive forms and by the character class-number formula. Its output of nine fields therefore also covers `d<=652`. No Heegner classification is used in that finite calculation; standard Gauss/class-number correspondences remain mathematical dependencies.

**Execution (local):**

```sh
python3 research/phase379/tao_652_exact.py
python3 research/phase378/tao_zero_free_1024.py
```

The first script was executed locally this round. The second is retained from Phase378 and had been reported as passing there; no fresh execution of it is claimed here. A separate high-precision `mpmath` cross-check verified the beta and two eta enclosures in this round, but its output is not part of acceptance.

**Reverse implication deliberately not claimed:** `d<=652` does not rule out Siegel zeros for arbitrary primitive real characters.

## 2. Original Gram determinant: do not switch integers mid-proof

The older Tenth Discriminant route works with the **same original** positive integral trace Gram `G_Q=E_Q B_Q E_Q^T` on the source lattice, the same ordinary jets, and the same field-return map. It is *not* recovered from the analytic route above merely by changing `d` in a theorem statement.

- Main reports its `322^4` field theorem; the separate 302/301 research branches have distinct levels of discharge and ongoing semantic review issue #50.
- Phase377 PR #287's full-root preflight/build/axiom checks were reported green in the uploaded research record, while the PR remains a research draft. The global source-to-number-field argument is a separate proof obligation.
- A real invertible change of coordinates preserves neither the original integral lattice nor prime valuations in general; unimodular integral transport preserves the numerical determinant. A determinant of a different source matrix is not automatically the determinant originally estimated.

**Next exact obligation:** independent reconstruction of *one* full field-return claim (including the lattice, derivative, trace weight, and number-field discriminant), not another governance wrapper or claim count.

## 3. Alpoge RH/Dirichlet GRH: source-level, not analogical, imports

The [Lean/Mathlib community statement of 21 November 2026](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) reports official and independent checker acceptance of the original RH proof and corresponding Dirichlet statements. This is stronger external evidence than our finite tests.

The adversarial repository has A7/A8/A9 source reports. A9 correctly separates right-half nonvanishing from line confinement under reflection, and identifies character inversion, critical-strip quantifiers and principal-pole exceptions as mandatory transports. It does **not** establish a new proof of RH, all-number-field Hecke GRH or graph/automorphic Ramanujan bounds.

For Tao's bounded class-number calculation, the hypothesis required is much less than full Dirichlet GRH: no **real** zero of `L(s,chi_D)` in the interval `(7/8,1)` for the actual fundamental quadratic characters under consideration. State this weak interface; prove it from the cited external theorem only with precise conductor and primitive-character correspondence.

**Next exact obligation:** source-level Lean statement matching the real primitive quadratic-character zero exclusion, with imported `DirichletLNonvanishingRightOfHalf` and analytic pole guards, not a new assumed `ZF` in a source-level theorem.

## 4. Masullo: two false appendix identities, not a global refutation

Source: user-uploaded Alessandro Maria Masullo, *The Music of the Primes* (940 pages), 20 November 2026 version.

**R1: Appendix C, Lemma C.3.4.1(2), printed p.697.** For `T=diag(1,-1)` on `C^2`, the ONB `e1,e2` gives `sum |<Te,e>|=2`. The ONB `u=(e1+e2)/sqrt(2)`, `v=(e1-e2)/sqrt(2)` gives `0`. The *signed* trace is `0` in both bases. The claimed absolute sum ONB invariance is false; replacing it by ordinary trace invariance and the inequality `sum |<Te,e>|<=||T||_1` is valid.

**R2: Appendix C, Lemma C.3.4.4(2), printed p.698.** With `T=E_11`, `A=E_12`, `AT=0` but `TA=E_12`, hence `||AT||_1=0` and `||TA||_1=1`. The alleged identity `||AT||_1=||TA||_1` is false. The correct general estimates are the two *separate* inequalities `||AT||_1<=||A||*||T||_1` and `||TA||_1<=||A||*||T||_1`; also `tr(AT)=tr(TA)` when the trace-class conditions hold. Trace cyclicity does not imply equality of trace norms.

**Downstream scope:** source searches locate references to Lemma C.3.4.4 in spectral and diagonal-kernel arguments (including pp. 501-502). Those may use only the valid ideal-continuity properties; each use must be checked before declaring a global collapse. A phrase `Theorem ??` and unfinished `Theorem 13.3.1.2` remain in Chapter 13 p.522, so the zero-location deduction cannot be treated as a proved theorem from this manuscript. In particular, the transition from a restricted trace identity to full Weil-test positivity must be established, not assumed.

`research/phase379/typed_transport_controls.py` contains exact finite matrix witnesses and a family of Taylor-jet tests. It does not formalize Masullo's functional analysis.

## 5. Discriminant-conductor-zero Atlas: preserve zero *multiplicity* for Re(s)>0

Let `chi` be a Dirichlet character of source modulus `M` and `chi^[N]` its induced character at a multiple `N`. Where the analytic identities hold, write

`L(s,chi^[N])=F(s)*L(s,chi)`, `F(s)=prod_{p|N}(1-chi(p)*p^(-s))`.

If `Re(s)>0`, then each correction factor is nonzero: either `chi(p)=0`, or `|chi(p)*p^(-s)|<=p^(-Re(s))<1`. Thus `F(s)` is a **holomorphic local unit** on the open right half-plane. For any `s0` there where the source `L` is holomorphic and vanishes to finite order `m`, its local factorization `L(s)=(s-s0)^m*g(s)`, `g(s0)!=0`, yields

`ord_{s0} L(s,chi^[N]) = ord_{s0} L(s,chi) = m`.

The same local-unit principle preserves meromorphic order (including poles) when formulated in meromorphic terms; do not silently treat a principal-character pole as a zero.

**Sharp boundary counterexample:** primitive `chi_-4(3)=-1`, induced from modulus 4 to modulus 12, acquires factor `1+3^(-s)`, which vanishes at `s=(2k+1)*pi*i/log 3`, on **Re(s)=0**. A numerical verifier of `Re(s)>0` cannot be promoted to one of the closed right half-plane.

This statement is a standard local-holomorphic consequence, stronger in semantics than the already merged MMF-6 *pointwise* zero-set theorem. It is **not a new Lean proof of analytic multiplicities**; that would require a source-level theorem for analytic orders and the actual Mathlib change-level identity.

## 6. Selberg-Ihara: exact spectral displacement and the failed universal analogue

For a finite connected `(q+1)`-regular graph, `q>=2`, the Ihara Bass formula is

`Z_G(u)^(-1) = (1-u^2)^(|E|-|V|)*det(I-u*A+q*u^2*I)`.

An adjacency eigenvalue `lambda` gives the quadratic `q*u^2-lambda*u+1=0`. In the **nontrivial** case `|lambda|>2*sqrt(q)`, set `t=arcosh(|lambda|/(2*sqrt(q)))>0`. Its two inverse-root moduli are exactly

`|u_+|=q^(-1/2)*exp(t)`, `|u_-|=q^(-1/2)*exp(-t)` (in either order),

and under `u=q^(-s)`, their real spectral coordinates are

`Re(s)=1/2 +/- t/log(q)`.

This is a genuine coordinate-independent spectral obstruction: similarity of the adjacency matrix cannot erase it. The existing source graph is a connected 4-regular two-switched `K4,4` pair with exact characteristic factor `x^2-2x-6`. The eigenvalue `1+sqrt(7)>2*sqrt(3)` yields off-circle Ihara poles and `Re(s) approximately 0.20649684694, 0.79350315306` (not `1/2`). The real parts are numerical displays of the **algebraic** root formula, not a new computed zero of Riemann zeta.

For a compact hyperbolic surface, the analogous obstruction is a Laplacian eigenvalue `0<lambda<1/4`: Selberg zero coordinates `1/2 +/- sqrt(1/4-lambda)` are then real, rather than lying on the vertical line. The spectral-gap condition and trivial eigenvalue `0` must be treated separately; noncompact surfaces have additional complications. Dirichlet GRH does not supply a general Selberg spectral gap.

## 7. Shared theorem interfaces, not shared proofs

| Line | Exact source object | Surviving invariant | Missing / conditional bridge |
|---|---|---|---|
| Tao | imaginary quadratic field, fundamental D, primitive chi_D | sign at real 7/8 and class number formula | imported `ZF(7/8)` and Epstein/Poisson |
| Original Gram | integer sample lattice, E_Q and positive trace B_Q | exact integral Gram determinant under permitted U | independent source-to-field semantic review |
| Alpoge | zeta/primitive Dirichlet L and formal zero predicate | RH/Dirichlet scope under independent check | human conceptual reconstruction; Hecke/automorphic extension |
| Masullo | adelic Hilbert and trace operators | cyclic trace, separate trace-norm inequalities | broken appendix claims; full spectral-positivity bridge |
| Conductor atlas | primitive chi and induced modulus N | zeros **and multiplicity** on Re>0 by analytic-unit factor | formal local-order transport & source modulus proof |
| Ihara | finite regular graph and adjacency spectrum | off-circle displacement and spectrum under graph isomorphism | no general Ramanujan/Dirichlet transfer |
| Selberg | hyperbolic surface Laplacian spectrum | spectral gap controls exceptional real zeros | no universal gap from arithmetic GRH |

**False converses to retain:** no tenth field does not imply general zero-freeness; Dirichlet GRH does not imply universal Ihara Ramanujan/Selberg gap; a finite positive trace family does not imply positivity on all admissible tests; a trace value invariant under bases does not make the absolute diagonal sum invariant.

## 8. Implementation -> tests -> interpretation

Local run commands in this dossier:

```sh
python3 research/phase379/tao_652_exact.py
python3 research/phase379/typed_transport_controls.py
```

The first has exact rational acceptance and a near-threshold negative control. The second checks two exact 2x2 matrix witnesses, local Taylor multiplicities by polynomial convolution, a boundary Euler factor, and a numerical Ihara radius crosscheck. This is **not** root Lean compilation or human refereeing.

**Strongest surviving result:** a correct, auditable conditional `ZF(7/8) => d<=652` *derivation* with its nontrivial finite inequalities witnessed by exact fractions, matching prior challenge results.

**Most damaging open problem:** replacing **external analytic identities and zero-free inputs** with source-level verified correspondences while retaining exactly the mathematical object Tao asks to bound; and separately, establishing an independently reviewed original integer trace-Gram field-return theorem.

**Promotion rule:** only claim `P` for a complete exact theorem with the precise hypotheses and source; label executable rational comparisons `M`; mark `A` for imported propositions; retain false lemmas `R`. The finite code plus the preceding prose cannot bootstrap themselves into an unconditional RH, Hecke GRH or tenth-discriminant solution.

**Resource parity:** all local finite scripts are standard-library Python; external 17M-line Lean recompilation was neither required nor performed. No new theorem is being justified by inaccessible GPU/CPU time. New Lean formalization should target the analytic bridge, not superficial files or governance.
