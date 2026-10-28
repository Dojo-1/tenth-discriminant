"""Check the saved first-run actual-field transport proof; never runs Lean."""
from pathlib import Path
import hashlib,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1];prefix='research/ender_radius_bridge/'
d=json.loads((p/'PHASE107_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,n:subprocess.check_output(['git','show',ref+':'+n],cwd=r)
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
for n in ['PHASE107_PROTOCOL.md','run_phase107.ps1']:assert blob(d['registered_commit'],prefix+n)==(p/n).read_bytes()
for group in ['sha256','frozen_sha256']:
 for n,h in d[group].items():assert sha((r/n).read_bytes())==h,n
with zipfile.ZipFile(p/d['archive']['path']) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==4
 raw={n:z.read(n) for n in z.namelist()}
assert sha((p/d['archive']['path']).read_bytes())==d['archive']['sha256']
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert len(d['runs'])==1
x=d['runs'][0];assert x['phase']==107 and x['mode']=='build' and x['attempt']==1 and x['exit_code']==0 and not x['stop_reason']
assert x['cumulative_before_seconds']==0 and x['time_limit_seconds']==600 and 0<x['elapsed_seconds']<600
assert x['memory_threshold_mb']==8192 and 0<x['observed_peak_working_set_bytes']<8192*1024**2
assert x['arguments']==['env','lean','-j','1','../research/ender_radius_bridge/Phase107EvenFieldTwoClass.lean']
stem=x['stdout'].removesuffix('.stdout.log')
assert json.loads(raw[stem+'.result.json'].decode('utf-8-sig'))==x
source=raw[x['source_snapshot']];assert sha(source)==x['source_sha256']
assert source==(p/'Phase107EvenFieldTwoClass.lean').read_bytes()
s=source.decode('utf-8');log=raw[x['stdout']].decode('utf-8-sig')
public=['even_chart_of_even_parameter','arbitrary_even_discriminant_bound','arbitrary_discriminant_bound','parity_refined_discriminant_bound','classNumber_gt_two_of_large_discriminant','even_parameter_control','odd_parameter_control','factor_four_control','odd_chart_exclusion_control']
assert re.findall(r'(?m)^theorem (\w+)',s)==public
assert not re.findall(r'(?m)^(?:def|abbrev|axiom|opaque) ',s)
assert not any(t in log for t in ['error:','sorryAx','NONSTANDARD_AXIOM','maximum number of heartbeats','maximum recursion depth'])
assert 'AUDIT_OK TenthDiscriminant.EvenFieldTwoClass: 11 logical declarations; 11 theorems; 0 runtime-only auxiliaries excluded' in log
ns='TenthDiscriminant.EvenFieldTwoClass.'
assert d['input_closures']=={'arbitrary_even_discriminant_bound':60578,'arbitrary_discriminant_bound':60689,'classNumber_gt_two_of_large_discriminant':60694}
for n,count in d['input_closures'].items():
 excluded=60 if n=='arbitrary_even_discriminant_bound' else 37
 assert f'PHASE107_INPUTS_OK {ns+n}: {count} reached; {excluded} forbidden roots excluded' in log
 assert re.search(re.escape("'"+ns+n+"' depends on axioms:")+r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]',log)
for n in public:assert ns+n in log
block=lambda text,tag:text.split('let '+tag+' : Array Name := #[',1)[1].split(']',1)[0]
names=lambda text,tag:re.findall(r'``([A-Za-z0-9_.]+)',block(text,tag))
a=names((p/'Phase88InputCheck.lean').read_text(encoding='utf-8'),'forbidden')
b=names((p/'Phase104InputCheck.lean').read_text(encoding='utf-8'),'forbidden')
assert len(a)==35 and len(b)==58 and b[:35]==a
assert names(s,'common')==a+['TenthDiscriminant.CoordinateTranslation.coordinate_translation_bridge','TenthDiscriminant.CoordinateTranslation.shifted_gram_counterexample']
assert names(s,'evenOnly')==b[35:]
assert 'then common++evenOnly else common' in s
assert 'let forbidden := if target==``'+ns+'arbitrary_even_discriminant_bound' in s
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow',prefix,'review','ledger','TAO_OBJECTIVE_AUDIT.md','TAO_OBJECTIVES_HISTORY.md','PRIOR_ART.md'],cwd=r,text=True).splitlines()
assert not set(changed).intersection(d['frozen_sha256'])
assert not any(n.startswith(('lean/','tools/','.github/','flow/','review/','ledger/')) and not n.endswith('.md') for n in changed)
assert len((r/'README.md').read_text(encoding='utf-8').splitlines())==61
# The separate timed-out CI remains a negative operational result, not green.
ci=json.loads((p/'PR37_CI_LIMIT_RECEIPT.json').read_text(encoding='utf-8'))
assert ci['head']==d['base'] and ci['conclusion']=='cancelled'
archive=p/'PR37_CI_LIMIT_EVIDENCE.zip';assert sha(archive.read_bytes())==ci['archive_sha256']
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None and set(z.namelist())=={'run','job','annotations','job.log'}
 evidence={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in evidence.items()}==ci['sha256']
assert json.loads(evidence['run'])['conclusion']=='cancelled'
job=json.loads(evidence['job']);assert job['conclusion']=='cancelled'
steps={x['name']:x['conclusion'] for x in job['steps']}
assert steps['Build exact statements']==steps['Reject incomplete or nonstandard proof dependencies']=='success'
assert steps['Require rejection of known-false strengthening attempts']=='cancelled'
assert any('maximum execution time of 25m0s' in x['message'] for x in json.loads(evidence['annotations']))
text=evidence['job.log'].decode('utf-8-sig')
assert text.index('PASS: mathematical controls, proof-audit probes, Gram, jet, multiplicity, degree, nonzero, affine and assembly controls.')<text.index('##[error]The operation was canceled.')
print('PASS: full arbitrary even-field transport/all-parity h<=2 bound; nine fixed public statements/four controls, zero definitions; FIRST full run100.7739366s;11logical/11theorems/0runtime,standard3;60even/37combined exclusions,three fresh closures;4raw;prior production/evidence frozen.')
print('Standalone only; no replay, root integration, external CI, cutoff optimization or full-classification claim. PR37 CI timeout remains a separate stopped record.')
