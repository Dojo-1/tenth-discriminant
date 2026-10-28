# Phase97: actual even class summation gives a prime-prefix bound

The FULL registered standalone target passed on its FIRST invocation:
`EvenClassAggregation.prime_prefix_bound` and `uniform_two_class_bound`.
For positive squarefree d congruent to1 or2 modulo4, actual h(K)<=2,
EVERY finite admissible P with p<=natural t, define

    A=2*pi*t/sqrt(4*d), B=4*sqrt(actualM(K)*t/(4*d)).
    card(P)<=h(K)/4*(A+B+1)<=(A+B+1)/2.

No family, points, slice, count or cardinality identity is supplied by the
caller. The coherent actual family96 supplies4*card(P) selected points;
generic actual_class_slice preserves each class slice's cardinality and
membership; PointAt supplies prime normalization and norm bounds. The
exact class partition and generic two_class_accounting then sum counts.
Actual4d remains explicit in both area and boundary terms.
[Human double-counting proof](EVEN_CLASS_SUM_GUIDE.md).

[Protocol](PHASE97_PROTOCOL.md) and [runner](run_phase97.ps1) registered at
`18fde895efc0a8dc50d46e34d2322c64c45383ce` before source/execution.
Base: `3dfdd7704597de6cbd5f4cb38ebd447ba61202bc`.
Lean4.19.0; Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`.

One target PASS,90.1254956s; observed peak process working set3,245,568,000
bytes. Time cap600s, cumulative allowance1200s, per-process memory guard
8192MB. No repair, retry, internal/outer resource stop or extra Lean run.
Source SHA256:
`f8be4ea6bc9f517580b1f54c55a6160576b66a7933d9178ca7ab45ddc666752c`.
Six public theorem types, no new definitions; namespace6logical/6theorems/
0runtime auxiliaries. Only `propext`, `Classical.choice`, `Quot.sound`.
Fresh uniform-target closure54,805excludes the same47old inputs as96 PLUS
the odd-field ClassAggregation prime-prefix/uniform bounds (49total).
Controls: empty actual slice, absent-class slice, two labels projecting
to one value, valid h1/h2axis accounting and its h3counterexample.
The generic slice/accounting lemmas are reused directly; odd-field prefix
theorems do not enter the proof.

## Verify saved evidence

```sh
python research/ender_radius_bridge/verify_phase97_results.py
```

PASS: source/snapshots/transcripts, single bounded invocation, six types,
no new definitions, four controls,49exclusions/standard axioms,
[4rawfiles](PHASE97_RAW.zip), [manifest](PHASE97_RESULTS.json),1,522frozen
prior files and61README lines. It does not execute Lean. Exact executed
command from lean/:
`lake env lean -j 1 ../research/ender_radius_bridge/Phase97EvenClassAggregation.lean`.
No replay of prior proofs or numerical campaigns occurred.

Standalone research only. Production/root/tools/pins/certificates/CI and
all prior protocols/raw/verifiers/reviews/ledgers/failures remain unchanged.
The96whole-library audit remains historical, not a new97root build/audit.
No external exact-head CI or independent human review is claimed. Argon's
report is not received/assessed; no reviewer agent started. No publication
or merge. Earlier negative results remain unchanged.

## Scope boundary

The second bound is uniform in h<=2; actualM(K) is STILL field-dependent.
Integration, complete weighted prime loss, actual Minkowski normalization
and contradiction on the SAME original positive integer Gram remain open.
Radicandd and actual field discriminant4d need explicit matching. No
scalar-envelope candidate is a premise; no new even cutoff, full
classification, optimality, novelty or upstream acceptance is asserted.
Existing field bounds remain unchanged.
