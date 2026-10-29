"""Read-only integrity check for a failed, terminal proof cycle. Never runs Lean."""
from pathlib import Path
import difflib, hashlib, json, re, subprocess, zipfile
p=Path(__file__).resolve().parent
r=p.parents[1]
d=json.loads((p/'PHASE114_RESULTS.json').read_bytes())
def sha(b): return hashlib.sha256(b).hexdigest()
def git(*args, **kw): return subprocess.check_output(['git',*args],cwd=r,**kw)
assert d['status']=='RESOURCE_STOP_FULL_TARGET_NOT_ACCEPTED'
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
assert git('show',d['registered_commit']+':research/ender_radius_bridge/PHASE114_PROTOCOL.md')==(p/'PHASE114_PROTOCOL.md').read_bytes()
for name,h in d['sha256'].items(): assert sha((r/name).read_bytes())==h,name
assert sha((p/d['archive']['path']).read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(p/d['archive']['path']) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(set(z.namelist()))==8
    raw={name:z.read(name) for name in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert len(d['runs'])==2 and d['unused_slots_forfeited_after_resource_stop']==1
assert sum(x['elapsed_seconds'] for x in d['runs'])==d['cumulative_elapsed_seconds']<1200
sources=[]
for i,x in enumerate(d['runs'],1):
    assert x['attempt']==i and x['exit_code']==1 and x['phase']==114
    assert x['mode']=='build' and x['time_limit_seconds']==600 and x['memory_threshold_mb']==8192
    assert 0<x['elapsed_seconds']<600 and 0<x['observed_peak_working_set_bytes']<8192*1024**2
    assert x['arguments']==['env','lean','-j','1','../../tenth-radial-blocks/research/ender_radius_bridge/Phase114RadialBlocks.lean']
    assert x['cwd'].replace('\\','/').endswith('/work/tenth-discriminant/lean')
    assert x['protocol_commit']==d['registered_commit'][:7]
    source=raw[x['source_snapshot']]
    assert sha(source)==x['source_sha256']
    sources.append(source.decode())
    prefix=x['source_snapshot'].removesuffix('.source.lean')
    assert json.loads(raw[prefix+'.result.json'])==x
    log=raw[x['stdout']].decode('utf-8-sig')
    assert 'error:' in log and 'AUDIT_OK TenthDiscriminant.RadialBlocks:' not in log
    assert 'PHASE114_INPUTS_OK ' not in log
    if i==1:
        assert x['stop_reason']=='' and 'maximum number of heartbeats' not in log
    else:
        assert x['stop_reason']=='lean_internal_resource_limit'
        assert 'maximum number of heartbeats (200000)' in log
        assert ':75:0: error: (deterministic) timeout' in log
        assert ':158:0: error: (deterministic) timeout' in log
        assert 'PROJECT_AXIOM TenthDiscriminant.RadialBlocks.integer_prime_block_bridge' in log
        assert 'PHASE114_NONSTANDARD_AXIOM' in log
assert (p/'Phase114RadialBlocks.lean').read_bytes()==sources[1].encode()
assert len(list(p.glob('PHASE114_build_*.result.json')))==2
assert not re.search(r'(?m)^\s*(axiom|unsafe|set_option maxHeartbeats|set_option maxRecDepth)\b',sources[1])
def surface(s):
    types={m[1]:m[0] for m in re.findall(r'(?m)^(theorem (\w+)[\s\S]*?) := by',s)}
    defs={m[1]:m[0] for m in re.findall(r'(?m)^(def (\w+)[\s\S]*?)(?=\n\n)',s)}
    return {'types':types,'definitions':defs}
a,b=map(surface,sources)
assert a==json.loads((p/'PHASE114_FROZEN_SURFACE.json').read_bytes())
assert set(a['types'])==set(b['types']) and set(a['definitions'])==set(b['definitions'])
assert sorted(n for n in a['types'] if a['types'][n]!=b['types'][n])==['real_hermitian_control','singular_control']
for name in ('types','definitions'):
    for n,s in a[name].items():
        t=b[name][n]
        # Exact character comparison except the disclosed annotation parentheses.
        if name=='types' and n in ('singular_control','real_hermitian_control'):
            assert ''.join(s.split()).replace('(','').replace(')','')==''.join(t.split()).replace('(','').replace(')','')
        else: assert ''.join(s.split())==''.join(t.split()),n
patch=''.join(difflib.unified_diff(sources[0].splitlines(True),sources[1].splitlines(True),fromfile='attempt1',tofile='attempt2'))
assert patch==(p/'PHASE114_REPAIR1.diff').read_text(encoding='utf-8')
frozen={}
for record in git('ls-tree','-r','-z',d['registered_commit']).split(b'\0'):
    if not record: continue
    meta,name=record.split(b'\t',1); name=name.decode()
    if name.startswith('.agent/') or name in d['reader_exceptions']: continue
    frozen[name]=meta.split()[2].decode()
assert len(frozen)==d['frozen_files']
names=sorted(frozen)
hashes=git('hash-object','--stdin-paths',input=('\n'.join(names)+'\n').encode()).decode().splitlines()
assert len(hashes)==len(names)
for n,h in zip(names,hashes): assert h==frozen[n],n
assert git('rev-parse','refs/heads/codex/control-priority-policy').decode().strip()==d['base_source']
for name in ('README.md','TAO_OBJECTIVES_CURRENT.md'):
    assert len((r/name).read_text(encoding='utf-8').splitlines())==61
print(f'PASS evidence integrity:2 failed invocations, terminal default-heartbeat stop,8raw files,{len(frozen)}frozen Git blobs; source/signature syntax deltas disclosed.')
print('FULL PROOF TARGET NOT ACCEPTED. No Lean replay, production integration, new CI or cutoff gain.')
