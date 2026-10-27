"""Check the saved arbitrary-basis helper; no Lean execution or full-bridge claim."""
from pathlib import Path
from decimal import Decimal
import hashlib,json,re,subprocess,zipfile
f=Path(__file__).resolve().parent;root=f.parents[1]
d=json.loads((f/'PHASE71_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,p:subprocess.check_output(['git','show',ref+':'+p],cwd=root)
for n,h in d['sha256'].items():assert sha((f/n).read_bytes())==h,n
assert blob(d['registered_commit'],'research/ender_radius_bridge/PHASE71_PROTOCOL.md')==(f/'PHASE71_PROTOCOL.md').read_bytes()
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=root,check=True)
zp=f/d['raw_archive']['path'];assert sha(zp.read_bytes())==d['raw_archive']['sha256']
with zipfile.ZipFile(zp) as z:
 assert z.testzip() is None and len(z.namelist())==8
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
rs=d['builds'];assert [r['exit_code'] for r in rs]==[1,0] and [r['attempt'] for r in rs]==[1,2]
assert sum(Decimal(str(r['elapsed_seconds'])) for r in rs)==Decimal(d['target_seconds'])<1200
for r in rs:
 assert not r['stop_reason'] and r['elapsed_seconds']<=600
 assert r['memory_threshold_mb']==8192 and r['observed_peak_working_set_bytes']<8192*1024**2
 assert sha(raw[r['source_snapshot']])==r['source_sha256']
 assert json.loads(raw[r['stdout'].replace('.stdout.log','.result.json')].decode('utf-8-sig'))==r
 assert 'maximum number of heartbeats' not in raw[r['stdout']].decode('utf-8-sig')
sources=[raw[r['source_snapshot']].decode('utf-8') for r in rs]
types=lambda s:{m.group(1):' '.join(s[m.start():s.index(' :=',m.end())].split()) for m in re.finditer(r'(?m)^theorem\s+(\w+)',s)}
defs=lambda s:{m.group(1):m.group(0) for m in re.finditer(r'(?ms)^def (\w+)\b.*?(?=^theorem |^def |\Z)',s)}
assert len(types(sources[-1]))==14 and types(sources[0])==types(sources[1])
assert len(defs(sources[-1]))==3 and defs(sources[0])==defs(sources[1])
assert raw[rs[-1]['source_snapshot']]==(f/'Phase71BasisArithmetic.lean').read_bytes()
failed=raw[rs[0]['stdout']].decode('utf-8-sig');assert 'error:' in failed and 'sorryAx' in failed
log=raw[rs[-1]['stdout']].decode('utf-8-sig');assert 'error:' not in log and 'sorryAx' not in log
assert 'AUDIT_OK TenthDiscriminant.IdealBasisArithmetic: 23 logical declarations; 20 theorems; 5 runtime-only' in log
assert re.search(re.escape("'TenthDiscriminant.IdealBasisArithmetic.normalized_form_of_basis' depends on axioms:")+r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]',log)
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow'],cwd=root,text=True).splitlines()
assert not [n for n in changed if not n.endswith('.md')],changed
for p in ['README.md','lean/TenthDiscriminant.lean','research/ender_radius_bridge/Phase69IdealNormForm.lean','research/ender_radius_bridge/PHASE69_RESULTS.json','research/ender_radius_bridge/PHASE69_RAW.zip']:
 assert (root/p).read_bytes()==blob(d['base'],p),p
print('PASS: new preregistered helper;2raw attempts/8files;14types/3definitions preserved;23/20/5 audit; no heartbeat stop or old69/prod mutation.')
print('Integrity only. No full chosen-basis/count bridge, new-head CI, uniform coefficient bound, arithmetic B or cutoff inferred.')
