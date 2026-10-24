"""Proof-only grouping for the unchanged 208 prime labels."""
from generate_phase34_pilot import BASE, prime
from generate_phase35_pilot import ROOT


def main():
    ps = BASE+[p for p in range(29, 100000) if prime(p)][:200]
    count = (len(ps)+15)//16
    text = ("import TenthDiscriminant.ResidueMaskBridge\n"
            "import TenthDiscriminant.FusedWheelMasks\n\n"
            "/-! Generated small primality proofs, aggregated along the exact data split. -/\n"
            "namespace TenthDiscriminant\n\n")
    for i in range(count):
        text += (f"theorem phase35PrimeChunk{i}_checked :\n"
                 f"    checkedOddPrimes (phase35MaskChunk{i}.map Prod.fst)=true := by\n"
                 f"  norm_num [checkedOddPrimes, phase35MaskChunk{i}]\n\n")
    checks = ", ".join(f"phase35PrimeChunk{i}_checked" for i in range(count))
    text += ("theorem phase35_all_primes_checked :\n"
             "    checkedOddPrimes ((phase34Base++phase34Extra).map Prod.fst)=true := by\n"
             "  rw [phase35_entries_split]\n"
             f"  simp only [List.map_append, checkedOddPrimes_append, {checks}, Bool.and_self]\n\n"
             "theorem phase35_extra_primes_checked :\n"
             "    checkedOddPrimes (phase34Extra.map Prod.fst)=true := by\n"
             "  have h := phase35_all_primes_checked\n"
             "  rw [List.map_append, checkedOddPrimes_append] at h\n"
             "  exact (Bool.and_eq_true_iff.mp h).2\n\nend TenthDiscriminant\n")
    (ROOT/"lean/TenthDiscriminant/FusedWheelPrimes.lean").write_text(text, encoding="utf-8", newline="\n")
    print(f"Generated {count} checked-prime groups; no prime labels changed.")


if __name__ == "__main__":
    main()
