# Phase316-B — preregister exact small-norm ideal rigidity as a stronger gauge control

Date 2026-11-14 Madrid, recorded AFTER Phase316-A original wild-gauge focused CI passed, BEFORE Phase316-B source or tests. The **real field theorem and reported cutoff** remain unchanged.

## Universal elementary identity and theorem target

For fundamental imaginary discriminant -D, D≡3 mod4, D>3, O_K=Z[omega], omega²-omega+m=0, m=(D+1)/4, every z=a+b omega has

  N(z)=a²+ab+mb²,
  4N(z)=(2a+b)²+D b².

If b ≠0, since b integer, b²≥1, and since 4N is divisible4 while D=4m-1, the displayed identity forces N(z)≥m. Therefore any NONZERO element with N(z)<m is a rational integer a and N(z)=a². This is true for EVERY such D, independent of class number. The class-number-one assumption enters only after: every integral ideal is principal, hence its norm-shell coefficient a_K(n) for positive n<m is exactly 1 if n is a square and 0 otherwise (global units ±1 for D>3). Thus all primes p<m are inert; split or ramified primes would give an ideal of norm p which is impossible under h1.

This is classical elementary class-number-one arithmetic, NOT a newly discovered uniform bound.

## Frozen tests

1. D43 and D163 h1: check every ideal norm shell 1≤n<m via independent Kronecker divisor-sum ideal counts; verify a_K(n)=1 for squares,0 otherwise. Also compare all principal generators modulo± from the actual maximal-order radius≥sqrt(m) norm ball; no missing rational elements.
2. D187 h2 and inert2/inert5: exact negative controls: ideal coefficients a(11)=a(17)=1 while there are NO principal elements norm11 or17 (both <m=47). This discriminates global h1 from the identical local small norm-form support.
3. The existing Phase316 gauge shift nu(z)=v_(omega)-v_(baromega) vanishes for EVERY rational integer z=a, hence it fixes ALL exact h1 principal ray125 tags in the subthreshold shells n<m, including the full tame and conductor2 data when defined. Verify by direct enumeration, and reassert that a separate higher-norm original Gram mod25 difference occurs (Phase316-A).
4. A scoped Lean theorem may formalize the universal polynomial norm gap; if no kernel check, label [P-paper] with the explicit identity and integer argument, not [P-Lean]. Do not claim the all-ideals conclusion is formalized unless a separate class-group bridge actually exists.

## Kill / governance

Any D43/D163 small-norm ideal count mismatch, rational-generator count mismatch, nonh1 D187 counterworld failure, or nonzero gauge shift on a rational integer retires the corresponding claim. The norm form constraint itself does NOT add a new determinant valuation. Even after fixing all small n<m shells, the synthetic full conductor250 convolution countermodel may differ from actual native Gram mod25, which would sharpen the missing global-generator residue obligation.
