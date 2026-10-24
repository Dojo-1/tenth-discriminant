"""Fixed eleven-seed partition; generation is not proof of any certificate."""
import json
from pathlib import Path
from generate_phase34_pilot import mask

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
QUOTIENTS = [0, 1, 392, 784]
SEEDS = [3 + 8 * k for k in range(23) if not (mask(23) >> ((3 + 8 * k) % 23)) & 1]


def main():
    records = []
    for k in QUOTIENTS:
        for i, seed in enumerate(SEEDS):
            name = f"Phase35Block{k}_{i}Check.lean"
            source = ("import TenthDiscriminant.FusedWheelParameters\n\n"
                      "namespace TenthDiscriminant\n"
                      f"example : phase35Block {k} {seed}=true := by decide +kernel\n"
                      "end TenthDiscriminant\n")
            (HERE / name).write_text(source, encoding="utf-8", newline="\n")
            records.append({"quotient": k, "seed_index": i, "seed": seed, "proof_file": name})
    (HERE / "Phase35SeedsCheck.lean").write_text(
        "import TenthDiscriminant.FusedWheelParameters\n\n"
        "namespace TenthDiscriminant\n"
        f"example : phase35Seeds={str(SEEDS)} := by decide +kernel\n"
        "end TenthDiscriminant\n", encoding="utf-8", newline="\n")
    manifest = {"scope": "fixed Phase35 cost pilot; generated inputs, not outcomes",
                "quotients": QUOTIENTS, "seeds": SEEDS, "blocks": records}
    (HERE / "PHASE35_MANIFEST.json").write_text(json.dumps(manifest, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"seed_count": len(SEEDS), "seeds": SEEDS,
                      "quotients": QUOTIENTS, "planned_blocks": len(records)}))


if __name__ == "__main__":
    main()
