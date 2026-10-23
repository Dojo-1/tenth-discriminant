#!/usr/bin/env python3
"""API examples and adversarial controls of the apparatus audit itself.

The old theorem-only collector is reproduced under a different command name to
expose a specific coverage gap. This is not a defect in already audited proofs.
"""
from pathlib import Path
import subprocess
import re
import tempfile
from audit import project_coverage

ROOT = Path(__file__).resolve().parent
LEGACY = r'''
open Lean Elab Command
elab "#legacy_audit_namespace " ns:ident : command => do
  let scopeName := ns.getId
  let env <- getEnv
  let mut count := 0
  for (name, info) in env.constants.toList do
    if scopeName.isPrefixOf (Lean.privateToUserName name) then
      match info with
      | .axiomInfo _ => throwError "PROJECT_AXIOM {name}"
      | .thmInfo _ =>
        let dependencies <- Lean.collectAxioms name
        for dep in dependencies do
          unless dep == ``propext || dep == ``Classical.choice || dep == ``Quot.sound do
            throwError "NONSTANDARD_AXIOMS {name}: {dependencies}"
        count := count + 1
      | _ => pure ()
  if count == 0 then throwError "EMPTY_PROOF_AUDIT {scopeName}"
  logInfo m!"LEGACY_OK {scopeName}"
'''
LEGACY = LEGACY.replace('<-', '\u2190')
PUBLIC = r'''
open TenthDiscriminant
example (P : Finset Complex) (J R S : Nat)
    (hR : 1 <= R) (hS : 1 <= S) (hJ : S <= J)
    (hc : 2*(R-1)+(S-1) < P.card) :
    (rectangularTraceGram P J R S).PosDef :=
  rectangularTraceGram_posDef_of_point_count P J R S hR hS hJ hc

example (P : Finset Complex) (R S : Nat)
    (hR : 1 <= R) (hS : 1 <= S) (hc : 3*R+S < P.card) :
    0 < (rectangularTraceGram P S R S).det := by
  exact (rectangularTraceGram_det_bounds P S R S hR hS (by omega) (by omega)).1

example (P : Finset Complex) (J R S : Nat)
    (hR : 1 <= R) (hS : 1 <= S) (hJ : S <= J)
    (hc : 2*(R-1)+(S-1) < P.card) :
    (rectangularTraceGram P J R S).det <=
      Finset.univ.prod (fun i => rectangularTraceGram P J R S i i) :=
  (rectangularTraceGram_det_bounds P J R S hR hS hJ hc).2

example : 0 < (rectangularTraceGram {0} 1 1 1).det := by
  apply (rectangularTraceGram_det_bounds {0} 1 1 1 (by decide) (by decide)
    (by decide) (by simp)).1
'''
SENTINEL = '\ntheorem sentinel : 2+2=4 := by decide\n'
HIDDEN = '''namespace ExternalAuditFixture
axiom value : True
end ExternalAuditFixture
namespace ApparatusProbe
opaque unusedValue : True := ExternalAuditFixture.value
'''+SENTINEL+'end ApparatusProbe\n'
PROBES = [
    ('definition_only', True, 'namespace ApparatusProbe\ndef answer : Nat := 42\nend ApparatusProbe', 'AUDIT_OK'),
    ('opaque_safe', True, 'namespace ApparatusProbe\nopaque answer : Nat := 42\nend ApparatusProbe', 'AUDIT_OK'),
    ('private_safe', True, 'namespace ApparatusProbe\nprivate def answer : Nat := 42\nend ApparatusProbe', 'AUDIT_OK'),
    ('unused_opaque_custom_axiom', False, HIDDEN, 'NONSTANDARD_AXIOMS'),
    ('unused_definition_custom_axiom', False, HIDDEN.replace('opaque unusedValue', 'noncomputable def unusedValue'), 'NONSTANDARD_AXIOMS'),
    ('private_opaque_custom_axiom', False, HIDDEN.replace('opaque unusedValue', 'private opaque unusedValue'), 'NONSTANDARD_AXIOMS'),
    ('safe_generated_looking_name', False, HIDDEN.replace('unusedValue', 'looksGenerated._cstage2'), 'NONSTANDARD_AXIOMS'),
    ('unused_opaque_incomplete', False, HIDDEN.replace('axiom value : True', 'theorem value : True := by sorry'), 'NONSTANDARD_AXIOMS'),
    ('project_axiom', False, 'namespace ApparatusProbe\naxiom value : True\nend ApparatusProbe', 'PROJECT_AXIOM'),
    ('empty_namespace', False, '', 'EMPTY_PROOF_AUDIT'),
]


def compile_case(folder: Path, label: str, source: str) -> subprocess.CompletedProcess[str]:
    path = folder / (label + '.lean')
    path.write_text('import TenthDiscriminant\n'+source+'\n', encoding='utf-8')
    return subprocess.run(['lake', 'env', 'lean', str(path)], cwd=ROOT,
                          text=True, capture_output=True, timeout=120)


def expect(folder: Path, label: str, source: str, success: bool, marker: str = '') -> None:
    result = compile_case(folder, label, source)
    output = result.stdout + result.stderr
    if (result.returncode == 0) != success or (marker and marker not in output):
        raise SystemExit(f'{label}: unexpected outcome\n{output}')
    print(f'PASS: apparatus {label}', flush=True)
    if not success:
        print(output.strip(), flush=True)


def check_import_gate(folder: Path) -> None:
    root = folder / 'imports'
    (root / 'TenthDiscriminant').mkdir(parents=True)
    (root / 'TenthDiscriminant.lean').write_text('import TenthDiscriminant.A\n')
    (root / 'TenthDiscriminant/A.lean').write_text('import TenthDiscriminant.B\n')
    (root / 'TenthDiscriminant/B.lean').write_text('')
    if len(project_coverage(root)) != 2:
        raise SystemExit('Import closure positive control failed')
    (root / 'TenthDiscriminant/Orphan.lean').write_text('')
    try:
        project_coverage(root)
    except ValueError as error:
        if 'UNAUDITED_PROJECT_MODULES' not in str(error):
            raise
    else:
        raise SystemExit('An unimported module escaped the gate')
    (root / 'TenthDiscriminant/Orphan.lean').unlink()
    (root / 'TenthDiscriminant/B.lean').write_text('import TenthDiscriminant.A\n')
    try:
        project_coverage(root)
    except ValueError as error:
        if 'CYCLIC_PROJECT_IMPORT' not in str(error):
            raise
    else:
        raise SystemExit('A cyclic import escaped the gate')
    print('PASS: import closure accepts a complete graph and rejects orphans/cycles', flush=True)


with tempfile.TemporaryDirectory() as tmp:
    folder = Path(tmp)
    check_import_gate(folder)
    expect(folder, 'public_rectangular_api', PUBLIC, True)
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    snippets = re.findall(r'```lean\n(.*?)```', readme, re.S)
    if not snippets:
        raise SystemExit('No readable Lean example was found')
    expect(folder, 'readme_examples', '\n'.join(snippets), True)
    for name in ['README.md', 'HUMAN_GUIDE.md', 'FORMALIZATION.md']:
        text = (ROOT / name).read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if '://' not in target and not target.startswith('#'):
                if not (ROOT / target.split('#', 1)[0]).is_file():
                    raise SystemExit(f'{name}: broken local link {target}')
    print('PASS: all three reader documents have resolvable local links', flush=True)
    expect(folder, 'legacy_unused_opaque_gap', LEGACY+HIDDEN+'\n#legacy_audit_namespace ApparatusProbe', True, 'LEGACY_OK')
    for label, success, source, marker in PROBES:
        expect(folder, label, source+'\n#audit_namespace ApparatusProbe', success, marker)
print('PASS: readable API, import coverage and compiled-constant audit controls')
