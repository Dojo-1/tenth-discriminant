"""Check saved even ideal-lattice evidence; does not execute Lean."""
from pathlib import Path
from decimal import Decimal
import hashlib,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent
r=p.parents[1]
d=json.loads((p/'PHASE89_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,n:subprocess.check_output(['git','show',ref+':'+n],cwd=r)
prefix='research/ender_radius_bridge/'
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
for n in ['PHASE89_PROTOCOL.md','run_phase89.ps1']:
 assert blob(d['registered_commit'],prefix+n)==(p/n).read_bytes()
for n,h in d['sha256'].items():assert sha((r/n).read_bytes())==h,n
for n,h in d['frozen_sha256'].items():assert sha((r/n).read_bytes())==h,n
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow',prefix,'review','ledger','TAO_OBJECTIVE_AUDIT.md','TAO_OBJECTIVES_HISTORY.md','PRIOR_ART.md'],cwd=r,text=True).splitlines()
assert not set(changed).intersection(d['frozen_sha256'])
assert not any(n.startswith(('lean/','tools/','.github/','flow/','review/','ledger/')) and not n.endswith('.md') for n in changed)
archive=p/d['archive']['path']
assert sha(archive.read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==8
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert [x['attempt'] for x in d['runs']]==[1,2]
assert [x['exit_code'] for x in d['runs']]==[1,0]
spent=Decimal(0)
for x in d['runs']:
 assert x['phase']==89 and x['mode']=='build' and not x['stop_reason']
 assert Decimal(str(x['cumulative_before_seconds']))==spent
 spent+=Decimal(str(x['elapsed_seconds']))
 assert x['time_limit_seconds']==600 and 0<x['elapsed_seconds']<600
 assert x['memory_threshold_mb']==8192 and 0<x['observed_peak_working_set_bytes']<8192*1024**2
 assert x['arguments']==['env','lean','-j','1','../research/ender_radius_bridge/Phase89EvenIdealCount.lean']
 stem=x['stdout'].removesuffix('.stdout.log')
 assert json.loads(raw[stem+'.result.json'].decode('utf-8-sig'))==x
 assert sha(raw[x['source_snapshot']])==x['source_sha256']
 log=raw[x['stdout']].decode('utf-8-sig')
 assert not any(s in log for s in ['maximum number of heartbeats','maximum recursion depth','deterministic timeout'])
assert spent==Decimal('96.3390948')==Decimal(d['target_seconds']) and spent<1200
sources=[raw[x['source_snapshot']].decode('utf-8') for x in d['runs']]
old='simpa only [hcard,hdR] using hb'
new='simpa only [hcard,hdR,Nat.cast_mul,Nat.cast_ofNat] using hb'
assert sources[0].count(old)==1 and sources[0].replace(old,new)==sources[1]
assert sources[1]==(p/'Phase89EvenIdealCount.lean').read_text(encoding='utf-8')
headers=lambda s:{m.group(1):s[m.start():s.index(':=',m.start())] for m in re.finditer(r'(?m)^theorem (\w+)',s)}
assert headers(sources[0])==headers(sources[1])
assert list(headers(sources[1]))==d['public_theorems'] and len(d['public_theorems'])==14
assert re.findall(r'(?m)^def (\w+)',sources[1])==['integerBasis','normQ','cross']
# Exact one-line repair also preserves all definitions, main theorem and controls.
failed=raw[d['runs'][0]['stdout']].decode('utf-8-sig')
assert '182:2: error: type mismatch' in failed
assert 'NONSTANDARD_AXIOMS TenthDiscriminant.EvenIdealCount.count_for_actual_form' in failed
assert 'PHASE89_NONSTANDARD_AXIOM sorryAx' in failed
passed=raw[d['runs'][1]['stdout']].decode('utf-8-sig')
assert all(s not in passed for s in ['error:','sorryAx','NONSTANDARD_AXIOMS'])
assert 'AUDIT_OK TenthDiscriminant.EvenIdealCount: 24 logical declarations; 21 theorems; 5 runtime-only' in passed
assert 'PHASE89_INPUTS_OK TenthDiscriminant.EvenIdealCount.actual_ideal_form_and_count: 44910 reached' in passed
assert re.search(r"'TenthDiscriminant.EvenIdealCount.actual_ideal_form_and_count' depends on axioms:\s*\[propext,\s*Classical.choice,\s*Quot.sound\]",passed)
block=lambda s:s.split('let forbidden : Array Name := #[',1)[1].split('for name in forbidden do',1)[0]
names=lambda s:re.findall(r'``([A-Za-z0-9_.]+)',block(s))
assert names(sources[1])==names((p/'Phase88InputCheck.lean').read_text(encoding='utf-8'))+['TenthDiscriminant.UniformTwoClass.odd_classNumber_gt_two','TenthDiscriminant.OddFieldTwoClass.arbitrary_odd_discriminant_bound']
assert len(names(sources[1]))==37
assert len((r/'README.md').read_text(encoding='utf-8').splitlines())==61
print('PASS: actual even ideal form and uniform finite off-axis count;14types/3defs/main theorem/controls unchanged;sole cast-normalization repair;FAIL46.283882/PASS50.0552128;8rawfiles;24/21/5standard3axioms;44910closure excludes37roots;prior production/evidence frozen.')
print('Standalone only; no even cutoff, production integration, external CI or completed independent human review.')
