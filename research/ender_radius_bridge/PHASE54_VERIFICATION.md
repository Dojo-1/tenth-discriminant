# Phase54: local verification of the62.5-billion bound

**Local PASS.** For any actual totally complex rational degree-two number
field K of class number one, Lean proves

    (NumberField.discr K).natAbs < 62500000000.

No root, field isomorphism, range certificate or numerical premise is
supplied by the caller. This is a direct analytic cutoff. It does not
announce a full classification or optimal constant. Read the
[human mathematical argument](RECOVERED_CUTOFF_GUIDE.md) alongside this
acceptance record; the guide was frozen while the proof was an attempt.
The target is now accepted locally. Exact-head CI and independent human
semantic review remain separate.

Protocol `58f984ca03a2b965de420954cf27c88902ecbf91` fixed500^4, the
recovered-budget method and caps before implementation. The first target
build FAIL66.1649854s exposed old100b caller obligations after weakening
the helper guard. All three changed source files at that attempt are
retained. The only repair adds an explicit62500000000<=D consequence
for the old caller; its100b statement and old affine separation remain.
Second target build PASS100.1674636s; total166.332449s, no resource stop
or third target build. The new recovered-field proof did not change
between these attempts.

The first root run was interrupted: handle48424 disappeared, no result
record or completion marker survived, and no lake/lean process remained.
Its partial raw logs are retained as incomplete, not successful evidence.
The reconciled retry root PASS59.315637s (6817-step build). A UTF8 source
editing launcher failed before mutation or proof execution and was fixed;
its transcript remains in the conversation.

Fresh signature, boundary-control, generic-field application and input
checks PASS41.3241577s. The transitive closures of the new odd-chart,
canonical actual-discriminant and abstract-field bounds contain55469,
55804 and58598 constants respectively. None reaches the21 explicitly
listed older-cutoff/classification/finite-answer/fixed-ratio roots;
no unsafe or unresolved constant or nonstandard axiom is accepted.
This checks actual dependencies, not imports. The list is explicit in
`Phase54InputCheck.lean`; it is not an independent semantic proof audit.

Whole-project compiled audit PASS32.1187411s:4710 logical declarations,
3967 theorems,16968 runtime-only auxiliaries. Only `propext`,
`Classical.choice`, `Quot.sound` are permitted.163 project modules are
reachable and acyclic, with no source proof escapes. Source correspondence
passes all250 saved endpoint pairs; this alone certifies no Arb inequality.

The manifest verifies exact bytes/hashes, exact helper generalizations,
the preserved failed sources and guard repair, prior Phase53 evidence and
Phase51 reviewed sources/report/correction. Full audit stdout is retained
in a ZIP, read back exactly before its duplicate was removed. Original
CRLF raw records are preserved; whitespace checks recognize CR at EOL.

From repository root, with the pinned elan binaries on PATH:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase54.ps1 -Mode build
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase54.ps1 -Mode root
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase54.ps1 -Mode input
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase54.ps1 -Mode audit
python research/ender_radius_bridge/verify_phase54_results.py
git -c core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol diff --check
```

Do not rerun the bounded target to manufacture new timing. The saved
original records preserve its attempts. From `lean`, source correspondence
was checked with `python verify_sources.py`. Integrity verification does
not execute Lean or establish independent review.

Previous published bd2a207 completed pinned CI40331755630, including
4687/3944/16968 audit and all inherited controls.
[Final record before the next push](https://github.com/Dojo-1/tenth-discriminant/pull/28#issuecomment-6420605867).
That success does not cover Phase54. Phase51 review also predates this
proof. New exact-head CI must be reported separately. No merge or Tao
submission is authorized by this verification record.
