# Phase380B — actual switched-graph PSD obstruction and Epstein normalization check

**21 November 2026. Additive research note, no modification of the original integer trace-Gram or Lean theorem.** The main [Phase380 analysis](ROUND_PHASE380_ALL_LINES.md) already documents the separate finite-diagonal PSD toy. The stronger result below concerns the **actual 16-vertex 4-regular switched-K4,4 graph** previously used by Selberg-Ihara.

## Actual-graph calculation

For adjacency A, q=3 and B=12I-A² on the nontrivial 14-dimensional spectral subspace (exclude the two connected-bipartite trivial eigenvectors with adjacency eigenvalues +4 and -4):

- exact integer trace(B)=136 >0,
- exact integer determinant(B)=12^12 = 8,916,100,448,256 >0,
- a nontrivial integer vector v, equal +1 on vertices 0..3, -1 on 8..11, and zero elsewhere, is orthogonal to both trivial eigenvectors and satisfies vᵀ B v=-8<0.

Thus **positive trace plus positive determinant do not imply PSD**, even for the legitimate nontrivial spectral subspace of an actual connected regular graph. The independent source program and arithmetic explanation are in [Selberg-Ihara S2](https://github.com/Dojo-1/RH-on-Selberg-Ihara/blob/research/selberg-ihara-v0/docs/S2_FULL_SPECTRAL_PSD_FAILURE.md); the local standalone integer version was executed in this continuation. No actual Selberg operator or nonabelian Hecke zeta claim follows.

This adds a useful obstruction for proposed partial trace/Weil positivity bridges, and refines the older abstract diagonal counterworld without replacing its historical record. Sylvester's inertia law transports the obstruction across invertible frames; lossy observation does not.

## Independent-formula *numerical* normalization sanity

At s=33/64, for **known class-number-one** D=-163, an independently evaluated 163-term Hurwitz-zeta character sum for ζ(s)L(s,χ_D) agreed with the principal Epstein/Poisson expression, including the parity (-1)^(nk) Bessel correction, to about 4×10^(-45) at 45 decimal digits. This is **M numerical**, not a proof of analytic continuation. It tests the factor of 2/unit normalization and independent special-function representation. The exact acceptance remains the Fraction-based [zero_free_33_64_certificate.py](zero_free_33_64_certificate.py), with the corrected denominator endpoint and a strict rational lower margin >1/1000.

## Gates

**P:** classical full-form PSD⇔Ramanujan criterion under the Bass identity; standard analytic identities remain cited external theorems. **M:** finite integer graph trace, determinant and negative witness; independent high-precision analytic sanity; earlier rational benchmark. **H:** field-to-character source-level Lean proof of d<=199, external source-semantic field review #50, Masullo spectral completeness, actual Selberg transport. **R:** earlier pre-commit wrong rational enclosure endpoint and any inference from scalar trace/determinant signs to global positivity.

Keep draft, do not merge. The original 322^4/301^4 fields and every root audit remain untouched.