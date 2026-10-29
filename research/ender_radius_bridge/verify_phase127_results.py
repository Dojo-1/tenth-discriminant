"""Verify all saved radial proof attempts and exact proof-only repairs;no Lean replay."""
from pathlib import Path
import hashlib,json,re,difflib,subprocess,zipfile,math
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()

def main():
    m=json.loads((HERE/'PHASE127_RESULTS.json').read_text(encoding='utf-8'))
    f=json.loads((HERE/'PHASE127_FROZEN.json').read_text(encoding='utf-8'))
    for name,digest in f['immutable_files'].items():assert sha((ROOT/name).read_bytes())==digest
    archive=HERE/m['archive'];assert sha(archive.read_bytes())==m['archive_sha256']
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None and len(z.namelist())==16
        assert set(z.namelist())==set(m['raw_sha256'])
        for name,digest in m['raw_sha256'].items():assert sha(z.read(name))==digest
        results=m['native_results'];assert [x['exit_code'] for x in results]==[1,1,0]
        assert [x['attempt'] for x in results]==[1,2,3]
        assert len(list(HERE.glob('PHASE127_build_*.result.json')))==3
        sources=[];spent=0
        for n in results:
            assert not n['stop_reason'] and n['observed_peak_working_set_bytes']<8192*1024**2
            assert n['time_limit_seconds']==math.floor(600-spent)
            assert abs(n['cumulative_before_seconds']-spent)<0.00001
            assert n['elapsed_seconds']<n['time_limit_seconds'];spent+=n['elapsed_seconds']
            source=z.read(n['source_snapshot']);assert sha(source)==n['source_sha256'];sources.append(source)
            out,count=re.subn(r'(^(?:private )?theorem .*?:= by\n).*?(?=^(?:private )?theorem |^end$)',lambda x:x.group(1)+'<PROOF>\n',source.decode(),flags=re.S|re.M)
            assert count==9 and sha(out.encode())==f['outside_proofs_sha256']
            text=source.decode();control=text[text.index('theorem nonmultiplicative_control'):text.index('\nend\n')]
            assert sha(control.encode())==f['control_sha256'] and z.read(n['stderr'])==b''
        assert spent<600 and abs(spent-m['cumulative_seconds'])<0.00001
        assert sha(sources[0])==f['first_source_sha256']
        assert sources[-1]==(HERE/'Phase127RadialAction.lean').read_bytes()
        for attempt in (2,3):
            q=json.loads(z.read(f'PHASE127_PROOF_REPAIR_{attempt}.json'))
            assert sha(sources[attempt-2])==q['before_sha256'] and sha(sources[attempt-1])==q['after_sha256']
            diff=''.join(difflib.unified_diff(sources[attempt-2].decode().splitlines(True),sources[attempt-1].decode().splitlines(True),fromfile=f'attempt{attempt-1}',tofile=f'attempt{attempt}'))
            assert z.read(q['diff']).decode()==diff
        for n in results[:-1]:assert 'error:' in z.read(n['stdout']).decode()
        log=z.read(results[-1]['stdout']).decode('utf-8-sig')
        assert 'error:' not in log and 'sorryAx' not in log
        assert 'AUDIT_OK TenthDiscriminant.Phase127RadialAction: 16 logical declarations; 16 theorems; 0 runtime-only auxiliaries excluded' in log
        assert log.count('PHASE127_INPUTS_OK ')==3
        for name,count in m['fresh_counts'].items():assert f'PHASE127_INPUTS_OK TenthDiscriminant.Phase127RadialAction.{name}: {count} reached;70forbidden roots excluded' in log
    assert subprocess.check_output(['git','diff','--name-only',m['base_commit'],'--','lean','.github'],cwd=ROOT)==b''
    links=0
    for name in ['RADIAL_ACTION_CURRENT.md','PHASE127_VERIFICATION.md']:
        p=HERE/name
        for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
            if '://' not in target:
                assert (p.parent/target.split('#',1)[0]).exists();links+=1
    print(f'PASS saved127:all actual radial laws;3complete calls/2failed sources+exact repairs/16raw;9frozen types/control;16namespace/3fresh70root closures;{links}links. No Lean replay;production unchanged.')

if __name__=='__main__':main()
