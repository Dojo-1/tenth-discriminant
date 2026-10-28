"""Verify bounded scheduling evidence and unchanged inherited gates; never executes Lean."""
from pathlib import Path
import ast,hashlib,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1];prefix='research/ender_radius_bridge/'
d=json.loads((p/'PHASE109_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,n:subprocess.check_output(['git','show',ref+':'+n],cwd=r)
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
assert blob(d['registered_commit'],prefix+'PHASE109_PROTOCOL.md')==(p/'PHASE109_PROTOCOL.md').read_bytes()
for group in ['sha256','frozen_sha256']:
 for n,h in d[group].items():assert sha((r/n).read_bytes())==h,n
old=blob(d['base'],'lean/negative_controls.py').decode('utf-8').replace('\r\n','\n')
new=(r/'lean/negative_controls.py').read_text(encoding='utf-8')
start=old.index("subprocess.run([sys.executable, str(root / 'exact_gram_controls.py')]")
end=old.index("print('PASS: mathematical controls",start)
old_calls=ast.parse(old[start:end]).body
jobs=[]
for node in old_calls:
 call=node.value;assert isinstance(call,ast.Call) and ast.unparse(call.func)=='subprocess.run'
 assert ast.unparse(call.args[0].elts[0])=='sys.executable'
 wrapped=call.args[0].elts[1];assert ast.unparse(wrapped.func)=='str'
 path=wrapped.args[0];assert ast.unparse(path.left)=='root' and isinstance(path.op,ast.Div)
 kw={k.arg:k.value for k in call.keywords};assert ast.unparse(kw['cwd'])=='root' and ast.literal_eval(kw['check']) is True
 jobs.append((ast.literal_eval(path.right),ast.literal_eval(kw['timeout'])))
expected=[('exact_gram_controls.py',120),('jet_uniqueness_controls.py',120),('jet_negative_controls.py',120),('multiplicity_negative_controls.py',120),('degree_negative_controls.py',240),('nonzero_negative_controls.py',360),('affine_negative_controls.py',240),('assembly_negative_controls.py',360)]
assert jobs==expected
calls=[n for n in ast.walk(ast.parse(new)) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='run_families']
assert len(calls)==1 and ast.unparse(calls[0].args[0])=='root' and ast.literal_eval(calls[0].args[1])==expected
prefix_new=new[:new.index('run_families(root, [')]
prefix_new=prefix_new.replace('from control_schedule import run_families\n','',1)
prefix_new=prefix_new.replace("subprocess.run([sys.executable, str(root / 'control_schedule_tests.py')],\n               cwd=root, check=True, timeout=120)\n",'',1)
assert prefix_new==old[:start]
assert new[new.index("print('PASS: mathematical controls"):]==old[end:]
helper=ast.parse((r/'lean/control_schedule.py').read_text(encoding='utf-8'))
pools=[n for n in ast.walk(helper) if isinstance(n,ast.Call) and ast.unparse(n.func)=='ThreadPoolExecutor']
assert len(pools)==1 and {k.arg:ast.literal_eval(k.value) for k in pools[0].keywords}=={'max_workers':2}
ci=blob(d['base'],'.github/workflows/lean.yml');assert ci==(r/'.github/workflows/lean.yml').read_bytes() and b'timeout-minutes: 25' in ci
archive=p/d['archive']['path'];assert sha(archive.read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==6
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert len(d['runs'])==1;x=d['runs'][0]
assert x['phase']==109 and x['attempt']==1 and x['exit_code']==0 and not x['stop_reason']
assert x['time_limit_seconds']==120 and 0<x['elapsed_seconds']<120 and x['observed_peak_memory']=='UNOBSERVED'
assert x['command'][1:]==['control_schedule_tests.py'] and x['cwd']=='lean'
stem=x['stdout'].removesuffix('.stdout.log');assert json.loads(raw[stem+'.result.json'])==x
for snapshot,h in x['source_sha256'].items():
 assert sha(raw[snapshot])==h
 name=snapshot.removeprefix(stem+'.');assert raw[snapshot]==(r/'lean'/name).read_bytes()
log=raw[x['stderr']].decode('utf-8');assert 'Ran 6 tests' in log and 'OK' in log and 'FAILED' not in log
assert log.count(' ... ok')==6
assert len((r/'README.md').read_text(encoding='utf-8').splitlines())==61
assert len((r/'TAO_OBJECTIVES_CURRENT.md').read_text(encoding='utf-8').splitlines())==61
print('PASS: same8families/arguments/timeouts/order;legacy pairs/probes and child bytes unchanged;max2worker cap;six synthetic tests FIRST PASS;6raw;mathematical source/root/pins/workflow25m and prior evidence frozen.')
print('Synthetic evidence is not Lean/CI success. One separately registered publication CI on the new actual-field source remains to be recorded; stopped PR37 remains cancelled.')
