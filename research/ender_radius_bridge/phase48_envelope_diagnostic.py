"""One preregistered rational diagnostic; not a Lean cutoff proof."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import platform
import subprocess
import time

root = Path(__file__).resolve().parents[2]
out = Path(__file__).with_name("PHASE48_RESULTS.json")
if out.exists():
    raise SystemExit("Refusing to overwrite the registered execution record")
started = time.perf_counter()
record = {"scope": "exact rational envelope diagnostic only", "status": "FAIL",
          "python": platform.python_version(),
          "protocol_commit": subprocess.check_output(
              ["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()}
try:
    paths = ["research/ender_radius_bridge/PHASE48_PROTOCOL.md",
             "research/ender_radius_bridge/HUNDRED_BILLION_GUIDE.md",
             "lean/TenthDiscriminant/TunedRadiusFamily.lean",
             "lean/TenthDiscriminant/TunedAnalyticCutoff.lean",
             "lean/TenthDiscriminant/AspectRatioLowerEnvelope.lean"]
    record["source_sha256_raw"] = {
        p: hashlib.sha256((root / p).read_bytes()).hexdigest() for p in paths}
    slope = F(999997, 1000000) - F(4, 5)
    loss = F(5820, 1000) - F(813, 1000)
    zero = loss / slope
    controls = {str(u): str(slope*u-loss) for u in [F(25), F(253, 10)]}
    assert slope > 0
    assert slope*zero-loss == 0
    assert F(25) < zero < F(253, 10)
    assert F(controls["25"]) < 0 < F(controls["253/10"])
    assert F(controls["253/10"]) == F(529241, 10000000)
    record.update(status="PASS", gap_slope=str(slope), gap_loss=str(loss),
                  crossing=str(zero), controls=controls,
                  inference="These envelopes separate iff u exceeds the crossing; "
                  "overlap is inconclusive about the actual budgets. No new D cutoff.")
except Exception as exc:
    record["error"] = repr(exc)
    raise
finally:
    record["elapsed_seconds"] = time.perf_counter()-started
    out.write_text(json.dumps(record, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(record, indent=2))
