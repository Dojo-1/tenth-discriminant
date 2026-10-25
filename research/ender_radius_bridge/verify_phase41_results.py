"""Validate preserved records and links; never rerun the observational pilot."""
import ast
import hashlib
import json
from pathlib import Path
import re
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main():
    manifest = read_json(HERE / "PHASE41_RESULTS.json")
    records = [manifest["pilot"], *manifest["proof_attempts"], *manifest["verification"]]
    assert {p.name for p in HERE.glob("PHASE41_*.result.json")} == {r["record"] for r in records}
    assert len(manifest["proof_attempts"]) == 1
    for item in records:
        actual = read_json(HERE / item["record"])
        for key in ("elapsed_seconds", "observed_peak_working_set_bytes", "exit_code"):
            assert actual[key] == item[key], (item["record"], key)
        assert actual["exit_code"] == 0 and actual["stop_reason"] == ""
        assert actual["elapsed_seconds"] <= actual["time_limit_seconds"]
        assert actual["observed_peak_working_set_bytes"] <= 8192*1024**2
        assert (HERE / actual["stderr"]).is_file()
    pilot = read_json(HERE / manifest["pilot"]["output"])
    assert len(pilot["checks"]) == 17 and all(pilot["checks"].values())
    assert (pilot["D"], pilot["C"], pilot["precision_bits"]) == (100000000003, 25, 256)
    assert pilot["protocol_commit"] == manifest["protocol_commit"]
    for path, expected in manifest["source_fingerprints_lf_sha256"].items():
        content = (ROOT / path).read_bytes().replace(b"\r\n", b"\n")
        assert hashlib.sha256(content).hexdigest() == expected, path
    archive = manifest["audit_raw_archive"]
    archive_bytes = (HERE / archive["path"]).read_bytes()
    assert len(archive_bytes) == archive["bytes"]
    assert hashlib.sha256(archive_bytes).hexdigest() == archive["sha256"]
    with zipfile.ZipFile(HERE / archive["path"]) as bundle:
        assert bundle.namelist() == [archive["entry"]]
        raw = bundle.read(archive["entry"])
    assert len(raw) == archive["raw_bytes"]
    assert hashlib.sha256(raw).hexdigest() == archive["raw_sha256"]
    assert b"4543 logical declarations; 3812 theorems; 16951 runtime-only" in raw
    inputs = next(r for r in records if r.get("mode") == "input")
    input_log = read_json(HERE / inputs["record"])["stdout"]
    assert "13525 reached; no listed cutoff" in (HERE / input_log).read_text(encoding="utf-8")
    ast.parse((HERE / "phase41_aspect_pilot.py").read_text(encoding="utf-8"))
    count = 0
    docs = [ROOT / p for p in ("README.md", "STATUS.md", "TAO_OBJECTIVES_CURRENT.md", "lean/FORMALIZATION.md")]
    docs += [HERE / "ASPECT_RATIO_GUIDE.md", HERE / "PHASE41_VERIFICATION.md"]
    for doc in docs:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
            if target.startswith(("http:", "https:", "#", "mailto:")):
                continue
            assert (doc.parent / target.split("#")[0]).exists(), (doc, target)
            count += 1
    print(f"PASS: five terminal records,17 recorded pilot checks,source fingerprints,input closure and lossless raw audit; {count} local reader targets")
    print("Scope: correspondence only; no pilot rerun, universal new cutoff or remote CI inference.")


if __name__ == "__main__":
    main()
