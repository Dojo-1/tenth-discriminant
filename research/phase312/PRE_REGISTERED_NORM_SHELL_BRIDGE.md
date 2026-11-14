# Phase312-C — post-A/B, pre-code: class number one actually imposes GLOBAL norm-shell equality

2026-11-13. This target is recorded after the Phase312-A original-source reconstruction and matched class-control results, and after the B local-ring transport was designed. BEFORE C code or C measurements. Fixed matched radius21, D43 h1, D163 h1, D183 h8.

## Classical theorem [P-paper, imported Dedekind zeta factorization]

For imaginary quadratic K with fundamental discriminant -D, D>3, every positive integer n has total number of integral ideals of norm n

   a_K(n) = sum_{d|n} chi_{-D}(d),

where chi is the primitive quadratic Kronecker character. Every nonzero algebraic integer z of norm n determines a principal ideal (z). Since units=±1, the number r_K(n) of elements of norm n equals

   r_K(n) = 2*(number of principal integral ideals of norm n).

Therefore h(K)=1 implies r_K(n)=2*a_K(n) for EVERY n. The converse with every n is also valid, since each ideal class contains some integral ideal; if every norm n has all ideals principal, h=1. The exact ray-class count carries finer residue data but the unweighted identity does not imply distribution among the 12 residue unit orbits.

## Preregistered fixed finite controls

- Compute a_K(n) independently from quadratic-character divisor sums for all 1<=n<=21². Implement the Kronecker character at p2 from negative fundamental discriminant mod8 and at odd p via Legendre, p|D returns0. No use of the norm-ball element enumerator in a_K(n).
- Compute r_K(n) independently from exhaustive maximal-order integer coordinates a,b satisfying a²+ab+m b²=n, using same matched radius21.
- For D43/D163 h1, assert r=2a for every n<=441; for D183 h8, demand an explicit smallest failure (expected n2, since 2 splits but norm2 not principal).
- Separately partition nonzero elements coprime5 into 12 +/- residue-unit orbits. For any field, this is an exact accounting of PRINCIPAL ideals only; it does not count nonprincipal ideals in D183.
- Antisymmetry kill: for any genuine centrally symmetric norm ball Q, epsilon(-z)=-epsilon(z) so sum_Q epsilon(z)=0. This does not distinguish h1. Its first moment is a NULL statistic unless the summation breaks +/- symmetry with typed weights. Second moments survive.
- Preserve the ray exact sequence as imported theorem and class numbers from independent reduced forms. Do not pretend n<=441 proves h=1 globally; this computation only tests the known classifications.
- These tests do not yet reconstruct the ray-character-weighted norm sums, do not prove a uniform lower bound on primitive Gram rank defects, and do not improve 322^4.

## Stop rule

Any ideal-character mismatch on a known split/inert/ramified prime, first failing n outside expected control, incorrectly identified residue orbit, or failure of moment antisymmetry invalidates the derived experimental claim. Do not change the original field source or exact baseline.
