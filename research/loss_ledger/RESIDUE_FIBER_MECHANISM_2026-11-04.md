# Post-observation mathematical reconstruction: a residue-balanced horizontal-fiber kernel

Date: 2026-11-04. **Proven elementary modular argument** for a *specific* original-source finite Gram; the explanation was discovered *after* the T3/source-kernel CI witness, so is not retrospectively counted as preregistered. Evidence P (hand argument under explicit D=19, p=3, supports), M (exact Python/CI), not a new uniform tenth-discriminant theorem.

## Source and witness

Fix D=19, characteristic p=3, R=4, S=J=3 and the repository's original integer-pair ordinary-Z-jet Gram G(Q) (the conjugate W is held fixed before Z differentiation). Its row order is (r,s) in row-major enumeration, 0<=r<4 and 0<=s<3. The 12-dimensional vector

    v = 2 e_(0,1) + e_(3,2)

has zero coefficients except index 1 = 2 and index 11 = 1, in the specified row-major order.

Its row polynomial is f(Z,W)=Z^3 W^2 + 2 W. Over F_9 = F_3[s]/(s^2+19), the quadratic is irreducible because -19 = 2 mod 3 is nonsquare. With Z=x+ys and W=x-ys, Frobenius yields Z^3=W and W^3=Z, so

    f(Z,W) = W^3-W = Z-W = 2ys (mod 3).

The positive ordinary Z derivatives satisfy d_Z f=3 Z^2 W^2=0 and d_Z^2 f=6 Z W^2=0 modulo 3. For y=0, also f=0.

At rho=6, Q_6={(x,y)∈Z² : x²+19y²<=36} has 13 real-axis points y=0, x=-6,...,6, and 9 points *each* in y=1 and y=-1: x=-4,...,4. For each fixed y=+/-1, every residue x mod 3 occurs exactly three times. For any original row (r,s), its j=0 jet is polynomial in x,y with integral coefficients, and so the reduced trace pairing with f depends only on x mod3. Each such sum is 0 mod3 because all three residue values repeat three times. For j=1,2, the v-jet is 0 mod3, and the y=0 layer gives 0 for j=0. Therefore

    G(Q_6) v = 0 in (F_3)^12

for the full exact original trace Gram, without invoking a surrogate matrix. This is an explicit *extra* modular relation beyond the generic Frobenius row-exponent two-direction nullity: the same v is not null at Q_5 (and Q_5 has rank 10, Q_6 rank 9).

## An exact row coordinate detects failure away from balance

At the row (0,1), whose zero-order jet is W, the reduced trace pairing between the f-jet (2ys) and W=(x,-y) is

    B_19((0,2y),(x,-y)) = -4*19*y^2.

At rho=5 the non-real layers have 5 points each, so sum y^2=10; at rho=6 nine each =>18; at rho=7 eleven each =>22. Thus the (0,1) component of G(Q_rho)*v modulo3 equals

    rho=5: (-76*10) mod3 =2;
    rho=6: (-76*18) mod3 =0;
    rho=7: (-76*22) mod3 =2.

This yields a **hostile control**: even though Q_5 subset Q_6 subset Q_7, the modular kernel witness appears at radius6 and is absent at 5 and 7. The positive-semidefinite real Gram order does not imply a monotone modular kernel space.

## Limit of inference

An extra null direction modulo p does **not** alone establish an *additional* p-adic determinant factor beyond an existing two-sided diagonal factorization. An invertible residual K may have a singular principal subblock. To claim an improved determinant valuation one must inspect appropriate Smith determinantal divisors or det K modulo p^m, and then give a same-Q real-geometric bound. For rho=6 the earlier exact finite determinant test reports v3(det G)=8, whereas the generic rectangular source factor gives at least4; these are **finite experimental facts**, not uniform extra factors.

This mechanism suggests testing residue-balanced fibers at larger supports, but no fixed Qthin(D) uniform condition has been established. Nothing here changes the 322^4 theorem, identifies our Gram with Lorscheid's tropicalized scheme, or establishes new math literature priority.
