"""Check saved exact integration evidence; never runs Lean."""
from pathlib import Path
import hashlib,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1];prefix='research/ender_radius_bridge/'
d=json.loads((p/'PHASE111_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,n:subprocess.check_output(['git','show',ref+':'+n],cwd=r)
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
for n in ['PHASE111_PROTOCOL.md','run_phase111.ps1']:assert blob(d['registered_commit'],prefix+n)==(p/n).read_bytes()
for group in ['sha256','frozen_sha256']:
 for n,h in d[group].items():assert sha((r/n).read_bytes())==h,n
accepted=(p/'Phase110PassiveTransport.lean').read_text(encoding='utf-8');body,checker=accepted.split('open Lean Elab Command',1)
imports=''.join('import TenthDiscriminant.'+n+'\n' for n in ['CoordinateTranslation'])
assert (r/'lean/TenthDiscriminant/PassiveTransport.lean').read_text(encoding='utf-8')==body.replace('import TenthDiscriminant\n',imports,1)
assert (p/'Phase111InputCheck.lean').read_text(encoding='utf-8')=='import TenthDiscriminant\n\nopen Lean Elab Command'+checker.replace('phase110','phase111').replace('PHASE110','PHASE111')
assert (r/'lean/TenthDiscriminant.lean').read_text(encoding='utf-8')==blob(d['base'],'lean/TenthDiscriminant.lean').decode().replace('\r\n','\n')+'import TenthDiscriminant.PassiveTransport\n'
a=p/d['archive']['path'];assert sha(a.read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(a) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==25
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert set(d['runs'])=={'build','root','input','audit'}
args={'build':['build','TenthDiscriminant.PassiveTransport'],'root':'build','input':['env','lean','-j','1','../research/ender_radius_bridge/Phase111InputCheck.lean'],'audit':['env','lean','-j','1','Audit.lean']}
logs={}
for mode,x in d['runs'].items():
 assert x['phase']==111 and x['mode']==mode and x['attempt']==1 and x['exit_code']==0 and not x['stop_reason']
 assert x['cumulative_before_seconds']==0 and x['time_limit_seconds']=={'build':600,'root':1200,'input':180,'audit':180}[mode]
 assert 0<x['elapsed_seconds']<x['time_limit_seconds'] and x['memory_threshold_mb']==8192
 assert 0<x['observed_peak_working_set_bytes']<8192*1024**2 and x['arguments']==args[mode]
 stem=x['stdout'].removesuffix('.stdout.log');assert json.loads(raw[stem+'.result.json'].decode('utf-8-sig'))==x
 for suf,n in [('.source.lean','lean/TenthDiscriminant/PassiveTransport.lean'),('.root.lean','lean/TenthDiscriminant.lean'),('.input.lean',prefix+'Phase111InputCheck.lean')]:assert raw[stem+suf]==(r/n).read_bytes()
 assert sha(raw[x['source_snapshot']])==x['source_sha256']
 logs[mode]=raw[x['stdout']].decode('utf-8-sig')
 assert not any(t in logs[mode] for t in ['error:','sorryAx','NONSTANDARD_AXIOM','maximum number of heartbeats','maximum recursion depth'])
assert '31 logical declarations; 27 theorems; 0 runtime-only auxiliaries excluded' in logs['build']
for n,count in d['input_closures'].items():assert f'PHASE111_INPUTS_OK TenthDiscriminant.PassiveTransport.{n}: {count} reached' in logs['input']
assert d['input_closures']=={'jet_covariance':5880,'passive_integer_cast':13936,'passive_translation_bridge':33095}
assert len(re.findall(r'``TenthDiscriminant\.[A-Za-z0-9_.]+',checker.split('for name in forbidden do')[0]))==70
assert d['whole_audit_marker'] in logs['audit']
assert '5393 logical declarations; 4593 theorems; 17015 runtime-only auxiliaries excluded' in logs['audit']
assert 'IMPORT_COVERAGE_OK: 198 project modules reachable' in raw['PHASE111_SOURCE_CHECKS.log'].decode()
# Explain the global inventory delta, including the existing rowSection equation.
with zipfile.ZipFile(p/'PR38_CI_EVIDENCE.zip') as z:
 old=z.read('job.log').decode('utf-8-sig')
start=old.index('IMPORT_COVERAGE_OK:');end=old.index('AUDIT_OK TenthDiscriminant:',start)
names=lambda text:set(re.findall(r'DEPENDENCIES_CHECKED ([^;\s]+)',text))
old_names=names(old[start:end]);new_names=names(logs['audit'])
namespace={n for n in names(logs['build']) if n.startswith('TenthDiscriminant.PassiveTransport.') or n.startswith('_private.TenthDiscriminant.PassiveTransport.')}
assert len(old_names)==5361 and len(new_names)==5393 and len(namespace)==31
assert not old_names-new_names
assert new_names-old_names==namespace|{'TenthDiscriminant.rowSection.eq_1'}
assert 'all 250 interval pairs match' in raw['PHASE111_SOURCE_CHECKS.log'].decode()
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github'],cwd=r,text=True).splitlines()
assert set(n for n in changed if not n.endswith('.md'))<={'lean/TenthDiscriminant.lean','lean/TenthDiscriminant/PassiveTransport.lean'}
assert not set(changed).intersection(d['frozen_sha256'])
assert len((r/'README.md').read_text(encoding='utf-8').splitlines())==61
print('PASS: exact accepted20statements/proofs,4definitions,4controls/reports;ONErootimport;70exclusions/threefreshclosures;four first checks;25raw;prior evidence frozen. No standalone replay or cutoff reduction.')
print(d['whole_audit_marker'])
