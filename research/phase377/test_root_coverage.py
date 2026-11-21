"""Phase377: falsify structural project-root coverage before running the real audit.

This uses the EXISTING lean/audit.py project_coverage routine against both
the actual repository and disposable mini-repositories. It also implements a
second minimal import-scan oracle for the six newly registered modules.

These are structural tests. They cannot replace \`lake build\`,
\`#audit_namespace\`, negative mathematical controls, or independent review.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import re
import tempfile
import unittest

REPO=Path(__file__).resolve().parents[2]
LEAN=REPO/"lean"
ROOT=LEAN/"TenthDiscriminant.lean"
AUDIT=LEAN/"audit.py"
REQUIRED=(
    "Phase371CausalReceipt",
    "Phase372ExecutionAttempts",
    "Phase373ClockAuthoritySquare",
    "Phase374ManifestRefinement",
    "Phase375PolicyTransport",
    "Phase376IndependentWitness",
)

spec=importlib.util.spec_from_file_location("phase377_actual_root_audit",AUDIT)
assert spec and spec.loader
actual=importlib.util.module_from_spec(spec)
spec.loader.exec_module(actual)


def independent_reachability(module_root:Path)->set[str]:
    """Independent, deliberately simple DFS over project import statements."""
    def project_imports(path:Path)->list[str]:
        body=actual.source_code(path)
        result=[]
        for line in body.splitlines():
            match=re.match(r"^\s*import\s+(.+?)\s*$",line)
            if not match:
                continue
            result.extend(token for token in match.group(1).split()
                          if token.startswith("TenthDiscriminant."))
        return result
    visited=set()
    active=set()
    def visit(name):
        if name in active:
            raise ValueError("CYCLE: "+name)
        if name in visited:
            return
        path=module_root.joinpath(*name.split(".")).with_suffix(".lean")
        if not path.is_file():
            raise ValueError("MISSING: "+name)
        active.add(name)
        for dep in project_imports(path):
            visit(dep)
        active.remove(name)
        visited.add(name)
    visit("TenthDiscriminant")
    return visited


def write_fixture(root:Path,imports:list[str],with_extra:bool=True)->None:
    (root/"TenthDiscriminant").mkdir(exist_ok=True,parents=True)
    (root/"TenthDiscriminant.lean").write_text(
        "\n".join("import TenthDiscriminant."+n for n in imports)+"\n",
        encoding="utf-8")
    (root/"TenthDiscriminant"/"A.lean").write_text(
        "namespace TenthDiscriminant\nexample : True := by trivial\nend TenthDiscriminant\n",
        encoding="utf-8")
    if with_extra:
        (root/"TenthDiscriminant"/"B.lean").write_text(
            "namespace TenthDiscriminant\nexample : True := by trivial\nend TenthDiscriminant\n",
            encoding="utf-8")


class RootCoverageAuditControls(unittest.TestCase):
    def test_all_six_modules_are_explicit_root_imports(self):
        imports=ROOT.read_text(encoding="utf-8")
        for module in REQUIRED:
            self.assertEqual(
                len(re.findall(r"(?m)^import TenthDiscriminant\."+module+r"$",imports)),
                1,module)

    def test_actual_project_root_coverage_is_complete(self):
        audited=actual.project_coverage(LEAN)
        for module in REQUIRED:
            self.assertIn("TenthDiscriminant."+module,audited)
        self.assertGreater(len(audited),100)

    def test_independent_dfs_matches_existing_audit_module_set(self):
        expected=set(actual.project_coverage(LEAN))
        observed=independent_reachability(LEAN)
        self.assertEqual(observed-{"TenthDiscriminant"},expected)

    def test_missing_new_module_is_reported_not_silently_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            write_fixture(root,["A"])
            with self.assertRaisesRegex(ValueError,"UNAUDITED_PROJECT_MODULES.*TenthDiscriminant.B"):
                actual.project_coverage(root)

    def test_new_module_registering_repairs_fixture_without_bypass(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            write_fixture(root,["A","B"])
            self.assertEqual(actual.project_coverage(root),
                             ["TenthDiscriminant.A","TenthDiscriminant.B"])

    def test_cyclic_project_import_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            write_fixture(root,["A"])
            p=root/"TenthDiscriminant"/"A.lean"
            p.write_text("import TenthDiscriminant.A\n",encoding="utf-8")
            with self.assertRaisesRegex(ValueError,"CYCLIC_PROJECT_IMPORT"):
                actual.project_coverage(root)

    def test_absent_project_import_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            write_fixture(root,["A","C"],with_extra=False)
            with self.assertRaisesRegex(ValueError,"MISSING_PROJECT_IMPORT.*TenthDiscriminant.C"):
                actual.project_coverage(root)

    def test_root_audit_still_runs_kernel_audit_and_negative_controls(self):
        script=AUDIT.read_text(encoding="utf-8")
        workflow=(REPO/".github/workflows/lean.yml").read_text(encoding="utf-8")
        self.assertIn("project_coverage(root)",script)
        self.assertIn("subprocess.run(['lake', 'env', 'lean', 'Audit.lean']",script)
        self.assertIn("subprocess.run([sys.executable, str(root / 'apparatus_controls.py')]",script)
        self.assertIn("run: python3 audit.py",workflow)
        self.assertIn("run: python3 negative_controls.py",workflow)
        self.assertIn("run: lake build",workflow)

    def test_forbidden_proof_escape_can_be_detected_in_real_modules(self):
        for module in REQUIRED:
            path=LEAN/"TenthDiscriminant"/(module+".lean")
            source=actual.source_code(path)
            self.assertIsNone(re.search(
                r"\b(sorry|admit|axiom|native_decide|unsafe)\b",source),module)

    def test_negative_control_proof_escape_detected_in_fixture(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"Fake.lean"
            path.write_text(
                "namespace Fake\n-- sorry (comment only)\n"
                "theorem foo : True := by sorry\nend Fake\n",
                encoding="utf-8")
            scanned=actual.source_code(path)
            self.assertRegex(scanned,r"\bsorry\b")

    def test_comment_only_proof_escape_not_triggered(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"Fake.lean"
            path.write_text(
                "namespace Fake\n-- sorry is commentary, not a proof\n"
                "theorem foo : True := by trivial\nend Fake\n",
                encoding="utf-8")
            self.assertNotRegex(actual.source_code(path),r"\bsorry\b")

    def test_no_silent_root_audit_exemption_for_new_phases(self):
        source=AUDIT.read_text(encoding="utf-8")
        self.assertNotIn("PHASE371_SKIP",source)
        self.assertNotIn("PHASE377_ALLOWLIST",source)
        for module in REQUIRED:
            self.assertNotIn(module,source)  # no special cases in audit.py


if __name__=="__main__":
    unittest.main()
