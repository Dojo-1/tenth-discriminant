# Author response to review/PHASE2_GPT-6.1-Sol.md

| Finding | Accepted? | Action | Evidence |
|---|---|---|---|
| F1 FATAL (tail over empty range in cover.py) | Yes | Guard: tail only if T>P, G(T)>0, P>=2b/a certified | Reviewer's counterexample (R=11999990, S=149999) now gives lower bound = exact mass (diff within ±5e10, was +6.6e18) |
| F2 GAP (float rounding past root) | Yes | T := R//3 exact integer; G(T)>0 certified in Arb | coverage_v3: 43/43 intervals recertified |
| F3 SLOPPY (2b/a identity) | Yes | Exact hypothesis checked in asymptotic.py | prints True |
| F4 SLOPPY (floats in "exact" verifier, 1x1 crash, nan) | Yes | Arb checks, Mat(), stderr surfaced, domain guard | 46/46 pass; 1x1 case runs |
| F5 GAP (verify_exact_large.gp absent) | Timing | File was pushed (a799f7d) after reviewer's clone | Request re-run |
| F6 NIT (repo instructions treated as data) | Agree — correct behaviour | none | — |
| A7: limit ratio 64/49, not 4/3, for fixed C | Yes | Corrected in asymptotic.py output | — |

## Not yet reviewed by anyone independent (changed after the reviewer's clone)
- fdd8052: N3' tighter split bound (π/2)t/√D + √(t/D) with exact partial summation in cover.split_mass.
  The reviewer independently derived the same N3' bound in Phase 1 B1; the partial-summation code is unaudited.
- tools/verify_exact_large.gp.

## Still CANNOT-VERIFY (reviewer had no network)
- N9 Dusart (1999) primary statement; Green's text vs. quoted lemmas (reviewer re-derived N4–N7 independently, so
  the proof no longer depends on Green's wording); novelty (Tao comment threads).
