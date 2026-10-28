"""Check saved exact integration evidence; never runs Lean."""
from pathlib import Path
import hashlib,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1];prefix='research/ender_radius_bridge/'
d=json.loads((p/'PHASE108_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,n:subprocess.check_output(['git','show',ref+':'+n],cwd=r)
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
for n in ['PHASE108_PROTOCOL.md','run_phase108.ps1']:assert blob(d['registered_commit'],prefix+n)==(p/n).read_bytes()
for group in ['sha256','frozen_sha256']:
 for n,h in d[group].items():assert sha((r/n).read_bytes())==h,n
accepted=(p/'Phase107EvenFieldTwoClass.lean').read_text(encoding='utf-8');body,checker=accepted.split('open Lean Elab Command',1)
imports=''.join('import TenthDiscriminant.'+n+'\n' for n in ['EvenTwoClass','OddFieldTwoClass','AxiomAudit'])
assert (r/'lean/TenthDiscriminant/EvenFieldTwoClass.lean').read_text(encoding='utf-8')==body.replace('import TenthDiscriminant\n',imports,1)
assert (p/'Phase108InputCheck.lean').read_text(encoding='utf-8')=='import TenthDiscriminant\n\nopen Lean Elab Command'+checker.replace('phase107','phase108').replace('PHASE107','PHASE108')
assert (r/'lean/TenthDiscriminant.lean').read_text(encoding='utf-8')==blob(d['base'],'lean/TenthDiscriminant.lean').decode().replace('\r\n','\n')+'import TenthDiscriminant.EvenFieldTwoClass\n'
a=p/d['archive']['path'];assert sha(a.read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(a) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==25
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert set(d['runs'])=={'build','root','input','audit'}
args={'build':['build','TenthDiscriminant.EvenFieldTwoClass'],'root':'build','input':['env','lean','-j','1','../research/ender_radius_bridge/Phase108InputCheck.lean'],'audit':['env','lean','-j','1','Audit.lean']}
logs={}
for mode,x in d['runs'].items():
 assert x['phase']==108 and x['mode']==mode and x['attempt']==1 and x['exit_code']==0 and not x['stop_reason']
 assert x['cumulative_before_seconds']==0 and x['time_limit_seconds']=={'build':600,'root':1200,'input':180,'audit':180}[mode]
 assert 0<x['elapsed_seconds']<x['time_limit_seconds'] and x['memory_threshold_mb']==8192
 assert 0<x['observed_peak_working_set_bytes']<8192*1024**2 and x['arguments']==args[mode]
 stem=x['stdout'].removesuffix('.stdout.log');assert json.loads(raw[stem+'.result.json'].decode('utf-8-sig'))==x
 for suf,n in [('.source.lean','lean/TenthDiscriminant/EvenFieldTwoClass.lean'),('.root.lean','lean/TenthDiscriminant.lean'),('.input.lean',prefix+'Phase108InputCheck.lean')]:assert raw[stem+suf]==(r/n).read_bytes()
 assert sha(raw[x['source_snapshot']])==x['source_sha256']
 logs[mode]=raw[x['stdout']].decode('utf-8-sig')
 assert not any(t in logs[mode] for t in ['error:','sorryAx','NONSTANDARD_AXIOM','maximum number of heartbeats','maximum recursion depth'])
assert '11 logical declarations; 11 theorems; 0 runtime-only auxiliaries excluded' in logs['build']
for n,count in d['input_closures'].items():assert f'PHASE108_INPUTS_OK TenthDiscriminant.EvenFieldTwoClass.{n}: {count} reached' in logs['input']
assert d['input_closures']=={'arbitrary_even_discriminant_bound':60578,'arbitrary_discriminant_bound':60689,'classNumber_gt_two_of_large_discriminant':60694}
assert len(re.findall(r'``TenthDiscriminant\.[A-Za-z0-9_.]+',checker.split('  let evenOnly')[0]))==37
assert len(re.findall(r'``TenthDiscriminant\.[A-Za-z0-9_.]+',checker.split('  let evenOnly')[1].split('  let forbidden')[0]))==23
assert 'then common++evenOnly else common' in checker
assert d['whole_audit_marker'] in logs['audit']
assert '5361 logical declarations; 4565 theorems; 17015 runtime-only auxiliaries excluded' in logs['audit']
assert 'IMPORT_COVERAGE_OK: 197 project modules reachable' in raw['PHASE108_SOURCE_CHECKS.log'].decode()
assert 'all 250 interval pairs match' in raw['PHASE108_SOURCE_CHECKS.log'].decode()
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github'],cwd=r,text=True).splitlines()
assert set(n for n in changed if not n.endswith('.md'))<={'lean/TenthDiscriminant.lean','lean/TenthDiscriminant/EvenFieldTwoClass.lean'}
assert not set(changed).intersection(d['frozen_sha256'])
assert len((r/'README.md').read_text(encoding='utf-8').splitlines())==61
print('PASS: exact accepted9statements/proofs,0definitions,4controls/reports;ONErootimport;60even/37combined exclusions/threefreshclosures;four first checks;25raw;prior evidence frozen. No standalone replay or cutoff reduction.')
print(d['whole_audit_marker'])
