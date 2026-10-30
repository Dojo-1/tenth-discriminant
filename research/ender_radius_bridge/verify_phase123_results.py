"""Verify saved Phase123 matrices and provenance; never evaluate polynomial jets."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import re
import subprocess
import zipfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]

def det(a):
    a=[[Fraction(x) for x in row] for row in a]
    value=Fraction(1)
    for k in range(len(a)):
        row=next((i for i in range(k,len(a)) if a[i][k]),None)
        if row is None:
            return 0
        if row!=k:
            a[k],a[row]=a[row],a[k]
            value=-value
        pivot=a[k][k]
        value*=pivot
        for i in range(k+1,len(a)):
            q=a[i][k]/pivot
            for j in range(k,len(a)):
                a[i][j]-=q*a[k][j]
    assert value.denominator==1
    return value.numerator

def main():
    manifest=json.loads((HERE/'PHASE123_RESULTS.json').read_text(encoding='utf-8'))
    frozen=json.loads((HERE/'PHASE123_FROZEN.json').read_text(encoding='utf-8'))
    for name,digest in frozen['files'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
    archive=HERE/manifest['archive']
    assert hashlib.sha256(archive.read_bytes()).hexdigest()==manifest['archive_sha256']
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None and len(z.namelist())==5
        assert set(z.namelist())==set(manifest['raw_sha256'])
        for name,digest in manifest['raw_sha256'].items():
            assert hashlib.sha256(z.read(name)).hexdigest()==digest,name
        native=manifest['native_result']
        assert native['exit_code']==0 and native['stop_reason']=='' and native['elapsed_seconds']<60
        assert z.read(native['source_snapshot'])==(HERE/'phase123_two_sided_oracle.py').read_bytes()
        data=json.loads(z.read(native['data']))
        assert z.read(native['stderr'])==b''
        assert b'PASS: 80 fixed cases' in z.read(native['stdout'])
    expected={(d,p,R,S,J) for d,p in [(1,3),(19,3),(2,5),(1,7)]
              for R,S in [(0,2),(2,0),(1,1),(4,2),(9,3)] for J in (0,1,p,p+1)}
    assert len(data['cases'])==80
    assert {(c['D'],c['p'],c['R'],c['S'],c['J']) for c in data['cases']}==expected
    for c in data['cases']:
        n=c['R']*c['S'];U,G,K=c['U'],c['G'],c['K']
        assert all(len(A)==n and all(len(row)==n for row in A) for A in [U,G,K])
        assert all(type(x) is int for A in [U,G,K] for row in A for x in row)
        assert len(c['weights'])==n and sum(c['weights'])==c['F']
        delta=[c['p']**k for k in c['weights']]
        UG=[[sum(U[i][k]*G[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                assert sum(UG[i][k]*U[j][k] for k in range(n))==delta[i]*K[i][j]*delta[j]
        assert det(U)==1 and det(G)==c['detG'] and det(K)==c['detK']
        assert c['detG']==c['p']**(2*c['F'])*c['detK']
    assert sum(c['detG']==0 for c in data['cases'])==manifest['zero_determinants']==18
    assert sum(c['detG']>0 for c in data['cases'])==manifest['positive_determinants']==62
    assert sum(c['jet_coordinates_checked'] for c in data['cases'])==manifest['jet_coordinates_checked']==15840
    assert data['negative_controls']==manifest['negative_controls']==4
    old=set(subprocess.check_output(['git','ls-tree','-r','--name-only',manifest['base_commit']],cwd=ROOT,text=True).splitlines())
    changed=set(subprocess.check_output(['git','diff','--name-only',manifest['base_commit']],cwd=ROOT,text=True).splitlines())
    allowed={'.agent/state.json','.agent/notes.md','research/ender_radius_bridge/FORTY_EIGHT_BILLION_GUIDE.md'}
    assert (old & changed)<=allowed,(old & changed)-allowed
    links=0
    for name in ['TWO_SIDED_ARITHMETIC_GUIDE.md','FORTY_EIGHT_BILLION_GUIDE.md']:
        p=HERE/name;text=p.read_text(encoding='utf-8')
        assert text.count(chr(92)+'[')==text.count(chr(92)+']')
        for target in re.findall(r'\]\(([^)]+)\)',text):
            target=target.split('#',1)[0]
            if target and '://' not in target:
                assert (p.parent/target).exists(),target
                links+=1
    print(f'PASS saved123:5raw;80fixed matrices;15840reported jet coordinates;18zero/62positive;exact Fraction determinant checks;old sources frozen;{links}links. No trial/Lean replay;finite data not universal proof.')

if __name__=='__main__':
    main()
