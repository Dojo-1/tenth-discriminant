"""Seal/verify fixed50b evidence and preserved earlier records; no Lean run."""
from pathlib import Path
import hashlib,json,re,subprocess,sys,zipfile

here=Path(__file__).resolve().parent;root=here.parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
lf=lambda p:p.read_text(encoding='utf-8-sig').replace('\r\n','\n')
old=lambda n,ref='80107ff':subprocess.check_output(['git','show',ref+':'+n],cwd=root).decode().replace('\r\n','\n')
records=sorted(here.glob('PHASE56_*.result.json'));rows=[json.loads(lf(p)) for p in records]
assert len(rows)==4 and {r['mode'] for r in rows}=={'build','root','input','audit'}
assert all(r['attempt']==1 and r['exit_code']==0 and not r['stop_reason'] for r in rows)
assert all(r['elapsed_seconds']<r['time_limit_seconds'] for r in rows)
assert all(r['observed_peak_working_set_bytes']<=8192*1024**2 for r in rows)
radius=root/'lean/TenthDiscriminant/TunedRadiusFamily.lean'
upper=root/'lean/TenthDiscriminant/TunedAnalyticCutoff.lean'
recovered=root/'lean/TenthDiscriminant/RecoveredAnalyticCutoff.lean'
strong=root/'lean/TenthDiscriminant/StrongSmallPrimeRecoveryGain.lean'
source=root/'lean/TenthDiscriminant/FiftyBillionCutoff.lean'
# Old logarithm statements/bodies stay intact; only new geometry lemma is added.
s=old('lean/TenthDiscriminant/TunedRadiusFamily.lean')
a=s.index('theorem log_large ');b=s.index('theorem log_R_bounds ',a);logs=s[a:b]
s=(s[:a]+s[b:]).replace('62500000000','41006250000').replace(': 500 ≤ fourthRoot',': 450 ≤ fourthRoot').replace('show 500^2^2 ≤ D','show 450^2^2 ≤ D').replace('(500 : Real)^3','(450 : Real)^3').replace('have hu := log_large_recovered D hD','have hu := log_large_geometry D hD')
s=s.replace('import TenthDiscriminant.AspectRatioLowerEnvelope','import TenthDiscriminant.AspectRatioLowerEnvelope\nimport TenthDiscriminant.StrongSmallPrimeRecoveryGain')
a=s.index('theorem log_R_bounds ');expected=s[:a]+logs+s[a:]
current=lf(radius);a=current.index('theorem log_large_geometry ');b=current.index('theorem log_R_bounds ',a)
assert current[:a]+current[b:]==expected
s=old('lean/TenthDiscriminant/TunedAnalyticCutoff.lean');a=s.index('theorem odd_large_classNumber_ne_one ')
s=s[:a].replace('62500000000','41006250000').replace('521/100000','521/90000').replace('have hu := log_large_recovered D hD','have hu := log_large_geometry D hD')+s[a:].replace('have hbase : 62500000000','have hbase : 41006250000')
assert s==lf(upper)
s=old('lean/TenthDiscriminant/RecoveredAnalyticCutoff.lean')
for n in ['dimensions','normalized_lower','radius_lt_R','chosen_radius','normalized_upper']:
    s=s.replace(n+' D hD',n+' D (by omega)')
assert s==lf(recovered)
assert lf(root/'lean/TenthDiscriminant.lean').replace('import TenthDiscriminant.StrongSmallPrimeRecoveryGain\n','').replace('import TenthDiscriminant.FiftyBillionCutoff\n','')==old('lean/TenthDiscriminant.lean')
allowed={'lean/TenthDiscriminant.lean',*(p.relative_to(root).as_posix() for p in [radius,upper,recovered,strong,source])}
changed=subprocess.check_output(['git','diff','--name-only','80107ff','--','lean/TenthDiscriminant','lean/TenthDiscriminant.lean','lean/lean-toolchain','lean/lakefile.lean','tools','.github'],cwd=root,text=True).splitlines()
assert set(changed)<=allowed,changed
# Historical verifiers are not current-root validators after these source edits.
prior54=json.loads(lf(here/'PHASE54_RESULTS.json'))
for n,h in prior54['raw_sha256'].items():assert sha((root/n).read_bytes())==h,n
for n,h in prior54['source_sha256_lf'].items():
    payload=old(n,'86abe21').encode() if n.startswith('lean/') else lf(root/n).encode()
    assert sha(payload)==h,n
prior55=json.loads(lf(here/'PHASE55_RESULTS.json'))
for n,h in prior55['raw_sha256'].items():assert sha((root/n).read_bytes())==h,n
for n,h in prior55['source_sha256_lf'].items():assert sha(old(n,'86abe21').encode())==h,n
sys.path.insert(0,str(root/'lean'));import audit as coverage
mods=coverage.project_coverage(root/'lean');assert len(mods)==165
for m in mods:
    p=(root/'lean').joinpath(*m.split('.')).with_suffix('.lean')
    assert not re.search(r'\b(sorry|admit|axiom|native_decide|unsafe)\b',coverage.source_code(p))
audit=next(r for r in rows if r['mode']=='audit')
archive=here/'PHASE56_AXIOM_AUDIT_RAW.zip';manifest=here/'PHASE56_RESULTS.json'
if '--seal' in sys.argv:
    assert not archive.exists() and not manifest.exists()
    raw=here/audit['stdout'];payload=raw.read_bytes()
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:z.writestr(raw.name,payload)
    with zipfile.ZipFile(archive) as z:assert z.read(raw.name)==payload
    assert raw.resolve().parent==here.resolve()
    raw.unlink() # Verified duplicate only; full raw audit retained in ZIP.
    texts=[radius,upper,recovered,strong,source,root/'lean/TenthDiscriminant.lean',here/'PHASE56_PROTOCOL.md',here/'Phase56InputCheck.lean',here/'run_phase56.ps1',here/'FIFTY_BILLION_GUIDE.md']
    files=records+list(here.glob('PHASE56_*.log'))+[archive]
    data=dict(status='LOCAL_PASS',scope='fixed actual-field discriminant bound50000000000; stronger existing weights',protocol_commit='a42ab4fdbc7da06e1fb528703b4c6904e09db567',
        target_attempts=1,target_build_seconds=next(r['elapsed_seconds'] for r in rows if r['mode']=='build'),
        raw_sha256={p.relative_to(root).as_posix():sha(p.read_bytes()) for p in files},source_sha256_lf={p.relative_to(root).as_posix():sha(lf(p).encode()) for p in texts},
        audit_entry=audit['stdout'],audit_raw_sha256=sha(payload),audit_raw_bytes=len(payload),
        semantic_review='Phase55 frozen86abe21 predates these edits',exact_head_ci='separate; not yet published')
    manifest.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
data=json.loads(lf(manifest))
for n,h in data['raw_sha256'].items():assert sha((root/n).read_bytes())==h,n
for n,h in data['source_sha256_lf'].items():assert sha(lf(root/n).encode())==h,n
with zipfile.ZipFile(archive) as z:payload=z.read(data['audit_entry'])
assert sha(payload)==data['audit_raw_sha256'] and len(payload)==data['audit_raw_bytes']
assert b'AUDIT_OK TenthDiscriminant: 4755 logical declarations; 4012 theorems; 16968 runtime-only' in payload
inp=lf(here/next(r for r in rows if r['mode']=='input')['stdout'])
for count in [55475,55810,58604]:assert f'{count} reached; none of25 listed' in inp
assert inp.count('TUNED_INPUTS_OK ')==3 and inp.count('depends on axioms:')==2
print('PASS: four first-attempt terminal records; exact inherited-helper changes, raw/source/archive hashes;')
print('165 reachable modules/no escapes; audit4755/4012/16968; three fresh25-input exclusions;')
print('earlier Phase54 raw/source and Phase55 first-report evidence preserved at frozen86abe21.')
print('Integrity only; no transferred review, CI, human independence or optimality claim.')
