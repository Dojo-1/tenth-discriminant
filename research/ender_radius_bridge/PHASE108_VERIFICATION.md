# Phase108: actual-field two-class bound joins the library

All nine accepted public theorem statements/proofs, zero definitions,
four controls and reports are exact after replacing the root import with
EvenTwoClass,OddFieldTwoClass,AxiomAudit. The checker is relocated with
phase diagnostic names changed;60even/37combined exclusions and all three
fresh roots are unchanged. ONE new root import exposes the module.
[Current guide](ALL_FIELD_BOUND_CURRENT.md) · [Production source](../../lean/TenthDiscriminant/EvenFieldTwoClass.lean).

Base62a92e4790e89cc45ae5338eff8976b66eb33a45;
preregistration3b383c6c2afc63b4bc2c60fbd2288a5576093507.

| Check | Exact command from lean | Recorded seconds | Result |
| --- | --- | ---: | --- |
| Module | `lake build TenthDiscriminant.EvenFieldTwoClass` | 89.0258049 | PASS first invocation |
| Root | `lake build` | 28.642620899999997 | PASS first invocation |
| Fresh inputs | `lake env lean -j 1 ../research/ender_radius_bridge/Phase108InputCheck.lean` | 41.8073276 | PASS first invocation |
| Whole audit | `lake env lean -j 1 Audit.lean` | 28.890939099999997 | PASS first invocation |

All stayed below the registered time and8192MB per-owned-process limits;
no repair, probe, replay or resource stop. Native recorded floating values
are preserved verbatim above. Namespace11logical/11theorems/0runtime;
whole audit5361logical/4565theorems/17015runtime, standard three axioms.
Fresh closure sizes60578/60689/60694 match107, with60even/37combined
excluded roots. The all-parity result explicitly uses the existing odd
h<=2 theorem; no independence from that used branch is claimed.

`python lean/verify_sources.py` passed all250endpoint identities (not Arb
margins). The existing import-coverage function confirms197reachable
project modules. One inherited EOFblankline is preserved byte-exactly.
[Manifest](PHASE108_RESULTS.json) · [25raw artifacts](PHASE108_RAW.zip).
Saved-evidence check, no Lean replay:
`python research/ender_radius_bridge/verify_phase108_results.py`.

The actual all-field conclusion is absdiscr<2^52 under actual h<=2, odd
absdiscr<2^50, with no caller chart/generator/isomorphism. The50billion h1
cutoff is unchanged. No classification, optimality or independent human
review is asserted. No external CI/publication here: [PR37's CI stop](PR37_CI_LIMIT_RECEIPT.md)
remains cancelled/draft/unmerged. No rerun, raised limit or changed workflow.
