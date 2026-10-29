# Phase118: actual ordinary-jet radial estimate

**FULL REGISTERED TARGET PASS, standalone Lean only.** Registered at
`7378fa5557d5ab13139295cf945e4d81ab4815c2`, before source or invocation.
Published class-number-one cutoff stays50 billion;48 billion is a candidate.

The source uses the production RadialOperator polynomial directly. It proves
the full descending-factorial coefficient bound; ordinary derivatives of
linear-factor powers over any commutative ring; the complete Leibniz formula;
the opposite-degree case; exact integer centering on the whole disc;
the old uniform bound for every r,s,j<=r; vanishing above the actual degree;
and the factor(13/20)^s bound for s,j<S and r>=9S. No derivative is divided,
sample removed, Gram replaced or prime exponent altered.

The fixed rational log checker proves log(20/13)>=.43. For S>=100 and
25S<=R<=26S, the exact rectangular row savings are at least R^2*S/100.
The scalar separation at logD>=24.5813 retains margin.0001862561. This
does not prove that the full original-Gram upper bound has that saving,
nor discharge the production radius/floor guards in the actual-field theorem.
The stronger.013 bound remains paper; this sufficient.010 estimate is checked.

The first invocation FAILED in117.154457s without a resource stop. It found
an invalid cast tactic into an arbitrary commutative ring, a redundant
tactic, incorrectly aligned factors in norm monotonicity, and a missing
local positivity fact. The full failed source/logs remain in the raw archive.
An exact [proof-only repair diff](PHASE118_REPAIR1.json) is preserved.
The second invocation PASSED in45.6828647s, with no third invocation.
These timings are execution records, not a matched-runtime speed claim.

Both calls retain the19 public types and both complete data definitions
byte-exact; each has a600s/8192MB limit and unchanged default Lean heartbeat
and recursion limits. Total162.8373217s, below1200s. Sampled per-process
working sets were3,099,459,584 and3,143,409,664 bytes, not aggregate peaks.
Four nonfatal linter warnings remain; no style repair/replay was made.

Successful namespace audit:49 logical declarations,47 theorems,3 runtime
auxiliaries excluded. Every public type is checked, both definitions printed.
Fresh closures: coefficient10911; actual norm gain14203; scale gain23312.
All70 preregistered earlier roots are excluded, with only propext,
Classical.choice and Quot.sound. Failed-run audit rejections are preserved.
All1769 earlier Git blobs outside current readers/task state remain unchanged.

Actual command, run twice from the secondary checkout:

```powershell
& ./research/ender_radius_bridge/run_phase118.ps1 -Mode build
```

The runner executes the new source from the primary pinned cache atab5558f:

```text
lake env lean -j 1 ../../tenth-radial-blocks/research/ender_radius_bridge/Phase118RadialJetMajorant.lean
```

Recheck saved evidence without rerunning Lean:

```text
python research/ender_radius_bridge/verify_phase118_results.py
python research/ender_radius_bridge/verify_pr41_publication.py
```

[Machine manifest](PHASE118_RESULTS.json) · [Eight raw artifacts](PHASE118_RAW.zip) ·
[Readable mathematics](RADIAL_JET_GUIDE.md). No production source/root change,
root build, new CI, publication, independent reviewer or Tao posting in118.
PR41's earlier CI covers the operator integration, not this research source.
The old117 verifier checks a frozen reader snapshot and therefore rejects
the updated current guide; the new publication verifier checks all historical
117 hashes against the exact published Git tree instead. No old verifier,
manifest, stopped experiment or historical mathematical source was edited.
