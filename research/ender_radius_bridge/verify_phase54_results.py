"""Seal/verify Phase54 evidence; integrity checks do not execute Lean."""
from pathlib import Path
from decimal import Decimal
import hashlib, json, re, subprocess, sys, zipfile

here=Path(__file__).resolve().parent; root=here.parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
lf=lambda p:p.read_text(encoding='utf-8-sig').replace('\r\n','\n')
old=lambda n:subprocess.check_output(['git','show','bd2a207:'+n],cwd=root).decode().replace('\r\n','\n')
records=sorted(here.glob('PHASE54_*.result.json'))
rows=[json.loads(lf(p)) for p in records]
assert len(rows)==5
builds=[r for r in rows if r['mode']=='build']
assert [r['exit_code'] for r in builds]==[1,0]
assert all(r['exit_code']==0 for r in rows if r['mode']!='build')
assert all(not r['stop_reason'] for r in rows)
spent=sum(Decimal(str(r['elapsed_seconds'])) for r in builds)
assert spent<1200
assert all(r['elapsed_seconds']<r['time_limit_seconds'] for r in rows)
assert all(r['observed_peak_working_set_bytes']<=8192*1024**2 for r in rows)
radius=root/'lean/TenthDiscriminant/TunedRadiusFamily.lean'
upper=root/'lean/TenthDiscriminant/TunedAnalyticCutoff.lean'
source=root/'lean/TenthDiscriminant/RecoveredAnalyticCutoff.lean'
assert lf(here/'Phase54Attempt1Radius.lean')==lf(radius)
assert lf(here/'Phase54Attempt1Recovered.lean')==lf(source)
first=lf(here/'Phase54Attempt1Upper.lean')
a=first.index('theorem odd_large_classNumber_ne_one '); b=first.index('\nend\n',a)
seg=first[a:b].replace('  have hd := dimensions D hD',
    '  have hbase : 62500000000 ≤ D := by omega\n  have hd := dimensions D hbase')
for name in ['radius_lt_R','chosen_radius','normalized_upper','normalized_lower']:
    seg=seg.replace(name+' D hD',name+' D hbase')
assert first[:a]+seg+first[b:]==lf(upper)
# Verify the helper generalization exactly; do not merely inspect file names.
s=old('lean/TenthDiscriminant/TunedRadiusFamily.lean')
a=s.index('theorem log_large '); b=s.index('theorem log_R_bounds ',a); original_log=s[a:b]
s=(s[:a]+s[b:]).replace('100000000000','62500000000').replace('have hu := log_large D hD','have hu := log_large_recovered D hD')
new_log=original_log.replace('log_large ','log_large_recovered ').replace('100000000000','62500000000').replace('253/10','248/10').replace('2^11*5^11','2^8*5^12').replace('(2 : Real)^11','(2 : Real)^8').replace('(5 : Real)^11','(5 : Real)^12')
a=s.index('theorem log_R_bounds ')
assert s[:a]+original_log+new_log+s[a:]==lf(radius)
s=old('lean/TenthDiscriminant/TunedAnalyticCutoff.lean');a=s.index('theorem odd_large_classNumber_ne_one ')
assert s[:a].replace('100000000000','62500000000').replace('have hu := log_large D hD','have hu := log_large_recovered D hD')+s[a:]==first
assert lf(root/'lean/TenthDiscriminant.lean').replace('import TenthDiscriminant.RecoveredAnalyticCutoff\n','')==old('lean/TenthDiscriminant.lean')
changed=subprocess.check_output(['git','diff','--name-only','bd2a207','--','lean/TenthDiscriminant','lean/TenthDiscriminant.lean','tools','.github'],cwd=root,text=True).splitlines()
assert set(changed)<={'lean/TenthDiscriminant.lean','lean/TenthDiscriminant/RecoveredAnalyticCutoff.lean','lean/TenthDiscriminant/TunedRadiusFamily.lean','lean/TenthDiscriminant/TunedAnalyticCutoff.lean'}
prior=json.loads(lf(here/'PHASE53_RESULTS.json'))
for n,h in prior['raw_sha256'].items():assert sha((root/n).read_bytes())==h,n
for n,h in prior['source_sha256_lf'].items():
    payload=old(n).encode() if n=='lean/TenthDiscriminant.lean' else lf(root/n).encode()
    assert sha(payload)==h,n
review=json.loads(lf(here/'PHASE51_RESULTS.json'))
assert sha((here/'PHASE51_REVIEW_REPORT.md').read_bytes())==review['report_sha256']
for n,h in review['reviewed_source_sha256_lf'].items():assert sha(lf(root/n).encode())==h,n
assert sha(lf(here/'CONJUGATION_BRIDGE_GUIDE.md').encode())==review['correction_sha256_lf']
sys.path.insert(0,str(root/'lean'))
import audit as coverage
mods=coverage.project_coverage(root/'lean');assert len(mods)==163
for m in mods:
    p=(root/'lean').joinpath(*m.split('.')).with_suffix('.lean')
    assert not re.search(r'\b(sorry|admit|axiom|native_decide|unsafe)\b',coverage.source_code(p))
audit=next(r for r in rows if r['mode']=='audit')
archive=here/'PHASE54_AXIOM_AUDIT_RAW.zip';manifest=here/'PHASE54_RESULTS.json'
if '--seal' in sys.argv:
    assert not archive.exists() and not manifest.exists()
    raw=here/audit['stdout'];payload=raw.read_bytes()
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:z.writestr(raw.name,payload)
    with zipfile.ZipFile(archive) as z:assert z.read(raw.name)==payload
    assert raw.resolve().parent==here.resolve()
    raw.unlink() # Only verified duplicate removed; full bytes retained in archive.
    texts=[radius,upper,source,root/'lean/TenthDiscriminant.lean',here/'PHASE54_PROTOCOL.md',here/'Phase54Attempt1Radius.lean',here/'Phase54Attempt1Upper.lean',here/'Phase54Attempt1Recovered.lean',here/'Phase54InputCheck.lean',here/'run_phase54.ps1',here/'RECOVERED_CUTOFF_GUIDE.md']
    files=records+list(here.glob('PHASE54_*.log'))+[archive]
    data=dict(status='LOCAL_PASS',scope='actual totally-complex degree-two field discriminant below62500000000',
        protocol_commit='58f984ca03a2b965de420954cf27c88902ecbf91',cumulative_build_seconds=str(spent),
        interruption='First root handle48424 missing, no result and no surviving lake/lean process; partial logs retained. Root retried once and passed. Target runs not repeated. UTF8 source-edit launcher failed before mutations/build and was corrected.',
        raw_sha256={p.relative_to(root).as_posix():sha(p.read_bytes()) for p in files},
        source_sha256_lf={p.relative_to(root).as_posix():sha(lf(p).encode()) for p in texts},
        audit_entry=audit['stdout'],audit_raw_sha256=sha(payload),audit_raw_bytes=len(payload),
        exact_head_ci='separate, not yet published',semantic_review='Phase51 predates this proof')
    manifest.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
data=json.loads(lf(manifest))
for n,h in data['raw_sha256'].items():assert sha((root/n).read_bytes())==h,n
for n,h in data['source_sha256_lf'].items():assert sha(lf(root/n).encode())==h,n
with zipfile.ZipFile(archive) as z:payload=z.read(data['audit_entry'])
assert sha(payload)==data['audit_raw_sha256'] and len(payload)==data['audit_raw_bytes']
assert b'AUDIT_OK TenthDiscriminant: 4710 logical declarations; 3967 theorems; 16968 runtime-only' in payload
inp=lf(here/next(r for r in rows if r['mode']=='input')['stdout'])
for count in [55469,55804,58598]:assert f'{count} reached; none of21 listed' in inp
assert inp.count('TUNED_INPUTS_OK ')==3 and inp.count('depends on axioms:')==1
print('PASS: five terminal records, preserved failure/exact guard repair, exact helper generalization;')
print('raw/source/archive hashes, prior Phase53 evidence and Phase51 reviewed sources intact;')
print('163 reachable modules/no escapes; audit4710/3967/16968; three fresh21-input exclusion checks.')
print('Evidence integrity only; no independent semantic review or exact-head CI inferred.')
