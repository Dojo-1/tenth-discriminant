# Phase387.1 — Closed-form occupied-class certificate from the original thin ellipse

**22 November 2026. Elementary exact integer geometry; additive to Phase387, no new discriminant cutoff.**

Use the SAME original source ellipsoid

  Q = {(x,y) in Z^2 : x^2 + D*y^2 <= rho^2}

at D=322^4+15=10,750,371,871, rho=14,689,950, R=D//4, J=S=R//25.

By integer-square inequalities (no floating point), the vertical half-width is

  Y = floor(sqrt(rho^2/D)) = 141.

For any -Y<=y<=Y, the available source x coordinates form the COMPLETE integer interval

  [-L_y,L_y],  L_y=floor(sqrt(rho^2-D*y^2)).

The minimum interval width occurs at |y|=Y, and exact integer squares give

  L_min = L_141 = 1,437,528,   2*L_min+1 = 2,875,057.

Let q=p^(m+1)=3^(m+1). If q <= 2,875,057, every x interval meets EVERY residue class modulo q, because the interval contains at least q consecutive integers. In this regime the occupied pair-residue count is therefore EXACTLY

  C_m = q * min(q,2*Y+1) = q * min(q,283).

Proof: y in [-141,141] realizes exactly min(q,283) distinct y residues, and for each realized y residue the x interval realizes every x residue modulo q. When q<=283, all q^2 pairs occur; when 283<q<=2,875,057, the y residues are distinct and all 283*q pairs occur. No 6.5-billion-point enumeration is used.

The q values at m=1,...,12 are <=3^13=1,594,323, so ALL TWELVE levels admit the closed formula. At m=13, q=3^14=4,782,969>2,875,057 and the formula no longer applies; the exact 283-slice sum gives C_13=1,349,220,519 and the elementary rank bound contributes zero at that depth.

Thus without any modular histogram loops, the exact 12-depth class sum is

  sum_(m=1)^12 C_m
    = sum_(m=1)^4 3^(2(m+1))
      + 283*sum_(m=5)^12 3^(m+1)
    = 66,420 + 676,686,960
    = 676,753,380.

With n=R*S=288,926,236,423,151,306 and J=S=107,503,718,

  12*n - 2*J*676,753,380 = 3,321,607,828,039,681,992.

The Phase387 conditional p-adic Smith/Gram theorem therefore supplies the additional p3 lower valuation

  2*(12*n-2*J*676,753,380)
    = 6,643,215,656,079,363,984

beyond the original Frobenius 2F(3) factor. This closed arithmetic witness is independently checked by research/phase387/occupied_depths.py and local integer-square calculations, but NOT a Lean-kernel proof of the Smith lemma, a full production determinant, or a new class-number-one discriminant bound.

**Falsification:** if the actual original thinRadius, the source ellipse equation, the held-W ordinary derivative, or the source classes differ, this count no longer certifies the same Gram. A p-adic histogram with zero weights can improve the GRAM rank, but not reduce the EVALUATION module's occupied-column generator count; do not substitute the 59 mod3-active weights for these occupied classes.

**Evidence:** P (elementary paper proof under exact source geometry); M (integer arithmetic); H (source-type Lean integration and non-overlap with Phase278-284); R (any interpretation as a new unconditional field cutoff).
