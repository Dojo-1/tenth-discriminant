# The lower bridge: count a staircase, then control its tail

Phases 23–24 check the finite conversion from factorial weights to the
determinant's odd-prime weights and discharge the analytic tail estimate.
Under the documented arithmetic, radius and interval guards, class number
one now forces the unchanged mathematical `prime_mass≤upper_B` comparison
on the actual Gram. Numerical certificate interpretation is still separate.

## Why the quadratic correction is there

For one row index `r`, put `k=floor(r/p)`. The determinant weight counts
the staircase `min(k,0), min(k,1), …, min(k,S−1)`. When `k≤S`, its sum is
a rectangle of area `S*k` minus the triangular corner `k(k+1)/2`.
Consequently, with

$$A(p)=\sum_{r<R}\lfloor r/p\rfloor,\qquad
Q(p)=\sum_{r<R}\lfloor r/p\rfloor^2,$$

the exact identity is

$$\boxed{F(p)=(S-\tfrac12)A(p)-\tfrac12Q(p).}$$

The program's guard `R≤P*S` ensures `k<S` for every `r<R` and `p>P`.
The proof permits the harmless equality `k=S` too. Dropping `Q` is false:
at `R=5,S=2,p=3`, `F=2`, `A=2`, `Q=2`, so the omitted-loss formula gives
`3` instead of `2`. Without the quotient guard, the polynomial formula
also fails; the staircase has already saturated. Both falsifiers compile.

## Where factorials enter

Let `H` be the [factorial mass](FACTORIAL_LOWER_GUIDE.md). Split its exact
Legendre identity at `P≥2`:

$$H=B_{\rm small}+T+E,$$

where `Bsmall` counts **all powers** of small primes (including `2`),
`T=∑_{p>P} A(p) log p`, and `E` counts their remaining powers `p²,p³,…`.
All these sums are finite, with prime indices below `R`.

Write `V=R(R−1)/2`, `W=R(R−1)(2R−1)/6`, and

$$J=\sum_{\substack{P<p<R\\p\text{ prime}}}
\frac{\log p}{p(p-1)}.$$

Lean checks `A(q)≤V/q` and `Q(p)≤W/p²`. A finite geometric sum bounds
`∑_{j≥2}p^(−j)` by `1/(p(p−1))`; also `1/p²≤1/(p(p−1))`. Therefore
`E≤V*J` and `∑_{p>P} Q(p)log p≤W*J`. No prime-distribution result is used.

For any supplied `I≥J`, the checked scalar `Hlow≤H` gives

$$\sum_{p>P}F(p)\log p\ge
(S-\tfrac12)(H_{\rm low}-B_{\rm small}-VI)-WI/2=:b.$$

The actual sum on the left is nonnegative, so it also exceeds `max(b,0)`.
Add the exact small **odd** prime contributions and multiply by two. This
is precisely the mathematical clipping and integer coefficients used by
production `prime_mass`. The production enumeration through `P` agrees
with the restricted finite sums: primes at or above `R` have zero weight.
Lean checks these coefficient, padding and branch identities too.

## A positive potential pays for the tail

Phase 24 proves production's unchanged tail bound

$$J\le I(P)=\frac{\log(P+1)}P+\log(1+1/P).$$

Use the positive potential

$$K(x)=\frac{\log(x+1)}x+\log(x+1)-\log x,\qquad x>0.$$

Its derivative is `−log(x+1)/x²`, and `K(P)=I(P)`. To compare one integer
summand, set `g(x)=−K(x)+log(m)/x` on `[m−1,m]`, for `m>1`. Then

$$g'(x)=\frac{\log(x+1)-\log m}{x^2}\ge0.$$

Comparing its endpoints gives

$$\frac{\log m}{m(m-1)}\le K(m-1)-K(m).$$

Sum over the integers from `P+1` through `R`. The right side telescopes
to `K(P)−K(R)≤K(P)`. The prime indices are a subset and all omitted terms
are nonnegative. If `R≤P`, the prime sum is empty. This is the paper's
integral comparison expressed as a finite potential-drop proof: no infinite
sum, convergence theorem or estimate for prime distribution is needed.

## Exactly what is now connected

`ellipse_enderPrimeMassLower_le_counted_upperB` uses the proven tail bound,
not an analytic hypothesis. For squarefree `D≡3 (mod 4)`, class number one,
strict small-prime range and the displayed radius/count guards, it gives

$$\texttt{prime\_mass}\le L(R,S)\le\texttt{upper\_B}.$$

`classNumber_ne_one_of_ender_comparison` consequently rules out class number
one **if a strict real comparison `upper_B<prime_mass` is supplied**.
The saved Arb output is not assumed to supply that comparison. Interpreting
its enclosures and guards, proving the universal closure, handling even
cases and checking the finite classification remain open. No checked cutoff,
new numerical run or novelty is claimed.

[Lean source](../../lean/TenthDiscriminant/PrimeMassLower.lean) ·
[Preregistration and execution](PHASE23_PROTOCOL.md). Eight controls cover
the split boundary, empty large-prime set, guard endpoint, both clipping
branches and the two false strengthenings. From `lean/`: `lake build`,
`python verify_sources.py`, `python audit.py`, `python negative_controls.py`.

[PrimeTail.lean](../../lean/TenthDiscriminant/PrimeTail.lean) and
[Phase 24](PHASE24_PROTOCOL.md) check the tail, composition and exclusion
criterion. Eight further controls include `m=2`, empty and nonempty prime
tails, the split boundary, positivity, and false zero-tail/zero-input claims.
