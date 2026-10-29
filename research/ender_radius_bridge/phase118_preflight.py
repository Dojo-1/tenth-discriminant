"""Static freeze before bounded Lean; no Lean invocation and no numerical trial."""
from pathlib import Path
import hashlib,json,re,subprocess
p=Path(__file__).resolve().parent;r=p.parents[1];primary=r.parent/'tenth-discriminant'
git=lambda *args,**kw:subprocess.check_output(['git',*args],cwd=r,**kw)
protocol='7378fa5557d5ab13139295cf945e4d81ab4815c2'
assert git('show',protocol+':research/ender_radius_bridge/PHASE118_PROTOCOL.md')==(p/'PHASE118_PROTOCOL.md').read_bytes()
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=primary).decode().strip()=='ab5558ff7b482a6bec185b37115b6faf57a82c28'
s=(p/'Phase118RadialJetMajorant.lean').read_bytes().decode()
assert not re.search(r'\b(sorry|admit|axiom)\b|set_option (maxHeartbeats|maxRecDepth)',s)
surface={'types':{m[1]:m[0] for m in re.findall(r'(?m)^(theorem (\w+)[\s\S]*?) := by',s)},'definitions':{m[1]:m[0] for m in re.findall(r'(?m)^(def (\w+)[\s\S]*?)(?=\n\n)',s)}}
assert len(surface['types'])==19 and len(surface['definitions'])==2
for name in surface['types']:assert '#check TenthDiscriminant.RadialJetMajorant.'+name+'\n' in s
for name in surface['definitions']:assert '#print TenthDiscriminant.RadialJetMajorant.'+name+'\n' in s
f=p/'PHASE118_FROZEN_SURFACE.json'
if f.exists():assert json.loads(f.read_bytes())==surface,'Public target or data definition changed'
else:f.write_bytes((json.dumps(surface,ensure_ascii=False,indent=2)+'\n').encode())
readers={'README.md','STATUS.md','lean/FORMALIZATION.md','TAO_OBJECTIVES_CURRENT.md','TAO_REPLY_BRIEF.md','research/ender_radius_bridge/RADIAL_OPERATOR_CURRENT.md'}
frozen={}
for rec in git('ls-tree','-r','-z',protocol).split(b'\0'):
    if not rec:continue
    meta,name=rec.split(b'\t',1);name=name.decode()
    if name.startswith('.agent/') or name in readers:continue
    frozen[name]=meta.split()[2].decode()
names=sorted(frozen)
hashes=git('hash-object','--stdin-paths',input=('\n'.join(names)+'\n').encode()).decode().splitlines()
for name,h in zip(names,hashes):assert h==frozen[name],name
for name in ('lean/TenthDiscriminant/RadialOperator.lean','lean/TenthDiscriminant.lean'):
    assert (primary/name).read_bytes()==(r/name).read_bytes()
prior=list(p.glob('PHASE118_build_*.result.json'))
for file in prior:assert not json.loads(file.read_bytes())['stop_reason'],'Permanent resource stop'
for file in p.glob('PHASE118_build_*.source.lean'):
    assert file.with_name(file.name.replace('.source.lean','.result.json')).exists(),'Unreconciled prior invocation'
assert len(prior)<3 and sum(json.loads(f.read_bytes())['elapsed_seconds'] for f in prior)<1200
print(f'PHASE118_PREFLIGHT_OK:19 public targets/2 data definitions frozen;{len(frozen)} prior Git blobs unchanged;primary ab555;prior invocations {len(prior)}')
