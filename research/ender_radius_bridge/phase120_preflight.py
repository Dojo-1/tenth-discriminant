"""Freeze full actual-field target and registered arithmetic dependency policy."""
from pathlib import Path
import hashlib,json,re,subprocess
p=Path(__file__).resolve().parent;r=p.parents[1];primary=r.parent/'tenth-discriminant'
git=lambda *args,**kw:subprocess.check_output(['git',*args],cwd=r,**kw)
protocol='ec81001b325345440a2ea83a05a33aa9ad2d6cff'
assert git('show',protocol+':research/ender_radius_bridge/PHASE120_PROTOCOL.md')==(p/'PHASE120_PROTOCOL.md').read_bytes()
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=primary).decode().strip()=='ab5558ff7b482a6bec185b37115b6faf57a82c28'
accepted=(p/'Phase119RadialDetBound.lean').read_bytes().decode()
dependency=accepted[:accepted.index('#audit_namespace TenthDiscriminant.RadialDetBound')]
s=(p/'Phase120RadialCutoff.lean').read_bytes().decode();assert s.startswith(dependency)
assert not re.search(r'\b(sorry|admit|axiom)\b|set_option (maxHeartbeats|maxRecDepth)',s)
body=s[s.index('namespace TenthDiscriminant.RadialCutoff'):]
surface={'types':{m[1]:m[0] for m in re.findall(r'(?m)^(theorem (\w+)[\s\S]*?) := by',body)},'definitions':{m[1]:m[0] for m in re.findall(r'(?m)^(def (\w+)[\s\S]*?)(?=\n\n)',body)}}
assert len(surface['types'])==15 and len(surface['definitions'])==0
for name in surface['types']:assert '#check TenthDiscriminant.RadialCutoff.'+name+'\n' in s
f=p/'PHASE120_FROZEN_SURFACE.json'
if f.exists():assert json.loads(f.read_bytes())==surface,'Public target changed'
else:f.write_bytes((json.dumps(surface,ensure_ascii=False,indent=2)+'\n').encode())
extract=lambda text:set(re.findall(r'``(TenthDiscriminant\.[\w.]+)',text[text.index('  let forbidden : Array Name := #['):text.index('  for name in forbidden do')]))
policy=json.loads((p/'PHASE120_DEPENDENCY_POLICY.json').read_bytes())
assert len(policy['allowed_from_earlier_operator_exclusions'])==4 and len(policy['additional_exclusions'])==7
assert extract(s)==(extract(accepted)-set(policy['allowed_from_earlier_operator_exclusions']))|set(policy['additional_exclusions'])
assert len(extract(s))==policy['forbidden_roots']==73
readers=['README.md','STATUS.md','lean/FORMALIZATION.md','TAO_OBJECTIVES_CURRENT.md','TAO_REPLY_BRIEF.md','research/ender_radius_bridge/RADIAL_OPERATOR_CURRENT.md']
frozen={}
for rec in git('ls-tree','-r','-z',protocol).split(b'\0'):
    if not rec:continue
    meta,name=rec.split(b'\t',1);name=name.decode()
    if name.startswith('.agent/') or name in readers:continue
    frozen[name]=meta.split()[2].decode()
names=sorted(frozen);hashes=git('hash-object','--stdin-paths',input=('\n'.join(names)+'\n').encode()).decode().splitlines()
assert len(names)==len(hashes)
for name,h in zip(names,hashes):assert h==frozen[name],name
for name in ('lean/TenthDiscriminant/RadialOperator.lean','lean/TenthDiscriminant.lean'):
    assert (primary/name).read_bytes()==(r/name).read_bytes()
baseline={'registered_commit':protocol,'reader_exceptions':readers,'frozen_files':len(frozen),
  'accepted_dependency_sha256':hashlib.sha256(dependency.encode()).hexdigest(),
  'accepted_dependency_commit':'57a4654d3a43f1f69ad8f892cb41983afde946e0'}
f=p/'PHASE120_FROZEN_BASELINE.json'
if f.exists():assert json.loads(f.read_bytes())==baseline
else:f.write_bytes((json.dumps(baseline,indent=2)+'\n').encode())
prior=list(p.glob('PHASE120_build_*.result.json'))
for file in prior:assert not json.loads(file.read_bytes())['stop_reason'],'Permanent resource stop'
assert not any(json.loads(f.read_bytes())['exit_code']==0 for f in prior),'Full target already passed; no replay'
for file in p.glob('PHASE120_build_*.source.lean'):
    assert file.with_name(file.name.replace('.source.lean','.result.json')).exists(),'Unreconciled prior invocation'
assert len(prior)<3 and sum(json.loads(f.read_bytes())['elapsed_seconds'] for f in prior)<1200
print(f'PHASE120_PREFLIGHT_OK:15 public targets/0new data;accepted119 dependency exact;73registered exclusions;{len(frozen)} prior Git blobs unchanged;primary ab555;prior invocations {len(prior)}')
