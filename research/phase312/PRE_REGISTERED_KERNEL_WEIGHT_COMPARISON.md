# Phase312-D — post-C, pre-code: universal inert full-residue jet kernel versus existing valuationWeight

2026-11-13. Hypothesis specified AFTER Phase312-A Fermat moments passed CI, B local Hensel isomorphism passed in a previous run, and C global norm-shell code was introduced. This is BEFORE D comparator implementation. Scope is rank of the FULL F25 residue-jet evaluation of the SAME original rectangular polynomial labels; it is not a new uniform field theorem or analytic cutoff.

## Algebraic theorem target [P-paper, elementary]

At inert p5, O/pO=F25, W=bar(Z)=Z^5 at every residue point, and the ordinary Z derivatives (W held fixed) of any polynomial of order >=5 vanish over F5. Let j_eff=min(J,5), J>=1. The full residue-jet kernel is the restriction of the ideal

    I = (Z^5-W, (Z^25-Z)^j_eff) ⊂ F5[Z,W]

to the rectangular span {Z^r W^s:0<=r<R,0<=s<S}. The quotient is isomorphic to F5[Z]/((Z^25-Z)^j_eff), of dimension 25*j_eff. The equivalence of jet vanishing with root multiplicity holds because j_eff<=5 and all factorials j! for j<5 are invertible.

If R>=25*j_eff and S>=1, the s=0 monomials Z^0..Z^(25*j_eff-1) already span the entire quotient, hence

    rank_F5,full_jet(E)=25*j_eff,
    h=kernel_dimension=R*S-25*j_eff.

Unimodular lifting of the modular kernel basis (explicit pivot remainder on these 25*j_eff basis rows) gives a SAME-original-source first-level divisibility p^(2h) of its integer trace Gram under inertness, provided the ring-coefficient and ordinary-jet semantic bridge is established. It is a LOWER bound, not automatically additive to previous weights or trace radicals.

## Explicit old weight comparator, native regime

With the repository native integer parameters R=floor(D/4), S=J=floor(R/25), S>=1, we have R>=25S, and the existing weight formula evaluates exactly (since R>=5(S-1)) to

    w5(R,S) = S*(S-1)*(3R-5*(S+1))/6.

The full-residue first-level kernel h=RS-25*min(S,5). Expected comparisons:

- S=1, 25<=R<=49: w=0, h=R-25 (h positive except R25).
- S=2, 50<=R<=74: w=R-5, h=2R-50, so h>w by R-45.
- S>=3 and R>=25S: w>=h, hence this FIRST-LEVEL rank argument cannot exceed the existing weight formula in the hypothetical large-field regime.

This comparison is of actual formula exponents and a proposed SAME-ORIGINAL source transport. It is NOT a proof that a higher primitive 5-adic trace defect adds independently to w, nor a cutoff improvement.

## Bounded controls

- Compute exact quotient remainders modulo F5 for every original monomial row, then check rank and h for (R,S,J)=(40,1,1), (50,2,2), (75,3,3), (125,5,5), (150,6,6), native R25S.
- Independently evaluate actual full F25 grid ordinary jets at D163 p5 for the first three small arms, and verify the matrix rank equals 25*j_eff without relying only on the combinatorial formula. The 75x3 arm uses 225 rows, 75 complex observation/jet channels and can be checked with the existing GF25 Gaussian rank.
- Verify explicit modular row remainders against every ordinary jet (j=0..J-1) and all 25 residues for the R50,S=J2 arm; not just aggregate numerical rank.
- Hostile boundary: for R<25*j_eff, NEVER assert full-column rank from the formula; for J>5, ordinary jets j>=5 vanish and j_eff clamps to5.
- For S>=3 run exact integer comparisons at native R=25S,25S+1,25S+24, plus large S20,50. NO new uniform h1 theorem without a Lean bridge from the actual original Z[√−D] rows and independent analytic budget; no addition to w.

## Stop rules

If the quotient dimension/rank or explicit modular relation fails, retire the claimed universal kernel. If h>w only for low S, do not imply improvement at the 322^4 cutoff. If higher-lift moment data differ between h1/nonh1 fields, do not infer h1-specificity without an independent global theorem.


## Post-D precode addendum — E: EXACT original integer-order D163 bridge

This addendum is recorded AFTER Phase312-D's finite-field ranks and native kernel-vs-weight comparisons passed hosted CI and BEFORE E code. It changes no earlier predictions.

Freeze D163, p5 inert, NATIVE Phase206 rho21/R40/S=J1, original actual INTEGER coordinates Q={(x,y)∈Z²:x²+163y²≤441}, expected Q109. The original ring is Z[√-163], NOT the full omega maximal order. Its multiplication and original trace are (ac-163bd, ad+bc), Tr(x conj(y))=2(ac+163bd), exactly as in Lean/TenthDiscriminant/IntegerTraceGram. The 40 rows are 1,Z,...,Z^39, ordinary jet j0.

For each r25..39, the integer-unimodular row shear T_r=Z^r-Z^(r-24) is divisible by5 at EVERY original point, since z^25=z in the unramified quadratic residue ring. There are exactly15 such divided rows. Prediction: verify all original integer-order E40×(2Q) entries mod625 and all 40×40 same-original Gram cells U G U^T=D5 Gprim D5 mod125, giving the **local** bound v5(det original G)>=2·15=30. Gram nonvanishing follows from 43 distinct rational points (y=0) supporting a Vandermonde matrix rank40. Old valuationWeight(40,1,5)=0.

This is a SAME ORIGINAL integer-order small-S index-square improvement but not a uniform cutoff result (large native S>=3 old weight dominates the first-level kernel). Kill if source policy, integer ring coordinates, exact /5, 1600 Gram covariance cells, or 43-point nonvanishing condition fails. No additive old-weight claim or exact v5 valuation.
