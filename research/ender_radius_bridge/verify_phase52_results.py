"""Seal once or verify preserved small-prime recovery evidence; no Lean run."""
from pathlib import Path
from decimal import Decimal
import hashlib,json,re,subprocess,sys,zipfile

here=Path(__file__).resolve().parent
root=here.parents[1]
manifest=here/'PHASE52_RESULTS.json'
digest=lambda b:hashlib.sha256(b).hexdigest()
lf=lambda p:p.read_text(encoding='utf-8-sig').replace('\r\n','\n')
path=lambda n:root/n.replace('\\','/')
records=sorted(here.glob('PHASE52_*.result.json'))
rows=[json.loads(p.read_text(encoding='utf-8-sig')) for p in records]
assert len(rows)==6
builds=[r for r in rows if r['mode']=='build']
assert [r['exit_code'] for r in builds]==[1,1,0]
assert all(not r['stop_reason'] for r in rows)
assert all(r['exit_code']==0 for r in rows if r['mode']!='build')
spent=sum(Decimal(str(r['elapsed_seconds'])) for r in builds)
assert spent<1200 and all(r['elapsed_seconds']<r['time_limit_seconds'] for r in rows)
assert all(r['observed_peak_working_set_bytes']<=8192*1024**2 for r in rows)
source=root/'lean/TenthDiscriminant/SmallPrimeRecovery.lean'
first=lf(here/'Phase52Attempt1.lean');second=lf(here/'Phase52Attempt2.lean')
assert first.replace(
    '  have ha : (0 : Real) ≤ (S : Real)-1/2 := by exact_mod_cast hS; linarith',
    '  have ha : (0 : Real) ≤ (S : Real)-1/2 := by\n'
    '    have h : (1 : Real) ≤ S := by exact_mod_cast hS\n    linarith').replace(
    '    exact Finset.single_le_sum (fun _ _ => Nat.zero_le _) (Finset.mem_range.mpr (by omega))',
    '    exact Finset.single_le_sum (fun _ _ => Nat.zero_le _)\n'
    '      (show (3 : Nat) ∈ Finset.range R from Finset.mem_range.mpr (by omega))').replace(
    '    have hnat : 0 < valuationWeight R S 3 := by norm_num at ht; omega',
    '    have hnat : 0 < valuationWeight R S 3 :=\n'
    '      lt_of_lt_of_le (by decide : 0 < min (3/3 : Nat) 1) (ht.trans hr)')==second
assert second.replace('    exact Finset.single_le_sum (fun _ _ => Nat.zero_le _)\n',
    '    exact Finset.single_le_sum\n'
    '      (f := fun r : Nat => ∑ t ∈ Finset.range S, min (r/3) t)\n'
    '      (fun _ _ => Nat.zero_le _)\n')==lf(source)
oldroot=subprocess.check_output(['git','show','10b684c:lean/TenthDiscriminant.lean'],cwd=root).decode().replace('\r\n','\n')
assert lf(root/'lean/TenthDiscriminant.lean').replace(
    'import TenthDiscriminant.SmallPrimeRecovery\n','')==oldroot
changed=subprocess.check_output(['git','diff','--name-only','10b684c','--',
    'lean/TenthDiscriminant','lean/TenthDiscriminant.lean','tools','.github'],cwd=root,text=True).splitlines()
assert set(changed)<={'lean/TenthDiscriminant.lean','lean/TenthDiscriminant/SmallPrimeRecovery.lean'}
review=json.loads((here/'PHASE51_RESULTS.json').read_text(encoding='utf-8'))
assert digest((here/'PHASE51_REVIEW_REPORT.md').read_bytes())==review['report_sha256']
for n,h in review['reviewed_source_sha256_lf'].items():assert digest(lf(path(n)).encode())==h,n
assert digest(lf(here/'CONJUGATION_BRIDGE_GUIDE.md').encode())==review['correction_sha256_lf']
for phase,ref in [('49','f0fe28a'),('50','69010f4')]:
    prior=json.loads((here/f'PHASE{phase}_RESULTS.json').read_text(encoding='utf-8'))
    for n,h in prior['raw_sha256'].items():assert digest(path(n).read_bytes())==h,n
    for n,h in prior['source_sha256_lf'].items():
        if n.replace('\\','/')=='lean/TenthDiscriminant.lean':
            payload=subprocess.check_output(['git','show',ref+':lean/TenthDiscriminant.lean'],cwd=root).decode().replace('\r\n','\n').encode()
        else:payload=lf(path(n)).encode()
        assert digest(payload)==h,n
audit=next(r for r in rows if r['mode']=='audit')
archive=here/'PHASE52_AXIOM_AUDIT_RAW.zip'
if '--seal' in sys.argv:
    assert not manifest.exists() and not archive.exists()
    raw=here/audit['stdout'];payload=raw.read_bytes()
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:z.writestr(raw.name,payload)
    with zipfile.ZipFile(archive) as z:assert z.read(raw.name)==payload
    assert raw.resolve().parent==here.resolve()
    raw.unlink()  # Verified duplicate only; complete raw bytes retained in ZIP.
    files=records+list(here.glob('PHASE52_*.log'))+[archive]
    texts=[source,root/'lean/TenthDiscriminant.lean',here/'PHASE52_PROTOCOL.md',
        here/'Phase52Attempt1.lean',here/'Phase52Attempt2.lean',here/'Phase52InputCheck.lean',
        here/'run_phase52.ps1',here/'SMALL_PRIME_RECOVERY_GUIDE.md']
    data=dict(scope='strict recovery of exact existing3/5 terms in the certified proxy; no numerical cutoff',
        status='LOCAL_PASS',protocol_commit='ce1456f00baa2c3aad2a4ba6a50bdfd5c7241e62',
        cumulative_build_seconds=str(spent),
        interruption='audit launch not executed: approval-service workspace credits exhausted; user restored credits; saved input reconciled PASS, not rerun; audit attempt1 then PASS',
        raw_sha256={p.relative_to(root).as_posix():digest(p.read_bytes()) for p in files},
        source_sha256_lf={p.relative_to(root).as_posix():digest(lf(p).encode()) for p in texts},
        audit_entry=audit['stdout'],audit_raw_sha256=digest(payload),audit_raw_bytes=len(payload),
        exact_head_ci='separate; not yet published',semantic_review='Phase51 predates this module')
    manifest.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
data=json.loads(manifest.read_text(encoding='utf-8'))
for n,h in data['raw_sha256'].items():assert digest(path(n).read_bytes())==h,n
for n,h in data['source_sha256_lf'].items():assert digest(lf(path(n)).encode())==h,n
with zipfile.ZipFile(archive) as z:payload=z.read(data['audit_entry'])
assert digest(payload)==data['audit_raw_sha256'] and len(payload)==data['audit_raw_bytes']
assert b'AUDIT_OK TenthDiscriminant: 4672 logical declarations; 3929 theorems; 16968 runtime-only' in payload
inp=lf(here/next(r for r in rows if r['mode']=='input')['stdout'])
assert inp.count('depends on axioms:')==4
sys.path.insert(0,str(root/'lean'))
import audit as coverage
mods=coverage.project_coverage(root/'lean');assert len(mods)==161
for m in mods:
    p=(root/'lean').joinpath(*m.split('.')).with_suffix('.lean')
    assert not re.search(r'\b(sorry|admit|axiom|native_decide|unsafe)\b',coverage.source_code(p))
print('PASS: six terminal records, two failed sources/exact repairs, raw/source/archive hashes;')
print('prior Phase49/50 evidence and Phase51 reviewed sources/report/correction intact;')
print('161 reachable modules/no source escapes; compiled audit4672/3929/16968.')
print('Scope: evidence correspondence, not fresh proof execution or independent review.')
