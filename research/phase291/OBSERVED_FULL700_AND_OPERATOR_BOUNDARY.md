# Phase291 — full original 700-row p5 primitive trace Gram: exact finite valuation 3497

**12 November 2026. POST-RESULT ledger.** User supplied Biswas and Petrovic, *On Extended Eigenvalues of Operators* (2005), and the prior Noether §12 elementary-divisor work. The new full-source finite computations are AI-authored with pinned, preserved exact GitHub Actions receipts, *not* independent peer review, not an asymptotic/large-D theorem, and not a proof of any class-number-one discriminant cutoff.

## Source frozen before code

Original finite D=563, rho=51, R=140, S=J=5, complete centered Q359 (y=-2,-1,0,1,2, all 359 original points). Every one of the n700 integer monomial rows Z^r W^s is used; all j=0..4 **ordinary** Z-jets with W held fixed, both 3590 original signed integer-pair observation channels, and original Gram metric B=diag(2,1126) repeated for each (j,q). Freeze `source_probe.py` Git blob `3f954b59d9f86b06ad53667c869b5b24f2e6c7f6` and `ordinary_jet_filtration.py` blob `dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8`. Source jet oracles replay 480 two-channel entry checks. The old source interpolation sufficient condition 359>2(139)+4=282 ensures original full-row rational nondegeneracy (as separately established in the repo).

At **inert p5**, `(-563 mod5)=2` nonsquare. Old unimodular source-polynomial Frobenius row frame uses `k_(r,s)=min(floor(r/5),4-s)`. Its exact OLD k-histogram is `{0:160,1:150,2:140,3:130,4:120}` and its PREVIOUSLY counted evaluation index sum is **F5=1300**. Every normalized original source entry is an integer original Z-jet of `Z^(r-5k) W^s (Z^5-W)^k /5^k`. No p-unit of this 1300 should be counted as new Phase291 mass.

## Exact 700-row finite source Smith and primitive pairing [M + classical P algebra]

Let E be the original 700x3590 integral observation matrix and T in GL_700(Z) its OLD unipotent polynomial row frame. With D_old=diag(5^k), `T E=D_old C0`, `C0` fully original and integral. Its **secondary** p-local Smith row reduction, with row map U in GL_700(Z5) and ***internal*** Smith column operations used solely for finding levels, gives `U C0=D_secondary Cprim` in ORIGINAL observation columns, where `D_secondary=diag(5^e)`.

The exact p5 **secondary source** Smith profile at frozen precision K8 (also replayed K9) is
`{0:620,1:5,5:15,6:60}`. **All 700 levels are resolved**, so `sum e_i=5+5*15+6*60=440`. The original C0 rank mod5 is 620 and its UNSATURATED Gram rank is 610: the apparent 10-dimensional unsaturated radical is **discarded** (the Phase277 saturation counterworld requires this). The truly primitive recovered Cprim has rank **700** mod5; thus it is the full saturated row image over Z5.

The original-metric primitive pairing is `Hprim=Cprim B Cprim^T`. The exact normalized source index identity gives

```
v5(det G_original)
  = 2 * sum k + 2 * sum e + v5(det Hprim)
  = 2 * (1300 + 440) + v5(det Hprim).
```

No Smith COLUMN operation is transported through B, and the factors are not added twice. The full 700x700 primitive H is reconstructed modulo5/25/125 with enough prior source digits. Its exact p5 Smith profile is
`{0:684,1:15,2:1}` (no censored >=3 levels), hence `v5 det Hprim=15+2=17`. Therefore the **exact finite original-source result** is

\[
\boxed{v_5(\det G_{563})=2(1300+440)+17=3497.}
\]

This does **not** require expanding the huge 700x700 integer determinant. The original trace B has odd-p entries units at p5; the residual 17 is a restricted-pairing valuation, *not* a metric weighting typo.

## Independent implementation controls and CI receipts [M, not peer review]

- [Phase291-A run #43261279662](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43261279662): full original K8 C0 source, historical D283/p5 exact 140-row primitive control (hist 60/15/30/20/15, index195, p-unit primitive Gram), fixed diagonal Smith toy, original-jet oracle, full 700-row secondary Smith, primitive H mod5 corank16, `v5 det G>=3496`.
- [Phase291-B run #43262107271](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43262107271): using **same** K8 raw precision and tracked row map, primitive H mod25 has profile `{0:684,1:15,>=2:1}`; independent older Phase280 first-two Smith algorithm, full Gram symmetry and shear controls. Lower >=3497, one unresolved depth.
- [Phase291-C run #43262594081](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43262594081): separately preregistered K9 with `5^(9+4)` original numerator precision, maximum source e6 permits exactly 3 primitive digits; older frozen Phase281 third-layer Smith algorithm yields **`{0:684,1:15,2:1,>=3:0}`**, so the valuation **3497 is exact**. K8 H25 profile replay and no column metric transform.
- [Phase291-D run #43263311001](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43263311001): independent 350+350 original Noether-inversion parity decomposition, each separately p-saturated, **all 122,500 cross-pairing entries vanish modulo125**; each sector reconstitutes the global source and H Smith profiles. The sector results:
  
  | original parity | n | OLD F5 | secondary idx | source Smith | primitive H Smith | residual H v5 | original sector Gram v5 |
  |---|---:|---:|---:|---|---|---:|---:|
  | even | 350 | 650 | 218 | (0:310,1:3,5:7,6:30) | (0:341,1:8,2:1) | 10 | **1746** |
  | odd | 350 | 650 | 222 | (0:310,1:2,5:8,6:30) | (0:343,1:7) | 7 | **1751** |
  | sum | 700 | 1300 | 440 | (0:620,1:5,5:15,6:60) | (0:684,1:15,2:1) | **17** | **3497** |
  
  The UNIQUE depth-two primitive line is in the **even sector**. Original source parity is a valid p5 direct summand since 1/2 is a Z5-unit, but NOT a Z2 integral projector. The 350+350 experiment adds **no new valuation** to the already certified 3497.

The tests are code-level confirmations with different internal Smith algorithms and source representations. They are not truly independent human proofs; shared raw helpers and AI authorship remain a limitation.

## Split-prime negative control

At split p7, `(-563 mod7)=4` square, so **no inert Frobenius factor**. The full original E modulo p7 has rank175, its unsaturated Gram rank165; capped-K2 source Smith `{0:175,1:35,>=2:490}` gives an evaluation-index LOWER bound1015 and a conservative `v7 det G>=2030`. **490 source levels are unresolved** and no p7 primitive pairing is computed or claimed. Large local source factors can arise at split primes too, so they must never be marketed as new *inert* prime mass.

## Operator-theory bridge and caution [P-paper + counterworld]

Biswas–Petrovic *On Extended Eigenvalues of Operators*, finite-dimensional Theorem 2.5/Corollary2.6 and powers/commutant Theorem5.6, study nonzero operators X satisfying AX=λXA. For finite real SPD G, every complex extended eigenvalue λ is a ratio of strictly positive real spectral values, so λ>0. If X is **invertible**, determinant gives λ^n=1, hence **λ=1**: a scalar-rescaled invertible intertwiner is a genuine COMMUTANT gauge. Every power G^m has the same commutant because x↦x^m is injective on positive eigenvalues. These are classical spectral restrictions, NOT newly proved original lattice symmetries.

Negative exact toy: A=diag(1,4) is positive over R; X=[[0,1],[1,0]] invertible does NOT satisfy AX=-XA over R, but `AX=-XA mod5` holds because A's mod5 eigenvalues 1 and -1. Thus **modp operator anticommutation can exist while real SPD anticommutation is impossible**, and neither is a license to transport rational/real frames as GL_Z. This negative control was exercised in Phase291-D. The parity-invariant source lattice uses an explicit C2 group action; it is not a physical Noether current or an adiabatic Schr dynamics.

## Why this does not solve the tenth discriminant

D563 is NOT assumed class-number-one. In fact it is not: in `O_K=Z[(1+sqrt(-563))/2]`, the norm form is `N(a+b omega)=a²+ab+141b²`. Since -563 is 1 mod3, the rational prime3 splits, giving an integral ideal of norm3, but the norm form has no integer solution N=3: for b=0 it would be a²=3, and for |b|>=1 the real lower is (563/4)b²>3. Hence that prime ideal is not principal and h(K)>1. This is a small direct algebraic negative control, not an appeal to the classification of Heegner fields.

The exact full-source 3497 therefore provides a **high-quality finite invariant of the original geometric sampler**, not a new disqualifying exponent for a hypothetical h=1 field or a better cutoff (the conditional 321^4 branch #157 remains draft). The remaining theorem target is a uniform source- and p-local statement that controls the SECONDARY evaluation index and genuine **fully primitive** restricted-pairing Smith profile for the growing R,S,J,Q family at h=1 admissible D, across changing transverse support walls. The preceding four CI runs prove nothing asymptotic by themselves.

**Evidence register:** [P-paper] classic source Smith/Cauchy–Binet factorization, odd-prime parity projector, SPD extended eigenoperator spectral restriction and elementary norm counterworld; [M] fixed full D563 finite source, exact programmed modulus / rank / original jets, and independent internal replay; [H] any uniform discriminant theorem or phase-wall spectral transport inequality; [R] treating unsaturated radical10 as extra valuation, treating split p7 as inert, attributing Noether/Biswas prior theorems to this code, or adding 3497 to already used original-source p5 exponents. Independent human mathematical and source-to-field reviews #50/#51 must remain separate, and this PR remains DRAFT.
