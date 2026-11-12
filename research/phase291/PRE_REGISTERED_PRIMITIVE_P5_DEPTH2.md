# Phase291-B: preregister exact second-layer primitive pairing at fixed K=8

**Date: 2026-11-12. Registered AFTER successful Phase291-A [run #43261279662](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43261279662), and BEFORE Phase291-B script or observations.** No post-hoc adjustment of its fixed p5 source precision. Original D563 full source: R=140, S=J=5, Q359, N700, M3590, all ordinary Z-jets and original metric (2,2D).

## Already observed, immutable baseline [M]

At inert p5, old Frobenius F5=1300. The exact 700-row p5 K=8 Smith normalized-source profile is `{0:620,1:5,5:15,6:60}` (all 700 levels below K8, total 440). The successfully reconstructed p-primitive C has full row rank 700 mod5. Its true metric restricted Gram Hprim mod5 has rank **684**, corank **16**; therefore `v5 det(G_original)>=2*(1300+440)+16=3496`. UNSATURATED C0 Gram rank610 and its "radical" 10 **must NOT** be added. Split p7 K2 was censored with 490 levels; exclude it from this p5 follow-on.

## New independent experiment [not yet measured]

Reconstruct the SAME primitive 700x3590 source at **precision p²=25**, using the tracked unimodular row map U from the exact p5 K8 Smith computation, never using the internally permuted Smith observation columns in B:
`Cprim25[i,:] = ( (U*C0)[i,:] mod 5^8 ) / 5^e_i mod 25`.
The maximum observed e_i=6, so `e_i + 2 <= 8` for all 700 rows: two primitive p-adic digits are genuinely available at the FROZEN original source precision. Check Cprim25 mod5 equals prior Cprim5 coefficientwise, rank700 mod5, ordinary source rows and metric unchanged.

Compute `H25=Cprim25 B Cprim25^T mod25`. Verify symmetry, the full mod5 rank684 and independent original-weighted entry dot products. Then call the **separate, previously frozen Phase280** first-two Smith algorithm `first_two_smith(H25,5)` on the 700x700 primitive H; it uses only internal matrix Smith operations and is independent of Phase291's new secondary-source Smith routine. Require exactly 684 p-unit levels by the known first-layer rank. This classifies the remaining 16 into:
- `n1` levels with exactly exponent 1,
- `n_ge2` levels unresolved at depth >=2.

The new, preregistered metric `n_ge2` is **not predicted**. If n_ge2=0, the entire primitive H determinant has exact valuation16, giving `v5(det G_original)=3496` (finite source exact). If n_ge2>0, report the strict finite `v5(det G_original)>=3496+n_ge2` and preserve censored remainder; do NOT claim exact valuation. A negative result or unexpectedly deep pairing is useful. No change of K or source is authorized to improve output.

Controls: historical original Phase280 `first_two_smith` blob `7abffdf4f4916dacef08ebe097e5eed700837ad4`; fixed diagonal Smith toy `diag(1,5,25)` has counts (1,1,1); integral row/column shear of the 700x700 H25 preserves the p² profile; left/right transpose invariance; no independently counted source indices. Use signed 64-bit only where `700*(5^8)^2<2^63`; p² Gram matrix products have much smaller bounds.

**Stop conditions:** no p-full reconstruction, mismatch Cprim25 mod5, incorrect input H-rank 684, determinant metric drift, failed toy/shear, changed original row module or any new "factor" added from an unsaturated source. Keep draft and independent semantic gates for any actual field bound.
