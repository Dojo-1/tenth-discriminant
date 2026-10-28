"""Verify saved actual even weighted original-Gram evidence without executing Lean."""
from pathlib import Path
import hashlib,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
d=json.loads((p/'PHASE99_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,n:subprocess.check_output(['git','show',ref+':'+n],cwd=r)
prefix='research/ender_radius_bridge/'
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
for n in ['PHASE99_PROTOCOL.md','run_phase99.ps1']:
 assert blob(d['registered_commit'],prefix+n)==(p/n).read_bytes()
for n,h in d['sha256'].items():assert sha((r/n).read_bytes())==h,n
for n,h in d['frozen_sha256'].items():assert sha((r/n).read_bytes())==h,n
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow',prefix,'review','ledger','TAO_OBJECTIVE_AUDIT.md','TAO_OBJECTIVES_HISTORY.md','PRIOR_ART.md'],cwd=r,text=True).splitlines()
assert not set(changed).intersection(d['frozen_sha256'])
assert not any(n.startswith(('lean/','tools/','.github/','flow/','review/','ledger/')) and not n.endswith('.md') for n in changed)
archive=p/d['archive']['path'];assert sha(archive.read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==4
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert len(d['runs'])==1
x=d['runs'][0]
assert x['phase']==99 and x['mode']=='build' and x['attempt']==1 and x['exit_code']==0
assert not x['stop_reason'] and x['cumulative_before_seconds']==0
assert x['time_limit_seconds']==600 and 0<x['elapsed_seconds']<600
assert x['memory_threshold_mb']==8192 and 0<x['observed_peak_working_set_bytes']<8192*1024**2
assert x['arguments']==['env','lean','-j','1','../research/ender_radius_bridge/Phase99EvenSplitPrimeBudget.lean']
stem=x['stdout'].removesuffix('.stdout.log')
assert json.loads(raw[stem+'.result.json'].decode('utf-8-sig'))==x
assert sha(raw[x['source_snapshot']])==x['source_sha256']
assert raw[x['source_snapshot']]==(p/'Phase99EvenSplitPrimeBudget.lean').read_bytes()
s=raw[x['source_snapshot']].decode('utf-8');log=raw[x['stdout']].decode('utf-8-sig')
assert not any(t in log for t in ['error:','sorryAx','NONSTANDARD_AXIOMS','maximum number of heartbeats','maximum recursion depth'])
assert re.findall(r'(?m)^theorem (\w+)',s)==['remainder_prefix_bound','actual_gram_budget','empty_control','gaussian_split_control','parameter_divisor_control','prime_two_control','one_column_control']
assert re.findall(r'(?m)^def (\w+)',s)==['countBound']
assert 'AUDIT_OK TenthDiscriminant.EvenSplitPrimeBudget: 11 logical declarations; 10 theorems; 0 runtime-only' in log
assert 'PHASE99_INPUTS_OK TenthDiscriminant.EvenSplitPrimeBudget.actual_gram_budget: 57514 reached' in log
for n in ['remainder_prefix_bound','actual_gram_budget']:
 assert re.search(re.escape("'TenthDiscriminant.EvenSplitPrimeBudget."+n+"' depends on axioms:")+r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]',log)
block=lambda t:t.split('let forbidden : Array Name := #[',1)[1].split('for name in forbidden do',1)[0]
names=lambda t:re.findall(r'``([A-Za-z0-9_.]+)',block(t))
assert names(s)==names((p/'Phase98InputCheck.lean').read_text(encoding='utf-8'))+['TenthDiscriminant.SplitPrimeBudget.countBound','TenthDiscriminant.SplitPrimeBudget.remainder_prefix_bound','TenthDiscriminant.SplitPrimeBudget.actual_gram_budget']
assert len(names(s))==52
assert 'rectangularTraceGram (ellipsePoints D rho) S R S i i' in s
assert 'Real.sqrt (4*D)' in s and '(EvenQuadraticField D)' in s
assert 'PrimeDivisorLoss.excluded_budget_without_divisors' in s
assert 'EvenClassAggregation.uniform_two_class_bound' in s
assert len((r/'README.md').read_text(encoding='utf-8').splitlines())==61
print('PASS: actual even prime prefix -> full original-Gram weighted budget; first invocation, no repair; seven public types, one definition, five controls; 11 logical/10 theorem/0 runtime, standard three axioms; 57514 closure/52 exclusions; four raw records; prior production/evidence frozen.')
print('Standalone only. Actual M(K) normalization, final same-Gram comparison/even cutoff, integration, external CI and human review remain open.')
