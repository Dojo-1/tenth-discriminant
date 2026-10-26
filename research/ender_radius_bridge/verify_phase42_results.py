"""Read preserved acceptance/failure records; never rerun the capped cutoff."""
import hashlib
import json
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
    manifest = load(HERE / "PHASE42_RESULTS.json")
    records = manifest["proof_attempts"] + manifest["partial_verification"]
    assert {p.name for p in HERE.glob("PHASE42_*.result.json")} == {r["record"] for r in records}
    assert [r["exit_code"] for r in manifest["proof_attempts"]] == [1, 99]
    assert manifest["proof_attempts"][-1]["stop_reason"] == "time_limit"
    assert not manifest["new_100b_cutoff_accepted"]
    assert not (ROOT / manifest["unaccepted_candidate"]["original_path"]).exists()
    assert len(list(HERE.glob("PHASE41_pilot_*.result.json"))) == 1
    assert not list(HERE.glob("PHASE42_pilot*"))
    for item in records:
        actual = load(HERE / item["record"])
        for key in ("elapsed_seconds", "observed_peak_working_set_bytes", "exit_code"):
            assert item[key] == actual[key], (item["record"], key)
        assert actual["observed_peak_working_set_bytes"] <= 8192*1024**2
        if item in manifest["partial_verification"]:
            assert actual["exit_code"] == 0 and not actual["stop_reason"]
        assert (HERE / actual["stderr"]).exists()
    for path, expected in manifest["source_fingerprints_lf_sha256"].items():
        assert digest((ROOT / path).read_bytes().replace(b"\r\n", b"\n")) == expected, path
    candidate = (ROOT / manifest["unaccepted_candidate"]["preserved_path"]).read_text(encoding="utf-8")
    old_header = "/-! Close the new family's counted upper budget and compose to the actual\nfield. No finite classification or previous cutoff is a proof premise. -/"
    new_header = "/-! UNACCEPTED Phase42 candidate: the fixed target hit its registered time\nlimit. This file is preserved outside the library, not imported or certified\nby the root. Its proposed upper budget and field cutoff remain unverified. -/"
    assert new_header in candidate
    assert digest(candidate.replace(new_header, old_header).encode()) == manifest["unaccepted_candidate"]["attempted_lf_sha256"]
    archive = manifest["audit_raw_archive"]
    data = (HERE / archive["path"]).read_bytes()
    assert len(data) == archive["bytes"] and digest(data) == archive["sha256"]
    with zipfile.ZipFile(HERE / archive["path"]) as bundle:
        assert bundle.namelist() == [archive["entry"]]
        raw = bundle.read(archive["entry"])
    assert len(raw) == archive["raw_bytes"] and digest(raw) == archive["raw_sha256"]
    assert b"4573 logical declarations; 3839 theorems; 16955 runtime-only" in raw
    geometry = next(r for r in manifest["partial_verification"] if r["mode"] == "geometry")
    geometry_log = load(HERE / geometry["record"])["stdout"]
    text = (HERE / geometry_log).read_text(encoding="utf-8")
    assert "NO_UNACCEPTED_100B_CUTOFF_IN_LIBRARY" in text
    assert "13721 reached" in text and "23486 reached" in text
    docs = [ROOT / p for p in ("README.md", "STATUS.md", "TAO_OBJECTIVES_CURRENT.md", "lean/FORMALIZATION.md")]
    docs += [HERE / "TUNED_CUTOFF_GUIDE.md", HERE / "PHASE42_VERIFICATION.md"]
    count = 0
    for doc in docs:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
            if target.startswith(("https:", "http:", "#", "mailto:")):
                continue
            assert (doc.parent / target.split("#")[0]).exists(), (doc, target)
            count += 1
    print(f"PASS: both failure/stop records,three partial checks,candidate-body preservation,source/archive hashes and{count} local reader targets")
    print("Scope: no cutoff retry, new pilot, universal100-billion theorem or remote CI inference.")


if __name__ == "__main__":
    main()
