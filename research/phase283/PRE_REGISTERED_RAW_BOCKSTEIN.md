# Phase283 — preregistered raw first-Bockstein witness, D403/p3

Registered 12 November 2026 **before** adding or running the Phase283 regression. AI-authored protocol. This is an independent check of the proposed first-lift interpretation, not independent human mathematical review.

## Immutable source

Original D403 integer quadratic source: D=403, rho=40, R=100, S=J=4, all 219 points (x,y) in x^2+403y^2 <= rho^2, original monomials Z^r W^s (0<=r<R, 0<=s<S), **ordinary Z derivatives** for j=0,1,2,3 holding W fixed, two integer-coordinate channels per point. The source map is **raw** T = E_raw^T, not its Frobenius-normalized C0 and not its original weighted trace Gram. Prime p=3 is inert. Preserve helper blobs `research/phase206/source_probe.py` = `3f954b59d9f86b06ad53667c869b5b24f2e6c7f6`, `research/phase204/ordinary_jet_filtration.py` = `dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8`.

## Mathematical proposal [P-paper, not yet independently checked]

For any integer matrix T, beta_1 : ker(T mod p) -> coker(T mod p) sends v (mod p) to [T(v_lift)/p mod p]. This is well-defined because changing the lift by p*w changes the image by (T mod p)*w. Under p-integral invertible input and output gauge transformations, beta_1 is naturally transported. In Smith form, rank(beta_1) equals the multiplicity of elementary divisor exponent exactly 1 (not the total positive-exponent nullity).

The original coefficient vectors f_a(Z,W)=Z^a(Z^3-W), a=0,...,8, all lie within the R=100,S=4 original rectangle. At each original node z=x+yu,w=x-yu, inertness ensures z^3=w (mod 3). Since all *ordinary* derivatives of Z^3-W have integral coefficients divisible by 3, all four ordinary jets of f_a are divisible by 3: f_a belongs to ker(T mod 3).

In the j=3 block, Leibniz gives (ordinary third derivative of f_a)/3 = 2*z^a (mod 3). Meanwhile the j=3 block of T mod3 is zero for **every** original row because an ordinary third derivative is divisible by 3!=6. The nine residue nodes z (x mod3,y mod3) exhaust F_9. Therefore the nine 2*z^a column vectors a=0,...,8 are linearly independent over F3 (degree <9 root bound over F9). Their classes survive in coker(T mod3), establishing **rank(beta_1) >=9** for this raw D403 p3 map.

## Frozen executable conditions and kill controls

1. Check source D403/rho40/R100/SJ4/Q219 and exactly nine residue nodes (x mod3,y mod3); check p3 inert.
2. Use the unchanged original **exact integer** ordinary-jet oracle to calculate f_a jets as jet(D,a+3,0,j,z) - jet(D,a,1,j,z), on ALL 219 original source points and ALL j=0,1,2,3. Every resulting coordinate must be exactly divisible by 3. Do not construct a synthetic normalized matrix.
3. Divide each coordinate by 3, then reduce modulo 3. The j3 block must match independently constructed 2*z^a in the quadratic residue algebra for every point. Its rank must be exactly 9 by two explicitly different modular-rank checks (9 witness vectors, hence lower bound 9 is sharp on that witness subspace).
4. Under an integral unit shear f_1 -> f_1+f_0, witness independence and the complete quotient relation must persist. Lift change f_a -> f_a+3*g must change the quotient **only** by the raw source image of g; the j3 projection must remain unchanged.
5. Toy source diag(1,p,p^2): the first Bockstein has rank exactly 1, to prevent mistaking the first Smith nullity (2) for the exact-first-grade multiplicity (1).
6. Split-prime negative control: D403,p11, sample z=u at y=1. Z^11-W is NOT 11-divisible there. Do not apply an inert Frobenius row quotient to a split source.
7. Hasse/ordinary control: the third Hasse derivative of Z^3 is 1 modulo 3 while the original ordinary third derivative is 6. Replacing ordinary jets with Hasse coefficients changes this problem.
8. Run in a clean pinned Python environment, bounded <=10 minutes, and fail rather than edit any predictions or source conventions after observing results.

## Scope and stop conditions

[M only after passing CI] finite original-source nine-witness calculation; [P-paper] elementary Bockstein proof pending external reconstruction; [H] whether these first-lift classes yield any new uniform mass after complete Frobenius/evaluation/primitive pairing accounting. This test **cannot** add nine valuation units to the existing D403 Frobenius exponent F3=570, or the Phase281 K3 index, or improve 321^4, or exclude Siegel zeroes.

Failure of any divisibility, j3 identity, rank, signed-coordinate, row-shear, lift-change, split, or ordinary-versus-Hasse control invalidates the claimed witness. Do not merge the new branch before exact-head pinned CI and source review. PR #173 raw rank and PR #157/#50 independent semantic theorem gates remain separate.
