# Phase313 — preregistered tame/wild ray transport, norm-shell convolution, and sign-parity Gram

2026-11-14 (Madrid). This document precedes Phase313 code. Stacked on Phase312 PR #204 exact head 40609187c8df8d21f08ed8150ca6d9c138e9bb8a. Parent PRs #203 and #204 passed their focused and whole-root Lean CI, but remain DRAFT research branches pending external review. No main change and no change to 322^4. Evidence lattice: P-paper conditional algebra, M fixed computations after CI, H uniform extra field mass, S typed Worldlet/tendril semantics, R false local/class-one promotions.

## Target A: explicit wild logarithm, not yet a global Gram theorem

For squarefree D>3, D=3 mod4 and prime5 INERT, let O_D=Z[omega], omega^2-omega+m=0, m=(D+1)/4. For any z prime to5 (its residue in F25 is nonzero) define

  epsilon_5(z) = (z^5-conj(z))/5 mod5 ∈ F25;
  delta_5(z) = epsilon_5(z) / conj(z) mod5 ∈ F25.

This division occurs inside the RESIDUE FIELD F25, not inside integers or an arbitrary order with zero divisors. Prove by exact arithmetic and a short ring identity:

  delta_5(xy)=delta_5(x)+delta_5(y);
  delta_5(-x)=delta_5(x);
  delta_5(conj(x))=conj(delta_5(x));
  delta_5(1+5u) = -conj(u) mod5.

As a consequence, [z]↦([z mod5]/±, delta_5(z)) is an isomorphism

  (O_D/25)^×/±1 ≅ (F25^×/±1) × (F25,+)
                 ≅ C12 × (Z/5)^2,

with 300 classes. It is a canonical explicit map using the chosen global conjugation and fifth power, **NOT** an unexamined coordinate-identification across D. Count all 600 unit residues modulo25 and check the 300 ± orbits. Verify all 25 wild values occur once above each of 24 tame residues; actual group-product homomorphism tests, inverse, conjugation and ±; compare D43(h1), D163(h1), D183(h8), D203(h4). Every unit residue must reconstruct uniquely; reject nilpotent zero divisor "division".

Wild group algebra over k=F5 (or F25) has k[C5×C5]≈k[U,V]/(U^5,V^5); augmentation ideal J=(U,V), J^9=0 while J^8≠0, graded dimensions 1,2,3,4,5,4,3,2,1. Ordinary k^×-valued group characters are trivial on wild C5² (no element of order5 in F25^× of size24). This is a classical finite group-algebra fact, not discovery of physical quantum or novel cohomology.

## Target B: principal ray norm-shell distributions and a real class-one constraint

For D43 (h=1), D163 (h=1), D183 (h=8) use MATCHED actual original maximal-order radius21, norm n<=441. Ignore observations divisible by5 (ray ideals must be prime to5), quotient the remaining norm-shell elements by exactly ±1 and tag each principal ideal (z) with its tame/wild class at conductor25.

For every coprime positive m,n with 5∤mn and mn<=441, in h1 fields, all ideals are principal and UNIQUE IDEAL FACTORIZATION yields the full class distribution convolution:

  C_{mn}(c,w) = Σ_{(c1,w1)(c2,w2)=(c,w)}
                  C_m(c1,w1) C_n(c2,w2).

Also check moment identities for a_K(n)=Σ_{d|n}chi_-D(d), B(n)=Σδ(z), C2(n)=Σδ(z)^2, H(n)=Σδ(z)*conj(δ(z)) over principal IDEALS, each counted once:

  B(mn)=a(n)B(m)+a(m)B(n);
  C2(mn)=a(n)C2(m)+a(m)C2(n)+2 B(m)B(n);
  H(mn)=a(n)H(m)+a(m)H(n)
          +B(m)conj(B(n))+conj(B(m))B(n).

These formulas are a classical corollary of h1+unique factorization OF IDEALS, not automatic vanishing mod5 and not a second theorem characterizing class number. Test all eligible pairs, do not just fit a few selected cases.

Predeclared non-h1 hostile witness D183: omega has norm46=2*23 and 2,23 are NOT norms of any elements (since m46>23 and neither2 nor23 a square). Thus the principal-only distribution has C_2=C_23=0 yet C_46≠0. This witnesses two NONPRINCIPAL prime ideals whose product is principal, proving principal-only convolution fails without h1. Check actual ray tag of omega and conductor25 unit membership. An h1 class-number constraint is thereby connected to ray higher-lift distributions, but no Gram valuation follows without an explicit map of this convolution to a p-adic primitive trace radical.

Check global first normalized δ-moment B(n) for nonzero witnesses; unlike unnormalized ε it is invariant under sign, so may survive. Do NOT assume it is nonzero for all fields/norms; record measured status.

## Target C: exact source-parity orthogonality, independent of class number

For the unchanged original D203 Q263 source and its 50 Phase307 shears plus exact /5 primitive rows, every source polynomial has a definite parity under (Z,W)↦(-Z,-W). Original row Z^rW^s has parity (r+s)%2; the F_r and K_a shears preserve that parity. Ordinary j derivatives have parity rowParity-j. Full Q is closed under z↦-z. Therefore the same ORIGINAL trace Gram is EXACTLY block diagonal in even/odd row labels, and the primitive Gram is too, for every integral modulus—not just mod5.

Use Phase311 original primitive Gram modulo5^3, check every cross-parity cell ZERO, split the 100-row Gram into two 50-row pieces, independently recover all Smith depth multiplicities and exact primitive v5(det)=38, hence original 138 via its 50 source divisions. Note: splitting a form changes computational organization, NOT determinant valuation; no extra mass allowed. Hostile asymmetric Q (remove one sign partner) should fail the parity guard.

## Stop/promotion

Stop and retire any assertion if unit-group bijection, δ homomorphism, C2/H moment convolution, norm-shell coprimality, original parity Gram, or Smith-depth block sum fails. Do not confuse the exact fixed-field norm-shell class-one constraint with a UNIFORM congruence forcing additional valuation. No new global discriminant bound, Lean field-class theorem, or independent referee is claimed by this work.
