"""Validate preserved Phase43 records without rerunning Lean or any pilot."""
import hashlib
import json
import math
from pathlib import Path
import re
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    manifest = load(HERE / "PHASE43_RESULTS.json")
    records = manifest["proof_attempts"] + manifest["verification"]
    assert {p.name for p in HERE.glob("PHASE43_*.result.json")} == {r["record"] for r in records}
    assert len(manifest["proof_attempts"]) == 1
    for item in records:
        actual = load(HERE / item["record"])
        for key in ("exit_code", "elapsed_seconds", "observed_peak_working_set_bytes"):
            assert actual[key] == item[key], (item["record"], key)
        assert actual["exit_code"] == 0 and actual["stop_reason"] == ""
        assert actual["elapsed_seconds"] <= actual["time_limit_seconds"]
        assert actual["observed_peak_working_set_bytes"] <= 8192*1024**2
        assert (HERE / actual["stderr"]).exists()
    history = manifest["prior_negative_history"]
    old = [load(HERE / path) for path in history["records"]]
    assert [r["exit_code"] for r in old] == history["exit_codes"] == [1, 99]
    assert old[-1]["stop_reason"] == "time_limit"
    assert [r["elapsed_seconds"] for r in old] == history["elapsed_seconds"]
    total = sum(r["elapsed_seconds"] for r in old) + manifest["proof_attempts"][0]["elapsed_seconds"]
    assert math.isclose(total, history["combined_Phase42_and_Phase43_proof_build_seconds"], abs_tol=1e-9)
    assert len(list(HERE.glob("PHASE41_pilot_*.result.json"))) == 1
    assert not list(HERE.glob("PHASE43_pilot*"))
    for path, expected in manifest["source_fingerprints_lf_sha256"].items():
        assert digest((ROOT / path).read_bytes().replace(b"\r\n", b"\n")) == expected, path
    old_body = (HERE / "Phase42UnacceptedCutoff.lean").read_text(encoding="utf-8")
    new_body = (ROOT / "lean/TenthDiscriminant/TunedAnalyticCutoff.lean").read_text(encoding="utf-8")
    marker = "namespace TenthDiscriminant.FirstCertificate.Tuned"
    old_body, new_body = old_body.split(marker, 1)[1], new_body.split(marker, 1)[1]
    assert old_body == new_body
    assert digest(new_body.encode()) == manifest["mathematical_body_sha256"]
    archive = manifest["audit_raw_archive"]
    data = (HERE / archive["path"]).read_bytes()
    assert len(data) == archive["bytes"] and digest(data) == archive["sha256"]
    with zipfile.ZipFile(HERE / archive["path"]) as bundle:
        assert bundle.namelist() == [archive["entry"]]
        raw = bundle.read(archive["entry"])
    assert len(raw) == archive["raw_bytes"] and digest(raw) == archive["raw_sha256"]
    assert b"4602 logical declarations; 3868 theorems; 16955 runtime-only" in raw
    inputs = next(r for r in manifest["verification"] if r["mode"] == "input")
    text = (HERE / load(HERE / inputs["record"])["stdout"]).read_text(encoding="utf-8")
    for count in (55436, 55569, 55772):
        assert f"{count} reached; none of16 listed" in text
    docs = [ROOT / p for p in ("README.md", "STATUS.md", "TAO_OBJECTIVES_CURRENT.md", "TAO_REPLY_BRIEF.md", "lean/FORMALIZATION.md", "lean/README.md", "lean/HUMAN_GUIDE.md", "lean/MATHEMATICAL_SPINE.md")]
    docs += [HERE / "HUNDRED_BILLION_GUIDE.md", HERE / "PHASE43_VERIFICATION.md"]
    count = 0
    for doc in docs:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
            if target.startswith(("https:", "http:", "#", "mailto:")):
                continue
            assert (doc.parent / target.split("#")[0]).exists(), (doc, target)
            count += 1
    print(f"PASS: four local records,three input closures,unchanged candidate body,prior negative history,source/archive hashes; {count} local reader targets")
    print("Scope: correspondence, not independent review or exact-head remote CI; no rerun or new pilot.")


if __name__ == "__main__":
    main()
