# Phase123: the actual two-sided integer Gram, reconstructed

**The human derivation and one sealed definition-level check are complete.**
This is progress on the arithmetic-review obligation, not a new cutoff,
new Lean theorem, independent peer review or acceptance of Phase122.
The full six-part research goal remains active.

[Human derivation](TWO_SIDED_ARITHMETIC_GUIDE.md): G=E B E^T with B repeating
(2,2D). The actual polynomial row matrix U_p has determinant1 and satisfies
U_p E=Delta_p Ehat with INTEGER quotient coordinates. Hence the middle
matrix K_p=Ehat B Ehat^T is integral and U_p G U_p^T=Delta_p K_p Delta_p,
including its shared diagonal pivots. Reflecting the s coordinate gives
sum(k)=valuationWeight, so the SAME original determinant has p^(2F(p)).
Every ordinary derivative, the selected-order/maximal-order distinction,
strict small-prime guard, empty cases and separate positivity input are explicit.

Protocol25db00e was corrected at2793645 BEFORE oracle implementation: the
initial constant-row expression2|Q|J was wrong forJ>1 because positive
derivatives of1 vanish. The fixed negative control hasJ=1 and exact2|Q|.
Original registration remains in Git. Frozen script/input commit8b41a87.
No after-execution repair, retry, grid/endpoint change or hidden pilot.

One fixed Python run, native0,0.7029999999940628seconds under60seconds.
80cases,15,840jet coordinates, fournegative controls,18zero determinants
and62positive determinants (including empty matrices with determinant1).
Zero determinants are NOT positivity evidence. Memory was not measured;
no memory-cap or process-peak claim. No external libraries or production/
previous-trial imports. The finite cases do not prove universal quantifiers.

Executed command (with the60-second subprocess timeout):

```text
python research/ender_radius_bridge/phase123_two_sided_oracle.py research/ender_radius_bridge/PHASE123_trial_20261029195950.data.json
```

Five raw files preserve exact source/data/stdout/stderr/native result.
[Manifest](PHASE123_RESULTS.json) records all hashes; [archive](PHASE123_RAW.zip).
The read-only verifier checked the saved two-sided identities and determinants
using Fraction Gaussian elimination, distinct from the oracle's Bareiss method:

```text
python research/ender_radius_bridge/verify_phase123_results.py
```

PASS:80fixed saved matrices,18zero/62positive, five raw hashes,18relative links,
unchanged old tracked sources outside the short current guide/task-state scope.
No original jets or sealed trial were replayed by the verifier. All production
Lean, pins, workflows, old reports/protocols/raw failures remain unchanged.

Argon's review06d3986 targets39e9ce3; all173inherited modules are unchanged.
Its incomplete build/axiom audit remain incomplete. Prior PR43CI checked202
modules in its own tree; it is separate from this new exposition/check and
independent semantic review. No current CI or new reviewer was launched here.

Next obligations: reconstruct the geometric comparison and all rounding/guards;
reconcile exact-version replay evidence; register a separate bounded successor
for the failed47.5bproof; expose arbitrary-field classification and useful
radial laws with their own checks. No automatic merge or external posting.
