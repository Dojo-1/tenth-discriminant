# Phase312 — post-Phase311, pre-code: Fermat-quotient moment Worldlets and class-one specificity

Date: 2026-11-13. Stacked on Phase311 PR #203 head aa0907017b488b37a111a725e833edc3ca2b8324. This protocol predates Phase312 code. No Work mode, no main merge, no modification to original 322^4 bound. Respect [P]/[A]/[M]/[H]/[S]/[R].

## Question

Do class-number-one constraints on hypothetical large imaginary quadratic fields force residue-multiplicity or higher-lift moment congruences that contribute *genuinely new* valuation to the SAME ORIGINAL trace Gram beyond existing valuationWeight? This is a local mechanism and countercontrol, NOT proof of that uniform claim.

## Arithmetic and known prior art

Let O_D=Z[omega], omega^2=omega-m, m=(D+1)/4 and p=5 inert. Set epsilon_D(z)=(z^5-conjugate(z))/5 mod5 in O/5O=F25. Integral because conjugation is Frobenius modulo5; multiplication law epsilon(xy)=epsilon(x)conj(y)+conj(x)epsilon(y) mod5. The additive rule has cross terms: epsilon is NOT an additive derivation. This is known p-derivation/unramified Frobenius-lift mathematics, not claimed novel. Eta(z)=(z^25-z)/5 mod5=conjugate(epsilon(z)); all verified in exact ring arithmetic modulo25.

## Predeclared full-original D203 source reconstruction

Freeze original Phase304 D203 Q263 rho24 R50/S=J2 100-row source and EXACT Phase307 50 integer row shears and 50 /5 primitive source. Fix z∈Q, W=conj(z), ordinary Z-jets j0/j1 holding W FIXED.

For 45 Frobenius-difference rows r=5..49:
  F_r=(Z^r-Z^(r-5)W)/5,
  j0=z^(r-5)*epsilon(z),
  j1=z^(r-1)+(r-5)z^(r-6)*epsilon(z).
At r=5 the second term is zero without using a negative exponent.

For five Hermite rows a=0..4:
  K_a=(Z^(45+a)W-2Z^(26+a)+Z^(2+a))/5,
  j0=-z^(45+a)*epsilon(z),
  j1=-z^(49+a)-a*z^(44+a)*epsilon(z)-2*z^a*conj(epsilon(z)).

The remaining 50 rows are the original polynomials. Therefore each primitive value/j1 coordinate is affine-linear in u(z)=(1,epsilon(z),conj(epsilon(z)))∈F25^3. Reconstruct ALL 100×1052 primitive omega coordinates mod5 from local residue, epsilon and source-row labels; compare EVERY coordinate against independent frozen Phase307 original modulo25 /5.

## Corrected moment-data requirement

For each residue zbar retain full 3×3 Hermitian moment M_zbar=sum_{q in Q,qbar=zbar}u(q)conj(u(q))^T. Sufficient statistics include n, sum epsilon, sum conj(epsilon), sum epsilon², sum conj(epsilon)², sum epsilon*conj(epsilon). Earlier suggestion of only n, sum epsilon and sum epsilon*conj(epsilon) was INCOMPLETE for general affine primitive rows; epsilon² also matters.

Let C_j(zbar) be the original-row 100×3 coefficient matrix for ordinary jet j. Then G_primitive mod5 equals Tr_F25/F5 of sum_zbar,j C_j M_zbar conj(C_j)^T. Compare all 10000 primitive trace Gram cells to independent original oracle and known Phase311 primitive rank63. An actual source lift separation: 1 and6 both in D203 Q263, same residue1, but epsilon(1)=0, epsilon(6)=4, and F5 j0 differs.

## Class-number specificity and moving-frame controls

Use D43 (h1), D163 (h1), D183 (h8 by complete classical reduced-form enumeration). All are squarefree, 3mod4, inert at p5, and m=11/41/46 congruent mod5. Use a deliberately MATCHED rho21 for all three (not their native field theorem). Compare original residue counts, epsilon moments, original R40/S=J1 first-level Gram, without preregistered directional effect. D183 non-h1 also has a ramified norm3 ideal that cannot be principal since m46>3 and3 non-square.

Same residue ring modulo5 does NOT authorize naive identification modulo25 when m differs. Construct corrected Hensel isomorphism phi: O_D/25→O_E/25,
 phi(omega_D)=omega_E+5*t,
 t=((m_E-m_D)/5)*(2omega_E-1)^(-1) mod5.
Verify source relation, involution, multiplicativity on a finite independent grid, epsilon covariance. Only compare transported higher-lift data with this declared ring map. This is a genuine check against mistaking coordinate artifacts for class-one signals.

## Ray-class branch

For h1, D>3, p5 inert, classical ray exact sequence yields |Cl_(5)|=24/2=12 and |Cl_(25)|=600/2=300. With D183 h8, sizes96/2400. Implement finite local unit counts and complete reduced forms, treating the global ray formula as an imported classical theorem—not something proved by counting local units. Bounded norm-ball sums are not forced to vanish by these cardinalities.

## Global bridge and stop rules

Current Lean theorem rectangularTraceGram_valuation_of_classNumber_one applies to the SAME original integer-order Gram and existing valuationWeight. There is still no theorem transporting new maximal-order moments to a uniform class-one determinant improvement. Any new inequality requires source identity, independent index contributions and non-overlapping valuation counts.

Fail if any original D203 primitive entry, j1 derivative, moment Gram, moment conjugation symmetry, corrected ring transport or epsilon covariance fails. Keep draft and original 322^4 bound. Claim statuses: [P-paper] conditional algebraic formulas; [M after CI] fixed finite tests; [H] global class-one moment inequality; [R] local ring fingerprints alone detect h1 or unproven additive valuations.
