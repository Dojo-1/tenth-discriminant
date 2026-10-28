"""Verify saved actual prefix-count evidence; no Lean rerun or weighted-loss claim."""
from pathlib import Path
from decimal import Decimal
import hashlib, json, re, subprocess, zipfile

f = Path(__file__).resolve().parent
root = f.parents[1]
d = json.loads((f / 'PHASE81_RESULTS.json').read_text(encoding='utf-8'))
sha = lambda b: hashlib.sha256(b).hexdigest()
blob = lambda ref, p: subprocess.check_output(['git', 'show', ref + ':' + p], cwd=root)
for n, h in d['sha256'].items():
    assert sha((f / n).read_bytes()) == h, n
for n in ['PHASE81_PROTOCOL.md', 'run_phase81.ps1']:
    assert blob(d['registered_commit'], 'research/ender_radius_bridge/' + n) == (f / n).read_bytes(), n
subprocess.run(['git', 'merge-base', '--is-ancestor', d['registered_commit'], 'HEAD'], cwd=root, check=True)
zp = f / d['raw_archive']['path']
assert sha(zp.read_bytes()) == d['raw_archive']['sha256']
with zipfile.ZipFile(zp) as z:
    assert z.testzip() is None and len(z.namelist()) == 8
    raw = {n: z.read(n) for n in z.namelist()}
assert {n: sha(b) for n, b in raw.items()} == d['raw_sha256']
rs = d['builds']
assert [r['attempt'] for r in rs] == [1, 2] and [r['exit_code'] for r in rs] == [1, 0]
elapsed = Decimal(0)
for r in rs:
    assert not r['stop_reason'] and r['elapsed_seconds'] <= 600
    assert abs(Decimal(str(r['cumulative_before_seconds'])) - elapsed) < Decimal('1e-9')
    elapsed += Decimal(str(r['elapsed_seconds']))
    assert r['time_limit_seconds'] == 600 and r['memory_threshold_mb'] == 8192
    assert r['observed_peak_working_set_bytes'] < 8192 * 1024**2
    assert sha(raw[r['source_snapshot']]) == r['source_sha256']
    assert json.loads(raw[r['stdout'].replace('.stdout.log', '.result.json')].decode('utf-8-sig')) == r
    assert 'maximum number of heartbeats' not in raw[r['stdout']].decode('utf-8-sig')
assert elapsed == Decimal(d['target_seconds']) == Decimal('148.9122284')
sources = [raw[r['source_snapshot']].decode('utf-8') for r in rs]
fixed = sources[0].replace('exact congrArg Subtype.val he⟩', 'exact congrArg (fun x : (J C : Ideal (𝓞 K)) => (x : 𝓞 K)) he⟩')
fixed = fixed.replace('have htotalR : (U.card : Real)=∑ C, q C := by exact_mod_cast htotal', 'have htotalR : (U.card : Real)=∑ C, q C := by\n    simpa only [Nat.cast_sum,q] using congrArg (fun n : Nat => (n : Real)) htotal')
assert fixed == sources[1]
types = lambda s: {m.group(1): ' '.join(s[m.start():s.index(' := by', m.end())].split()) for m in re.finditer(r'(?m)^theorem\s+(\w+)', s)}
assert len(types(sources[-1])) == 8 and types(sources[0]) == types(sources[1])
assert list(types(sources[-1])) == d['public_theorems']
assert raw[rs[-1]['source_snapshot']] == (f / 'Phase81ClassAggregation.lean').read_bytes()
old = (f / 'Phase62PrimeAxis.lean').read_text(encoding='utf-8')
assert sources[-1].split('theorem two_class_accounting', 1)[1].split('theorem actual_class_slice', 1)[0].strip() == old.split('theorem two_class_accounting', 1)[1].split('theorem counterexample_axis_control', 1)[0].strip()
failed = raw[rs[0]['stdout']].decode('utf-8-sig')
for s in ['congrArg Subtype.val he', 'mod_cast has type', 'NONSTANDARD_AXIOMS', 'sorryAx']:
    assert s in failed, s
log = raw[rs[-1]['stdout']].decode('utf-8-sig')
assert 'error:' not in log and 'sorryAx' not in log
assert 'AUDIT_OK TenthDiscriminant.ClassAggregation: 8 logical declarations; 8 theorems; 0 runtime-only' in log
for n in ['actual_class_slice', 'prime_prefix_bound', 'uniform_two_class_bound']:
    assert re.search(re.escape("'TenthDiscriminant.ClassAggregation." + n + "' depends on axioms:") + r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]', log), n
assert 'def TenthDiscriminant.ControlledPrimeFamily.ClassCountData' in log and 'def TenthDiscriminant.ResidueMultiplicity.PointAt' in log
for p, h in d['preserved_sha256'].items():
    assert sha((root / p).read_bytes()) == h == sha(blob(d['base'], p)), p
changed = subprocess.check_output(['git', 'diff', '--name-only', d['base'], '--', 'lean', 'tools', '.github', 'flow'], cwd=root, text=True).splitlines()
assert not [n for n in changed if not n.endswith('.md')], changed
assert (root / 'README.md').read_bytes() == blob(d['base'], 'README.md')
print('PASS: preregistration; FAIL/PASS and8rawfiles;8unchanged types; only subtype-domain/sum-cast repairs; exact62accounting;8/8/0standard-axiom audit; production80/prior evidence unchanged.')
print('Saved integrity only. Actual admissible-prime prefix COUNT proved locally; full weighted loss/even-field/cutoff/external CI remain separate.')
