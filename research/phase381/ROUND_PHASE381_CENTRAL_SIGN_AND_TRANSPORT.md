# Phase381 — Central Epstein sign, exact symmetry, and typed cross-line obstructions

**21 November 2026, research-only.** Primary goal: Terence Tao's tenth-discriminant / Siegel-zero challenge. This branch is stacked on Phase380 and **does not** replace the unconditional original integer trace-Gram, alter the Lean imports, merge any prior branch, or close independent mathematical review [#50](https://github.com/Dojo-1/Tenth-Discriminant/issues/50).

## 1. A simpler, stronger-assumption conditional theorem

Let `D=-d<0` be a negative **fundamental field discriminant** with `d>=200`, and assume the imaginary quadratic field `K` has class number one. Then `O_K^×={±1}`. With `a=sqrt(d)/2` and the parity-dependent `b in {0,1}`, the principal ideal norm form is `Q(m,n)=(m+b*n/2)^2+a^2*n^2`.

The classical Epstein/Poisson analytic continuation of the principal ideal series gives, for `s>1/2` (and by limit at `s=1/2`),

```
zeta_K(s) = zeta(2s)
          + Beta(s-1/2, 1/2)*a^(1-2s)*zeta(2s-1)
          + E_b(s,a).
```

At the **central point** `s=1/2`, the poles in the two main terms cancel. By `zeta(1+2eps)=1/(2eps)+gamma+O(eps)`, `zeta(2eps)=-1/2-eps*log(2*pi)+O(eps^2)`, `Beta(eps,1/2)=1/eps+2*log(2)+O(eps)`, and `a^(-2eps)=1-2eps*log(a)+O(eps^2)`, their sum tends to

```
M_(1/2)(d) = gamma + (1/2)*log(d) - log(8*pi)
           = (1/2)*log(d/C),  C=(8*pi*exp(-gamma))^2.
```

### The exact non-floating gate

[central_threshold_exact.py](central_threshold_exact.py) obtains rational brackets for `pi` from the Machin arctangent formula, for `log(2)` from the positive atanh series, for Euler's constant from `H_n-log(n)-1/(2n)<gamma<H_n-log(n)-1/(2(n+1))`, and for `exp(gamma)` from positive Taylor series plus geometric remainder. It certifies, **only by Fraction comparisons**,

```
199 < C < 1593/8 = 199.125 < 200.
```

A tighter display-only rational enclosure is approximately `199.1182499 < C < 199.1212765`. The actual high-precision value `199.12077003757...` lies inside; no floating decimal is an acceptance test.

For `d>=200`, monotonicity of log and `log(x)>=1-1/x` for `x>=1` yield

```
M_(1/2)(d) = (1/2)log(d/C)
           > (1/2)(1-(1593/8)/200)
           = 7/3200.
```

The **actual** central Fourier/Bessel term is

```
E_b(1/2,a)=4 * sum_(n,k>=1) cos(pi*b*n*k)*K_0(2*pi*a*n*k).
```

Use `K_0(x)<=K_(1/2)(x)=sqrt(pi/(2x))*exp(-x)`, `a>=7`, and `r=exp(-pi*sqrt(d))`. Since `pi>3`, `sqrt(d)>14`, and `exp(16)>10000` by a six-term positive Taylor sum, `0<r<1/10000`. With `nk>=n+k-1`,

```
|E_b(1/2,a)| <= 2*r/(1-r)^2 < 1/4000.
```

The separate [central_sign_certificate.py](central_sign_certificate.py) asserts these final rational inequalities and the bound

```
zeta_K(1/2) > 7/3200 - 1/4000 = 31/16000 > 0.
```

**Conditional conclusion, with direction and scope:** `zeta(1/2)<0` gives `L(1/2,chi_D)<0`, whereas `L(1,chi_D)>0` by the quadratic class-number formula. By continuity a REAL zero exists in `(1/2,1)`. Hence the **assumption of no real zeros of primitive quadratic Dirichlet L-functions in (1/2,1)** (a consequence of Dirichlet GRH) implies every imaginary quadratic class-number-one field has `d<=199`.

This is a **strictly stronger zero-free assumption** than Phase380's `ZF(33/64)`, despite yielding the same numerical cutoff. Its benefit is a shorter mathematical mechanism, *not* a stronger assertion under the Phase380 hypothesis. The paper derivation uses classical external Epstein/Poisson, Gamma/zeta asymptotics, Bessel, Dirichlet class-number and analytic continuation identities. No new Lean proof of these inputs is claimed.

The finite `d<=199` classification was already checked in Phase380 by two independent exact algorithms (62 fundamental negatives, nine class-number-one survivors); this phase does not rebrand it as an independent human review.

## 2. A reflective identity: moving through 1/2 does not create a new sign method

Set `M_s(a)=zeta(2s)+Beta(s-1/2,1/2)*a^(1-2s)*zeta(2s-1)`. By the classical Riemann zeta functional equation,

```
Beta(s-1/2,1/2)*zeta(2s-1)
  = pi^(2s-1)*Gamma(1-s)/Gamma(s)*zeta(2-2s)
```

for `0<s<1`, `s!=1/2`, using analytic continuation for `s<1/2`. Define `C_s=pi^(2s-1)*Gamma(1-s)/Gamma(s)>0`, with `C_s*C_(1-s)=1`. Then

```
M_s(a) = C_s*a^(1-2s)*M_(1-s)(a).
```

The factor is positive, so the main-term **sign and zero threshold are exactly reflection invariant**. Numerical exploration at reflected points (e.g. 1/4 versus 3/4) is only a check of an analytic identity, not its proof. Thus evaluating the same two-term main at `s<1/2` cannot lower its threshold independently of the reflected `1-s` argument. **Do not confuse this with an optimality theorem for arbitrary test functions, Bessel remainders, or other arithmetic methods.**

The full Dedekind completed functional equation gives a corresponding sign equivalence for the complete `zeta_K(s)` on the real open interval `(0,1)`; the quadratic imaginary gamma/field factor is positive there. This also blocks a spurious "cross the line to gain sign" strategy, but not an independently strengthened analytic input.

## 3. The original Gram remains a separate mathematical object

For the original finite integer evaluation matrix `E` and trace-channel metric `B`, `G=E B E^T`. Modulo an odd prime `p`, if the row map `F_p^r -> F_p^m` is injective, its row space `V` satisfies an elementary linear-algebra theorem:

```
ker(G mod p) is isomorphic to V intersect V^{perp_B}.
```

Thus full row rank of `E mod p` does **not** imply nonsingularity of `G mod p` when the induced quadratic form has an isotropic radical on V. The Phase380 exact source example has `rank_F5 E=4`, `rank_F5 G=3`. Under `U in GL_r(F_p)`, `G -> U G U^T` preserves rank and radical dimension. More generally `E->EW` and `B->W^-1 B W^-T` preserve the *same* Gram, provided `W` is invertible. Neither observation projection nor change of metric without its transport is an invariant frame change.

This explains the obstruction in ordinary linear-algebra language; it is **not** a counterexample to the large-D p-adic valuation or actual field theorem. Human source-to-field review #50 stays open, as do 301^4 and 302^4 research branches.

## 4. Cross-line dependency ledger

- **Alpoge:** pinned Lean `DirichletLNonvanishingRightOfHalf` is externally checked and directly gives no real zeros on `(1/2,1)` for genuine primitive quadratic characters, with `s!=1` satisfying the pole guard. The *field-to-character correspondence* and principal Epstein identity are external bridges not formalized here.
- **Masullo:** supplied PDF Lemma B.4.4.8 (printed p.624) is false for arbitrary discrete sampling sets of bounded-strip points: Schwartz decay does not control arbitrarily growing local sample counts. Its own footnotes 25/26 note the missing hypothesis. This is separate from C.3.4.1(2), C.3.4.4(2) and incomplete Ch.13. For actual Hecke zeros, a quantified zero-count theorem may repair the relevant special case; the entire trace formula is **not** refuted by the abstract counterexample.
- **Conductor atlas:** source-masked Euler factors compose and preserve zero orders on `Re(s)>0`; boundary Euler zeros may add multiplicity. No character can be substituted by a primitive one after its modulus has masked a prime.
- **Selberg/Ihara:** the 16-vertex switched graph has two **negative** eigen-directions in `12I-A_nt²`, despite positive trace and determinant. The exact two-vector negative plane shows that a linear test family of codimension less than two cannot hide all negativity *provided positivity is checked on every linear combination*, not just individual generators.
- **Governance:** no changes to Phase377 root imports/audit, no merge, no independent arithmetical field-review promotion, no Hecke/graph zeta theorem imported from Dirichlet GRH.

## 5. Remaining proof targets

1. **Lean:** start with a typed central Epstein/L-function bridge at `s=1/2` and the exact `L(1/2)<0<L(1)` sign-change logic. Do not begin with a 17M-line re-verification or a new invented axiom.
2. **Original determinant:** independent human/other-code reconstruction of one local p-adic valuation and the field-return chart, at the original source `Q`, metrics and derivative convention; never conflate Gram det with field disc.
3. **Masullo:** explicitly replace the false B.4.4.8 with a polynomial-counting/spectral-seminorm lemma whose constants account for conductor and unitary components; then revisit its use in B.4.4.9 and p.453.
4. **Conductor:** a source-typed analytic-order-of-vanishing theorem at the closed-right-half-plane boundary.
5. **Ihara:** formalize Sylvester inertia and the dimension bound for restricted test spaces, separate from spectral-zeta transfer.

**Evidence:** P = standard identities/elementary paper proof under stated inputs; M = local exact Fraction and integer code, earlier finite checks; A = unformalized analytic and field-character source bridges; H = new Lean source-level formalizations and human semantic verification; R = unrestricted Masullo sampling lemma and universal positivity inferences. No new unconditional tenth-discriminant bound is claimed.
