# From a bound to a finite question

The effective bound is proved. The classification is not. Phase 30 closes
the mathematical entry conditions of the saved finite sieve and checks its
small end. It does not certify the saved large computation.

## Why only one residue class survives

Let d be positive and squarefree, and suppose the actual field
Q(sqrt(-d)) has class number one. The even chart already forces d=1 or 2.
In the odd chart put omega=(1+sqrt(-d))/2, so

    omega^2 - omega + (d+1)/4 = 0.

If d=7 modulo 8, the last coefficient is even. Sending omega to zero
therefore gives a ring map from the full integer ring to F2. Its kernel
is an ideal of norm two. Class number one makes this ideal principal,
so its generator must have norm two.

But a generator x+y*omega has norm

    x^2 + x*y + ((d+1)/4)*y^2.

For y=0 this cannot be two, since two is not a square. For y nonzero the
existing small-norm inequality rules out norm two when d>7. Thus d>7
forces d=3 modulo 8. The exception matters: omega has norm two at d=7.
Nothing here proves that d=7 has class number one.

This is local-to-global and back in a literal sense: a residue map gives
an ideal; the global class-number hypothesis gives a generator; its norm
returns an impossible local numerical value. No hypercomplex extension is
needed. The integral order and its residue maps already carry the bridge.

## A finite test that cannot discard a genuine solution

For an odd prime p, a test is allowed to reject d only when 4*p<=d.
It then looks for a residue r with r^2+d=0 modulo p. Such a residue would
contradict the checked small-prime theorem under class number one.
`modularRootTest_sound` proves that a Boolean root really is a square root
in ZMod p; the prime list itself must pass `checkedOddPrimes`.

The guard is strict in the original form p<(d+1)/4. At d=163, p=41 a
root exists, but the test must not bind: 164>163. A checked control shows
that incorrectly including this endpoint rejects 163. Separate controls
reject composite prime lists and lists containing two.

The fixed base primes are exactly 3,5,7,11,13,17,19,23. For every d>=92,
all their tests bind. Below 92, keeping exceptions 1,2,3,7, kernel-checked
finite evaluation leaves exactly

    1, 2, 3, 7, 11, 19, 43, 67.

This is a proved necessary list, not eight positive class-number proofs.
All nine familiar candidates, including 163, pass the necessary test;
passing is not sufficient. The actual field at d=23 is excluded separately.

## The remaining theorem, without euphemism

Supply a checked list of additional odd primes and prove, for every integer
d in [92,700000000000), that d=3 modulo 8 and acceptance by all guarded
tests imply d=163. `classNumber_one_nine_candidates_of_middle_certificate`
then gives the necessary nine-element list for the actual field. Its
certificate premise is explicit and is NOT supplied in this phase.
Proving class number one for each of the nine fields is a separate obligation
for an if-and-only-if classification.
Phase33 now supplies all nine positive proofs; see the
[all-nine positive-case guide](NINE_POSITIVE_GUIDE.md). The upper interval remains open.

The frozen Python CRT campaign reports [163] on that interval. Its saved
output is computational evidence, not a kernel certificate. A future bridge
must check exhaustive coverage, every residue/period translate, and the exact
guarded extra-prime list. This phase neither reruns nor modifies that campaign.

## Source and verification map

- [OddPrimeTwo](../../lean/TenthDiscriminant/OddPrimeTwo.lean): F2 quotient,
  norm-two obstruction, modulo-eight theorem and 7/23 controls.
- [FiniteSieveBridge](../../lean/TenthDiscriminant/FiniteSieveBridge.lean):
  guarded tests, small necessary list and conditional remaining reduction.
- [Protocol](PHASE30_PROTOCOL.md), committed before proof edits;
  [results](PHASE30_RESULTS.json), including the failed development attempt.

Run from `lean/`: `lake build`, `python verify_sources.py`, `python audit.py`,
`python negative_controls.py`, and
`lake env lean ../research/ender_radius_bridge/Phase30SignatureCheck.lean`.
Publication must report exact-head pinned CI separately from local checks.
