# Phase292 — preregistered neighboring-field test of the exact original-source p5 transport

**12 November 2026. Written BEFORE Phase292 code and CI.** This is a stacked DRAFT branch from Phase291 PR #182, not a merge to main. Phase291's D563 exact finite result is **previously observed** and a regression control, not a second blind discovery. Other mathematical review gates (#50 and #51) remain open.

## What actually transports between discriminants

Let D be positive squarefree, D ≡ 3 (mod 4), with the existing ORIGINAL source `params(D)`, ellipse Q_D, row lattice `L_D = Z^(R_D S_D)`, ordinary Z-jets holding W fixed and trace weights diag(2, 2D) per (j,q). **Different D produce different row ranks, observation supports, Gram determinants, and local fields; there is no GL_n(Z) change-of-frame between them.** The comparable invariants are typed Smith-level histograms and their source-normalized valuation decomposition.

For any odd inert p, the OLD Frobenius polynomial row basis `Z^(r-pk) W^s (Z^p-W)^k`, `k=min(floor(r/p), S-1-s)`, is unimodular before each row's *already-counted* p^k quotient. If the original rational Gram has full rank and a complete p-local Smith normalization of C0 is obtained in ORIGINAL observation columns, the *classical* identity is

```
 v_p(det G_D) = 2 F_p(D) + 2 I_p(D) + v_p(det H_prim,D)
 F_p(D) = sum_{r,s} k_(r,s)
 I_p(D) = sum_i e_i, exact ONLY if every secondary Smith level e_i is uncensored
 H_prim,D = C_prim,D B_D C_prim,D^T, with rank(C_prim,D mod p) = R_D S_D.
```

This is the **same Gram once**. In particular, the 1D/2D phase290/291 results cannot simply be appended to another method's p-adic budget. The Phase208 result already supplies `rank(C0 mod p) <= J T_p(Q)`, `T_p(Q)=|Q mod p^2|`, a first-layer SOURCE bound, not a primitive Gram claim.

## Candidate H, control, and preregistered kill conditions

**Blind neighbor D=587**, selected before evaluation as a nearby **prime / squarefree**, D≡3 mod4, p=5 inert (`-D≡3 mod5`) source in the SAME S=J5 stratum, but with a new ellipse and larger row module. All geometric quantities are analytical frozen predictions from `params(D)`, not observations to fit:

- D=587, rho=53, R=floor(D/4)=146, S=J=floor(R/25)=5, original Q383, five transverse y-layers with counts y0:107, each y±1:95, each y±2:43; m=2JQ=3830 columns, n=RS=730; interpolation guard 383 > 2(146−1)+(5−1)=294.
- **Old** inert p5 Frobenius level census `{k0:166,k1:156,k2:146,k3:136,k4:126}`, F5=1360. Original row C2 parity sectors: 365 each, with OLD F5=680 each; odd p permits the parity projectors, p2 does not.
- `Q587 mod25` has exactly 125 (x mod25,y mod25) classes because each of five transverse layers contains all 25 x residue classes. Therefore rank(C0 mod5)≤J*125=625, first-layer secondary nullity≥730−625=105 and the previously established *theoretical* original Gram bound is `v5(det G587)≥2(1360+105)=2930`. This bound alone is NOT a new theorem and is much weaker than an exact valuation.
- Held-out measurement: complete p5 K=9 secondary Smith profile of **all 730** original normalized rows. Then reconstruct primitive rows in original observation coordinates only if **all** 730 levels <9. Try 3 digits for primitive Gram only when max e≤6 (K−3); otherwise use fewer justified digits, explicitly censor the unresolvable level, and refuse to report exact valuation. No adaptive precision. Other prime panels may be investigated only in a later preregistered stage.

**Regression D=563:** a fresh parameterized source implementation must reproduce Phase291's frozen original rho51/R140/S=J5/Q359, old F=1300, secondary histogram `{0:620,1:5,5:15,6:60}`, primitive Gram K3 Smith `{0:684,1:15,2:1,>=3:0}`, and exact original v5=3497, without modifying PR182. This is an internal shared-data control, not fully independent verification.

**Falsification:** The proposed *overstrong* hypothesis "the primitive residual profile (0:684,1:15,2:1), or the normalized corank16, is a transport-invariant across neighboring D" is NOT assumed true. If D587 differs, label that invariance [R] at once. If it agrees, evidence is only two finite points, NOT a theorem. The weaker structural decomposition is an existing P-level algebraic identity and cannot be falsified by finite data without identifying an implementation or hypothesis mistake.

## Exact controls and stop rules

1. Freeze original two source helper Git blobs and prior Phase291 Smith code blob. Confirm D587 prime/squarefree with `params`, y counts, row/jet/column counts, old F and parity sectors, inert p5, full support. No Q3 ablation, no observation drops, no Gaussian shift, no p7 inert interpretation.
2. Build every normalized original ordinary jet using a new D-parameterized source function; use numerator precision `5^(9+4)`, divide row-by-row by OLD p^k only after integrality check. Independently compare exact integer-jet calculations for 16 frozen row labels (including near row boundary and each old k stratum), ALL j0..4, 3 original points, both integer channels; verify the original central inversion sign relation coefficientwise modulo p and p².
3. A numerically distinct modular Gaussian rank check must equal the level-zero Smith count. Verify source column count, full same-original trace metric, two specimen-supports and a fixed diagonal toy with censored e=9. Runtime arithmetic stays within signed int64 on modular matrices: `730*(5^9)^2<2^63`; raw source arithmetic uses Python unbounded integers.
4. If all source levels are uncensored, reconstruct original-observation Cprim at justified precision, verify rank n modp, compute its original metric restricted pairing H and obtain K3 profile with the previously frozen distinct Phase281 third-layer Smith algorithm (and Phase280 K2 replay). If K3 censored, report only a lower bound. No false full determinant exactness.
5. Compare the **signed** source sector parity Gram only at odd p; original row parity gives cross-sector zeros, no extra p-divisor. Primitive parity decomposition, if needed, is a separate future experiment—not an automatic identification of two different D lattices.
6. The number field for D587 has h>1: p3 splits because `-587≡1 (mod3)`, whereas norm of a+b(1+sqrt(-587))/2 is `(a+b/2)^2+(587/4)b^2` and cannot be 3. It is a stress source, NOT a class-number-one certification. The same is true for D563. No new 322^4 or 321^4 conclusion.
7. Keep new work DRAFT even with all focused CI successful; require explicit exact-head check, human math/source-to-field review, and independent field proof connection before merging or promoting any uniform theorem. Preserve negative results and old failed CI history.

## Claims by level

[P-paper] Full rank + Smith original-metric identity; exact old Frobenius census; odd-prime inversion symmetry; existing Phase208 mod-p rank ceiling.
[M after CI] Actual original D587 secondary index, primitive rank/depth if fully resolved, exact finite v5 when no primitive censored factors remain.
[H] Any **uniform** positive normalized secondary/primitive saving, field cutoff improvement, or moving-frame identification of differently ranked lattices.
[R if falsified] Fixed primitive-radical profile invariant under neighboring D.
