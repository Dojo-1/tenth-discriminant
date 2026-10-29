"""Read saved rational evidence; do not rerun the Phase124 trial or Lean."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import re
import subprocess
import zipfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]

def main():
    m=json.loads((HERE/'PHASE124_RESULTS.json').read_text(encoding='utf-8'))
    f=json.loads((HERE/'PHASE124_FROZEN.json').read_text(encoding='utf-8'))
    for name,sha in f['files'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==sha
    archive=HERE/m['archive']
    assert hashlib.sha256(archive.read_bytes()).hexdigest()==m['archive_sha256']
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None and len(z.namelist())==5
        assert set(z.namelist())==set(m['raw_sha256'])
        for name,sha in m['raw_sha256'].items():
            assert hashlib.sha256(z.read(name)).hexdigest()==sha
        n=m['native_result']
        assert n['exit_code']==0 and n['stop_reason']=='' and n['elapsed_seconds']<30
        assert z.read(n['source_snapshot'])==(HERE/'phase124_rational_accounting.py').read_bytes()
        assert z.read(n['stderr'])==b'' and b'PASS: all10 fixed rational checks' in z.read(n['stdout'])
        data=json.loads(z.read(n['data']))
    names=['ceiling_absorption','inner_radius','chosen_radius_guard','upper_count','centered_rounding','derivative_gain','scale_saving','normalized_constant','published_endpoint','coarse_endpoint']
    assert [c['name'] for c in data['checks']]==names
    for c in data['checks']:
        v=Fraction(c['numerator'],c['denominator']);r=c['relation']
        assert c['passed'] and {'positive':v>0,'negative':v<0,'nonnegative':v>=0,'zero':v==0}[r]
    values={c['name']:Fraction(c['numerator'],c['denominator']) for c in data['checks']}
    assert values['normalized_constant']==Fraction(3,20000)
    assert values['published_endpoint']==Fraction(1862561,10000000000)
    assert m['cutoff_unchanged']==48000000000
    old=set(subprocess.check_output(['git','ls-tree','-r','--name-only',m['base_commit']],cwd=ROOT,text=True).splitlines())
    changed=set(subprocess.check_output(['git','diff','--name-only',m['base_commit']],cwd=ROOT,text=True).splitlines())
    assert (old & changed)<={'.agent/state.json','.agent/notes.md','research/ender_radius_bridge/FORTY_EIGHT_BILLION_GUIDE.md'}
    count=0
    for name in ['GEOMETRIC_COMPARISON_GUIDE.md','FORTY_EIGHT_BILLION_GUIDE.md','PHASE124_VERIFICATION.md']:
        p=HERE/name;s=p.read_text(encoding='utf-8')
        assert s.count(chr(92)+'[')==s.count(chr(92)+']') and chr(92)*2 not in s
        for target in re.findall(r'\]\(([^)]+)\)',s):
            target=target.split('#',1)[0]
            if target and '://' not in target:
                assert (p.parent/target).exists(),target
                count+=1
    print(f'PASS saved124:10rational checks/5raw;explicit baseline slack3/20000;{count}links;old mathematical sources frozen. No trial/Lean replay;no analytic premise inferred.')

if __name__=='__main__':
    main()
