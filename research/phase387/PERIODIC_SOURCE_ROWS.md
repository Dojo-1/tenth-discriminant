# Phase387.3 — Eventual periodicity of normalized ordinary Frobenius rows

**22 November 2026 · elementary conditional paper theorem and independently checked finite controls.**

## Exact object

Keep the original selected quadratic order A_D=Z[beta], beta²=-D, its conjugation, the original held-W ordinary-Z derivatives, original rectangular row indices (r,s), and an odd prime p for which -D is nonsquare modulo p. The reduction A_D/p is therefore the field F_(p²). No changes of test Q, derivative convention, trace metric or number-field objects are permitted.

Write

\[
k(r,s)=\min(\lfloor r/p\rfloor,S-1-s),\quad
P_{r,s}(Z,W)=Z^{r-pk(r,s)}W^s(Z^p-W)^{k(r,s)}.
\]

The original integer jet division is

\[
F_{r,s,j}(z)=p^{-k(r,s)}(\partial_Z^jP_{r,s})(z,\bar z),
\]

which is an integer element of A_D when p is inert; the original source Frobenius-jet divisibility is already kernel-checked in InertFrobenius.lean/FrobeniusJet.lean.

## The eventual-row periodicity theorem

Let J be any positive ordinary derivative count, 0<=j<J, and define L=p(p²-1). For each fixed s, set T_s=p(S-1-s)+J. Then, for every r>=T_s and every integer source observation z,

\[
\boxed{F_{r+L,s,j}(z)\equiv F_{r,s,j}(z)\pmod p.}
\]

This is a paper derivation, **not a newly checked Lean theorem**.

**Proof.** For r>=T_s, the exponent k has saturated to k=S-1-s. Let a=r-pk, hence a>=J. Set h=Z^p-W. Every ordinary derivative h^(t)(z,bar z) is divisible by p in A_D: at t=0 this follows from inert Frobenius, at 1<=t<=p from (p)_t divisible by p, and at t>p it vanishes. The generalized ordinary Leibniz rule therefore makes

H_(k,l)(z) = p^(-k)*partial_Z^l(h^k)(z,bar z)

an *integral* source term independent of r after saturation. Expanding derivatives of Z^a W^s h^k gives

\[
F_{r,s,j}(z)=
\sum_{t=0}^{j}
\binom jt (a)_{\underline t}
z^{a-t}\bar z^{s}H_{k,j-t}(z),
\]

where a>=J means every exponent a-t>=1 for the allowed t<=j<J. Under r->r+L, k and all H factors are unchanged. Falling factorial coefficients (a+L)_{\underline t} agree with (a)_{\underline t} modulo p because p divides L. In the source residue field F_(p²), every nonzero z satisfies z^(p²-1)=1; therefore z^L=1. At z=0 both positive powers vanish. Hence the entire sum is unchanged modulo p. QED.

The argument is faithful to **ordinary** derivatives, not a Hasse-derivative replacement; no factorial has been dropped. It holds for any source Q, not merely the observed ellipse, provided the inert residue-field condition and the original normalization are met.

## Finite row-rank consequence and explicit scope

At each fixed s, all r>=T_s+L repeat an earlier row r-L>=T_s. Consequently the source-normalized evaluation matrix modulo p has row rank at most

\[
\sum_{s=0}^{S-1}\min\left(R,\ p(S-1-s)+J+p(p^2-1)\right).
\]

For the **same original D403/p3**, R100, S=J4, L=24, these four s-specific row budgets are 37,34,31,28, totaling **130**. This is a paper rank ceiling valid for every source observation support, sharper than the Phase387 crude occupied-column rank ceiling 216. The independent full original-class-compressed finite calculation [d403_compressed_rank.py](d403_compressed_rank.py) measures an even smaller **rank90**, so the periodicity inequality is **not** an exact rank theorem.

Under the existing nonsingularity/Smith premises, the row-rank ceiling alone gives at least 400-130=270 first-layer source evaluation index units (and at least 540 Gram valuation units after the original 2F3), as opposed to the class-count floor 184. This remains strictly inside the historical Phase281 >=840 evaluation index, so **no new additive valuation** is introduced. At production S=R//25 huge, this row-period bound is much weaker than Phase386's column-class compression and does not improve the 322^4 cutoff.

## Exact controls and negative cases

The standalone [periodic_source_rows.py](periodic_source_rows.py) checked 20,412 original source-jet comparisons each for D=19,43,283,403,412 at p3, S=J4, r>=13 and r+24. It also tested the p5 inert D3 case with period L=120. Three explicit counterexamples kill shorter shift candidates 8,12,16 in the D403 source:

- L=8, r13,s0,z=(0,1): normalized j1 differs modulo3;
- L=12, r13,s0,z=(1,1): j0 differs modulo3;
- L=16, r13,s0,z=(0,1): j1 differs modulo3.

The compressed-rank script separately checks that all 400 original source rows give rank90 and the derivative-channel ranks grow 27,54,81,90. Full source direct integer-pair ordinary jet checks and a residue-class permutation are controls against representation drift. All local checks passed; GitHub exact-head verification is tracked separately.

## Evidence and next bounded proof

- **P (paper, conditional):** eventual normalized-row periodicity and explicit row-rank ceiling under original inert source Frobenius and integer ordinary differentiation.
- **M:** cross-D modulo-p tests and rank90 matched historical source measurement with two elimination directions.
- **H:** exact source-typed Lean proof of periodicity; an algebraic explanation (rather than Gaussian elimination) of the observed gap 130 versus 90; an explicit correspondence, if any, between the nine additional j3 ranks and Phase284's nine Frobenius-overlapping Bockstein witnesses.
- **R:** assuming smaller periods 8,12,16; equating a matching dimension of nine with equality of the underlying subspaces; adding these rank-index units to the already counted Phase281 evaluation index.

**Stop rule:** the next proposed equality of nine-dimensional spaces must come with a source-matched map and a negative control, or remain an unproved observation. Do not infer new field bounds or transfer a finite modulo3 row-period result to general Selberg/Hecke zeta.
