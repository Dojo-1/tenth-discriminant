# Phase354 — 14^4 source count and the unchanged original Gram

19 November 2026. **Pre-registered before the new Lean module. Research-only.**

## Fixed carrier
Original `D : Nat`, `t=FirstCertificate.fourthRoot D`, `R=FirstCertificate.Tuned.R D=floor(D/4)`, `S=FirstCertificate.Tuned.S D=floor(R/25)`, `rho=FirstCertificate.Tuned.thinRadius D=ceil(11*t^3/25)`, full `Q=ellipsePairs D rho`.

The original source is NOT replaced by a five-band support, half-integer order, selected row minor, altered derivative or modified metric. The integer Gram retains all original ordinary Z jets j<S and all row-major (r,s) with r<R and s<S and trace weights 2 and 2D.

## Primary prediction

With `t>=14`, the existing cell-area lemma gives

`delta=(1+t^2)/2 <= (9/250)*t^3`,

`rho-delta >= (11/25-9/250)*t^3 = (101/250)*t^3`.

Mathlib's `Real.pi_gt_d2` yields `157/50<pi`. Exact rational inequality:

`(157/50)*(101/250)^2 > 51/100`.

Thus, on the exact source, `card Q>2R+S`, hence the already established interpolation guard `2*(R-1)+(S-1)<card Q` holds for every `D>=14^4=38416`.

Use the EXISTING `ellipseIntegerTraceGram_det_pos_of_count` to derive strictly positive determinant of `integerRectangularTraceGram Q D (S D) (R D) (S D)`. Also derive the original real Gram positivity and Hadamard bound using `ellipseTraceGram_det_bounds`, without a replacement matrix.

## Mandatory falsifiers
- The error bound with coefficient 9/250 MUST fail at t=13. This does not claim point-count failure at 13.
- The hard `D=14^4` endpoint and non-fourth-power nearby D must satisfy the original full ellipse count strictly.
- If `Real.pi_gt_d2` or another inequality fails, do not weaken or axiomatize it. Fix or retire.
- The root compiler and transitive axiom inspection must pass at exact head; `0 sorry` alone is not a proof.
- No new field discriminant cutoff is claimed or merged from these geometry and positivity results.

## Promotion rule
H until exact-head Lean build and source/axiom audit pass; then P relative to encoding for uniform source count and original Gram positivity only. M for fixed-range exact integer controls. Independent mathematical review remains a separate gate, and current field bound on public main remains unchanged.
