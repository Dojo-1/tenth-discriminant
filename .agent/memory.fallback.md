# Repository memory fallback

No mem0 operation is exposed in this workspace; this file stores only stable,
non-sensitive conventions until one is available.

- The arithmetic trace-Gram is integral first. The real matrix and each
  `ZMod m` matrix are projections of that same indexed integer matrix.
- A local Gram sum must retain the original global sample indexing. Reducing
  the sample finset to an image can collapse distinct points and change the
  matrix.
- A square prime factor of a Gram determinant needs an integral two-sided
  factorization after a determinant-preserving basis change. Divisibility of
  one row and one column alone is insufficient.
- Verify every new Lean head with the pinned Linux CI workflow; older green
  runs and the Windows wrapper timeouts do not certify it.
