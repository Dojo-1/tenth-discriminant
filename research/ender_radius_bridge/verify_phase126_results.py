"""Verify saved classification-interface acceptance;never replay Lean."""
from pathlib import Path
import hashlib,json,re,subprocess,zipfile
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()

def main():
    m=json.loads((HERE/'PHASE126_RESULTS.json').read_text(encoding='utf-8'))
    f=json.loads((HERE/'PHASE126_FROZEN.json').read_text(encoding='utf-8'))
    source=(HERE/'Phase126Classification.lean').read_bytes()
    assert sha(source)==f['first_source_sha256'] and m['repairs']==0 and not m['second_call_used']
    out,count=re.subn(r'(^theorem .*?:= by\n).*?(?=^theorem |^end$)',lambda x:x.group(1)+'<PROOF>\n',source.decode(),flags=re.S|re.M)
    assert count==2 and sha(out.encode())==f['outside_proofs_sha256']
    for name,digest in f['immutable_files'].items():assert sha((ROOT/name).read_bytes())==digest
    assert len(list(HERE.glob('PHASE126_build_*.result.json')))==1
    archive=HERE/m['archive'];assert sha(archive.read_bytes())==m['archive_sha256']
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None and len(z.namelist())==4
        for name,digest in m['raw_sha256'].items():assert sha(z.read(name))==digest
        n=m['native_result'];assert n['exit_code']==0 and n['attempt']==1 and n['stop_reason']==''
        assert n['elapsed_seconds']<300 and n['observed_peak_working_set_bytes']<8192*1024**2
        assert z.read(n['source_snapshot'])==source and z.read(n['stderr'])==b''
        log=z.read(n['stdout']).decode('utf-8-sig');assert 'error:' not in log and 'sorryAx' not in log
        assert 'AUDIT_OK TenthDiscriminant.Phase126Classification: 2 logical declarations; 2 theorems; 0 runtime-only auxiliaries excluded' in log
        for name,count in m['fresh_counts'].items():assert f'PHASE126_INPUTS_OK TenthDiscriminant.Phase126Classification.{name}: {count} reached;4required/8forbidden' in log
        assert log.count('PHASE126_INPUTS_OK ')==2
    assert subprocess.check_output(['git','diff','--name-only',m['base_commit'],'--','lean','.github'],cwd=ROOT)==b''
    links=0
    for name in ['CLASSIFICATION_INTERFACE_CURRENT.md','PHASE126_VERIFICATION.md']:
        p=HERE/name
        for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
            if '://' not in target:
                assert (p.parent/target.split('#',1)[0]).exists();links+=1
    print(f'PASS saved126:both full targets/firstcall/2namespace/2fresh required-and-excluded closures/4raw/{links}links. No Lean replay;no inherited source change.')

if __name__=='__main__':main()
