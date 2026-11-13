# Phase306-D — preregister full actual-source bridge, after A/B/C

Date 2026-11-13. A/B/C were already implemented and tested. This is a genuinely new follow-up before authoring the D bridge.

**Frozen source:** Phase304 highjet_d203_original.py (own frozen helper/source SHA gates), actual unchanged params(D=203): rho24, R50, S=J2, full genuine maximal-order Q263, original 100 source rows in order (r,s) -> 2*r+s, original ordinary Z-jets j=0,1 and original hermitian trace pairing Bomega.

**Proposed independent test:** fetch actual full E100x1052 source via Phase304, then reconstruct rows (0,2,4), corresponding to original (r,s)=(0,0),(1,0),(2,0), from independent pure-Python omega multiplication and original ordinary derivatives on ALL 263 actual observations. Compare EVERY selected evaluation coordinate modulo 5^3 (3*1052). Compare the 3x3 integer trace Gram modulo 5^3 against Phase304's separately reconstructed 3x3 Gram. Apply fixed nontrivial GL3(Z) moving frame, verify EXACT original integer covariance and determinant invariance on all 263 observations. Compare both linear-map (profunctor) orientations. Explicitly reject mismatched D, precision and nonintegral gauges.

**Required negative controls:** A deliberately wrong field coordinate chart, or omitting the ordinary derivative jet, must not match the frozen original source. The 263-point support must remain actual and unmodified. NO interpretation of the 3-row subblock as proving the full 100x100 Smith profile.

**Kill condition:** any failure in the actual evaluation (including its j=1 coordinates) or Gram prevents claiming source-faithfulness. No changes to the 322^4 bound. No external human review implied.