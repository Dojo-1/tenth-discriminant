# Phase43: fixed completion, fresh cutoff verification

Protocol605d01ab933676c13044d4475b4eceb29b302758 preceded the copy and run.
The new target's mathematical body was checked identical to the preserved
Phase42 candidate before its first execution. Only the status header
changed. The original candidate, protocol, hashes and failure records stay
unchanged. [Results](PHASE43_RESULTS.json) include the combined prior cost.

Historical attempt command from repository root (completed once; do not
treat a reproduction as part of the recorded76.3502975s run):

```powershell
powershell -NoProfile -File research/ender_radius_bridge/run_phase43.ps1 -Mode build
```

PASS76.3502975s, observed peak2910982144 bytes,600s/8192MB cap. No repair,
parameter tuning, new pilot or larger cap in Phase43. Phase42's failed
control and time stop remain INCOMPLETE; combined proof-build cost across
the three attempts is744.1774016s. Later acceptance does not erase those
attempts or establish why the older compiler stalled.

Separate post-acceptance verification:

```powershell
powershell -NoProfile -File research/ender_radius_bridge/run_phase43.ps1 -Mode root
powershell -NoProfile -File research/ender_radius_bridge/run_phase43.ps1 -Mode input
powershell -NoProfile -File research/ender_radius_bridge/run_phase43.ps1 -Mode audit
python lean/verify_sources.py
python research/ender_radius_bridge/verify_phase43_results.py
git diff --cached --check -- . ':!research/ender_radius_bridge/PHASE43_*.log' ':!research/ender_radius_bridge/PHASE43_*.result.json'
```

Full root PASS6810 steps in27.2377286s;156 modules reachable/acyclic and
no proof-source escapes. New public signatures show actual class number
one and positive-squarefree d only, including Mathlib's actual discriminant.
Old public200-billion statement remains present and unchanged.

Fresh compiled input/controls check PASS53.200717s. Odd, actual-radicand
and actual-discriminant closures55436/55569/55772 contain none of the16
listed old-cutoff/classification/finite-answer/fixed-ratio inputs. Private/
opaque bodies and types are traversed, all entries resolve and are safe,
only the three permitted axioms. Retained floor, radius, strict endpoint
and scalar separation/rejection controls compile; positive1,2,163 examples
pass separately and are not cutoff inputs.

Full compiled namespace audit PASS36.5992777s:4602 logical declarations,
3868 theorems,16955 runtime-only auxiliaries excluded. Its2005464-byte raw
stdout is preserved losslessly in the archive; manifest hashes and exact
readback were verified before removing only the unpacked duplicate.
Raw CRLF/BOM evidence remains original, excluded only from the source
whitespace presentation check, not from correspondence or proof checks.
No fresh local full parent-apparatus/rejection replay is inferred from
this compiled audit; the unchanged pinned CI supplies that separate gate.

Frozen Phase42 verification belongs to its2c020e0 snapshot. Its no100b-leak
check and root-source fingerprint should NOT be silently rerun as if they
described the current root, which deliberately adds accepted100b theorems.
Use the recorded commit to reproduce that historical negative/partial
checkpoint. Phase43 supplies its own current-state evidence instead of
weakening or rewriting the historical checks.

Prior-publication CI40170752901 on2c020e0 finished SUCCESS at07:14:58 UTC,
25 October2026, including the full build/audit/rejection gates. Security
40170751248 and separate CodeQL check also passed. The verified same-tree
synthetic merge and exact audit counts are in the
[final preceding-head record](PHASE42_PUBLICATION_FINAL.md), posted as
[comment6394778750](https://github.com/Dojo-1/tenth-discriminant/pull/28#issuecomment-6394778750)
before the newer push. Exact new-head pinned CI remains separate; its final PR28
record supersedes pending checkpoints. Research pilot/input/evidence
scripts are not silently added to the inherited CI scope.

No old mathematical source, frozen campaign, production tool, finite
certificate, dependency pin or workflow gate changes. The mathematical
diff is the fixed completion module and its root import. No merge, Tao
post, novelty, optimality, independent human review, arbitrary-field
representation, higher-class-number or full-classification claim.
