# One arithmetic test, two representations

Phase35 update: the [complete-seed certificate](FUSED_WHEEL_GUIDE.md) now
extends the actual-field bounded iff to d<892371480. The Phase34 resource
failures and its original frontier below remain historical evidence.

Purpose: make verification of the remaining interval practical without
changing which integers it excludes. This is a computational bridge, not
a new class-number theorem or an improved cutoff.

## The idea a human should retain

For a fixed positive modulus p, the old checker repeatedly asks whether
some r in 0,...,p-1 satisfies r²+d=0 modulo p. Instead, compute the set

    S_p = { -r² mod p : 0 <= r < p }

once. Membership of d mod p in this set answers the identical question.
A natural-number bit mask stores the set: its t-th bit is one exactly
when t belongs to S_p. This includes zero. There is no machine-word width
or floating-point approximation.

`maskRootTest_eq` proves this identity for EVERY natural d and positive p.
Even primality is unnecessary for the representation change. Primality is
still necessary in the separate theorem connecting the arithmetic test
to class number one.

The proof is short in substance. A bitwise union records membership in
a finite list. The equation (r²+d) mod p=0 is equivalent to
d mod p=(-r²) mod p. Substitute that equivalence in the finite existential.
`maskGuardedTest_eq` retains the exact guard 4*p<=d; it does not replace
that guard by 4*p<=d+1.

## Coverage cannot be optimized away

`maskWheelResidues_eq` proves that replacing root searches by correct masks
produces EXACTLY the old wheel list. This is stronger than equal lengths.
`maskTests_eq` proves the same identity for the subsequent prime tests.
The existing universal quotient/remainder coverage theorem remains the
reason no candidate can disappear from enumeration.

Neither a generated mask nor a fast execution is evidence of that mask's
meaning. Each literal mask must be checked against `negativeSquareMask`.
The fixed Phase34 mask check accepted all 208 literals (eight base primes
plus 200 extras), in the Lean kernel. This is local experimental evidence;
the generic semantic theorem is a separate library proof.

## Fixed experiment, not a classification

The frozen production parameters give period 892371480 and 200 extra
primes from 29 through 1289. The remaining interval requires 785 padded
quotient indices, 0 through 784, followed by the exact half-open filter.
The registered cost pilot uses only indices 0,1,392,784. It does not
replace full coverage with four examples, and its timings cannot establish
a cold-CI full-range runtime.

All four translate attempts were stopped at the registered 8192 MB memory
threshold, after approximately 56, 60, 62 and 62 seconds respectively.
None supplied a translate certificate. The checker still constructs the
wheel list before applying its final tests; the measured memory failure
applies to the combined computation, not an isolated attribution to one
operation. Correctness of the representation change does not imply that
its current evaluation strategy is efficient enough.

This negative result rules out simply repeating this monolithic evaluation
785 times under the same limits. A future attempt must change the certificate
organization (for example, checked bounded batches or fused enumeration),
prove its coverage, and re-test under a fresh preregistration. No such
refinement, memory improvement or full-range runtime is claimed here.

The checker uses a thin Lean/Std-only module, so individual experiments
do not import the whole number-field development. Generated data are
separated from their interpretation. The numerical values are not new
mathematical assumptions in the generic representation theorem.

## Things that would break the argument

- Discarding zero residues would retain integers the original test rejects.
- Using a wrong mask bit changes the answer; a mutation control detects it.
- Treating p=0 as a positive-modulus root search is invalid.
- Replacing strict inertness by the inclusive endpoint rejects d=163 at p=41.
- Omitting quotient indices or wheel residues invalidates whole-range coverage.

These controls are kept in the checked bridge and the earlier wheel proof.

## The actual mathematical frontier is unchanged

For positive squarefree d below one million, actual class number one is
equivalent to membership in the nine-element list; all nine positives are
proved. Class number one also forces the actual absolute discriminant below
700000000000. The ENTIRE interval [1000000,700000000000) remains unclosed
until a complete certificate and its field-theoretic composition are checked.

[Protocol](PHASE34_PROTOCOL.md) · [Results](PHASE34_RESULTS.json) · [All-nine proof](NINE_POSITIVE_GUIDE.md) ·
[Coverage proof](WHEEL_COVERAGE_GUIDE.md).
