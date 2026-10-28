"""Verify saved actual even prime-axis evidence without running Lean."""
from pathlib import Path
from decimal import Decimal
import hashlib,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
d=json.loads((p/'PHASE93_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,n:subprocess.check_output(['git','show',ref+':'+n],cwd=r)
prefix='research/ender_radius_bridge/'
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
for n in ['PHASE93_PROTOCOL.md','run_phase91.ps1']:
 assert blob(d['registered_commit'],prefix+n)==(p/n).read_bytes()
for n,h in d['sha256'].items():assert sha((r/n).read_bytes())==h,n
for n,h in d['frozen_sha256'].items():assert sha((r/n).read_bytes())==h,n
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow',prefix,'review','ledger','TAO_OBJECTIVE_AUDIT.md','TAO_OBJECTIVES_HISTORY.md','PRIOR_ART.md'],cwd=r,text=True).splitlines()
assert not set(changed).intersection(d['frozen_sha256'])
assert not any(n.startswith(('lean/','tools/','.github/','flow/','review/','ledger/')) and not n.endswith('.md') for n in changed)
archive=p/d['archive']['path'];assert sha(archive.read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==8
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert [x['attempt'] for x in d['runs']]==[1,2] and [x['exit_code'] for x in d['runs']]==[1,0]
spent=Decimal(0)
for x in d['runs']:
 assert x['phase']==93 and x['mode']=='build' and not x['stop_reason']
 assert Decimal(str(x['cumulative_before_seconds']))==spent
 spent+=Decimal(str(x['elapsed_seconds']))
 assert x['time_limit_seconds']==600 and 0<x['elapsed_seconds']<600
 assert x['memory_threshold_mb']==8192 and 0<x['observed_peak_working_set_bytes']<8192*1024**2
 assert x['arguments']==['env','lean','-j','1','../research/ender_radius_bridge/Phase93EvenPrimeAxis.lean']
 stem=x['stdout'].removesuffix('.stdout.log')
 assert json.loads(raw[stem+'.result.json'].decode('utf-8-sig'))==x
 assert sha(raw[x['source_snapshot']])==x['source_sha256']
 log=raw[x['stdout']].decode('utf-8-sig')
 assert not any(s in log for s in ['maximum number of heartbeats','maximum recursion depth','deterministic timeout'])
assert spent==Decimal(d['target_seconds']) and spent<1200
sources=[raw[x['source_snapshot']].decode('utf-8') for x in d['runs']]
old='rw [hcombine,map_mul,hNg,norm_in_integer_basis]'
new='rw [hcombine,map_mul,hNg,EvenIdealCount.norm_in_integer_basis]'
assert sources[0].count(old)==1 and sources[0].replace(old,new)==sources[1]
assert sources[1]==(p/'Phase93EvenPrimeAxis.lean').read_text(encoding='utf-8')
headers=lambda s:{m.group(1):s[m.start():s.index(':=',m.start())] for m in re.finditer(r'(?m)^theorem (\w+)',s)}
assert headers(sources[0])==headers(sources[1])
assert list(headers(sources[1]))==d['public_theorems'] and len(d['public_theorems'])==11
assert not re.findall(r'(?m)^def (\w+)',sources[1])
assert sources[0].split('theorem controlled_class_prime_count',1)[1]==sources[1].split('theorem controlled_class_prime_count',1)[1]
failed=raw[d['runs'][0]['stdout']].decode('utf-8-sig')
assert 'ambiguous, possible interpretations' in failed and 'EvenIdealCount.norm_in_integer_basis' in failed
assert 'PHASE93_NONSTANDARD_AXIOM sorryAx' in failed
passed=raw[d['runs'][1]['stdout']].decode('utf-8-sig')
assert all(s not in passed for s in ['error:','sorryAx','NONSTANDARD_AXIOMS'])
a=d['audit']
assert a['logical']==13 and a['theorems']==13 and a['runtime']==0 and a['input_closure']==54650 and a['exclusions']==42
assert f"AUDIT_OK TenthDiscriminant.EvenPrimeAxis: {a['logical']} logical declarations; {a['theorems']} theorems; {a['runtime']} runtime-only" in passed
assert f"PHASE93_INPUTS_OK TenthDiscriminant.EvenPrimeAxis.controlled_class_prime_count: {a['input_closure']} reached" in passed
assert re.search(r"'TenthDiscriminant.EvenPrimeAxis.controlled_class_prime_count' depends on axioms:\s*\[propext,\s*Classical.choice,\s*Quot.sound\]",passed)
block=lambda s:s.split('let forbidden : Array Name := #[',1)[1].split('for name in forbidden do',1)[0]
names=lambda s:re.findall(r'``([A-Za-z0-9_.]+)',block(s))
assert names(sources[1])==names((p/'Phase92InputCheck.lean').read_text(encoding='utf-8'))+['TenthDiscriminant.PrincipalBasis.principal_form_of_class','TenthDiscriminant.PrincipalBasis.principal_class_form_and_prime_count','TenthDiscriminant.ActualPrimeAxis.actual_axis_card_le_two','TenthDiscriminant.ActualPrimeAxis.controlled_class_prime_count']
assert len(names(sources[1]))==42
assert len((r/'README.md').read_text(encoding='utf-8').splitlines())==61
print('PASS: actual even calibrated principal basis and full prime-normalized class count;11types/mainproof/5controls unchanged;even norm theorem qualification only;FAIL/PASS;8raw;42exclusions;standard3axioms;all prior production/evidence frozen.')
print('Standalone only; no complete prime-family/weighted same-Gram assembly, even cutoff, external CI or completed independent human review.')
