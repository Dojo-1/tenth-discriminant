"""Update current reader claims only after saved integration evidence passes."""
from pathlib import Path
import json
r=Path(__file__).resolve().parents[1];p=r/'research/ender_radius_bridge'
d=json.loads((p/'PHASE128_RESULTS.json').read_bytes());assert d['status']=='EXACT_INTEGRATION_ALL_FOUR_FIRST_CHECKS_PASS'
def edit(path,fn):
 q=r/path;s=q.read_text(encoding='utf-8');q.write_bytes(fn(s).encode())
def readme(s):
 s=s.replace('**Our Lean development proves that any imaginary quadratic number field with class number one has absolute field discriminant below 48 billion.**','**This branch proves that any imaginary quadratic number field with class number one has absolute field discriminant below 47.5 billion.**')
 s=s.replace('**At 48 billion and above, the bounds conflict.**','**At 47.5 billion and above, the bounds conflict.**')
 s=s.replace('**[Read the 48-billion proof](research/ender_radius_bridge/FORTY_EIGHT_BILLION_GUIDE.md)**','**[Read the short proof and its limits](research/ender_radius_bridge/STRUCTURAL_BRIDGE_CURRENT.md)**')
 old=next(x for x in s.splitlines() if x.startswith('The [48-billion proof is integrated unchanged]'))
 s=s.replace(old,'The [47.5-billion theorem and two structural interfaces](research/ender_radius_bridge/PHASE128_VERIFICATION.md) are integrated with all four local checks passing. Main retains the published 48-billion result until review and merge; exact-head CI/publication status is recorded in the draft PR. Lean checks the encoded statements and dependencies. [Exact scope](lean/FORMALIZATION.md) keeps that evidence separate from human mathematical review.')
 old=next(x for x in s.splitlines() if x.startswith('Independent human semantic review remains open.'))
 s=s.replace(old,'Independent human semantic review remains open. [Argon’s frozen review and project CI](research/ender_radius_bridge/VERIFICATION_LAYERS_CURRENT.md) concern different questions: no defect was confirmed, but its verdict remains insufficient evidence. That review does not cover the later radial improvement or new interfaces.')
 old=next(x for x in s.splitlines() if x.startswith('The repository also contains a separate canonical-family'))
 s=s.replace(old,'The [arbitrary-field classification interface](research/ender_radius_bridge/CLASSIFICATION_INTERFACE_CURRENT.md) transports the existing canonical-family proof and its separate finite certificates; it is not a new classification method. A separate [all-field bound for class number at most two](research/ender_radius_bridge/ALL_FIELD_BOUND_CURRENT.md) is published. Independent review, Mathlib acceptance and optimal constants remain open.')
 s=s.replace('[Same integer, integrated 48-billion proof](research/ender_radius_bridge/RADIAL_CUTOFF_CURRENT.md)','[Same integer and radial composition](research/ender_radius_bridge/STRUCTURAL_BRIDGE_CURRENT.md)')
 assert len(s.splitlines())==61
 return s
edit('README.md',readme)
intro='Current branch: the 47.5-billion actual-field theorem, arbitrary-field classification interface and actual radial composition laws are integrated unchanged; all four first local checks pass. Main retains the published 48-billion theorem. Exact-head CI/publication is a separate draft-PR gate. [Short mathematical account](research/ender_radius_bridge/STRUCTURAL_BRIDGE_CURRENT.md) · [Integration evidence](research/ender_radius_bridge/PHASE128_VERIFICATION.md). The failed Phase122 attempt remains unchanged; Phase125 is its separately registered successful successor. Historical entries below retain their original scope.'
for name in ['STATUS.md','lean/FORMALIZATION.md']:
 def update(s,name=name):
  lines=s.splitlines();assert lines[2].startswith('Current reader reconciliation (Phase122):')
  text=intro if name=='STATUS.md' else intro.replace('(research/','(../research/')
  lines[2]=text
  extra=['','## Phase128: one integrated library, three distinct consequences','',
   'Nineteen public statements and two private helpers are exact relocations into `EndpointCutoff`, `FieldClassification` and `RadialAction`. The cutoff applies to the actual absolute discriminant of every totally complex degree-two number field with class number one. The classification iff transports the existing canonical proof and its 700-billion finite endgame. The radial matrices satisfy identity, addition, inverse and jet/Gram composition; their fixed nonmultiplicativity control remains. These are separate consequences, not claims of novelty or independent review.','',
   'All four first checks passed: three-module build, full root build, all nineteen types/eight fresh closures, and the compiled whole audit. There are 205 reachable modules and 5,619 logical declarations / 4,807 theorems / 17,029 runtime auxiliaries; exactly 35 logical declarations were added and none removed. Old proof sources, controls, pins and workflows are unchanged. Publication and semantic review remain separately scoped.']
  return '\n'.join(lines[:3]+extra+lines[3:])+'\n'
 edit(name,update)
def ledger(s):
 lines=s.splitlines();assert len(lines)==61
 lines[2]='**Main’s published bound is 48 billion; this branch integrates 47.5 billion.**'
 lines[6]='The classification interface transports the existing canonical proof; it is not a new method or optimality claim.'
 for i,line in enumerate(lines):
  if line.startswith('| 1 |'):lines[i]='| 1 | Effective bound without Heegner input | **Branch cutoff: 47.5 billion**, actual fields and actual discriminants; all local integration checks pass. Main remains 48 billion; exact-head CI is separate. [Proof](research/ender_radius_bridge/STRUCTURAL_BRIDGE_CURRENT.md). |'
  elif line.startswith('| 2 |'):lines[i]='| 2 | Best efforts to optimize the constant | **Conservative improvement:** 700 to 47.5 billion on this branch; the latest step saves 0.5 billion from 48. Other approaches report much smaller bounds. No optimality claim. |'
  elif line.startswith('| 3 |'):lines[i]='| 3 | A finite computation can finish the range | **Existing canonical certificates and arbitrary-field interface.** The new iff transports that proof and its separate 700-billion endgame; it does not replace it with the 47.5-billion route. [Scope](research/ender_radius_bridge/CLASSIFICATION_INTERFACE_CURRENT.md). |'
  elif line.startswith('| 6 |'):lines[i]='| 6 | Stimulate new arguments or arrangements | **Reusable arrangements:** factorial prime mass, staircase weights, compatible ordinary-jet transport and actual radial composition/inverse laws. [Operators and invariants](research/ender_radius_bridge/RADIAL_ACTION_CURRENT.md). No novelty claim. |'
  elif line.startswith('| 11 |'):lines[i]='| 11 | Independent due diligence | **Partial:** Argon reviewed frozen39e9ce3/173modules; no defect confirmed, verdict insufficient evidence. Exact-source project CI passed; Argon’s own replay did not finish. Later radial proofs remain outside its scope. [Layers](research/ender_radius_bridge/VERIFICATION_LAYERS_CURRENT.md). |'
  elif line.startswith('The old bounded AI review at63be64b'):lines[i]='The older reviews do not cover the new 47.5-billion integration or radial laws.'
  elif line.startswith('keeps theorem checking, execution evidence'):lines[i]='keeps theorem checking, execution evidence and independent review separate. [Phase128](research/ender_radius_bridge/PHASE128_VERIFICATION.md) integrates 19 public types unchanged; full local checks pass, with exact-head CI/publication separately recorded in the draft PR.'
 assert len(lines)==61
 return '\n'.join(lines)+'\n'
edit('TAO_OBJECTIVES_CURRENT.md',ledger)
edit('research/ender_radius_bridge/CLASSIFICATION_INTERFACE_CURRENT.md',lambda s:s.replace('**Standalone Lean interface accepted; production integration is pending.**','**Integrated unchanged in this branch; all four local checks pass.**').replace('call was used. Full integration/build/audit/CI remain separate obligations.','call was used. [Integrated API](../../lean/TenthDiscriminant/FieldClassification.lean) and [Phase128 evidence](PHASE128_VERIFICATION.md) cover the production/root checks; exact-head CI and review remain separate.'))
edit('research/ender_radius_bridge/RADIAL_ACTION_CURRENT.md',lambda s:s.replace('**Standalone Lean laws accepted; integration is pending.**','**Integrated unchanged in this branch; all four local checks pass.**').replace('[Actual Lean laws](Phase127RadialAction.lean)','[Integrated actual Lean laws](../../lean/TenthDiscriminant/RadialAction.lean) · [Integration evidence](PHASE128_VERIFICATION.md)'))
edit('research/ender_radius_bridge/MEANING_PRESERVING_SOURCE_MAP.md',lambda s:s.replace('Source baseline: PR42 merge `0bde1bf`. This is a source map, not a new theorem.\nThe checked actual-field cutoff is 48 billion; the sole 47.5-billion endpoint attempt\n[failed elaboration](PHASE122_VERIFICATION.md) and was not repaired or retried.','Current branch: [Phase128](PHASE128_VERIFICATION.md) integrates the accepted47.5-billion successor, arbitrary-field classification interface and radial laws. All local checks pass; publication is separate. [Short current account](STRUCTURAL_BRIDGE_CURRENT.md).\n\nThe map below is the historical PR42/Phase122 baseline. Its failed attempt\n[remains unchanged](PHASE122_VERIFICATION.md); the successful successor is a separate registered cycle, not a retry of that stopped source.'))
edit('research/ender_radius_bridge/VERIFICATION_LAYERS_CURRENT.md',lambda s:s.replace('All173Argon-reviewed module blobs','| Phase126/127 structural proofs and Phase128 integration | Arbitrary-field iff and actual radial action; 19 public types/2 private helpers integrated exactly, all four first checks PASS; 205 modules, 5619 logical/4807 theorems/17029 runtime | These are project checks and same-assistant reconstructions. Exact-head publication and independent semantic review are separate. |\n\nAll173Argon-reviewed module blobs').replace('Standalone only;no production/root/newCI acceptance yet. Phase122failure stays preserved.','Integrated unchanged by Phase128 with all local checks; exact-head newCI/publication separate. Phase122failure stays preserved.'))
print('UPDATED128 current reader claims;README61lines/ledger61lines;historical proofs/results untouched')
