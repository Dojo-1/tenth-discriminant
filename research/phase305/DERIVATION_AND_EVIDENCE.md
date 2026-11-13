# Phase305 — Frobenius–Hermite source kernel (2026-11-13)

**Status:** AI-derived paper argument + exact bounded local computations, **not yet Lean-checked or independently reviewed**. Stacked draft on Phase304 #196; no merge and **no new field bound**. The source policy remains `params(D)` in `research/phase206/source_probe.py`.

## Precise local theorem [P-paper, proof to formalize]

Let p be a prime inert in an imaginary quadratic maximal order, so its residue field is F_(p^2). Let 1 <= J <= p, and define the F_p-linear source jet map on F_p[Z,W] by evaluating the ordinary Z-derivatives of orders j=0,...,J-1 at (z,z^p) for **all** z in F_(p^2), with W held fixed. Its kernel is

    I_(p,J) = (Z^p-W, (Z^(p^2)-Z)^J).

**Proof:** The first generator and all its ordinary Z-derivatives vanish under this evaluation in characteristic p because the derivative of Z^p is zero. Modulo this generator, substitute W=Z^p and get a polynomial f(Z). Since J<=p, derivatives commute with this substitution, including all the first J ordinary jets. Their vanishing at every point is exactly the condition that every root of Z^(p^2)-Z has multiplicity at least J; the polynomial has distinct roots, hence divisibility by its J-th power. The converse is immediate. For J>p ordinary j-th derivatives of order >=p vanish identically in characteristic p, so **replace J with min(J,p)** for the mod-p kernel statement; do NOT mistake these ordinary derivatives for Hasse derivatives.

For the original rectangular source of monomials Z^r W^s, 0<=r<R, 0<=s<S, define

    h_p(R,S,J) = R*S - dim_Fp span { Z^(r+p*s) mod (Z^(p^2)-Z)^j0 },
    j0=min(J,p).

When the source is evaluated at any subset of actual integral observations and the full original (non-normalized) integral trace Gram G is nonsingular, the kernel modulo p yields an integer unimodular source-row transformation U having h_p rows divisible by p. Consequently

    v_p(det G) >= 2*h_p(R,S,J)

**independent of class-number-one** after assuming p inert. This uses the unchanged integer source Gram and its trace form, not an added determinant or a changed jet policy. A GL_n(F_p) change of basis of source rows can be lifted to GL_n(Z) using elementary matrices (plus unit scaling chosen with +/-1 as necessary); at minimum the p-adic valuation identity holds with a Z_(p)-invertible row transform, which is enough for the inequality. The scalar rank bound is **only the first level** of the p-adic filtration.

## Exact small-source controls [M]

Calculated using the independent pure-Python modular polynomial-remainder rank script in this folder:

| D original params | p | rank of truncated source image | h_p | existing valuationWeight | h_p - valuationWeight |
|---|---:|---:|---:|---:|---:|
| 163: R40 S1 J1 | 5 | 25 | 15 | 0 | +15 |
| 203: R50 S2 J2 | 5 | 50 | 50 | 45 | +5 |
| 283: R70 S2 J2 | 3 | 18 | 122 | 67 | +55 |
| 283: R70 S2 J2 | 5 | 50 | 90 | 65 | +25 |
| 403: R100 S4 J4 | 5 | 100 | 300 | 550 | -250 |

For D203 and p5 there is also a separate observed 263-point maximal-order replay (run locally in the continuation, not yet a hosted CI claim): fifty unimodularly triangular source rows, divided by 5, give primitive evaluation rank 100, primitive Gram rank 63, and Gram Smith histogram {0:63,1:36,2:1}. Thus v5(det original G)=2*50+38=138, matching Phase304's original determinant. Phase304's prior 45-row primitive Gram had evaluation kernel dimension five; that particular kernel disappears on further saturation, while the restricted trace radical remains dimension 37. The observations are not an independent class-number calculation.

## Five additional D203 row relations [P-polynomial, M-replayed]

Phase304 used 45 rows (Z^5-W)Z^(r-5), 5<=r<50. Add for a=0,...,4

    K_a(Z,W) = Z^(45+a)*W - 2*Z^(26+a) + Z^(2+a).

On W=Z^5 this becomes Z^a*(Z^25-Z)^2, and its first ordinary Z derivative also vanishes at all z in F25. The K_a leading source rows are odd s=1 at r45,...,49; the original 45 leading source rows are even s=0 at r5,...,49. The elementary operations can be ordered without modifying any of their source rows, so the resulting U has determinant 1. Every one of the 50 selected source evaluation rows is divisible by 5 in BOTH integral coordinate channels and at BOTH original ordinary jets.

## Critical comparison with existing field bound

The previously proved source theorem uses

    valuationWeight(R,S,p) = sum_(r<R) sum_(t<S) min(floor(r/p),t).

Our first-level kernel bound and that higher-divisibility bound **overlap**. The valid immediate lower bound is v_p(det G) >= 2*max(h_p, valuationWeight), NOT the sum 2*(h_p+valuationWeight). At large J, the new first-level bound can be strictly weaker. A useful improvement of the original 322^4 field statement would require a uniform compatible improvement at ALL actual source parameters, an arithmetic-to-analytic same-Gram bridge, and independent semantic review. None is established here. No claim of novelty relative to prior Frobenius methods.

## Next theorem targets

1. Formalize F_p polynomial jet-kernel equality, including the J<=p boundary and the degeneration for ordinary derivatives j>=p.
2. Formalize a full-rank mod-p lattice lift and the index-square determinant identity without presuming a particular arbitrary flag.
3. Build a multilevel p-adic filtration of the same original source, and compare it against valuationWeight without double counting.
4. Check original source and original analytic upper in the large-D regime; use matched non-h1 fields as hostile controls.

**Corrections:** The earlier CI at PR196 head 0c56b41d failed in two `ZMod 5` characteristic goals, not in the class-number theorem. An explicit characteristic-five fix was committed to PR196 as `96d3ee0a`. It must compile before promotion to [P-Lean].
