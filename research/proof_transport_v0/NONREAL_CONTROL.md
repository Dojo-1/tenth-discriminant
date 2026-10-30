# Nonreal-fiber corrective control (registered after v0 pilot)

**Correction trigger:** v0's D=19/rho=2 ellipse contains only the five real-axis points. Its imaginary jet coordinates are identically zero. The first successful Rust run therefore checks matrix algebra, but not the promised nontrivial quadratic trace metric. Preserve the original result and reinterpret its scope accordingly. The prior [PR47 registration comment](https://github.com/Dojo-1/tenth-discriminant/pull/47#issuecomment-6520958709) fixes this correction **before this new Rust integration test was run**.

## Fixed extension and known oracle

Use the *actual full* integer ellipse Q=ellipsePairs(1,2) with D=1, p=3, R=4, S=J=2, rho=2. Q has 13 pairs including y!=0; the strict sufficient positivity guard is 2(R-1)+(S-1)=7<13. The previously explored reference det=2690908182187868160 is a **known development value**, not a held-out experiment. D=1 is the Gaussian field with actual field discriminant -4: do NOT call the selected parameter D its field discriminant.

Add a paired anti-control D=2,p=3 with full ellipsePairs(2,2), which also has nonreal points. The prime is split in the selected residue order; the transformed third-power row cannot have a universal integral quotient at that nonreal observation. The negative test must fail the quotient without filtering those samples.

## New executable guards

- Exercise nonzero imaginary observation coordinates and show that reweighting the fixed observation E from diag(2,2D) to the wrong D changes its Gram.
- Reconstruct original E, U_p E, integer Ehat and K=Ehat B Ehat^T. Require exact U G U^T=Delta K Delta on all original Q.
- Require detG>0, p^(2F) dividing detG and determinant/rank invariance for both TU and UT (same modular field only).
- Use checked i128 and exact Bareiss arithmetic. Overflow stops the run instead of weakening a claim.
- Keep previously proved Lean source, main classification, frozen PR45/PR46, old sample and prior results intact.
- Promote only the narrow bounded test. This is the same author's Rust implementation using an earlier same-author Python reference, not independent reproduction. No uniform analytic improvement, discriminant cutoff, or topological curvature is claimed.
