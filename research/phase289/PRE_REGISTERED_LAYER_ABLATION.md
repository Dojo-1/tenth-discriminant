# Phase289-C — post-heldout preregistered transverse-layer ablation

**12 November 2026. Registered AFTER the third-source held-out D563 exact CI PASS [#43247424896](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43247424896), and BEFORE writing/running the ablation code.** The recorded D563 K=179, strict=36 and approximate normalized extra gain 0.001386825 are already observed, NOT new prospective predictions. The earlier D283/D403 gains ~0.01958 / ~0.01801 are also known. This is an exploratory causal intervention on the *sampling geometry*, NOT a new field-source theorem, human-independent review or replacement of the original D563 Gram.

## Frozen original source and suspected mechanism

At D563, the unchanged Phase206 helper returns rho51, R140, S=J5, Q359 and its sampling disk contains five y layers. Layer arithmetic (direct integer norm, not tuned after observed gain):
- y=0: x from -51 to 51, **103** points;
- y=+/-1: x from -45 to 45, **91** each, 182 together;
- y=+/-2: x from -18 to 18, **37** each, 74 together.
Total Q359. The earlier D283/rho31 and D403/rho40 original disks have only y=0,+/-1, because rho^2<4D in both, whereas D563 has rho^2=2601>4D=2252. This is an exactly identifiable discrete transverse-slice bifurcation, not yet a demonstrated cause of the 4-fiber correlation loss.

Define the **counterfactual ablated source** Q3 = {q in original Q359 : |y|<=1}, cardinality 285, and its removed set Qextra of 74 points. Keep EXACT D563, rho51, R140,S=J5, all original 700 Z^r W^s rows and all five ordinary Z-jets (W held fixed), the ORIGINAL 2,2D channel metric, and the SAME deterministic 72 old pairs / 36 quartets. The original interpolation sufficient guard remains valid: |Q3|=285>2(R-1)+(S-1)=282. Hence the ablated Gram is still positive definite. **Do not** use Q3's determinant, arithmetic divisibility or any resulting analytic bound in the D563 field theorem; it is a different source.

## Frozen tests and interpretation

1. Confirm frozen Phase206 and Phase204 source hashes; independently enumerate all D563 disk points and each y slice, all counts above, and the y-inversion and x-inversion symmetries of Q359/Q3/Qextra.
2. Using the IDENTICAL original 72-pair/36-quartet partition and ordinary-jet+trace source, compute every quartet for both original Q359 and ablated Q285, reconstruct the same exact A/B/quad Fischer inequality and first lexicographic nonzero cross witness, independent original jets and conservative dyadic gains. Report K_original and K_ablated, strict groups and normalized approx WITHOUT prespecifying the ablation's improvement direction or amount.
3. Require K_original=179 and strict_original=36 from the ALREADY OBSERVED D563 exact baseline; if it changes, stop. Do NOT choose a different partition or row depth to recover a desired result.
4. For the first quartet verify exact matrix equality `G_Q359=G_Q285+G_Qextra`; the deleted-point Gram is positive semidefinite by construction, but its removal has **NO monotonicity theorem for ratios** `V_pair/V_four`. A different quartet saving is an intervention-dependent observation, not automatically proof of mechanism.
5. Exact NO-uniform 0.0043 certificate: the baseline per-quartet dyadic rule already guarantees `2^K < V_pair/V_four <= 2^(K+strict)`. At D563 K=179, strict=36, so its actual normalized extra log gain is <=215 ln2/98000 <215/98000 <43/10000. This **refutes any claimed uniform lower bound >=43/10000 for this particular four-fiber incremental saving** over all admissible field parameters, independently of approximate logs. It does not refute different possible analytic constructions or a weaker uniform rate.
6. Retain Phase207/288 no-double-counting constraints: the old pair matching is used once, a Q3-versus-Q359 comparison is NOT a single same-Gram arithmetic/analytic sandwich, and real moving Schur shears are NOT p-integral gauges.
7. If the ablation FAILS to restore the large gain, retain that outcome and reject the simplistic y-layer causal explanation. If it restores some gain, record measured intervention effect under changed support, not a universal theorem. Keep all further speculation [H].

No fitted numerical threshold for K_ablated, no field bound, no Siegel-zero statement. Exact-head focused+Markdown+Lean CI and human audit gates remain open.
