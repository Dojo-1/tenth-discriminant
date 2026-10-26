"""Check saved review integrity and scope metadata; does not execute Lean."""
from pathlib import Path
import hashlib
import json
import subprocess

root = Path(__file__).resolve().parents[2]
folder = Path(__file__).resolve().parent

def read(name):
    return json.loads((folder / name).read_text(encoding="utf-8"))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

dispatch = read("PHASE58_DISPATCH.json")
receipt = read("PHASE58_RECEIPT.json")
assert dispatch["target"] == "63be64b4ba3ff9795f552dd34bc415f6ea3acb25"
assert dispatch["registered_commit"] == "610f750d36eb05f81c92d0421c997a6189bd2d35"
assert dispatch["fresh_context"] and not dispatch["children_allowed"] and not dispatch["rerolls_allowed"]
assert 0 <= receipt["conservative_elapsed_seconds"] <= dispatch["wall_cap_seconds"] == 1800
for name, key in [("PHASE58_REVIEW_BRIEF.md", "brief_sha256"), ("PHASE58_PROTOCOL.md", "protocol_sha256")]:
    assert sha(folder / name) == dispatch[key], name
    old = subprocess.check_output(["git", "show", dispatch["registered_commit"] + ":research/ender_radius_bridge/" + name], cwd=root)
    assert hashlib.sha256(old).hexdigest() == dispatch[key], name
assert sha(folder / "PHASE58_REVIEW_REPORT.md") == receipt["first_report_sha256"] == receipt["reviewer_reported_sha256"]
assert sha(folder / "PHASE58_SOURCE_HASHES.json") == receipt["source_manifest_sha256"]
sources = read("PHASE58_SOURCE_HASHES.json")["hashes"]
assert len(sources) == 184
for name, expected in sources.items():
    assert sha(root / name) == expected, name
changed = subprocess.check_output(["git", "diff", "--name-only", dispatch["target"], "--", "lean"], cwd=root, text=True)
changed_sources = [name for name in changed.splitlines() if not name.endswith(".md")]
assert not changed_sources, changed_sources
print("PASS: registered protocol/brief; first native report hash; bounded receipt; 184 source/check/pin hashes; unchanged Lean source/check/pin tree (documentation excluded).")
print("Integrity only: no Lean rerun, independent semantic verdict, new cutoff or whole-library certification follows.")
