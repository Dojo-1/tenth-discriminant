"""Verify saved exact production integration; never executes Lean."""
from pathlib import Path
import hashlib,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
d=json.loads((p/'PHASE98_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,n:subprocess.check_output(['git','show',ref+':'+n],cwd=r)
prefix='research/ender_radius_bridge/'
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
for n in ['PHASE98_PROTOCOL.md','run_phase98.ps1']:
 assert blob(d['registered_commit'],prefix+n)==(p/n).read_bytes()
for n,h in d['sha256'].items():assert sha((r/n).read_bytes())==h,n
for n,h in d['frozen_sha256'].items():assert sha((r/n).read_bytes())==h,n
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow',prefix,'review','ledger','TAO_OBJECTIVE_AUDIT.md','TAO_OBJECTIVES_HISTORY.md','PRIOR_ART.md'],cwd=r,text=True).splitlines()
assert not set(changed).intersection(d['frozen_sha256'])
production=[n for n in changed if n.startswith(('lean/','tools/','.github/','flow/')) and not n.endswith('.md')]
assert set(production)=={'lean/TenthDiscriminant.lean','lean/TenthDiscriminant/EvenClassAggregation.lean'}
source=(r/'lean/TenthDiscriminant/EvenClassAggregation.lean').read_text(encoding='utf-8')
accepted=(p/'Phase97EvenClassAggregation.lean').read_text(encoding='utf-8')
body,checker=accepted.split('open Lean Elab Command',1)
assert source==body.replace('import TenthDiscriminant\n','import TenthDiscriminant.EvenPrimeFamily\nimport TenthDiscriminant.ClassAggregation\n',1)
headers=lambda s:{m.group(1):s[m.start():s.index(':=',m.start())] for m in re.finditer(r'(?m)^theorem (\w+)',s)}
assert headers(source)==headers(accepted) and len(headers(source))==6
assert re.findall(r'(?m)^def (\w+)',source)==[]
root=blob(d['base'],'lean/TenthDiscriminant.lean').decode('utf-8').replace('\r\n','\n')
assert root+'import TenthDiscriminant.EvenClassAggregation\n'==(r/'lean/TenthDiscriminant.lean').read_text(encoding='utf-8')
inputs=(p/'Phase98InputCheck.lean').read_text(encoding='utf-8')
block=lambda s:s.split('let forbidden : Array Name := #[',1)[1].split('for name in forbidden do',1)[0]
names=lambda s:re.findall(r'``([A-Za-z0-9_.]+)',block(s))
assert names(inputs)==names(accepted) and len(names(inputs))==49
archive=p/d['archive']['path'];assert sha(archive.read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==25
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert set(d['runs'])=={'build','root','input','audit'}
for mode,x in d['runs'].items():
 assert x['phase']==98 and x['mode']==mode and x['attempt']==1 and x['exit_code']==0
 assert not x['stop_reason'] and x['cumulative_before_seconds']==0
 assert x['time_limit_seconds']=={'build':600,'root':1200,'input':180,'audit':180}[mode]
 assert 0<x['elapsed_seconds']<x['time_limit_seconds']
 assert x['memory_threshold_mb']==8192 and 0<x['observed_peak_working_set_bytes']<8192*1024**2
 stem=x['stdout'].removesuffix('.stdout.log')
 assert json.loads(raw[stem+'.result.json'].decode('utf-8-sig'))==x
 for suffix,path in [('source','lean/TenthDiscriminant/EvenClassAggregation.lean'),('root','lean/TenthDiscriminant.lean'),('input',prefix+'Phase98InputCheck.lean')]:
  assert raw[stem+'.'+suffix+'.lean']==(r/path).read_bytes()
 assert sha(raw[x['source_snapshot']])==x['source_sha256']
 log=raw[x['stdout']].decode('utf-8-sig')
 assert not any(s in log for s in ['error:','sorryAx','NONSTANDARD_AXIOMS','maximum number of heartbeats','maximum recursion depth'])
build=raw[d['runs']['build']['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant.EvenClassAggregation: 6 logical declarations; 6 theorems; 0 runtime-only' in build
log=raw[d['runs']['input']['stdout']].decode('utf-8-sig')
assert f"PHASE98_INPUTS_OK TenthDiscriminant.EvenClassAggregation.uniform_two_class_bound: {d['input_closure']} reached" in log
assert re.search(r"'TenthDiscriminant.EvenClassAggregation.uniform_two_class_bound' depends on axioms:\s*\[propext,\s*Classical.choice,\s*Quot.sound\]",log)
audit=raw[d['runs']['audit']['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant: 5253 logical declarations; 4465 theorems; 17004 runtime-only' in audit
struct=raw['PHASE98_SOURCE_CHECKS.log'].decode('utf-8-sig')
assert '192 project modules reachable; no source escapes' in struct and 'all 250 interval pairs' in struct
assert len((r/'README.md').read_text(encoding='utf-8').splitlines())==61
# Preserve the accepted standalone boundary byte-exact, including its blank EOF line.
ws=subprocess.run(['git','diff','--check',d['base'],'--','lean/TenthDiscriminant/EvenClassAggregation.lean'],cwd=r,capture_output=True,text=True)
assert ws.returncode==2 and ws.stdout.strip()=='lean/TenthDiscriminant/EvenClassAggregation.lean:114: new blank line at EOF.' and not ws.stderr
print('PASS: exact97to98 mathematical/control/report transport;6public types/0defs unchanged;ONErootimport;all4firstinvocationsPASS;25raw;192modules/250endpointidentities;49exclusions;5253/4465/17004standard3axioms;prior evidence frozen.')
print('No standalone97replay. Even cutoff, external exact-head CI and independent human review remain open.')
