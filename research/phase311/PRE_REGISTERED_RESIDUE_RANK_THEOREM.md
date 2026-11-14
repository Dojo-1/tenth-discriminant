# Phase311-D — post-C exact support-rank theorem and uniform-field negative control

2026-11-13. This theorem target is formulated AFTER Phase311-C hosted CI observed exact source-rank and residue-multiplicity results (D163/187/203/427), and BEFORE its source-code assertion/hostile test. The observed table is NOT backdated to the initial preregistration.

## Theorem [P-paper, standard linear algebra]

For p=5 inert, let V=F25^(J*25) be the full ORIGINAL ordinary-jet evaluation space at all 25 residue classes, with J<=p. Let C:F25^(n source coefficients) -> V be surjective, represented by an n x (25J) matrix of full column rank. Let W be diagonal with each observation multiplicity m_z mod5 repeated J times. Pulling back the diagonal Hermitian form gives H=C W bar(C)^T, hence

   rank_F25(H)=rank_F25(W)=J*#{z:m_z not 0 mod5}.

For a conjugation-invariant actual original norm-ball Q and integer-coefficient original polynomials, H is Frobenius-fixed, hence has entries in F5 and the unchanged original trace Gram is G=2H. Therefore

   rank_F5(G)=J*#{z:m_z not 0 mod5}.

Surjectivity C is ESSENTIAL. If rank C<25J, only the <= inequality is warranted. At J>=p ordinary derivatives j>=p vanish; replace J by J_eff=min(J,p) and require surjectivity only on the active original-jet space.

## Preregistered executable controls

- D163/J1: rank(C)=25, nonzero weighted classes25, rank(G)=25.
- D187/J1: same, even though non-h1.
- D203/J2: rank(C)=50, weighted classes19, rank(G)=38.
- D427/J4: rank(C)=100, weighted classes17, rank(G)=68.
- A synthetic *non-surjective* 1-row, 2-residue F25 matrix C=[1,1] with weights [1,4] has rank(C)=1<2, yet pulled-back Gram entry equals 2*(1+4)=0 mod5. This MUST NOT be asserted to have rank2. The strict inequality is a hostile control.
- D427 R=106,S=4,p=5 has existing valuationWeight=sum_r sum_t min(floor(r/5),t)=586, hence the existing weight FORMULA evaluates to 2w=1172, exceeding the new first-level Gram-nullity floor n-rank(G)=424-68=356. This is a comparison of formal weight magnitudes, NOT a new proof that the old field-divisibility theorem applies verbatim to the full maximal-order observation lift used for D427. It prevents claiming that the new first-level count automatically improves the prior bound.

Stop if any rank formula fails or the h1/non-h1 distinction is incorrectly promoted. No new analytic cutoff, no main merge, no performance claim.
