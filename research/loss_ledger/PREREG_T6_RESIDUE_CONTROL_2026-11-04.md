# Round201 follow-up T6 preregistration: radius-6-only residue-balanced kernel witness

2026-11-04. This T6 prediction was derived *after* the T3 exact source witness and its structural hand proof, but **before** executing the T6 radius-7 regression. It is deliberately separate from both the original Round201 preregistration and T5 transition preregistration.

Original fixed source: D=19, p=3, J=S=3, R=4; rows (r,s) lexicographically, ordinary Z derivatives with W held fixed; integer pair trace 2(ac+19bd); Q_rho = ellipsePairs D rho.

Frozen witness vector v=(0,2,0,0,0,0,0,0,0,0,0,1) in F_3^12 (row coefficients for 2W + Z^3 W^2).

**Precommitted exact T6 predictions:**
1. For rho=6, G(Q_6)*v = 0 mod3 (already empirically known from T3, not an independent new success).
2. For rho=5, the coordinate indexed by (0,1) of G(Q_5)*v is 2 mod3 (already empirically known).
3. For **rho=7 (new held-out radius)**, that coordinate equals 2 mod3 and hence v is *not* in ker(G(Q_7) mod3). The proof predicts this from x=-5..5 in each nonreal y=±1 layer, eleven points per layer, in contrast to nine for radius6.
4. For rho=5,6,7, the direct integer Gram-product coordinate equals -76*N_rho (not just the mod3 residue), with N_rho=(10,18,22). This is a stronger exact test than the nullspace rank alone, because other coordinate contributions cannot hide errors in the trace pairing.
5. The new test will compute **no new number-field cutoff**. Failure at any predicted coordinate invalidates the claimed specific residue-fiber mechanism, not the existing 322 field theorem.

No alternative Gram, replacement derivative, extra inert primes, or untyped F1 assertions permitted. The possible further hypothesis—that controlled residue-balanced fibers force a useful extra *uniform* p-adic Gram determinant factor—is explicitly NOT established by this finite T6 case.
