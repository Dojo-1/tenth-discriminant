"""Read saved Phase122 evidence; never execute Lean or the trial runner."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent

def digest(data):
    return hashlib.sha256(data).hexdigest()

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)

def main():
    record = json.loads((HERE / "PHASE122_RESULTS.json").read_text(encoding="utf-8"))
    frozen = json.loads((HERE / "PHASE122_FROZEN.json").read_text(encoding="utf-8"))
    assert record["status"] == "STOPPED_UNREPAIRED_ELABORATION_FAILURE_NO_NEW_CUTOFF"
    assert record["attempts"] == 1 and not record["repair_or_retry"]
    assert record["accepted_production_cutoff"] == 48000000000
    for name, sha in frozen["files"].items():
        assert digest((ROOT / name).read_bytes()) == sha, name
    assert digest((HERE / record["source"]).read_bytes()) == record["source_sha256"]
    archive = HERE / record["archive"]
    assert digest(archive.read_bytes()) == record["archive_sha256"]
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert set(z.namelist()) == set(record["raw_sha256"]) and len(z.namelist()) == 4
        for name, sha in record["raw_sha256"].items():
            assert digest(z.read(name)) == sha, name
        native = record["native_result"]
        assert json.loads(z.read(next(n for n in z.namelist() if n.endswith(".result.json"))).decode("utf-8-sig")) == native
        assert native["exit_code"] == 1 and native["stop_reason"] == ""
        assert native["time_limit_seconds"] == 300 and native["memory_threshold_mb"] == 8192
        assert native["elapsed_seconds"] < 300 and native["observed_peak_working_set_bytes"] < 8192 * 1024**2
        assert z.read(native["source_snapshot"]) == (HERE / record["source"]).read_bytes()
        log = z.read(native["stdout"]).decode("utf-8")
        for marker in ["21:2: error: type mismatch", "12291 / 500", "24582 / 1000", "PHASE122_NONSTANDARD_AXIOM sorryAx", "endpoint_certificate: 9884 reached;77forbidden roots excluded"]:
            assert marker in log, marker
        assert z.read(native["stderr"]) == b""
    # Compare every earlier tracked file, including historical negative evidence.
    allowed = {".agent/state.json", ".agent/notes.md", "STATUS.md", "TAO_OBJECTIVES_CURRENT.md", "lean/FORMALIZATION.md", "research/ender_radius_bridge/FORTY_EIGHT_BILLION_GUIDE.md", "research/ender_radius_bridge/RADIAL_CUTOFF_CURRENT.md"}
    count = 0
    for entry in git("ls-tree", "-r", "-z", record["base_commit"]).split(b"\0"):
        if not entry:
            continue
        meta, name = entry.split(b"\t", 1)
        name = name.decode("utf-8")
        if name in allowed:
            continue
        assert (ROOT / name).read_bytes() == git("cat-file", "blob", meta.split()[2].decode()), name
        count += 1
    assert len((ROOT / "README.md").read_text(encoding="utf-8").splitlines()) == 61
    ledger = (ROOT / "TAO_OBJECTIVES_CURRENT.md").read_text(encoding="utf-8")
    assert len(ledger.splitlines()) == 61
    assert "48-billion quantitative comparison remains paper" not in ledger
    links = 0
    for name in record["current_reader_checks"]["readers"]:
        file = ROOT / name
        for target in re.findall(r"\]\(([^)]+)\)", file.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            assert (file.parent / target).exists(), (name, target)
            links += 1
    print(f"PASS saved122: one unrepaired failed attempt; certificate-only9884/77roots;4raw;{count}prior blobs unchanged;{links}reader links;production cutoff48b unchanged. No proof replay.")

if __name__ == "__main__":
    main()
