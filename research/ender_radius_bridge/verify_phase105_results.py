"""Verify saved coordinate/translation proof and preserved failures; never runs Lean."""
from pathlib import Path
import hashlib,json,math,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
d=json.loads((p/'PHASE105_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,n:subprocess.check_output(['git','show',ref+':'+n],cwd=r)
prefix='research/ender_radius_bridge/'
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
for n in ['PHASE105_PROTOCOL.md','run_phase105.ps1']:
 assert blob(d['registered_commit'],prefix+n)==(p/n).read_bytes()
for group in ['sha256','frozen_sha256']:
 for n,h in d[group].items():assert sha((r/n).read_bytes())==h,n
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow',prefix,'review','ledger','TAO_OBJECTIVE_AUDIT.md','TAO_OBJECTIVES_HISTORY.md','PRIOR_ART.md'],cwd=r,text=True).splitlines()
assert not set(changed).intersection(d['frozen_sha256'])
assert not any(n.startswith(('lean/','tools/','.github/','flow/','review/','ledger/')) and not n.endswith('.md') for n in changed)
a=p/d['archive']['path'];assert sha(a.read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(a) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==12
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert len(d['runs'])==3
sources=[];logs=[];spent=0
for i,x in enumerate(d['runs'],1):
 assert x['phase']==105 and x['mode']=='build' and x['attempt']==i
 assert x['exit_code']==(0 if i==3 else 1) and not x['stop_reason']
 assert abs(x['cumulative_before_seconds']-spent)<1e-8
 assert x['time_limit_seconds']==min(600,math.floor(1200-spent))
 assert 0<x['elapsed_seconds']<x['time_limit_seconds']
 assert x['memory_threshold_mb']==8192 and 0<x['observed_peak_working_set_bytes']<8192*1024**2
 assert x['arguments']==['env','lean','-j','1','../research/ender_radius_bridge/Phase105CoordinateTranslation.lean']
 stem=x['stdout'].removesuffix('.stdout.log')
 assert json.loads(raw[stem+'.result.json'].decode('utf-8-sig'))==x
 assert sha(raw[x['source_snapshot']])==x['source_sha256']
 sources.append(raw[x['source_snapshot']].decode('utf-8'))
 logs.append(raw[x['stdout']].decode('utf-8-sig'));spent+=x['elapsed_seconds']
assert spent<1200
first,second,final=sources
assert final==(p/'Phase105CoordinateTranslation.lean').read_text(encoding='utf-8')
# Include the entire mathematical statement, including let-bound control data.
headers=lambda s:[s[m.start():s.index(':= by',m.start())] for m in re.finditer(r'(?m)^theorem \w+',s)]
for s in sources:
 assert headers(s)==headers(first) and len(headers(s))==29
 assert s.split('theorem shift_zero',1)[0]==first.split('theorem shift_zero',1)[0]
 assert re.findall(r'(?m)^def (\w+)',s)==['shift','orderPoint','embedding','integralPoint','oddCoordinates']
# Reconstruct the four exact proof-only repairs, without altering any control expectation.
s=first.replace('    rw [integralPoint_eval,integralPoint_eval] at he','    dsimp only at he\n    rw [integralPoint_eval,integralPoint_eval] at he',1).replace('shift_comp,integralPoint_shift D v,','shift_comp,(fun a => integralPoint_shift D a v),',1)
a=s.index('  dsimp only\n',s.index('theorem shifted_gram_counterexample'));b=s.index('\ntheorem zero_discriminant_control',a)
control='  dsimp only\n  refine ⟨?_,?_,by decide⟩\n  · rw [Matrix.det_fin_two]\n    norm_num [integerRectangularTraceGram,integerTraceGramMatrix,integerTraceGramEntry,\n      integerPairTrace,integerDerivativeRow,pairScale,pairMul,pairPow,pairConj,\n      Finset.sum_range_succ,Nat.descFactorial]\n  · rw [Matrix.det_fin_two]\n    norm_num [integerRectangularTraceGram,integerTraceGramMatrix,integerTraceGramEntry,\n      integerPairTrace,integerDerivativeRow,pairScale,pairMul,pairPow,pairConj,\n      shift,Finset.sum_range_succ,Nat.descFactorial]\n'
s=s[:a]+control+s[b:]
s=s.replace('  simp [pairEval,latticePoint]\n\ntheorem odd_index_control','  constructor\n  · simp [pairEval,latticePoint]\n  · decide\n\ntheorem odd_index_control',1)
assert s==second
needle='      Finset.sum_range_succ,Nat.descFactorial]\n  · rw [Matrix.det_fin_two]'
assert second.count(needle)==1
assert final==second.replace(needle,'      Finset.sum_range_succ,Nat.descFactorial]\n    have hc : ({0,(1,0)} : Finset (Int × Int)).card=2 := by decide\n    norm_num [hc]\n  · rw [Matrix.det_fin_two]',1)
assert all('NONSTANDARD_AXIOMS' in x and 'error:' in x for x in logs[:2])
log=logs[-1]
assert not any(t in log for t in ['error:','sorryAx','NONSTANDARD_AXIOMS','maximum number of heartbeats','maximum recursion depth'])
assert 'AUDIT_OK TenthDiscriminant.CoordinateTranslation: 43 logical declarations; 38 theorems; 11 runtime-only auxiliaries excluded' in log
assert d['input_closures']=={'coordinate_translation_bridge':37660,'odd_order_norm_commutes':17619,'shifted_gram_counterexample':12095}
for theorem,count in d['input_closures'].items():
 assert f'PHASE105_INPUTS_OK TenthDiscriminant.CoordinateTranslation.{theorem}: {count} reached' in log
 assert re.search(re.escape("'TenthDiscriminant.CoordinateTranslation."+theorem+"' depends on axioms:")+r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]',log)
block=lambda s:s.split('let forbidden : Array Name := #[',1)[1].split('for name in forbidden do',1)[0]
names=lambda s:re.findall(r'``([A-Za-z0-9_.]+)',block(s))
extra=['EvenTwoClass.even_classNumber_gt_two','EvenTwoClass.even_radicand_bound','EvenTwoClass.even_discriminant_bound','EvenMinkowski.actual_minkowski','EvenMinkowski.normalized_actual_gram_budget','EvenMinkowski.scalar_actual_gram_budget','EvenSplitPrimeBudget.actual_gram_budget','EvenClassAggregation.prime_prefix_bound','EvenClassAggregation.uniform_two_class_bound','EvenPrimeFamily.controlled_family']
assert names(final)==names((p/'Phase104InputCheck.lean').read_text(encoding='utf-8'))+['TenthDiscriminant.'+n for n in extra]
assert len(names(final))==68
assert len((r/'README.md').read_text(encoding='utf-8').splitlines())==61
print('PASS: full coordinate and literal-shift compatibility;29full types/5complete definitions/4control expectations fixed;all3runs/two exact proof repairs preserved;43logical/38theorems/11runtime;standard3axioms/68exclusions/threefreshclosures;12raw;prior production/evidence frozen.')
print('Standalone only, all three attempt slots consumed: do not replay. PR36 CI/merge covers be1c0e3, not this new proof. No cutoff reduction or blanket Gram determinant invariance.')
