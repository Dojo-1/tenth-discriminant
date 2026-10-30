# Exterior-volume reconstruction: exact check and limits

**The sole registered invocation passed in 0.265 seconds.** There was no
repair, retry, old campaign replay or Lean invocation. This adds an
[exterior-volume explanation](EXTERIOR_VOLUME_GUIDE.md), not a new theorem
or cutoff. The published 03cb58c mathematics and PR45 remain unchanged.

Protocol 481fd18 preceded implementation; source freeze d49f270 and manifest
commit 971ef12 preceded the trial. All eight fixed cases were selected by
their preregistered labels, not their determinant sign. Original and quotient
Gram entries agree with the sealed Phase123 data, using a new multiplication-
matrix construction of observations. All 220 maximal minors satisfy their
integral p^F factor and weighted Cauchy--Binet identity.

There are 24 nonzero minors and 196 zero minors. All eight selected determinants
are positive. Nontrivial F=1 occurs only in the two p=3, eight-row cases;
the other six cases have F=0. This is not a new nontrivial valuation check
at all three primes. J=1 means zero-order observations only; the earlier
all-order jet evidence is preserved separately and was not rerun.

Four negative-control families passed:

- Omitting the squared minor changes four cases.
- Using p^F instead of p^(2F) fails on both nonzero F=1 cases.
- An integer shear preserves determinant 1 while changing the diagonal
  product from 1 to 2; a Hadamard ceiling is not the volume itself.
- A positive real Gram of rank 2 has rank 1 modulo 3. This does not contradict
  rank preservation between unimodular frames over the SAME residue field.

The 60-second cap was retained. Memory was not measured; no memory cap or
peak is claimed. Five raw artifacts preserve the exact source, data,
stdout, empty stderr and native result. [Manifest](PHASE131_RESULTS.json)
· [Raw archive](PHASE131_RAW.zip) · [Frozen inputs](PHASE131_FROZEN.json).

The commands from the repository root were:

```sh
python .agent/run_phase131.py
python research/ender_radius_bridge/verify_phase131_results.py
```

The one-shot trial is terminal and must not be rerun. The saved verifier
reads the archive and scalar identities; it does not recompute observations
or determinants. All Lean sources, certificates, existing controls, pins and
workflows are unchanged from 03cb58c; its [proof CI](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41021656669)
and [security](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41021651935)
apply to that earlier mathematical/publication version. They are not relabelled
as CI for this follow-up revision. Its documentation/comparator delivery is
versioned separately. Same-assistant reconstruction remains distinct from
independent human semantic review, which is open.
