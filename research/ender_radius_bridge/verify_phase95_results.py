"""Verify saved coherent actual even prime-family evidence; never runs Lean."""
from pathlib import Path
from decimal import Decimal
import hashlib,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
d=json.loads((p/'PHASE95_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,n:subprocess.check_output(['git','show',ref+':'+n],cwd=r)
prefix='research/ender_radius_bridge/'
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
for n in ['PHASE95_PROTOCOL.md','run_phase95.ps1']:
 assert blob(d['registered_commit'],prefix+n)==(p/n).read_bytes()
for n,h in d['sha256'].items():assert sha((r/n).read_bytes())==h,n
for n,h in d['frozen_sha256'].items():assert sha((r/n).read_bytes())==h,n
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow',prefix,'review','ledger','TAO_OBJECTIVE_AUDIT.md','TAO_OBJECTIVES_HISTORY.md','PRIOR_ART.md'],cwd=r,text=True).splitlines()
assert not set(changed).intersection(d['frozen_sha256'])
assert not any(n.startswith(('lean/','tools/','.github/','flow/','review/','ledger/')) and not n.endswith('.md') for n in changed)
archive=p/d['archive']['path'];assert sha(archive.read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==12
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert [x['attempt'] for x in d['runs']]==[1,2,3] and [x['exit_code'] for x in d['runs']]==[1,1,0]
spent=Decimal(0)
for x in d['runs']:
 assert x['phase']==95 and x['mode']=='build' and not x['stop_reason']
 # The native runner accumulates binary floating-point elapsed values.
 assert abs(Decimal(str(x['cumulative_before_seconds']))-spent)<=Decimal('0.0000000001')
 spent+=Decimal(str(x['elapsed_seconds']))
 assert x['time_limit_seconds']==600 and 0<x['elapsed_seconds']<600
 assert x['memory_threshold_mb']==8192 and 0<x['observed_peak_working_set_bytes']<8192*1024**2
 assert x['arguments']==['env','lean','-j','1','../research/ender_radius_bridge/Phase95EvenPrimeFamily.lean']
 stem=x['stdout'].removesuffix('.stdout.log')
 assert json.loads(raw[stem+'.result.json'].decode('utf-8-sig'))==x
 assert sha(raw[x['source_snapshot']])==x['source_sha256']
 log=raw[x['stdout']].decode('utf-8-sig')
 assert not any(s in log for s in ['maximum number of heartbeats','maximum recursion depth','deterministic timeout'])
assert spent==Decimal('109.9848013')==Decimal(d['target_seconds']) and spent<1200
sources=[raw[x['source_snapshot']].decode('utf-8') for x in d['runs']]
old='[eval₂_add,eval₂_pow,eval₂_X,eval₂_C,Int.cast_natCast]'
new='[eval₂_add,eval₂_pow,eval₂_X,eval₂_C,Int.cast_natCast,map_natCast]'
assert sources[0].count(old)==1 and sources[0].replace(old,new)==sources[1]
oldproof='    simpa only '+new+' using\n      (eq_neg_iff_add_eq_zero.mp hz))'
newproof='    simp only [eval₂_add,eval₂_pow,eval₂_X,eval₂_C]\n    change z^2+((D : Int) : ZMod p)=0\n    simpa only [Int.cast_natCast] using (eq_neg_iff_add_eq_zero.mp hz))'
assert sources[1].count(oldproof)==1 and sources[1].replace(oldproof,newproof)==sources[2]
assert sources[2]==(p/'Phase95EvenPrimeFamily.lean').read_text(encoding='utf-8')
headers=lambda s,kind:{m.group(1):s[m.start():s.index(':=',m.start())] for m in re.finditer(r'(?m)^'+kind+r' (\w+)',s)}
assert headers(sources[0],'theorem')==headers(sources[1],'theorem')==headers(sources[2],'theorem')
assert list(headers(sources[2],'theorem'))==d['public_theorems'] and len(d['public_theorems'])==13
assert headers(sources[0],'def')==headers(sources[1],'def')==headers(sources[2],'def')
assert list(headers(sources[2],'def'))==['orderResidueMap','actualResidueMap','ClassCountData']
assert sources[0].split('theorem orderResidueMap_root',1)[1]==sources[1].split('theorem orderResidueMap_root',1)[1]==sources[2].split('theorem orderResidueMap_root',1)[1]
for x in d['runs'][:2]:
 log=raw[x['stdout']].decode('utf-8-sig')
 assert 'type mismatch' in log and 'PHASE95_NONSTANDARD_AXIOM sorryAx' in log
passed=raw[d['runs'][2]['stdout']].decode('utf-8-sig')
assert all(s not in passed for s in ['error:','sorryAx','NONSTANDARD_AXIOMS'])
assert 'AUDIT_OK TenthDiscriminant.EvenPrimeFamily: 28 logical declarations; 25 theorems; 0 runtime-only' in passed
assert 'PHASE95_INPUTS_OK TenthDiscriminant.EvenPrimeFamily.controlled_family: 54801 reached' in passed
assert re.search(r"'TenthDiscriminant.EvenPrimeFamily.controlled_family' depends on axioms:\s*\[propext,\s*Classical.choice,\s*Quot.sound\]",passed)
block=lambda s:s.split('let forbidden : Array Name := #[',1)[1].split('for name in forbidden do',1)[0]
names=lambda s:re.findall(r'``([A-Za-z0-9_.]+)',block(s))
assert names(sources[2])==names((p/'Phase94InputCheck.lean').read_text(encoding='utf-8'))+['TenthDiscriminant.ControlledPrimeFamily.controlled_family','TenthDiscriminant.ControlledPrimeFamily.fixed_family_odd_four','TenthDiscriminant.ControlledPrimeFamily.fixed_family_finite','TenthDiscriminant.ResidueMultiplicity.actualResidueMap','TenthDiscriminant.ResidueMultiplicity.actual_residue_pair_ne']
assert len(names(sources[2]))==47
assert len((r/'README.md').read_text(encoding='utf-8').splitlines())==61
print('PASS: actual even maps/distinct kernels and one controlled family for ALL finite prime sets;13public types/proofs and3definition types fixed;root-evaluation-proof-only repairs;FAIL/FAIL/PASS;12raw;28/25/0standard3axioms;54801closure47exclusions;all prior production/evidence frozen.')
print('All3 target slots consumed; no replay. Classsum/weighted same-Gram/even cutoff, production integration, external CI and independent human review remain open.')
