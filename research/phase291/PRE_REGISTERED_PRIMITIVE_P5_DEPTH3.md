# Phase291-C: fixed K=9 primitive p5 third-layer discriminator (preregistered)

**12 Nov 2026, AFTER Phase291-B successful run [#43262107271](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43262107271), BEFORE Phase291-C executable or test.** The observed Phase291-B full ORIGINAL D563 700-row source is immutable: p5 old Frobenius F=1300, exact secondary source index 440, max secondary exponent e=6, primitive H5 rank684, primitive H25 Smith histogram `{0:684,1:15,>=2:1}`. Hence established **lower** v5(det original Gram)>=3497, with one primitive residual line unresolved at depth2.

## Frozen next exact experiment; do not fit outcomes

The unchanged ORIGINAL source: D563 rho51, R140 S=J5, Q359 (all five y strata), 700 original rows and 3590 original real/imag integer observation columns, original metric diag(2,2D), ordinary Z derivatives with W held fixed, same frozen original helpers, inert p5 and same Frobenius-old row basis.

For one NEW, explicitly extended precision, choose **K=9** for the secondary-source Smith calculation, so `max e+3=6+3=9` is *sufficient* to reconstruct the primitive row source modulo **p³=125**. The modular source numerators must be computed modulo `p^(9+4)=p^13` before dividing by old p^k. This choice is derived from the PREVIOUSLY measured max e=6; the earlier K8 and L2 evidence remains unchanged and the K9 result cannot be called blind.

Use Phase291's identical vectorized tracked-row Smith operator with K9, verify exact levels histogram `{0:620,1:5,5:15,6:60}` and index440 (regression), then recover `Cprim125[i]=(U C0)_i/p^e_i mod 125` using ORIGINAL column coordinates (not internal Smith column swaps). Require:
1) full rank Cprim125 mod5=700, all row source/count/oracles unchanged, `Cprim125 mod5` equals the K9 Cprim5, exact coefficient-level checksum on frozen 16 original source rows against Phase291's source oracle, and no numerical int64 overflow (`700*(5^9)^2 < 2^63`);
2) `H125=Cprim125 B Cprim125^T mod125`, exact original signed trace metric, H125 mod5 rank684, exact old `H25=H125 mod25` profile `{0:684,1:15,>=2:1}` replayed with **existing Phase280 independent Smith K2**;
3) compute the new primitive H `K=3` Smith histogram with the PREEXISTING frozen `research/phase281/full_d403_third_layer.py` `smith_profile_k3` blob `d28b1420a371ca3a8a0297a19ecec75feedfc978`, not reusing the Phase291 saturation pivot implementation. Require first two histogram layers exactly 684 and 15, and `n_e2+n_ge3=1`. No predicted answer for n_e2.
4) Check self-adjoint row/column unimodular shear preserves this profile; independently check selected Gram entries as original weighted dot products, no eigenvalue/float approximations.

**Interpretation:** if the remaining single primitive level has exponent EXACTLY 2 (n_e2=1, n_ge3=0), then `v5(det Hprim)=15+2=17` and `v5(det G_original)=2*(1300+440)+17=3497` is **EXACT** for this finite D563 source. If it remains >=3, report at least 3498 and RETAIN unresolved primitive higher depth. No post-selected precision bump or new field theorem. The independently evaluated original S=J and row rank/point interpolant keep det positive. Preserve all failed runs and keep PR DRAFT for independent semantics and Lean review.

**Epistemic types**: [P-paper] Smith filtration and congruence identities, original rank implication; [M after exact CI] original n700 K9 primitive residual depth; [H] any uniform class-number-one bound or production-scale scaling; [R] adding UNSATURATED 10-dimensional radical or unvalidated split p7 profiles to original inert valuations.
