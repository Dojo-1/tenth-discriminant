# Phase286-B — post-primal dual-Poisson preregistration

Registered 12 November 2026 **after** the Phase286 primal exact-dyadic focused success at head `0d374ec`, but **before** authoring or executing the Phase286-B dual-sum regression. This is a new test, not an original Phase286 prospective outcome. All formulas are classical Poisson-summation consequences under the hypotheses, not novel theorems or independently externally reviewed results.

## Frozen dual identity and arithmetic specialization

For D squarefree with D=3 (mod 4), and for all real t>0, the two-coset order O=Z[u] disjoint_union ((1+u)/2+Z[u]), with u^2=-D, gives

`Theta_O(t)=sum_(alpha in O) exp(-t*N(alpha))
    = (2*pi/(t*sqrt(D)))*sum_(m,n in Z; m+n even) exp(-pi^2*(m^2+n^2/D)/t)`.

This follows from ordinary two-dimensional Poisson summation for a Gaussian on the rectangular lattice Z[u], with shifts (0,0) and (1/2,1/2) contributing multipliers 1 and (-1)^(m+n). The zero-frequency coefficient is 2*pi/(t sqrt(D)). No relation to class number is required.

Choose c=4, D in {19,403}, and **special dual-time**
`t_D=pi^2/(c*D*ln(2))`.
Then the dimensionless normalized theta is

`S_D(t_D)=(t_D*sqrt(D)/(2*pi))*Theta_O(t_D)
       =sum_(m+n even) 2^(-c*(D*m^2+n^2))`.

The right side is an exact **positive dyadic rational infinite series**, although the original-time Gaussian argument is transcendental. This experiment only certifies the dual right side; it does not numerically integrate or evaluate the original-time theta independently.

Freeze the box `max(|m|,|n|)<=N` with N=4. Let `S_box` be the exact dyadic sum in that box, and K=N+1=5. By L-infinity shells (8k points at radius k) and D>=1:

`0 <= S_D-S_box <= 8*sum_(k=K)^infty k*2^(-c*k^2)`.

The ratio of successive majorant terms for k>=K is bounded above by

`q_K=((K+1)/K)*2^(-c*(2*K+1))<1`.

Hence the entire unknown remainder is enclosed in

`B_dual = 8*K*2^(-c*K^2)/(1-q_K)`, an EXACT rational number. Require strict `B_dual < 2^(-94)`. Require the zero-mode bracket

`1+2^(-15) < S_box <= S_D < 1+2^(-14)`.

The lower inequality follows from the two legal (m,n)=(0,+/-2) terms (each 2^(-16)) and additional positive terms; the upper is an exact rational comparison. The deliberately WRONG control adding all odd-parity m+n must have a difference at least `2^(-3)` from S_box, because (m,n)=(0,+/-1) contribute 2*(2^(-4)). The alternative wrong normalization of a *single* coset must also be distinguished: its zero frequency has half the full-order coefficient.

## Angular generating identity [P-paper proof target only]

For complex formal parameters xi,eta and fixed t>0, the full-order two-coset theta is

`Theta_O(t,xi,eta) =
 (2*pi/(t*sqrt(D))) * sum_(m+n even)
 exp(((xi+eta-2*pi*i*m)^2)/(4*t)
    +((i*sqrt(D)*(xi-eta)-2*pi*i*n)^2)/(4*D*t))`.

The exact Gaussian Fourier transform proves the formula; the dual sum and all its finite xi/eta derivatives converge normally on compact parameter sets for each fixed t>0. Therefore derivatives at zero recover the Gaussian-damped mixed moments from the primal theta without dropping angular information. **Explicit uniformly controlled derivative tails as t->0 are NOT proved by the radial bound alone** and remain a separate research gate.

## Falsifiers, scope, CI

- The dual CI program must use only `Fraction` and integer powers of two, with no pi/ln2 floating-point evaluations; two independent exact sum constructions must agree (all grid points parity-filtered vs per-row parity enumeration).
- Check two D cases, N=4, c=4, parity constraint, exact q_K and B_dual and strict dyadic threshold; ensure positivity and zero-mode sandwich.
- Negative wrong-parity test must fail by >=1/8. A changed exponent c or illegal missing-coset parity must trigger falsification rather than revised expectations.
- Since the series is dyadic but the prefactor is transcendental, call this an **exact normalized dual theta certificate**, NOT an exact finite evaluation of Theta_O(t_D) as a real number.
- Do not claim a new universal discriminant bound, class-number-one result, zero-free-region theorem, novel Poisson result, or replacement of original integer trace Gram. The 321^4 and review #50 remain separate.
- Keep draft pending exact-head focused, Markdown and whole-root Lean CI. This follow-on is intentionally later than the successful primal Phase286 run and its provenance must remain visible.
