"""Validate Phase46 records and current source correspondence; do not rerun Lean."""
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    manifest = read_json(HERE / "PHASE46_RESULTS.json")
    records = manifest["records"]
    assert {p.name for p in HERE.glob("PHASE46_*.result.json")} == {r["record"] for r in records}
    for item in records:
        actual = read_json(HERE / item["record"])
        for key in ("mode", "exit_code", "elapsed_seconds", "observed_peak_working_set_bytes"):
            assert actual[key] == item[key], (item["record"], key)
        assert actual["stop_reason"] == ""
        assert actual["elapsed_seconds"] <= actual["time_limit_seconds"]
        assert actual["observed_peak_working_set_bytes"] <= 8192*1024**2
        assert (HERE / actual["stderr"]).exists()
    builds = [r for r in records if r["mode"] == "build"]
    inputs = [r for r in records if r["mode"] == "input"]
    assert [r["exit_code"] for r in builds] == [1, 0]
    assert [r["exit_code"] for r in inputs] == [1, 0]
    assert math.isclose(sum(r["elapsed_seconds"] for r in builds), manifest["cumulative_main_build_seconds"], abs_tol=1e-9)
    for path, expected in manifest["source_fingerprints_lf_sha256"].items():
        assert sha((ROOT / path).read_bytes().replace(b"\r\n", b"\n")) == expected, path
    old_source = (HERE / "Phase46Attempt1.lean").read_text(encoding="utf-8")
    new_source = (ROOT / "lean/TenthDiscriminant/QuadraticGeneratorBridge.lean").read_text(encoding="utf-8")
    assert old_source.replace("AdjoinRoot.liftHom_root _ _ _", "AdjoinRoot.liftHom_root _ _") == new_source
    old_root = subprocess.check_output(["git", "show", manifest["baseline"]+":lean/TenthDiscriminant.lean"], cwd=ROOT).decode().replace("\r\n", "\n")
    new_root = (ROOT / "lean/TenthDiscriminant.lean").read_text(encoding="utf-8")
    assert new_root.replace("import TenthDiscriminant.QuadraticGeneratorBridge\n", "") == old_root
    changed = subprocess.check_output(["git", "diff", "--name-only", manifest["baseline"], "--", "lean/TenthDiscriminant", ".github/workflows", "tools", "lean/lean-toolchain", "lean/lakefile.lean"], cwd=ROOT).decode().splitlines()
    assert set(changed) <= {"lean/TenthDiscriminant/QuadraticGeneratorBridge.lean"}, changed
    archived = manifest["audit_raw_archive"]
    data = (HERE / archived["path"]).read_bytes()
    assert len(data) == archived["bytes"] and sha(data) == archived["sha256"]
    with zipfile.ZipFile(HERE / archived["path"]) as bundle:
        assert bundle.namelist() == [archived["entry"]]
        raw = bundle.read(archived["entry"])
    assert len(raw) == archived["raw_bytes"] and sha(raw) == archived["raw_sha256"]
    assert b"4614 logical declarations; 3878 theorems; 16955 runtime-only" in raw
    text = (HERE / read_json(HERE / inputs[-1]["record"])["stdout"]).read_text(encoding="utf-8")
    for count in (55578, 55781):
        assert f"{count} reached; none of16 listed forbidden inputs" in text
    assert not list(HERE.glob("PHASE46_pilot*"))
    docs = [ROOT / p for p in ("README.md", "STATUS.md", "TAO_OBJECTIVES_CURRENT.md", "TAO_REPLY_BRIEF.md", "lean/FORMALIZATION.md", "lean/MATHEMATICAL_SPINE.md")]
    docs += [HERE / "GENERATOR_BRIDGE_GUIDE.md", HERE / "PHASE46_VERIFICATION.md"]
    links = 0
    for doc in docs:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
            if target.startswith(("http:", "https:", "#", "mailto:")):
                continue
            assert (doc.parent / target.split("#")[0]).exists(), (doc, target)
            links += 1
    print(f"PASS: six terminal records, both preserved failures/sources, sole arity repair, two input closures, source/archive hashes; {links} local reader targets")
    print("Scope: correspondence, not new Lean execution, independent review or publication-head CI.")


if __name__ == "__main__":
    main()
