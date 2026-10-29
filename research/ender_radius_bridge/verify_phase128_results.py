"""Verify saved Phase128 evidence, without rerunning a theorem or experiment."""
from pathlib import Path
import hashlib,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
d=json.loads((p/'PHASE128_RESULTS.json').read_bytes())
c=json.loads((p/'PHASE128_CORRESPONDENCE.json').read_bytes())
assert d['status']=='EXACT_INTEGRATION_ALL_FOUR_FIRST_CHECKS_PASS'
assert sha((p/'PHASE128_RAW.zip').read_bytes())==d['archive_sha256']
with zipfile.ZipFile(p/'PHASE128_RAW.zip') as z:
    assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==33
    raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert raw['PHASE128_CORRESPONDENCE.json']==(p/'PHASE128_CORRESPONDENCE.json').read_bytes()
for new,x in c['modules'].items():
    src=subprocess.check_output(['git','show',x['accepted_commit']+':'+x['accepted_path']],cwd=r)
    assert sha(src)==x['accepted_sha256'];a,b=x['body_range'];body=src[a:b]
    assert sha(body)==x['body_sha256']
    expected=(''.join('import TenthDiscriminant.'+n+'\n' for n in x['imports'])+'\n').encode()+body.replace(x['old_namespace'].encode(),new.encode())
    assert (r/x['path']).read_bytes()==expected and sha(expected)==x['source_sha256']
logs={};caps={'build':600,'root':1200,'input':240,'audit':180}
for mode,cap in caps.items():
    assert len(list(p.glob(f'PHASE128_{mode}_*.result.json')))==1
    x=d['runs'][mode];assert x['phase']==128 and x['mode']==mode and x['attempt']==1
    assert x['exit_code']==0 and not x['stop_reason'] and x['time_limit_seconds']==cap
    assert x['memory_threshold_mb']==8192 and 0<x['elapsed_seconds']<cap
    assert 0<x['observed_peak_working_set_bytes']<8192*1024**2
    for n,f in x['source_snapshots'].items():assert raw[f]==(r/c['modules'][n]['path']).read_bytes()
    assert raw[x['root_snapshot']]==(r/'lean/TenthDiscriminant.lean').read_bytes()
    assert raw[x['input_snapshot']]==(p/'Phase128InputCheck.lean').read_bytes()
    stem=x['root_snapshot'].removesuffix('.root.lean');assert json.loads(raw[stem+'.result.json'])==x
    assert raw[x['stderr']]==b''
    logs[mode]=raw[x['stdout']].decode('utf-8-sig')
    assert not re.search(r': error:|maximum number of heartbeats|maximum recursion depth|deterministic.*timeout',logs[mode])
    if mode in ('build','root'):assert 'Build completed successfully.' in logs[mode]
for n,x in d['namespace_audits'].items():
    assert f"AUDIT_OK TenthDiscriminant.{n}: {x['logical']} logical declarations; {x['theorems']} theorems; {x['runtime']} runtime-only auxiliaries excluded" in logs['input']
for num,count in [(125,3),(126,2),(127,3)]:
    matches=re.findall(rf'PHASE{num}_INPUTS_OK ([\w.]+): (\d+) reached;([^\n]*axioms \[[^]]+\])',logs['input'])
    assert len(matches)==count
    for name,size,tail in matches:
        axioms=re.search(r'axioms \[([^]]+)\]',tail)
        assert axioms and set(re.findall(r'[\w.]+',axioms[1]))=={'propext','Classical.choice','Quot.sound'}
    assert ('77forbidden' if num==125 else '4required/8forbidden' if num==126 else '70forbidden') in matches[0][2]
assert d['whole_audit_marker'] in logs['audit']
extract=lambda s:set(re.findall(r'DEPENDENCIES_CHECKED ([^;]+);',s))
with zipfile.ZipFile(p/'PHASE121_RAW.zip') as z:
    old=extract(z.read(next(n for n in z.namelist() if '_audit_' in n and n.endswith('.stdout.log'))).decode('utf-8-sig'))
new=extract(logs['audit']);assert len(old)==5584 and len(new)==d['whole_audit']['logical']
assert sorted(new-old)==d['added_declarations'] and not old-new
assert len(d['added_declarations'])==35 and d['whole_audit']=={'logical':5619,'theorems':4807,'runtime':17029}
assert sum(x['logical'] for x in d['namespace_audits'].values())==35
assert sum(len(x['public_names']) for x in c['modules'].values())==19
assert sha((p/'Phase128InputCheck.lean').read_bytes())==c['harness_sha256']
# Earlier verifiers intentionally assert "production unchanged". Their historical
# acceptance is not a claim about this integrated tree; preserve their raw records.
for phase in [123,124,125,126,127]:
    m=json.loads((p/f'PHASE{phase}_RESULTS.json').read_bytes())
    assert sha((p/m['archive']).read_bytes())==m['archive_sha256']
    with zipfile.ZipFile(p/m['archive']) as z:
        assert z.testzip() is None and set(z.namelist())==set(m['raw_sha256'])
        for n,h in m['raw_sha256'].items():assert sha(z.read(n))==h
print('PASS saved128:3exact modules/19public types/2private helpers;4first checks;8fresh closures;5619logical/4807theorems/17029runtime;35added/0removed;33raw. CI/review separate.')
