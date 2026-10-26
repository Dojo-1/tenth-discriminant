"""Saved-evidence integrity, not another Lean execution or arithmetic classification."""
from pathlib import Path
from decimal import Decimal
import hashlib,json,re,subprocess,zipfile
f=Path(__file__).resolve().parent
root=f.parents[1]
d=json.loads((f/'PHASE66_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,path:subprocess.check_output(['git','show',ref+':'+path],cwd=root)
for n,h in d['sha256'].items():assert sha((f/n).read_bytes())==h,n
assert blob(d['registered_commit'],'research/ender_radius_bridge/PHASE66_PROTOCOL.md')==(f/'PHASE66_PROTOCOL.md').read_bytes()
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=root,check=True)
zp=f/d['raw_archive']['path']
assert sha(zp.read_bytes())==d['raw_archive']['sha256']
with zipfile.ZipFile(zp) as z:
 assert z.testzip() is None and len(z.namelist())==4
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert len(d['builds'])==1
r=d['builds'][0]
assert r['exit_code']==0 and r['attempt']==1 and not r['stop_reason']
assert Decimal(str(r['elapsed_seconds']))==Decimal(d['target_seconds'])<600
assert r['cumulative_before_seconds']==0 and r['memory_threshold_mb']==8192
assert r['observed_peak_working_set_bytes']<8192*1024**2
assert sha(raw[r['source_snapshot']])==r['source_sha256']
assert raw[r['source_snapshot']]==(f/'Phase66ClassFiber.lean').read_bytes()
assert json.loads(raw[r['stdout'].replace('.stdout.log','.result.json')].decode('utf-8-sig'))==r
source=raw[r['source_snapshot']].decode('utf-8')
assert re.findall(r'(?m)^theorem\s+(\w+)',source)==d['public_theorems']
assert len(d['public_theorems'])==7
assert re.findall(r'(?m)^def\s+(\w+)',source)==d['public_definitions']
assert len(d['public_definitions'])==3
log=raw[r['stdout']].decode('utf-8-sig')
assert 'error:' not in log and 'sorryAx' not in log
assert 'AUDIT_OK TenthDiscriminant.ClassFiber: 15 logical declarations; 12 theorems; 3 runtime-only' in log
for name in ['class_fiber_lifting','residue_class_lifting']:
 assert re.search(re.escape("'TenthDiscriminant.ClassFiber."+name+"' depends on axioms:")+r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]',log),name
# The full actual predicate and fixed-class quantifier order were printed in this invocation.
assert 'def TenthDiscriminant.ClassFiber.NormLift.' in log
assert log.index('∃ J,')<log.index('∀ (I :')
assert log.index('residue_class_lifting.')<log.index('∀ (p : ℕ)')
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow'],cwd=root,text=True).splitlines()
assert not [n for n in changed if not n.endswith('.md')],changed
assert (root/'README.md').read_bytes()==blob(d['base'],'README.md')
for p in ['research/ender_radius_bridge/Phase65PrimeDivisorLoss.lean','research/ender_radius_bridge/PHASE65_RESULTS.json','research/ender_radius_bridge/PHASE65_RAW.zip','research/ender_radius_bridge/PHASE64_RESULTS.json','research/ender_radius_bridge/PHASE64_RAW.zip']:
 assert (root/p).read_bytes()==blob(d['base'],p),p
print('PASS: preregistration; single accepted source/4rawfiles; full class-wide types and predicate;15/12/3 audit; prior production and evidence unchanged.')
print('Integrity only. No Lean rerun, production CI, binary-form basis, representation multiplicity, arithmetic B or new cutoff inferred.')
