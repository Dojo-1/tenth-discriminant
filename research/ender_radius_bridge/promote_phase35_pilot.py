"""Promote ONLY complete accepted translates, as separate kernel proofs.

The run record selects scripts; Lean rechecks every selected block. A log
or generator cannot supply a theorem by itself. Imports serialize the
large reductions rather than running many memory-heavy kernels together.
"""
import json
from pathlib import Path
from generate_phase35_pilot import ROOT, HERE, QUOTIENTS, SEEDS


def main():
    results = json.loads((HERE / "PHASE35_PILOT_RESULTS.json").read_text(encoding="utf-8-sig"))
    blocks = results["blocks"]
    assert len(blocks) == 44
    index = {(b["quotient"], b["seed_index"]): b for b in blocks}
    assert len(index) == 44
    accepted = [q for q in QUOTIENTS if all(
        index[q, i]["status"] == "terminal" and index[q, i].get("exit_code") == 0
        and index[q, i]["seed"] == seed for i, seed in enumerate(SEEDS))]
    if not accepted:
        print("No complete translate; no concrete certificate module generated.")
        return
    destination = ROOT / "lean/TenthDiscriminant"
    previous = "FusedWheelMasks"
    for q in accepted:
        for i, seed in enumerate(SEEDS):
            module = f"Fused35Q{q}S{i:02d}"
            source = (f"import TenthDiscriminant.{previous}\n\n"
                      "/-! Generated closed block proof; the kernel recomputes the fixed predicate. -/\n"
                      "namespace TenthDiscriminant\n"
                      f"theorem phase35_block_{q}_{i} : phase35Block {q} {seed}=true := by decide +kernel\n"
                      "end TenthDiscriminant\n")
            (destination / f"{module}.lean").write_text(source, encoding="utf-8", newline="\n")
            previous = module
    source = (f"import TenthDiscriminant.{previous}\n"
              "import TenthDiscriminant.FusedWheelBridge\n\n"
              "namespace TenthDiscriminant\nset_option autoImplicit false\n\n"
              f"theorem phase35_seeds_exact : phase35Seeds={str(SEEDS)} := by decide +kernel\n")
    for q in accepted:
        names = ", ".join(f"phase35_block_{q}_{i}" for i in range(11))
        source += (f"\ntheorem phase35_q{q}_blocks : phase35Seeds.all (phase35Block {q})=true := by\n"
                   "  rw [phase35_seeds_exact]\n"
                   f"  simp only [List.all_cons, List.all_nil, {names}, Bool.and_self]\n"
                   f"\ntheorem phase35_q{q}_translate :\n"
                   "    maskTranslateClear (maskWheelResidues phase34Base)\n"
                   f"      892371480 1000000 700000000000 {q} phase34Extra=true :=\n"
                   f"  phase35_translate_of_blocks {q} phase35_q{q}_blocks\n")
    source += "\nend TenthDiscriminant\n"
    (destination / "FusedWheelPilot.lean").write_text(source, encoding="utf-8", newline="\n")
    print(json.dumps({"complete_pilot_quotients": accepted,
                      "separate_block_modules": len(accepted)*11,
                      "status": "generated scripts only; library recheck required"}))


if __name__ == "__main__":
    main()
