# Pre-registration — lowering the h=1 analytic cutoff (written BEFORE computing; 21 Oct 2026 22:15)
Baseline: our certified cutoff 1.5e4 (point probe 1.2e4). Target ladder: 1e4 -> 5e3 -> 2e3 -> 570 (twinheterodox v6) -> 164 (sharp).
Step A (diagnosis): at D = 1.2e4 decompose (upper - lower)/(R^2 S) into: Hadamard archimedean term, derivative term,
  point-count/log term, split-prime subtraction, ramified, prime-mass deficit (small primes, tail, capping g(k)).
  Report the ranking. No parameter tuning in step A.
Step B (levers), each tested separately against the same baseline, each must keep all brute-force controls passing:
  L1 composite norms: split primes are only part of the represented norms; subtract the provable non-prime part.
  L2 parameter freedom: J != S, rho, C, R jointly (pre-stated grid; report the grid).
  L3 auxiliary inert prime / van Dijk-style nonsingularity (weaker independence requirement).
  L4 sharper determinant bound than Hadamard (measured slack 3-10% on ellipse sets).
Kill: a lever that fails a brute-force control is dropped, not patched to pass. Every claimed cutoff must be re-certified
by contiguous intervals + (if needed) asymptotic closure, and the finite range below it checked by PARI.
Credit: L1 and L3 are ideas from twinheterodox v5/v6 and van Dijk; we reimplement them independently and cite them.
