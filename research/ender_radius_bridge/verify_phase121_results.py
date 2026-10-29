"""Verify exact unchanged production integration and preserved first-run evidence."""
from pathlib import Path
import hashlib,importlib.util,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
git=lambda *args,**kw:subprocess.check_output(['git',*args],cwd=r,**kw)
d=json.loads((p/'PHASE121_RESULTS.json').read_bytes())
assert d['status']=='EXACT_48B_INTEGRATION_ALL_FOUR_FIRST_CHECKS_PASS'
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
assert git('show',d['registered_commit']+':research/ender_radius_bridge/PHASE121_PROTOCOL.md')==(p/'PHASE121_PROTOCOL.md').read_bytes()
for n,h in d['sha256'].items():assert sha((r/n).read_bytes())==h,n
c=json.loads((p/'PHASE121_CORRESPONDENCE.json').read_bytes());assert c['modules']==d['modules']
for name,x in c['modules'].items():
    old=git('show',d['accepted_commit']+':'+x['accepted_path']);a,b=x['body_range'];body=old[a:b]
    assert sha(old)==x['accepted_sha256'] and sha(body)==x['body_sha256']
    assert body.endswith(('end TenthDiscriminant.'+name+'\n').encode())
    expected=(''.join('import TenthDiscriminant.'+i+'\n' for i in x['imports'])+'\n').encode()+body
    assert (r/x['path']).read_bytes()==expected and sha(expected)==x['source_sha256']
root=git('show',d['registered_commit']+':lean/TenthDiscriminant.lean')+''.join('import TenthDiscriminant.'+n+'\n' for n in c['modules']).encode()
assert (r/'lean/TenthDiscriminant.lean').read_bytes()==root
harness=(p/'Phase121InputCheck.lean').read_bytes();assert sha(harness)==c['harness_sha256']
assert harness.count(b'#check ')==56 and harness.count(b'#print ')==6 and harness.count(b'#audit_namespace ')==3
assert sha((p/d['archive']['path']).read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(p/d['archive']['path']) as z:
    assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==33
    raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert raw['PHASE121_CORRESPONDENCE.json']==(p/'PHASE121_CORRESPONDENCE.json').read_bytes()
caps={'build':600,'root':1200,'input':180,'audit':180}
args={'build':['build','TenthDiscriminant.RadialCutoff'],'root':'build',
 'input':['env','lean','-j','1','../research/ender_radius_bridge/Phase121InputCheck.lean'],
 'audit':['env','lean','-j','1','Audit.lean']}
logs={}
assert set(d['runs'])==set(caps)
for mode,x in d['runs'].items():
    assert len(list(p.glob('PHASE121_'+mode+'_*.result.json')))==1
    assert x['phase']==121 and x['mode']==mode and x['attempt']==1 and x['exit_code']==0 and not x['stop_reason']
    assert x['time_limit_seconds']==caps[mode] and x['memory_threshold_mb']==8192 and x['cumulative_before_seconds']==0
    assert 0<x['elapsed_seconds']<caps[mode] and 0<x['observed_peak_working_set_bytes']<8192*1024**2
    assert x['arguments']==args[mode]
    for name,n in x['source_snapshots'].items():
        assert raw[n]==(r/c['modules'][name]['path']).read_bytes()
        assert sha(raw[n])==x['source_sha256'][name]
    assert raw[x['root_snapshot']]==root and raw[x['input_snapshot']]==harness
    prefix=x['root_snapshot'].removesuffix('.root.lean')
    assert json.loads(raw[prefix+'.result.json'])==x and raw[x['stderr']]==b''
    log=raw[x['stdout']].decode('utf-8-sig');logs[mode]=log
    assert ': error:' not in log and 'NONSTANDARD_AXIOMS' not in log
    assert not re.search(r'maximum number of heartbeats|maximum recursion depth|deterministic.*timeout',log)
    if mode in ('build','root'):assert 'Build completed successfully.' in log
for name,x in d['observed_namespaces'].items():
    assert f"AUDIT_OK TenthDiscriminant.{name}: {x['logical']} logical declarations; {x['theorems']} theorems; {x['runtime_auxiliaries']} runtime-only auxiliaries excluded" in logs['input']
for kind,roots in d['fresh_closures'].items():
    limit=70 if kind=='GEOM' else 73
    assert len(roots)==(6 if kind=='GEOM' else 3)
    assert logs['input'].count('PHASE121_'+kind+'_INPUTS_OK ')==len(roots)
    for n,count in roots.items():
        m=re.search(rf'PHASE121_{kind}_INPUTS_OK {re.escape(n)}: {count} reached;{limit}forbidden roots excluded;axioms \[([^]]+)\]',logs['input'])
        assert m and set(re.findall(r'[\w.]+',m[1]))=={'propext','Quot.sound','Classical.choice'}
extract_policy=lambda s:s[s.index('  let forbidden : Array Name := #['):s.index('  for name in forbidden do')]
geom=harness.decode().split('elab "#phase121_geom_inputs ',1)[1].split('elab "#phase121_arith_inputs ',1)[0]
arith=harness.decode().split('elab "#phase121_arith_inputs ',1)[1]
for part,filename in [(geom,'Phase119RadialDetBound.lean'),(arith,'Phase120RadialCutoff.lean')]:
    assert extract_policy(part)==extract_policy(git('show',d['accepted_commit']+':research/ender_radius_bridge/'+filename).decode())
assert d['whole_audit_marker'] in logs['audit']
extract=lambda s:set(re.findall(r'DEPENDENCIES_CHECKED ([^;]+);',s))
with zipfile.ZipFile(p/'PHASE117_RAW.zip') as z:
    old=extract(z.read(next(n for n in z.namelist() if '_audit_' in n and n.endswith('.stdout.log'))).decode('utf-8-sig'))
new=extract(logs['audit']);added=sorted(new-old);removed=sorted(old-new)
assert len(old)==5450 and len(new)==5584 and len(added)==134 and not removed
assert added==c['inventory']['added'] and removed==c['inventory']['removed']
outside=[n for n in added if not any('TenthDiscriminant.'+m+'.' in n for m in c['modules'])]
assert outside==['TenthDiscriminant.exactOddPrimeMass.eq_1']
assert c['inventory']['compiler_generated_surplus']==['TenthDiscriminant.RadialJetMajorant.jet.eq_1','TenthDiscriminant.exactOddPrimeMass.eq_1']
assert all(n in added for n in c['inventory']['compiler_generated_surplus'])
spec=importlib.util.spec_from_file_location('phase121_coverage_saved',r/'lean/audit.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
assert len(module.project_coverage(r/'lean'))==d['reachable_modules']==202
frozen={}
for rec in git('ls-tree','-r','-z',d['registered_commit']).split(b'\0'):
    if not rec:continue
    meta,n=rec.split(b'\t',1);n=n.decode()
    if n.startswith('.agent/') or n in d['reader_exceptions'] or n=='lean/TenthDiscriminant.lean':continue
    frozen[n]=meta.split()[2].decode()
assert len(frozen)==d['frozen_files']==1806
names=sorted(frozen);hashes=git('hash-object','--stdin-paths',input=('\n'.join(names)+'\n').encode()).decode().splitlines()
assert len(names)==len(hashes)
for n,h in zip(names,hashes):assert h==frozen[n],n
# Historical reader hashes are checked against their accepted snapshot.
historical=json.loads((p/'PHASE120_RESULTS.json').read_bytes())
for n,h in historical['sha256'].items():assert sha(git('show',d['accepted_commit']+':'+n))==h,n
assert d['integrated_actual_field_cutoff']==48000000000
print('PASS saved121:3exact modules/56written types/6data;4FIRSTCHECKS;9fresh closures;5584logical/4772theorems;134added/0removed including2generated surplus;33raw;1806frozen Git blobs;202modules. Publication gates separate.')
