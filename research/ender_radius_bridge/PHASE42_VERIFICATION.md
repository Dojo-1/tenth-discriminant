# Phase42: preserve the incomplete cutoff attempt and its verified geometry

Preregistrationd35651962c2f05872ac2bb58d90f270b2f9af39b fixed the target,
family and budgets before edits. [Results](PHASE42_RESULTS.json) identify
both attempts, including the failed control and resource stop. **The phase
did not establish a100-billion cutoff.** The old200-billion bound remains.

From the repository root, the historical attempt command was executed
twice, with the one documented ceiling-control repair between executions:

```powershell
powershell -NoProfile -File research/ender_radius_bridge/run_phase42.ps1 -Mode build
```

Do not run it again: attempt2 hit the600s cap and the runner rejects any
retry after that resource stop. Attempt1 failed66.9683539s at an unevaluated
ceiling in the small-D rejection control. Explicit Nat.ceil_pos fixed the
same proposition. Attempt2 built TunedRadiusFamily, then stopped after
600.8587502s without completing the upper/field-composition target. Its
observed peak2887528448 bytes was below8192MB. The timer cap, not a new
mathematical contradiction, terminated the owned processes.

The compiler was alive with little sampled CPU and no output during part
of attempt2; external status reads also stalled/timed out. This observation
does not establish a cause. No process restart, budget increase or new
parameter/precision search occurred. Both raw failure/stop records survive.

The unaccepted source was moved to Phase42UnacceptedCutoff.lean outside
the library. Only its header comment changed to make that status explicit;
the manifest preserves its attempted and parked hashes. The planned full
cutoff input checker remains UNEXECUTED. The library root imports only the
accepted geometry module, so the following commands do not retry the
unaccepted upper/cutoff target:

```powershell
powershell -NoProfile -File research/ender_radius_bridge/run_phase42.ps1 -Mode root
powershell -NoProfile -File research/ender_radius_bridge/run_phase42.ps1 -Mode geometry
powershell -NoProfile -File research/ender_radius_bridge/run_phase42.ps1 -Mode audit
python lean/verify_sources.py
python research/ender_radius_bridge/verify_phase42_results.py
git diff --cached --check -- . ':!research/ender_radius_bridge/PHASE42_*.log' ':!research/ender_radius_bridge/PHASE42_*.result.json'
```

Partial root PASS:6809 steps,218.059089s, observed peak2795376640 bytes.
All155 project modules are reachable/acyclic, no source proof escapes.
Fresh geometry-input check PASS134.0465353s: chosen-radius closure13721,
normalized-lower closure23486, neither contains the16 listed old-cutoff,
classification, finite-answer or old fixed-ratio inputs. All visited
declarations resolve and are safe; only the three permitted axioms.
The compiled check also confirms that no unaccepted100-billion cutoff
declaration is present in the library. Positive1,2,163 controls pass there,
separately from the geometric proof inputs.

Compiled namespace audit PASS136.5587361s:4573 logical declarations,
3839 theorems,16955 runtime-only auxiliaries excluded. Raw stdout is
losslessly archived; byte-identical readback was verified before removing
only the redundant unpacked duplicate. Original raw CRLF/BOM evidence is
not rewritten to satisfy a whitespace presentation check. The exclusions
above apply only to raw logs/runner JSON, not sources or proof gates.
Frozen source correspondence checks250 endpoint pairs, not saved Arb
inequalities. No fresh full local parent-apparatus/rejection run is claimed.

Previous head3b0c018 passed pinned CI40168480662/security40168478985;
CodeQL's earlier NEUTRAL status was later superseded by verified SUCCESS.
The identical merge/head tree was checked. The
[terminal record](https://github.com/Dojo-1/tenth-discriminant/pull/28#issuecomment-6394531507)
was posted before any newer push, after retaining the same underlying run
through slow observations. New-head unchanged pinned CI remains separate;
the final PR28 record supersedes pending checkpoints. No success transfers
from an old tree or from partial geometry to the unaccepted cutoff.

No frozen campaign, production tool, certificate, old proof module, cutoff
statement, dependency pin or CI gate changes. No merge or Tao post; no
novelty, optimality, independent human review, arbitrary-field representation
or completed classification/challenge-objective claim.

The read-only evidence verifier passes both failure/stop records, all three
partial verification records, exact candidate-body preservation after its
header-only move, original source/raw-archive hashes and current local
reader targets. It neither retries the cutoff nor reruns the Phase41 pilot.
