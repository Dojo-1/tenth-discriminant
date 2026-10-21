# G1 — "First-strand" route (least split prime < D/4) — retired 21 Oct 2026

Idea (route map, O3∘B): h(−D)=1 forces every split prime >= (D+1)/4, so an effective explicit bound
"least prime p with chi(p)=+1 is < D/4" would exclude a tenth discriminant.

Why it is not a third route (DERIVED; literature status of Linnik–Vinogradov effectivity not verified):
- Showing a split prime exists below D^theta means showing the coefficients r(n) = sum_{d|n} chi(d) are not
  concentrated on inert/ramified structure — i.e. a lower bound on the split mass, which is a lower bound on
  L(1,chi) in disguise. That is exactly the Siegel-zero input of route B (now effective via Banks/OpenAI).
- So the "first-strand" statement is a reformulation of the problem, not a new instrument.
Contrast that survives as understanding (the enemy, one sentence):
  inert primes are cheap to find (least NON-residue: Burgess-type, effective), split primes are expensive
  (least residue: needs L(1,chi)); class number one lives entirely on the split side. This is the parity
  asymmetry Tao names; the determinant method is the parity-breaking instrument.
Sources consulted: survey McGown–Treviño (least non-residue); arXiv:1309.3595 (non-residue, GRH) — neither
addresses effectivity of the least prime RESIDUE.
Update (sources supplied by J. Vilela, 21 Oct 2026): Linnik–Vinogradov O_eps(D^{1/4+eps}) is NON-effective — its proof combines
Burgess (effective) with Siegel's L(1,chi) >> D^{-eps} (ineffective). Refs: arXiv:2404.08380; MathOverflow 401156.
This confirms the diagnosis: the least-residue bound inherits exactly the Siegel input of route B.
Corollary (DERIVED): with Banks' effective exclusion (1-beta) log q >= 3e-3, the Siegel step becomes effective, so an explicit
Linnik–Vinogradov bound is now obtainable — but only BY route B, so it adds nothing independent.
Alternatives rejected for this project: GRH (Ankeny, Lamzouri–Li–Soundararajan) is a forbidden input; Tatuzawa-type
"effective with at most one exception" is useless here — the possible exception is precisely the tenth discriminant.
