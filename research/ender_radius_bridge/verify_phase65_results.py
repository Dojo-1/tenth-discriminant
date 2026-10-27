"""Check saved evidence and fixed-target preservation; do not execute Lean."""
from pathlib import Path
from decimal import Decimal
import hashlib,json,re,subprocess,zipfile
f=Path(__file__).resolve().parent
root=f.parents[1]
d=json.loads((f/'PHASE65_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,path:subprocess.check_output(['git','show',ref+':'+path],cwd=root)
for n,h in d['sha256'].items(): assert sha((f/n).read_bytes())==h,n
assert blob(d['registered_commit'],'research/ender_radius_bridge/PHASE65_PROTOCOL.md')==(f/'PHASE65_PROTOCOL.md').read_bytes()
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=root,check=True)
zp=f/d['raw_archive']['path']
assert sha(zp.read_bytes())==d['raw_archive']['sha256']
with zipfile.ZipFile(zp) as z:
 assert z.testzip() is None and len(z.namelist())==8
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
rs=d['builds']
assert [r['exit_code'] for r in rs]==[1,0]
assert [r['attempt'] for r in rs]==[1,2]
assert sum(Decimal(str(r['elapsed_seconds'])) for r in rs)==Decimal(d['target_seconds'])<1200
for r in rs:
 assert not r['stop_reason'] and r['elapsed_seconds']<=600
 assert r['time_limit_seconds']==600 and r['memory_threshold_mb']==8192
 assert r['observed_peak_working_set_bytes']<8192*1024**2
 assert sha(raw[r['source_snapshot']])==r['source_sha256']
 assert json.loads(raw[r['stdout'].replace('.stdout.log','.result.json')].decode('utf-8-sig'))==r
first=raw[rs[0]['source_snapshot']].decode('utf-8')
last=raw[rs[1]['source_snapshot']].decode('utf-8')
types=lambda s:{m.group(1):' '.join(s[m.start():s.index(':=',m.end())].split()) for m in re.finditer(r'(?m)^theorem\s+(\w+)',s)}
assert len(types(last))==9 and types(first)==types(last)
assert list(types(last))==d['public_theorems']
assert first.split('#check',1)[1]==last.split('#check',1)[1]
assert raw[rs[1]['source_snapshot']]==(f/'Phase65PrimeDivisorLoss.lean').read_bytes()
failed=raw[rs[0]['stdout']].decode('utf-8-sig')
passed=raw[rs[1]['stdout']].decode('utf-8-sig')
assert 'error:' in failed and 'NONSTANDARD_AXIOMS' in failed and 'sorryAx' in failed
assert 'error:' not in passed and 'sorryAx' not in passed
assert 'AUDIT_OK TenthDiscriminant.PrimeDivisorLoss: 13 logical declarations; 13 theorems; 0 runtime-only' in passed
for name in ['prime_divisor_log_sum','prime_divisor_mass','excluded_budget_without_divisors']:
 assert re.search(re.escape("'TenthDiscriminant.PrimeDivisorLoss."+name+"' depends on axioms:")+r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]',passed),name
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow'],cwd=root,text=True).splitlines()
assert not [n for n in changed if not n.endswith('.md')],changed
assert (root/'README.md').read_bytes()==blob(d['base'],'README.md')
for p in ['research/ender_radius_bridge/PHASE64_RESULTS.json','research/ender_radius_bridge/PHASE64_RAW.zip','research/ender_radius_bridge/Phase62PrimeAxis.lean']:
 assert (root/p).read_bytes()==blob(d['base'],p),p
print('PASS: preregistration; both raw attempts; all9 public types/5 controls unchanged;13/13/0 audit; source bytes; prior production and evidence unchanged.')
print('Integrity only. No Lean rerun, production CI coverage, arithmetic B, field-ramification bridge or new cutoff inferred.')
