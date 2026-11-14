# Phase312-B — post-A, pre-code local 5-adic no-go / global remainder

Date: 2026-11-13. Written AFTER focused Phase312-A CI passed at PR #204 (run 43502932992) and the narrow Phase312 Lean polynomial check passed. BEFORE Phase312-B source/test implementation.

## Theorem target, classical unramified local algebra [P-paper]

For fundamental imaginary quadratic D,E with 5 inert, the completed maximal orders O_D⊗Z5 and O_E⊗Z5 are isomorphic as unramified quadratic Z5-algebras. Fix the specific residue chart omega_D→omega_E modulo5 when m_D≡m_E modulo5, m_D=(D+1)/4, m_E=(E+1)/4. Hensel's simple-root lemma lifts this chart uniquely to every ring modulo5^k in a compatible system, preserving complex conjugation (the unique nontrivial Z5-Galois automorphism).

The local rings, involution, Frobenius lift, and all purely internal local-ring invariants are thus indistinguishable, even though D163 has h1 and D183 has h8 (independent classical reduced-form control and a ramified norm3 obstruction). This is NOT a statement that norm balls Q_D(rho) and Q_E(rho) are isomorphic, nor that their ray class groups or their global class numbers agree.

## Explicit compatible lift (before implementation)

Given x_j in O_E modulo5^j satisfying f_D(x_j)=x_j²-x_j+m_D ≡0 mod5^j, begin x_1=omega_E modulo5. Let

   a_j = (f_D(x_j)/5^j) mod5,
   t_j = -(2*x_j-1)^(-1) * a_j mod5,
   x_(j+1) = x_j + 5^j t_j mod5^(j+1).

Here the division by5^j is valid coordinatewise because f_D(x_j) is in 5^j O_E. Verify exact source/target ring multiplication, compositional inverses, conjugation and coherence to fixed depth k<=6.

## Frozen tests

- D163 ↔ D183, and D43 ↔ D163, D43 ↔ D183. At k=1..6, every lift must satisfy target f_D(x_k)=0 mod5^k; its reduction mod5 is omega_E; and compatibility x_(k+1) mod5^k = x_k.
- For each level, homomorphism phi_k(a+b omega_D)=a+b*x_k: verify multiplication/conjugation on a bounded declared sample grid (negative entries included). Compose phi and reverse psi modulo5^k and demand identity for both generators 1,omega.
- The first two digits must match Phase312-A's checked mod25 correction t=(m_E-m_D)/5*(2omega_E-1)^(-1). Hence original epsilon covariance is a direct necessary consequence at level25.
- Do not infer class number from all equal local algebra data; for D183, ramified norm3 obstruction certifies non-h1 while D163 h1 is taken from independent reduced-form enumeration and classical form-class theorem.
- Source norm-ball matching remains a separate global restriction; same-local-ring does NOT imply the same Q, moment census, ray classes, or original 100-row Gram.

## Stop

If any lift fails a relation, compatibility, automorphism, inverse or separate mod25 expected value, retire the claimed implementation; do not misclassify it as a new uniform field-bound theorem. Full-root Lean proof of all Hensel statements is NOT included in the existing narrow polynomial identity.
