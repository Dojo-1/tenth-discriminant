# Why the wheel does not lose a solution

Current frontier: Phase35's [complete-seed proof](FUSED_WHEEL_GUIDE.md)
extends the bounded iff to d<892371480. The Phase31 scope below records
the original complete one-million check, not the latest endpoint.

A sieve output is not a proof of exhaustive coverage. Phase31 separates the
two questions: **did we enumerate every possible solution?** and **which of
those candidates pass the tests?** Its fixed target is [92,1000000), not the
whole remaining interval up to 700000000000. The finite target now compiles
in Lean; full-library and exact-head CI status accompany publication.

## One repeating pattern, with a no-loss rule

The checked class-number theorem supplies d=3 modulo 8 above 7. Thus start
with modulus 8 and allowed remainder 3. Suppose we have a modulus m and a
list of allowed remainders. To add a prime p, replace every remainder r by

    r, r+m, r+2m, ..., r+(p-1)m

and discard a replacement only if its negative is a square modulo p.
The new pattern repeats modulo m*p. This is the wheel's lift operator.
Its invariant is simple: an integer satisfying all the required nonsquare
conditions must still have its remainder in the allowed list.

Why no loss? Reduce that integer modulo m*p, calling its remainder z.
Then z mod m is its old allowed remainder, and

    z = (z mod m) + m*(z div m),       0 <= z div m < p.

So z occurs in the displayed list. Reduction also preserves its residue
modulo p, so the new test cannot discard it. `wheelLift_covers` proves this
for arbitrary positive m and p, not just the chosen pilot numbers.
`wheelResidues_cover` composes the operators without losing the invariant.
Primality is needed for the class-number application; this enumeration
identity itself only needs positivity.

## From a repeating pattern to an interval

Every natural d has the exact decomposition

    d = (d mod m) + m*(d div m).

For d<hi the quotient lies in 0,...,hi div m. Enumerate that entire quotient
range and every allowed remainder, then keep precisely lo<=d<hi. The final
filter removes padding and fixes the endpoint convention.
`intervalWheel_covers` proves that this covers every admissible interval
point. It does not trust an externally supplied claim that a list is complete.

This is the operational local-to-global bridge: local residue restrictions
form a repeating pattern; quotient and remainder transport that pattern over
the entire finite interval. The same proofs apply to larger wheels and the
full cutoff. They do not by themselves evaluate that larger instance.

## The fixed Phase31 attempt

The wheel primes are 3,5,7,11. They give modulus 9240 and 30 allowed residues.
The complete interval [92,1000000) then has 3245 wheel candidates. The extra
primes are fixed in the preregistration, from 13 through 127, and are checked
prime and odd in Lean. Their tests retain the exact guard 4*p<=d. In
particular, p=41 cannot reject d=163.

The independent exact control returns [163]. That is computational evidence,
not a Lean proof. `MillionSieve` attempts the same finite survivor identity
with kernel-checked evaluation. That identity is accepted. The coverage theorem
and the actual-field necessary-test theorem turn it into an exclusion theorem on
this entire interval. No class-number-one equality follows merely from 163
passing the tests.

Together with the already checked small end below 92, this gives the
necessary nine-element list below one million. The interval
[1000000,700000000000) remains unclosed. Phase33 separately proves all nine
positive equalities, so both directions are now checked below one million.
See the [positive-case guide](NINE_POSITIVE_GUIDE.md). This is not full classification.

## Evidence and source map

- [Preregistered protocol](PHASE31_PROTOCOL.md), committed before proof edits.
- [Results and preserved failures](PHASE31_RESULTS.json).
- [Universal wheel proof](../../lean/TenthDiscriminant/SieveWheel.lean).
- [Fixed finite attempt](../../lean/TenthDiscriminant/MillionSieve.lean).
- [Independent exact control](phase31_exact_check.py), which neither imports
  nor reruns the frozen full CRT campaign.

From `lean/`, run `lake build`, `python verify_sources.py`, `python audit.py`,
`python negative_controls.py`, and the Phase31 signature check. The publication
record must identify the exact tested commit/tree and terminal CI results.
