# Environment (set up 2026-10-21)

| Tool | Version | Purpose |
|---|---|---|
| python-flint (Arb) | 0.9.0 | Certified interval arithmetic for every numerical inequality |
| mpmath, sympy, numpy | latest | Exploration only (never certifies) |
| PARI/GP | apt pari-gp | Independent class-number check (`qfbclassno`, computed, no tables) |
| Lean 4 + Mathlib | user's machine (v4.11, H:) | Formal layer |

## Tools
- `tools/sieve_h1.py` — prototype class-number-one sieve.
  Control test passed: on [8, 10^6] it returns {11,19,43,67,163}, matching PARI's full list {3,4,7,8,11,19,43,67,163}
  (the four smallest are below the sieve's range by design).
  Speed: [8, 10^10] in 37 s on 2 cores. A linear scan to ~1.6e15 is too slow (~2 months);
  production version must enumerate residue classes (Watkins-style). Status: HYPOTHESIS-grade tool.

## Literature (lit/, hashes in lit/SHA256SUMS)
OpenAI Siegel (9pp, +TeX), OpenAI QRH 11/12 and 7/8, Banks, Kerr, Green v2, Kimura (+TeX source).

## Not used
- nnn-hyperbolic-ramdisk_v2: a memory/storage fabric for LLM agent context (RAM/NVMe/CXL tiers).
  Our workloads are CPU-bound integer sieving and interval arithmetic with tiny I/O, so a storage
  layer gives no speedup. Revisit only if a sieve run becomes I/O-bound.
