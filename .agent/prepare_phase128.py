"""Exact relocation of accepted proofs; no Lean invocation."""
from pathlib import Path
import hashlib,json,re,subprocess
r=Path(__file__).resolve().parents[1]; p=r/'research/ender_radius_bridge'
sha=lambda x:hashlib.sha256(x).hexdigest()
git=lambda *x:subprocess.check_output(['git',*x],cwd=r)
registered='3e95187dbcafc6c4a6fe77cb1964268d35a99479'
assert git('rev-parse','HEAD').decode().strip()==registered
assert not list(p.glob('PHASE128_*.result.json'))
specs=[(125,'Phase125Endpoint','EndpointCutoff','9523bcd0f039d8c50d9aaf034393445844630090',['RadialCutoff']),
 (126,'Phase126Classification','FieldClassification','4b22be0',['ClassNumberClassification','ImaginaryQuadraticRepresentation']),
 (127,'Phase127RadialAction','RadialAction','b00ca8e',['RadialOperator'])]
c={'registered_commit':registered,'modules':{}}; harness='import TenthDiscriminant\n\n'
for num,old,new,accepted,imports in specs:
    path=f'research/ender_radius_bridge/{old}.lean'
    src=git('show',accepted+':'+path)
    assert src==(r/path).read_bytes()
    text=src.decode(); start=text.index('/-!'); end=text.index('end TenthDiscriminant.'+old+'\n')+len('end TenthDiscriminant.'+old+'\n')
    body=text[start:end]; renamed=body.replace(old,new)
    out=(''.join('import TenthDiscriminant.'+x+'\n' for x in imports)+'\n'+renamed).encode()
    dest=f'lean/TenthDiscriminant/{new}.lean'; assert not (r/dest).exists()
    (r/dest).write_bytes(out)
    names=re.findall(r'^theorem (\w+)',body,re.M)
    harness+=''.join('#check TenthDiscriminant.'+new+'.'+x+'\n' for x in names)+'\n'
    diagnostics=text[end:].replace(old,new).replace(f'phase{num}_inputs',f'phase128_{num}_inputs')
    harness+=diagnostics+'\n'
    c['modules'][new]={'old_namespace':old,'accepted_commit':git('rev-parse',accepted).decode().strip(),
        'accepted_path':path,'accepted_sha256':sha(src),'body_range':[len(text[:start].encode()),len(text[:end].encode())],
        'body_sha256':sha(body.encode()),'imports':imports,'path':dest,'source_sha256':sha(out),'public_names':names}
assert sum(len(x['public_names']) for x in c['modules'].values())==19
root=git('show',registered+':lean/TenthDiscriminant.lean')
newroot=root+''.join('import TenthDiscriminant.'+x+'\n' for x in c['modules']).encode()
(r/'lean/TenthDiscriminant.lean').write_bytes(newroot)
(p/'Phase128InputCheck.lean').write_bytes(harness.encode())
c.update(root_before_sha256=sha(root),root_after_sha256=sha(newroot),harness_sha256=sha(harness.encode()))
(p/'PHASE128_CORRESPONDENCE.json').write_bytes((json.dumps(c,indent=2)+'\n').encode())
# Reuse the inspected process supervisor, with this protocol's fixed scope/budgets.
runner=(p/'run_phase121.ps1').read_text(encoding='utf-8').replace('121','128')
runner=runner.replace("[Math]::Min(600,[Math]::Floor(1200-$taskSpent))","[Math]::Min(600,[Math]::Floor(900-$taskSpent))")
runner=runner.replace("'root' {1200}; default {180}","'root' {1200}; 'input' {240}; default {180}")
runner=runner.replace("@('build','TenthDiscriminant.RadialCutoff')","@('build','TenthDiscriminant.EndpointCutoff','TenthDiscriminant.FieldClassification','TenthDiscriminant.RadialAction')")
runner=runner.replace("@('RadialJetMajorant','RadialDetBound','RadialCutoff')","@('EndpointCutoff','FieldClassification','RadialAction')")
runner=runner.replace('Exact118/119/120 mathematical integration and full actual-field48b cutoff','Exact125/126/127 integration:actual-field47.5b,field classification interface,radial action')
(p/'run_phase128.ps1').write_bytes(runner.encode())
print('PREPARED128:3 exact modules,19 public types,2 private helpers,3 imports,8 fresh closure commands;no Lean invocation')
