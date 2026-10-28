# Phase111: exact passive polynomial/jet/Gram integration

Basef7c30dfb50b03b68a2e36697e3a68fc9e046ab58;
preregistration6f8cf73fb6218a57d794e20cdc93e25669734ca8.
Accepted110body/reports are exact after replacing ONLY its root import by
CoordinateTranslation. All20public types/proofs,four complete definitions,
three private helpers,four controls/reports unchanged; ONE root import.
[Current guide](PASSIVE_TRANSPORT_CURRENT.md) · [Production source](../../lean/TenthDiscriminant/PassiveTransport.lean).

| First check | Exact command from lean | Recorded seconds | Result |
| --- | --- | ---: | --- |
| Module | `lake build TenthDiscriminant.PassiveTransport` | 62.4798341 | PASS |
| Root | `lake build` | 42.626777499999996 | PASS |
| Fresh closures | `lake env lean -j 1 ../research/ender_radius_bridge/Phase111InputCheck.lean` | 36.2416537 | PASS |
| Whole audit | `lake env lean -j 1 Audit.lean` | 60.6010078 | PASS |

No repair, repeat, probe, standalone110replay or resource stop. All stay
inside registered time/8192MB per-process bounds. Native floating result
values are preserved. Namespace31logical/27theorems/0runtime; standard3
axioms. Fresh closure5880/13936/33095, all70excluded inputs unchanged.

Whole inventory5393logical/4593theorems/17015runtime. Compared with the
published PR38whole audit, no declaration disappeared. Exactly the31new
namespace declarations plus TenthDiscriminant.rowSection.eq_1 entered
the inventory. The latter is the existing rowSection definition's newly
reachable equation lemma when the accepted proof unfolds that definition;
it is audited with permitted axioms too. This explains the extra theorem
beyond the namespace count. The saved verifier compares both inventories.

`python lean/verify_sources.py` passes all250endpoint identities (not Arb
margins); existing import coverage confirms198reachable modules.
The single inherited EOFblankline289 is preserved for exact correspondence.
[Manifest](PHASE111_RESULTS.json) · [all25raw artifacts](PHASE111_RAW.zip).
Saved check: `python research/ender_radius_bridge/verify_phase111_results.py`.
Previous math/root exceptONEimport,tools,pins,controller/workflow and all
historical evidence are frozen. No new mathematical proof/constant here.

One separately registered final-head pinned CI is required for this new
publication before user-authorized merge. External terminal receipt belongs
in its PR, after complete logs/security/tested-tree inspection. No head
changes/retries/limit increases after that dispatch. This local receipt
alone is not external CI or independent human review. No cutoff gain,
computational-hardness theorem or full-classification claim.
