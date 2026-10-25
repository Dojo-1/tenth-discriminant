"""Check preserved Phase47 evidence and current source; do not rerun Lean."""
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    manifest = load(HERE / "PHASE47_RESULTS.json")
    records = manifest["records"]
    assert {p.name for p in HERE.glob("PHASE47_*.result.json")} == {r["record"] for r in records}
    for item in records:
        actual = load(HERE / item["record"])
        for key in ("mode", "exit_code", "elapsed_seconds", "observed_peak_working_set_bytes"):
            assert actual[key] == item[key], (item["record"], key)
        assert actual["stop_reason"] == ""
        assert actual["elapsed_seconds"] <= actual["time_limit_seconds"]
        assert actual["observed_peak_working_set_bytes"] <= 8192*1024**2
        assert (HERE / actual["stderr"]).exists()
    builds = [r for r in records if r["mode"] == "build"]
    assert [r["exit_code"] for r in builds] == [1, 1, 0]
    assert math.isclose(sum(r["elapsed_seconds"] for r in builds), manifest["cumulative_main_build_seconds"], abs_tol=1e-9)
    for path, expected in manifest["source_fingerprints_lf_sha256"].items():
        assert sha((ROOT / path).read_bytes().replace(b"\r\n", b"\n")) == expected, path
    first = (HERE / "Phase47Attempt1.lean").read_text(encoding="utf-8")
    second = (HERE / "Phase47Attempt2.lean").read_text(encoding="utf-8")
    current = (ROOT / "lean/TenthDiscriminant/ImaginaryQuadraticRepresentation.lean").read_text(encoding="utf-8")
    first = first.replace("  letI : Algebra.IsQuadraticExtension Rat K where\n    toFree := inferInstance\n    finrank_eq_two' := hdegree", "  letI : Algebra.IsQuadraticExtension Rat K :=\n    { toFree := inferInstance, finrank_eq_two' := hdegree }")
    first = first.replace("map_div, map_sub", "map_div₀, map_sub")
    assert first == second
    second = second.replace("  simp only [antiInvariantProjection, map_div₀, map_sub, map_ofNat, hinv]", "  simp only [antiInvariantProjection, map_div₀, map_sub, map_ofNat]\n  rw [hinv x]")
    second = second.replace("IsGalois.tfae Rat K", "IsGalois.tfae (F := Rat) (E := K)")
    assert second == current
    old_root = subprocess.check_output(["git", "show", manifest["baseline"]+":lean/TenthDiscriminant.lean"], cwd=ROOT).decode().replace("\r\n", "\n")
    new_root = (ROOT / "lean/TenthDiscriminant.lean").read_text(encoding="utf-8")
    assert new_root.replace("import TenthDiscriminant.ImaginaryQuadraticRepresentation\n", "") == old_root
    changed = subprocess.check_output(["git", "diff", "--name-only", manifest["baseline"], "--", "lean/TenthDiscriminant", ".github/workflows", "tools", "lean/lean-toolchain", "lean/lakefile.lean"], cwd=ROOT).decode().splitlines()
    assert set(changed) <= {"lean/TenthDiscriminant/ImaginaryQuadraticRepresentation.lean"}, changed
    archive = manifest["audit_raw_archive"]
    data = (HERE / archive["path"]).read_bytes()
    assert len(data) == archive["bytes"] and sha(data) == archive["sha256"]
    with zipfile.ZipFile(HERE / archive["path"]) as bundle:
        assert bundle.namelist() == [archive["entry"]]
        raw = bundle.read(archive["entry"])
    assert len(raw) == archive["raw_bytes"] and sha(raw) == archive["raw_sha256"]
    assert b"4627 logical declarations; 3890 theorems; 16958 runtime-only" in raw
    inputs = next(r for r in records if r["mode"] == "input")
    text = (HERE / load(HERE / inputs["record"])["stdout"]).read_text(encoding="utf-8")
    for count, excluded in ((45866, 24), (20732, 24), (58569, 16)):
        assert f"{count} reached; none of{excluded} named forbidden inputs" in text
    assert not list(HERE.glob("PHASE47_pilot*"))
    docs = [ROOT / p for p in ("README.md", "STATUS.md", "TAO_OBJECTIVES_CURRENT.md", "TAO_REPLY_BRIEF.md", "lean/FORMALIZATION.md", "lean/MATHEMATICAL_SPINE.md")]
    docs += [HERE / "CONJUGATION_BRIDGE_GUIDE.md", HERE / "PHASE47_VERIFICATION.md", HERE / "GENERATOR_BRIDGE_GUIDE.md"]
    links = 0
    for doc in docs:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
            if target.startswith(("http:", "https:", "#", "mailto:")):
                continue
            assert (doc.parent / target.split("#")[0]).exists(), (doc, target)
            links += 1
    print(f"PASS: six terminal records, both failed sources and exact repairs, three input closures, source/archive hashes; {links} local reader targets")
    print("Scope: correspondence, not new proof execution, independent review or publication-head CI.")


if __name__ == "__main__":
    main()
