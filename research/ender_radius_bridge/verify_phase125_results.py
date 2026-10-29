"""Verify saved full successor acceptance and historical CI; no Lean replay."""
from pathlib import Path
import hashlib,json,re,subprocess,zipfile
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]

def sha(b):return hashlib.sha256(b).hexdigest()

def main():
    m=json.loads((HERE/'PHASE125_RESULTS.json').read_text(encoding='utf-8'))
    f=json.loads((HERE/'PHASE125_FROZEN.json').read_text(encoding='utf-8'))
    source=(HERE/'Phase125Endpoint.lean').read_bytes()
    assert sha(source)==f['first_source_sha256']
    assert sha((HERE/'Phase122Endpoint.lean').read_bytes())==m['old_phase122_sha256']==f['old_source_sha256']
    for name,digest in f['immutable_files'].items():assert sha((ROOT/name).read_bytes())==digest
    source_text=source.decode()
    pattern=r'(theorem endpoint_log_lower.*?:= by\n).*?(?=\ntheorem endpoint_separation)'
    outside,n=re.subn(pattern,lambda x:x.group(1)+'<ADAPTER>\n',source_text,flags=re.S)
    assert n==1 and sha(outside.encode())==f['outside_adapter_sha256']
    assert len(list(HERE.glob('PHASE125_build_*.result.json')))==1
    assert m['repairs']==0 and not m['second_call_used']
    zpath=HERE/m['archive'];assert sha(zpath.read_bytes())==m['archive_sha256']
    with zipfile.ZipFile(zpath) as z:
        assert z.testzip() is None and len(z.namelist())==4
        assert set(z.namelist())==set(m['raw_sha256'])
        for name,digest in m['raw_sha256'].items():assert sha(z.read(name))==digest
        native=m['native_result'];assert native['exit_code']==0 and native['attempt']==1 and native['stop_reason']==''
        assert native['elapsed_seconds']<300 and native['observed_peak_working_set_bytes']<8192*1024**2
        assert z.read(native['source_snapshot'])==source and z.read(native['stderr'])==b''
        log=z.read(native['stdout']).decode('utf-8-sig')
        assert 'error:' not in log and 'sorryAx' not in log
        assert 'AUDIT_OK TenthDiscriminant.Phase125Endpoint: 17 logical declarations; 17 theorems; 0 runtime-only auxiliaries excluded' in log
        assert log.count('PHASE125_INPUTS_OK ')==3
        for name,count in m['fresh_root_counts'].items():
            assert f'PHASE125_INPUTS_OK TenthDiscriminant.Phase125Endpoint.{name}: {count} reached;77forbidden roots excluded' in log
    ci=json.loads((HERE/'ARGON_EXACT_FROZEN_CI_RECEIPT.json').read_text(encoding='utf-8'))
    raw=HERE/'ARGON_EXACT_FROZEN_CI_RAW.zip';assert sha(raw.read_bytes())==ci['archive_sha256']
    with zipfile.ZipFile(raw) as z:
        assert z.testzip() is None and len(z.namelist())==6
        for name,digest in ci['raw_sha256'].items():assert sha(z.read(name))==digest
        run=json.loads(z.read('run.json'));job=json.loads(z.read('job.json'))
        assert run['head_sha']==job['head_sha']==ci['head'] and run['conclusion']==job['conclusion']=='success'
        assert run['run_attempt']==1 and run['event']=='push'
        controls=z.read('negative_controls.py');assert controls==subprocess.check_output(['git','show',ci['head']+':lean/negative_controls.py'],cwd=ROOT)
        assert controls.count(b'check=True')>=8
        log=z.read('job.log').decode('utf-8-sig')
        assert '##[error]' not in log and 'AUDIT_OK TenthDiscriminant: 4917 logical declarations; 4155 theorems; 16985 runtime-only auxiliaries excluded' in log
        assert 'PASS: mathematical controls, proof-audit probes, Gram, jet, multiplicity, degree, nonzero, affine and assembly controls.' in log
    assert subprocess.check_output(['git','diff','--name-only',m['base_commit'],'--','lean','.github'],cwd=ROOT)==b''
    print('PASS saved125:COMPLETE47.5b standalone/firstcall/4raw/17namespace/3fresh77-root closures;Phase122unchanged;exact39e9ce3historicalCI6raw confirmed. No Lean/job replay;production48b unchanged.')

if __name__=='__main__':main()
