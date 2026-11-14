# Phase288-B: preregister the weighted full-order remainder before code

12 November 2026. This is a separately preregistered extension AFTER Phase288 corrected focused CI #43238897531 succeeded. Original D283 and D403 integer-order evaluation/Gram are immutable. Phase287 weighted maximal-order angular response is NOT equivalent to the original unweighted Gram source. No independent human review or novel theorem claim.

## Domains and frozen predictions

K=Q(u), u^2=-D, D in {283,403}, D=3 mod4. The original source is Q_D in Z[u], with D283 (rho31,R70,S=J2,Q169) or D403 (rho40,R100,S=J4,Q219), ordinary Z-jets holding W fixed, trace metric (2,2D). The full maximal order O_K is the DISJOINT union of Z[u] and (1+u)/2 + Z[u]. Inside the SAME rho disk, the frozen expected counts of the missing half-coset are 192 (D283) and 260 (D403). An element (a+b u)/2 has integer norm (a^2+D b^2)/4 but real part of its square (a^2-D b^2)/4 can be a HALF-INTEGER; its field trace (a^2-D b^2)/2 is always an integer. Falsify any claim that the half-coset real component itself is always integral.

At t=ln2 let T_rho=sum over the full two-coset disk of Re(z^2)*2^(-N(z)). The original unchanged integer Gram has g=G_(1,Z^2)=2*T_Q for T_Q=sum over ORIGINAL Q_D of Re(z^2). Define the exact integer numerator

  A_rho=2^(rho^2) * sum over full two-coset disk Tr(z^2)*2^(-N(z)),
  R_rho=A_rho-2^(rho^2)*g.

Every summand in A_rho is integral because N(z)<=rho^2 and Tr(z^2) integer. Inversion pairs prove A_rho and R_rho are even; the origin contributes trace 0. Exact predicted bridge:

  T_rho=g/2 + R_rho/2^(rho^2+1).

R_rho explicitly includes (i) the Gaussian-weight change on original Q and (ii) the MISSING finite half-coset. Neither is the infinite outer tail. The finite full-order 4D coupled angular curvature difference at the two quadrant orientations is exactly T_rho^2, and need NOT equal original T_Q^2.

## Integral source-compatible external register

Keep Phase288's X=E B V with 4 original integer Noether-graded channels. The origin q0=(0,0) is the unique inversion-fixed original point. Define a FIFTH even integral observation covector V_R supported only on the original j0 REAL channel at q0 with coefficient R_rho/2. Its original-source pushforward X_R=E B V_R has entry R_rho at the constant row and zero at every other monomial row (all have positive total degree). Thus X_plus=(X,X_R) is an integral n x 5 C2-equivariant readout, even/odd grading (+,+,-,-,+). The integral I5 Schur completion is congruent to diag(G,I5), so G and ALL p-adic Smith exponents are unchanged (plus five unit factors). This fifth channel is openly an EXTERNAL Gaussian/coset data register. It is not an intrinsic arithmetic invariant learned from G and cannot generate new determinant mass.

## Certified infinite tail and frozen test

At t=ln2 and angular degree two the full two-coset Gaussian tail is bounded by the rational B_rho=8*(rho+2)^4*2^(-rho^2)/(1-q), where q=((rho+3)/(rho+2))^4*2^(-(2*rho+1))<1. For infinite weighted T_infty=T_rho+e, |e|<=B_rho and the squared-gap error is at most 2*|T_rho|*B_rho+B_rho^2. Frozen strict thresholds: B_31<2^(-930) and B_40<2^(-1560).

The exact standard-library Fraction program must: independently enumerate the original and half cosets; verify all original helper blob IDs and D283/D403 params; compare the original G_(1,Z^2) to T_Q; verify weighted angular contraction by BOTH direct O(rho)^2 pair enumeration and moment contraction; prove the exact R_rho identity and evenness; construct V_R and five-channel source parity; verify integral congruence and determinant on the SAME original 8-/16-row principal Grams; reject a wrong REAL-part-is-integral half-coset control; verify rational Gaussian tail inequalities; and explicitly reject new valuation claims. Keep the source and normalization fixed if a test fails.

Status: [P-paper] elementary exact algebra and conditional error estimate; [M only after passing CI] finite two-coset angular tests; [H] a new useful original-Gram analytic inequality beyond already-known pair correlation; [R] any inferred new local arithmetic divisibility. Preserve original Phase288 failed-run history and the PR157/#50 human review gates. Keep PR179 draft pending focused, Markdown and root Lean checks.
