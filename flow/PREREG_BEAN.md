# Pre-registration — seed "BEAN": inert-only determinant, no split-prime counting (BEFORE computing; 21 Oct 2026 22:20)
Idea: h(-D)=1 => every prime p < (D+1)/4 is inert (Rabinowitsch; elementary, no counting). Choose R < (D+1)/4, so EVERY odd
prime <= R is inert and the split/ramified subtraction is identically zero. The norm-ellipse evaluation set (J. Vilela)
lowers the archimedean term by ~(1/4) log D, which is what makes R < D/4 feasible.
Inputs: Green derivative determinant (N4–N7, reviewed), ellipse count (N8, reviewed), Hadamard, Dusart 2010, Rabinowitsch.
NOT used: split-prime counts, representation counts, L-functions, Siegel, GRH/QRH, Heegner.
Test: certify (D1,D2) with R <= (D1+1)/4 (so the inert claim holds for all D in the interval), lower = prime_mass(R,S),
no subtractions; same upper bound as cover.py. Report the smallest D where it works; then contiguous coverage + asymptotic.
Prediction (written now): works for D >~ 1e10–1e12, margin growing with D. Kill: if no D <= 1e30 certifies, the seed dies
(recorded in graveyard). Novelty claim only after re-checking the thread and twinheterodox repo for "no split count" proofs.

## OUTCOME (appended; nothing above edited) — point probes, R = floor((D+1)/4), best C in {10..160}
1e8: 0.899 · 1e10: 0.946 · 1e12: 1.005 CERTIFIED · 1e14: 1.046 · 1e16: 1.077 · 1e20: 1.123 · 1e30: 1.185 (all certified >= 1e12).
Prediction (1e10–1e12, margin growing) confirmed. Next: contiguous intervals + asymptotic + sieve below ~1e12; novelty re-check.
