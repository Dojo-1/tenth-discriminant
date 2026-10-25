# Phase50: shared sign-operator compatibility

Protocolf2dd1f7d89d29581f0d41ed7fe12b526bd2dca22 preceded the new91-line
module. The first and only target build PASS23.8670444s. No repair,
resource stop, parameter search, retry or extra agent was used.

Root6814 PASS23.6392964s. Public signatures, standard axioms and concrete
odd-p/symmetric-ellipse/prime-two controls PASS22.8116426s. Compiled audit
PASS29.1667922s:4650 logical declarations,3910 theorems,16968 runtime-only
auxiliaries excluded. Only propext,Classical.choice,Quot.sound allowed.
Coverage160 reachable/acyclic modules, no source escapes. The unchanged
source checker matches250 historical endpoint pairs, not Arb inequalities.

The exported support theorem uses the exact rectangularBasisMatrix,
positive odd p and differing total-degree parity. Its actual basis matrix
commutes with rectangularSignMatrix. The actual integer rectangular Gram
commutes with that same sign matrix under central sample symmetry.
No prime, inertness, class-number, radius or cutoff premise is smuggled
into these structural statements. The explicit p=2,R=3,S=2,row4,column1
entry-1 control rejects omitting oddness from the support theorem.

All prior Phase49 source/raw hashes are preserved. Its frozen root hash
is checked against local proof commitf0fe28a, and the current root differs
only by the new ParityCompatibility import. Do not invoke the older
current-root verifiers as if their snapshot fingerprints were still current.
The new verifier validates these scopes without rerunning Lean.

Commands from repository root:

```powershell
powershell -NoProfile -File research/ender_radius_bridge/run_phase50.ps1 -Mode build
powershell -NoProfile -File research/ender_radius_bridge/run_phase50.ps1 -Mode root
powershell -NoProfile -File research/ender_radius_bridge/run_phase50.ps1 -Mode input
powershell -NoProfile -File research/ender_radius_bridge/run_phase50.ps1 -Mode audit
python lean/verify_sources.py
python research/ender_radius_bridge/verify_phase50_results.py
```

These record the completed verification, not an instruction to consume
more registered proof attempts. The raw audit archive was read back before
removing its sole unpacked duplicate. Manifest source/raw hashes preserve
the accepted proof, four terminal records and all raw logs.

[Human explanation](PARITY_COMPATIBILITY_GUIDE.md) distinguishes checked
commutation from the elementary projector and transformed-Gram consequences.
There is no new determinant-product API, stronger valuation, strict size
saving, numerical cutoff, classification or independent review result.
Future exact-head CI is separate. The currently publisheddeab8c2 run
40225506827 was still executing its final rejection controls at this
local checkpoint; it does not cover these new mathematical modules.
