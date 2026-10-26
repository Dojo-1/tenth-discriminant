# The price of primes we cannot use

**Checked standalone Lean prototype; no new cutoff.** The original 50-billion result and production proof are unchanged. This bridge is not imported by the production library and is not covered by the earlier Phase58 review.

The determinant remains one positive integer. Geometry gives its Hadamard upper bound H. Each chosen good prime supplies the existing p^(2F(p)) divisor, so

    good-prime mass <= log H.

Choose a finite set P of odd primes at most L, a good subset G, and the excluded set E=P\G. With the original weight w(p)=2F(p)log(p), exact addition gives

    mass over P <= log H + excluded-prime mass.

This is useful when a higher-class-number hypothesis no longer guarantees that every small prime is good. The price of an excluded prime is its actual weight; merely counting excluded primes is insufficient.

## A count becomes a weighted price

Assume L>=3. Let N(n) count excluded primes at most n, all between 3 and L. For a decreasing real kernel f with f(L)>=0, exact finite Abel summation gives

    sum(p in E,f(p))
      = f(L)N(L) + sum(n=3,...,L-1, (f(n)-f(n+1))N(n)).

Every coefficient is nonnegative. A justified count bound N(n)<=B(n) therefore yields the same expression with B as an upper bound. The proof reuses pinned Mathlib's `Finset.sum_Ico_by_parts`.

The checked final theorem assumes a nonnegative scale C and w(p)<=C*f(p) at excluded primes. It concludes

    mass over P <= log H + C * [the finite expression with B].

The assumptions about f, C and B stay explicit. Applying this to class number at most two still requires proving suitable count and weight bounds from that arithmetic hypothesis, including ramified primes and any finite-range exceptions. The old X(2)=70000 campaign is not validated by this prototype.

## What was actually checked

The complete actual-Gram, Abel, positive-kernel and final assembly compiled on the third registered attempt. Both earlier proof failures and all snapshots/raw output are preserved. All 11 theorem type prefixes and the four definitions stayed unchanged; repairs only completed proof bodies.

The fixed controls cover a nonempty rational example giving 8/15, empty count/kernel terms, failure of the abstract count transfer with increasing or negative endpoint kernels, and the split local input D=19,p=5. The last control checks the nonsquare predicate, not a determinant counterexample.

The new namespace audit covers 36 logical declarations, 32 theorems and 5 runtime-only auxiliaries, with only the three standard axioms. Fresh closures for the good-prime bound, count transfer and final budget reach 48,165, 11,176 and 48,196 declarations and exclude the listed class-number-one, old-cutoff and classification roots.

The original trace normalization, ordinary derivatives, actual ellipse sample and matrix are retained. No field classification, higher-class-number range, optimality, novelty or independent human review follows. [Execution and evidence limits](PHASE59_VERIFICATION.md).
