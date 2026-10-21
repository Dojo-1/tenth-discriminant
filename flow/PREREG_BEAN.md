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
