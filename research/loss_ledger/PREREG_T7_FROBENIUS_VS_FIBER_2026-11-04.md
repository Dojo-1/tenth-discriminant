# Round201 T7 preregistration — distinguish universal Frobenius rows from residue-fiber extra kernel

Date: 2026-11-04. This is a new post-T6 prediction committed BEFORE T7 execution. It does not revise Round201's original frozen conjectures.

**Original integer source, extended rectangle:** D=19, p=3, R=4, S=J=4. Same original integer ordinary-Z derivatives, W held fixed, trace 2(ac+19bd), Q_rho=ellipsePairs 19 rho. There are 16 rows indexed (r,s), 0<=r<=3, 0<=s<=3, and no change of Gram construction.

By Frobenius z^3=W mod3, the three row vectors

  u_s = e_(3,s) - e_(0,s+1), s=0,1,2

yield zero mod3 jets at *every point* and all derivative orders j>=1. They are linearly independent and provide three universal kernel directions, matching the rectangular exponents with e_(3,s)=1 for s=0,1,2.

The residue-balanced vector from the radius-6 study is

  v = e_(3,2) - e_(0,1)

over F3, with polynomial Z^3 W^2-W. At every non-real node, its reduced j=0 jet is Z-W; its higher ordinary jets vanish mod3. At rho=6, each y=+/-1 horizontal layer has exactly 9 points x=-4,...,4, three copies per residue. Thus **T7a prediction**: G(Q6)v=0 mod3. Algebraically v is independent of {u_0,u_1,u_2}, because v-u_2=e_(0,3)-e_(0,1) and every combination of the u_s has coefficients at row (3,s) equal to its own combination coefficients. Hence **T7b**: rank_mod3(G(Q6))<=16-4=12, sharper than the original exponent-only upper 16-3=13. Note that this strengthens only the finite modular *rank* bound, not a certified determinant valuation lower.

At rho=7, non-real y=+/-1 layers have 11 points each, giving nonzero paired row (0,1) coordinate: **T7c prediction** v not in ker(G(Q7) mod3). The universal u_s remain in the kernels of both supports; no exact Q7 rank is preclaimed.

**T7d:** independently compute and verify G(Q6)v=0 and each G(Qrho)u_s=0, rank via deterministic modular elimination and the declared linear independence of [u0,u1,u2,v]. Check real Gram positive-definiteness using an exact integer determinant or the established source count; a scalar minor or numerical eigenvalue is not a substitute.

**Falsifiers:** failure of any u_s zero-jet relation indicates incorrect W convention; failure of v at rho6 indicates source/residue account wrong; failure of independent rank bound indicates a mistaken linear relation. Positive test does not give a *uniform D* condition for production Q_thin. Keep bound H.

Use same original-source Python grammar but now parametrized; do not materialize the gigantic production Gram.
