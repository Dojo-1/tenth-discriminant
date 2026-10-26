"""Saved finite-multiplicity evidence; never execute Lean or infer a new cutoff."""
from pathlib import Path
from decimal import Decimal
import hashlib,json,re,subprocess,zipfile
f=Path(__file__).resolve().parent;root=f.parents[1]
d=json.loads((f/'PHASE68_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,p:subprocess.check_output(['git','show',ref+':'+p],cwd=root)
for n,h in d['sha256'].items():assert sha((f/n).read_bytes())==h,n
assert blob(d['registered_commit'],'research/ender_radius_bridge/PHASE68_PROTOCOL.md')==(f/'PHASE68_PROTOCOL.md').read_bytes()
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=root,check=True)
zp=f/d['raw_archive']['path'];assert sha(zp.read_bytes())==d['raw_archive']['sha256']
with zipfile.ZipFile(zp) as z:
 assert z.testzip() is None and len(z.namelist())==12
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
rs=d['builds'];assert [r['exit_code'] for r in rs]==[1,0,0]
assert [r['attempt'] for r in rs]==[1,2,3]
assert sum(Decimal(str(r['elapsed_seconds'])) for r in rs)==Decimal(d['target_seconds'])<1200
elapsed=Decimal(0)
for r in rs:
 assert not r['stop_reason'] and r['elapsed_seconds']<=600
 assert abs(Decimal(str(r['cumulative_before_seconds']))-elapsed)<Decimal('1e-9')
 elapsed+=Decimal(str(r['elapsed_seconds']))
 assert r['time_limit_seconds']==600 and r['memory_threshold_mb']==8192
 assert r['observed_peak_working_set_bytes']<8192*1024**2
 assert sha(raw[r['source_snapshot']])==r['source_sha256']
 assert json.loads(raw[r['stdout'].replace('.stdout.log','.result.json')].decode('utf-8-sig'))==r
sources=[raw[r['source_snapshot']].decode('utf-8') for r in rs]
types=lambda s:{m.group(1):' '.join(s[m.start():s.index(' := by',m.end())].split()) for m in re.finditer(r'(?m)^theorem\s+(\w+)',s)}
assert len(types(sources[-1]))==12 and types(sources[0])==types(sources[1])==types(sources[2])
assert list(types(sources[-1]))==d['public_theorems']
definitions=lambda s:{m.group(1):m.group(0) for m in re.finditer(r'(?ms)^def (\w+)\b.*?(?=^theorem |^def |\Z)',s)}
assert len(definitions(sources[-1]))==4 and definitions(sources[0])==definitions(sources[1])==definitions(sources[2])
assert sources[1].split('\n#check',1)[0]==sources[2].split('\n#check',1)[0]
assert raw[rs[-1]['source_snapshot']]==(f/'Phase68ResidueMultiplicity.lean').read_bytes()
failed=raw[rs[0]['stdout']].decode('utf-8-sig');assert 'error:' in failed and 'NONSTANDARD_AXIOMS' in failed and 'sorryAx' in failed
for r in rs[1:]:
 log=raw[r['stdout']].decode('utf-8-sig')
 assert 'error:' not in log and 'sorryAx' not in log
 assert 'AUDIT_OK TenthDiscriminant.ResidueMultiplicity: 20 logical declarations; 16 theorems; 0 runtime-only' in log
log=raw[rs[-1]['stdout']].decode('utf-8-sig')
for n in ['class_family_four_lifts','finite_odd_square_representations']:
 assert re.search(re.escape("'TenthDiscriminant.ResidueMultiplicity."+n+"' depends on axioms:")+r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]',log),n
for n in ['FamilyGood','Admissible','PointAt']:assert 'def TenthDiscriminant.ResidueMultiplicity.'+n in log,n
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow'],cwd=root,text=True).splitlines()
assert not [n for n in changed if not n.endswith('.md')],changed
assert (root/'README.md').read_bytes()==blob(d['base'],'README.md')
for n in ['lean/TenthDiscriminant.lean','lean/TenthDiscriminant/ClassFiber.lean','lean/TenthDiscriminant/PrimeDivisorLoss.lean','research/ender_radius_bridge/PHASE67_RESULTS.json','research/ender_radius_bridge/PHASE67_RAW.zip']:
 assert (root/n).read_bytes()==blob(d['base'],n),n
print('PASS: preregistration;3terminal attempts/12rawfiles;12 unchanged types/4definitions; final print-only change;20/16/0 audit; production/prior evidence unchanged.')
print('Integrity only. No Lean rerun, production CI, common norm-form coordinates, arithmetic B or new cutoff inferred.')
