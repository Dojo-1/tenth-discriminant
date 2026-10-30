"""Verify saved exterior-minor evidence; never rerun observations or determinants."""
from pathlib import Path
from math import prod
import hashlib,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
d=json.loads((p/'PHASE131_RESULTS.json').read_bytes());f=json.loads((p/'PHASE131_FROZEN.json').read_bytes())
assert d['status']=='EXACT_EXTERIOR_COMPARATOR_PASS_FIRST_AND_ONLY_CALL'
assert sha((p/'phase131_exterior_comparator.py').read_bytes())==f['source_sha256']
assert sha((p/'PHASE131_PROTOCOL.md').read_bytes())==f['protocol_sha256']
git=lambda *args:subprocess.check_output(['git',*args],cwd=r)
assert git('show',d['source_frozen_commit']+':research/ender_radius_bridge/phase131_exterior_comparator.py')==(p/'phase131_exterior_comparator.py').read_bytes()
assert git('show',d['protocol_commit']+':research/ender_radius_bridge/PHASE131_PROTOCOL.md')==(p/'PHASE131_PROTOCOL.md').read_bytes()
assert git('diff',d['base'],'--name-only','--','lean','.github')==b''
assert len(list(p.glob('PHASE131_trial_*.result.json')))==1
assert sha((p/d['archive']).read_bytes())==d['archive_sha256']
with zipfile.ZipFile(p/d['archive']) as z:
    assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==5
    assert {n:sha(z.read(n)) for n in z.namelist()}==d['raw_sha256']
    n=d['native_result'];assert n['attempt']==1 and n['exit_code']==0 and not n['stop_reason']
    assert n['max_seconds']==60 and 0<n['elapsed_seconds']<60
    assert z.read(n['source_snapshot'])==(p/'phase131_exterior_comparator.py').read_bytes()
    assert z.read(n['stderr'])==b'' and b'PASS131:8fixedcases/220maximalminors' in z.read(n['stdout'])
    x=json.loads(z.read(n['data']))
expected={(D,q,R,S,1) for D,q in [(1,3),(19,3),(2,5),(1,7)] for R,S in [(1,1),(4,2)]}
assert {(c['D'],c['p'],c['R'],c['S'],c['J']) for c in x['cases']}==expected
assert len(x['cases'])==8 and sum(len(c['minors']) for c in x['cases'])==220
for c in x['cases']:
    assert len(c['E'])==len(c['Ehat'])==c['R']*c['S']
    assert all(len(row)==10 for row in c['E']+c['Ehat'])
    assert c['minor_factor']==c['p']**c['F']
    for m in c['minors']:
        assert m['minor']==m['transformed_minor']==c['minor_factor']*m['quotient_minor']
        assert m['metric_weight']==prod(c['B_diagonal'][j] for j in m['columns'])
    assert sum(m['metric_weight']*m['minor']**2 for m in c['minors'])==c['detG']
    assert sum(m['metric_weight']*m['quotient_minor']**2 for m in c['minors'])==c['detK']
    assert c['detG']==c['p']**(2*c['F'])*c['detK']
assert x['minor_count']==d['minor_count']==220
assert sum(m['minor']!=0 for c in x['cases'] for m in c['minors'])==x['nonzero_minors']==d['nonzero_minors']==24
assert x['zero_determinants']==d['zero_determinants']==0
assert x['controls']==d['controls']
assert x['controls']['omitted_square_cases_caught']==4
assert x['controls']['halved_exponent_nonzero_cases_caught']==2
assert x['controls']['diagonal_products']==[1,2] and x['controls']['shear_determinant']==1
assert x['controls']['rank_reduction']=={'real_rank':2,'mod3_rank':1}
for name in ['README.md','TAO_OBJECTIVES_CURRENT.md']:assert len((r/name).read_text(encoding='utf-8').splitlines())==61
links=0
for name in ['EXTERIOR_VOLUME_GUIDE.md','STRUCTURAL_BRIDGE_CURRENT.md','VERIFICATION_LAYERS_CURRENT.md','PHASE131_VERIFICATION.md']:
    q=p/name
    for target in re.findall(r'\]\(([^)]+)\)',q.read_text(encoding='utf-8')):
        target=target.split('#')[0]
        if target and '://' not in target:assert (q.parent/target).exists(),(name,target);links+=1
print(f'PASS saved131:8fixedcases/220minors/24nonzero/4controls;5raw;one invocation;{links}readerlinks;all Lean/workflows unchanged. No observation,determinant,oldtrial or Lean replay.')
