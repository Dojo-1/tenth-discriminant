# The bridge in one page: one field, two directions

Later analytic improvement: [Phase39](ANALYTIC_CUTOFF_OPTIMIZATION_GUIDE.md)
reduces the direct cutoff to200 billion without using this classification.
The reconstruction below keeps the original700-billion finite interval;
no saved certificate is shortened or retrospectively changed.

## The statement a mathematician should read first

For a positive squarefree integer d, let K = Q(sqrt(-d)). The public theorem
`imaginaryQuadratic_classNumber_one_iff` states

    h(K)=1  if and only if  d is one of 1,2,3,7,11,19,43,67,163.

Here h is Mathlib's actual number-field class number. K is the canonical
`AdjoinRoot` field, not a stand-in defined to satisfy the conclusion.
The statement has no range, numerical-certificate or prime-test premise.
Its proof and verification status are recorded in STATUS and the exact-head
PR checks. It is not a theorem representing arbitrary field types in this
canonical family, nor an independently human-reviewed proof.

## Why no other d can occur

The infinite and finite parts do different jobs.

First, the determinant argument proves that h(K)=1 forces d<7×10^11.
The same integer Gram determinant is positive over the reals, highly
divisible at small inert primes, and small by a real upper bound. For a
large d these demands conflict. The maximal-order identification, chosen
radius, lattice-area count, factorial estimate and logarithmic comparison
are all supplied in the existing cutoff chain. No Heegner classification
is imported as an input. The constant remains large; it is not optimized.

Second, below one million an already checked finite sieve leaves the nine
listed possibilities. The remaining interval is [1000000,700000000000).
Its size is not itself a proof of computational coverage. The coverage
argument is Euclidean division:

    d = r + M k,    0 ≤ r < M,    M = 892371480.

Class number one restricts r to a wheel formed from eight small primes.
A proved traversal covers this wheel using eleven seed subtrees. Those
labels are branch roots, not eleven sampled discriminants. For each
r, a natural-number bitset stores every possible k, not a sample. There
are at most785 positions. Its initial bits encode precisely the half-open
interval above, including its unequal end pieces.

Each of200 additional primes removes forbidden positions. An explicitly
checked modular inverse transports a periodic prime pattern along the
progression r+Mk. The crucial invariant is: **if h(K)=1, its bit survives
every filter**. Eleven closed kernel computations show every final bitset
is zero. A surviving bit cannot belong to a zero bitset: contradiction.
This is the local-to-global bridge. Its reverse direction is not assumed.

## Why all nine really work

Passing prime tests is only a necessary condition. It does not prove h=1.
The positive direction is separate: Minkowski gives a small ideal in each
ideal class; the checked residue obstructions and explicit principal small
ideals show every class is principal. The nine equalities are already
proved in `RemainingPositiveClassNumber` and its supporting modules.

The actual signed field discriminants are
-4,-8,-3,-7,-11,-19,-43,-67,-163. The jet-Gram determinant used in the
cutoff is a different determinant; do not confuse the two.

## What the experiments do—and do not—say

Phase36's registered720-second pilot was **incomplete**: ten seeds passed;
seed179 was time-stopped with60 seconds left. That failure remains frozen.
Phase37 was separately registered before execution. Its one unchanged
seed179 check passed in69.6638481 seconds, peak7942955008 bytes, below
the original180-second/8192MB per-seed limits. The library serializes all
eleven proofs so the compiler rechecks them rather than trusting the logs.
The final public claim requires the full build and transitive axiom audit,
not merely these pilot outcomes. Pinned CI is reported against its exact
commit; no PR is automatically merged.

## What still needs human judgment

The new [proof-input map](PROOF_INPUT_GUIDE.md) checks a specific circularity
risk. In the compiled dependency inventory, the cutoff does not borrow the
finite answer; the nine positive cases do not borrow the sieve; and the
finite certificate does not even reach the class-number definition. The
class-number library inputs inspected are generic finiteness, PID equivalence
and Minkowski bounds. This is internally gathered source evidence, not a
substitute for independent human semantic review.

Read the field definitions and the two proof directions first, then review
the cutoff's arithmetic/real normalization and the bit-retention/coverage
lemmas. A kernel verifies implications, not our choice of the right model.
Independent semantic review and Mathlib upstream review remain open.
There is no improved analytic constant, novelty claim, higher-class-number
result, general Siegel-zero theorem or submission to Tao here. Tao's request
for a human-generated summary is not fulfilled by relabelling AI prose.
