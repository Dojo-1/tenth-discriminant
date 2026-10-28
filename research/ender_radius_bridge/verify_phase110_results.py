"""Verify saved full passive polynomial/jet/Gram transport; never executes Lean."""
from pathlib import Path
import hashlib,json,math,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1];prefix='research/ender_radius_bridge/'
d=json.loads((p/'PHASE110_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,n:subprocess.check_output(['git','show',ref+':'+n],cwd=r)
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
for n in ['PHASE110_PROTOCOL.md','run_phase110.ps1']:assert blob(d['registered_commit'],prefix+n)==(p/n).read_bytes()
for group in ['sha256','frozen_sha256']:
 for n,h in d[group].items():assert sha((r/n).read_bytes())==h,n
archive=p/d['archive']['path'];assert sha(archive.read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==12
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert len(d['runs'])==3
sources=[];logs=[];spent=0
for i,x in enumerate(d['runs'],1):
 assert x['phase']==110 and x['mode']=='build' and x['attempt']==i
 assert x['exit_code']==(0 if i==3 else 1) and not x['stop_reason']
 assert abs(x['cumulative_before_seconds']-spent)<1e-8
 assert x['time_limit_seconds']==min(600,math.floor(1200-spent))
 assert 0<x['elapsed_seconds']<x['time_limit_seconds'] and x['memory_threshold_mb']==8192
 assert 0<x['observed_peak_working_set_bytes']<8192*1024**2
 assert x['arguments']==['env','lean','-j','1','../research/ender_radius_bridge/Phase110PassiveTransport.lean']
 stem=x['stdout'].removesuffix('.stdout.log');assert json.loads(raw[stem+'.result.json'].decode('utf-8-sig'))==x
 assert sha(raw[x['source_snapshot']])==x['source_sha256']
 sources.append(raw[x['source_snapshot']].decode('utf-8'));logs.append(raw[x['stdout']].decode('utf-8-sig'));spent+=x['elapsed_seconds']
assert spent<1200
first,second,final=sources
assert final==(p/'Phase110PassiveTransport.lean').read_text(encoding='utf-8')
headers=lambda text:[text[m.start():text.index(':= by',m.start())] for m in re.finditer(r'(?m)^theorem \w+',text)]
for text in sources:
 assert len(headers(text))==20 and headers(text)==headers(first)
 assert re.findall(r'(?m)^def (\w+)',text)==['translate','polynomialJet','monomialRow','polynomialGram']
 for name in ['translate','polynomialJet','monomialRow','polynomialGram']:
  pattern=r'(?ms)^def '+name+r'\b.*?(?=\n(?:private theorem|theorem|def)\b)'
  assert re.search(pattern,text).group()==re.search(pattern,first).group()
# Reconstruct the exact two allowed proof-only repairs. All control scripts stayed fixed.
s=first.replace('  simp [translate,h]\n','  unfold translate\n  simp only [neg_zero,Polynomial.C_0]\n  rw [h]\n  simp\n',1)
s=s.replace('  simp only [Polynomial.taylorAlgHom_apply,Polynomial.taylor_C]\n','  have hc : (Polynomial.taylorAlgHom (-b)).toRingHom (Polynomial.C (-c))=Polynomial.C (-c) := by\n    change Polynomial.taylor (-b) (Polynomial.C (-c))=Polynomial.C (-c)\n    simp\n  rw [hc]\n',1)
s=s.replace('  simp only [Polynomial.eval_C,Polynomial.map_map,hc]\n','  simp only [Polynomial.coe_evalRingHom,Polynomial.eval_C,Polynomial.map_map,hc]\n',1)
s=s.replace('  rw [CoordinateTranslation.shifted_points,polynomialGram_translation,monomial_gram_eq]\n  exact (integerRectangularTraceGram_cast Q D J R S hD).symm','  rw [CoordinateTranslation.shifted_points,polynomialGram_translation,\n    monomial_gram_eq _ _ (fun i : Fin (R*S) => (i.val/S,i.val%S))]\n  exact (integerRectangularTraceGram_cast Q D J R S hD).symm',1)
s=s.replace('    rw [CoordinateTranslation.shifted_points,polynomialGram_translation,monomial_gram_eq]\n    rfl\n','    rw [CoordinateTranslation.shifted_points,polynomialGram_translation]\n    exact monomial_gram_eq _ _ (fun i : Fin (R*S) => (i.val/S,i.val%S))\n',1)
assert s==second
assert final==second.replace('    simp [neg_add]\n','    simp [neg_add,add_comm]\n',1)
assert all('error:' in text and 'NONSTANDARD_AXIOMS' in text for text in logs[:2])
log=logs[-1]
assert not any(t in log for t in ['error:','sorryAx','NONSTANDARD_AXIOM','maximum number of heartbeats','maximum recursion depth'])
assert 'AUDIT_OK TenthDiscriminant.PassiveTransport: 31 logical declarations; 27 theorems; 0 runtime-only auxiliaries excluded' in log
assert d['input_closures']=={'jet_covariance':5880,'passive_integer_cast':13936,'passive_translation_bridge':33095}
ns='TenthDiscriminant.PassiveTransport.'
for n,count in d['input_closures'].items():
 assert f'PHASE110_INPUTS_OK {ns+n}: {count} reached;70forbidden roots excluded' in log
 assert re.search(re.escape("'"+ns+n+"' depends on axioms:")+r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]',log)
block=lambda text:text.split('let forbidden : Array Name := #[',1)[1].split('for name in forbidden do',1)[0]
names=lambda text:re.findall(r'``([A-Za-z0-9_.]+)',block(text))
old=names((p/'Phase104InputCheck.lean').read_text(encoding='utf-8'))
extra=['EvenTwoClass.'+n for n in ['even_classNumber_gt_two','even_radicand_bound','even_discriminant_bound']]+['EvenFieldTwoClass.'+n for n in ['arbitrary_even_discriminant_bound','arbitrary_discriminant_bound','parity_refined_discriminant_bound','classNumber_gt_two_of_large_discriminant']]+['CoordinateTranslation.'+n for n in ['coordinate_translation_bridge','shifted_gram_cast','shifted_posDef','shifted_valuation','shifted_gram_counterexample']]
assert names(final)==old+['TenthDiscriminant.'+n for n in extra] and len(names(final))==70
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow',prefix,'review','ledger','TAO_OBJECTIVE_AUDIT.md','TAO_OBJECTIVES_HISTORY.md','PRIOR_ART.md'],cwd=r,text=True).splitlines()
assert not set(changed).intersection(d['frozen_sha256'])
assert not any(n.startswith(('lean/','tools/','.github/','flow/','review/','ledger/')) and not n.endswith('.md') for n in changed)
assert len((r/'README.md').read_text(encoding='utf-8').splitlines())==61
assert len((r/'TAO_OBJECTIVES_CURRENT.md').read_text(encoding='utf-8').splitlines())==61
print('PASS: full passive polynomial/ordinary-jet/same-integer-Gram transport;20full types/4complete definitions/4controls fixed;two exact proof repairs;ALL3slots consumed;31logical/27theorems/0runtime;standard3axioms/70exclusions/threefreshclosures;12raw;prior production/evidence frozen.')
print('Standalone only, NO REPLAY. No replacement matrix, new cutoff, computational-hardness theorem, root integration or external CI for this new source.')
