# z — understanding (cap: one page)

c sha256: (see below)
enemy (named, step 1): the split bound counts ALL integers represented by the h forms (lattice points), not primes.
  Primes are a 1/log t fraction of them -> we lose a factor ~ log R / 2 (~10-15) in the split mass, and X(H) grows like
  (split coefficient)^2 ~ H^2. Measured: true split count is 6-19% of the bound.
  Remedy candidates: (a) upper-bound sieve on norm-form values (explicit Selberg/Brun-type, ideal version);
  (b) twinheterodox v5: Euler product of primitive norms (keeps composite norms on the other side);
  (c) small-prime sieve of lattice points (twinheterodox v3: 2,3,5,7) — constant gain only.
dead ends: G1 first-strand (least split prime) = route B in disguise (graveyard/G1). (H=20 point probe timed out at 10 min on 2 cores: compute, not math.)
what each hypothesis does:
- h <= H enters ONLY through O5 (split count) and O6 (ramified count). Everything else is h-independent.
- class group fibre: 4 reps per split prime summed over all classes (decategorified count) — this is why O5 is clean.
falsifier (pre-registered): certificate claiming "h > H on [D1,D2]" must never cover a D with h(-D) <= H (checked with PARI).
c sha256: 67e60b2235842843

enemy, one sentence: inert primes are cheap (Burgess), split primes are expensive (L(1,chi)); h=1 lives on the split side.
