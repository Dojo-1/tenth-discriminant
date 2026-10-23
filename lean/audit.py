#!/usr/bin/env python3
"""Check project import coverage, source escapes, and compiled axiom dependencies.

Import coverage is a structural check, not a Lean parser or a proof checker.
The compiled environment audit is authoritative for transitive dependencies.
"""
from pathlib import Path
import re
import subprocess
import sys


def source_code(path: Path) -> str:
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'/\-.*?\-/', '', text, flags=re.S)
    return re.sub(r'--[^\n]*', '', text)


def project_coverage(root: Path) -> list[str]:
    """Every project module must be reachable from the audited library root."""
    expected = {'.'.join(p.relative_to(root).with_suffix('').parts)
                for p in (root / 'TenthDiscriminant').rglob('*.lean')}
    seen: set[str] = set()
    active: set[str] = set()

    def visit(module: str) -> None:
        if module in active:
            raise ValueError('CYCLIC_PROJECT_IMPORT: ' + module)
        if module in seen:
            return
        path = root.joinpath(*module.split('.')).with_suffix('.lean')
        if not path.is_file():
            raise ValueError('MISSING_PROJECT_IMPORT: ' + module)
        active.add(module)
        for line in source_code(path).splitlines():
            words = line.strip().split()
            if words and words[0] == 'import':
                for dependency in words[1:]:
                    if dependency == 'TenthDiscriminant' or dependency.startswith('TenthDiscriminant.'):
                        visit(dependency)
        active.remove(module)
        seen.add(module)

    visit('TenthDiscriminant')
    missing = expected - seen
    if missing:
        raise ValueError('UNAUDITED_PROJECT_MODULES: ' + ', '.join(sorted(missing)))
    return sorted(expected)


def main() -> None:
    root = Path(__file__).resolve().parent
    modules = project_coverage(root)
    print(f'IMPORT_COVERAGE_OK: {len(modules)} project modules reachable', flush=True)
    for module in modules:
        path = root.joinpath(*module.split('.')).with_suffix('.lean')
        bad = re.search(r'\b(sorry|admit|axiom|native_decide|unsafe)\b', source_code(path))
        if bad:
            raise SystemExit(f'{path.name}: forbidden proof escape: {bad.group(0)}')
    run = subprocess.run(['lake', 'env', 'lean', 'Audit.lean'], cwd=root,
                         text=True, capture_output=True, timeout=300)
    print(run.stdout, end='')
    print(run.stderr, end='')
    if run.returncode:
        raise SystemExit(run.returncode)
    if 'AUDIT_OK TenthDiscriminant:' not in run.stdout:
        raise SystemExit('No completed Lean environment audit')
    print('PASS: all compiled project constants audited; only the three permitted axioms allowed.', flush=True)
    subprocess.run([sys.executable, str(root / 'apparatus_controls.py')],
                   cwd=root, check=True, timeout=240)


if __name__ == '__main__':
    main()
