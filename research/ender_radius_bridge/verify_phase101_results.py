"""Verify saved actual even normalization evidence without executing Lean."""
from pathlib import Path
import hashlib,json,math,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
d=json.loads((p/'PHASE101_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,n:subprocess.check_output(['git','show',ref+':'+n],cwd=r)
prefix='research/ender_radius_bridge/'
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
for n in ['PHASE101_PROTOCOL.md','run_phase101.ps1']:
 assert blob(d['registered_commit'],prefix+n)==(p/n).read_bytes()
for group in ['sha256','frozen_sha256']:
 for n,h in d[group].items():assert sha((r/n).read_bytes())==h,n
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow',prefix,'review','ledger','TAO_OBJECTIVE_AUDIT.md','TAO_OBJECTIVES_HISTORY.md','PRIOR_ART.md'],cwd=r,text=True).splitlines()
assert not set(changed).intersection(d['frozen_sha256'])
assert not any(n.startswith(('lean/','tools/','.github/','flow/','review/','ledger/')) and not n.endswith('.md') for n in changed)
a=p/d['archive']['path'];assert sha(a.read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(a) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==4*len(d['runs'])
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert len(d['runs'])==2
sources=[];logs=[];spent=0
for i,x in enumerate(d['runs'],1):
 assert x['phase']==101 and x['mode']=='build' and x['attempt']==i
 assert x['exit_code']==(1 if i==1 else 0) and not x['stop_reason']
 assert abs(x['cumulative_before_seconds']-spent)<1e-8
 assert x['time_limit_seconds']==min(600,math.floor(1200-spent))
 assert 0<x['elapsed_seconds']<x['time_limit_seconds']
 assert x['memory_threshold_mb']==8192 and 0<x['observed_peak_working_set_bytes']<8192*1024**2
 assert x['arguments']==['env','lean','-j','1','../research/ender_radius_bridge/Phase101EvenMinkowski.lean']
 stem=x['stdout'].removesuffix('.stdout.log')
 assert json.loads(raw[stem+'.result.json'].decode('utf-8-sig'))==x
 assert sha(raw[x['source_snapshot']])==x['source_sha256']
 sources.append(raw[x['source_snapshot']].decode('utf-8'))
 logs.append(raw[x['stdout']].decode('utf-8-sig'));spent+=x['elapsed_seconds']
assert spent<1200
first,final=sources
assert final==(p/'Phase101EvenMinkowski.lean').read_text(encoding='utf-8')
needle='  norm_num [sqrt_scale (D : Real) (Nat.cast_nonneg D)]\n  ring\n'
assert final==first.replace(needle,needle+'  simp\n') and first.count(needle)==1
headers=lambda s:[s[m.start():s.index(':=',m.start())] for m in re.finditer(r'(?m)^theorem \w+',s)]
assert headers(first)==headers(final) and len(headers(final))==16
assert re.findall(r'(?m)^def .*',first)==re.findall(r'(?m)^def .*',final)
assert re.findall(r'(?m)^def (\w+)',final)==['chartCost','scalarCost']
assert first.split('theorem gaussian_control',1)[1]==final.split('theorem gaussian_control',1)[1]
assert 'error: unsolved goals' in logs[0] and 'True ∨ Real.pi = 0' in logs[0] and 'NONSTANDARD_AXIOMS' in logs[0]
log=logs[-1]
assert not any(t in log for t in ['error:','sorryAx','NONSTANDARD_AXIOMS','maximum number of heartbeats','maximum recursion depth'])
assert d['namespace_audit']=='AUDIT_OK TenthDiscriminant.EvenMinkowski: 23 logical declarations; 21 theorems; 0 runtime-only auxiliaries excluded'
assert d['input_closure']==57646
assert d['namespace_audit'] in log
assert f"PHASE101_INPUTS_OK TenthDiscriminant.EvenMinkowski.scalar_actual_gram_budget: {d['input_closure']} reached" in log
for n in ['actual_minkowski','normalized_actual_gram_budget','scalar_actual_gram_budget']:
 assert re.search(re.escape("'TenthDiscriminant.EvenMinkowski."+n+"' depends on axioms:")+r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]',log)
block=lambda s:s.split('let forbidden : Array Name := #[',1)[1].split('for name in forbidden do',1)[0]
names=lambda s:re.findall(r'``([A-Za-z0-9_.]+)',block(s))
extra=['ClosedKernel.actual_majorant','ClosedKernel.closed_count_kernel','ClosedKernel.closed_actual_gram_budget','OddMinkowski.actual_minkowski','OddMinkowski.normalized_count_kernel','OddMinkowski.normalized_actual_gram_budget']
assert names(final)==names((p/'Phase100InputCheck.lean').read_text(encoding='utf-8'))+['TenthDiscriminant.'+n for n in extra]
assert len(names(final))==58
assert len((r/'README.md').read_text(encoding='utf-8').splitlines())==61
print('PASS: actual even M(K), closed count kernel, full normalized and scalar-dominated original-Gram budgets;16types/2defs/4controls fixed;first failure preserved, sole proof repair verified;standard3axioms/58exclusions;all raw and prior production/evidence frozen.')
print('Standalone only. Integration, all-range even cutoff, arbitrary-field transport, external CI and human review remain open.')
