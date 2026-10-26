# Phase66: actual class-fiber norm lifting

**First registered standalone invocation PASS,35.6280967s.** Protocolcca390f
precedes source and execution; base2dd80eb. No repair, second attempt,
separate Lean probe, resource stop or prior-campaign rerun occurred.

The accepted output prints both full public types: for each actual class C,
J is chosen before every ideal I and before every positive modulus/residue
map. NormLift is also printed: nonzero element, membership in J, the actual
principal-product identity, actual norm magnitude and exact ideal recovery.
No class-number-one, PID, supplied small representative or norm-lifting
premise occurs. Mathlib's existing Minkowski theorem supplies the bound;
this work supplies its class-wide lifting/recovery arrangement.

The compiled namespace audit checks15 logical declarations,12 theorems and
3 runtime-only auxiliaries, allowing only propext,Classical.choice,Quot.sound.
The two public root axiom prints have exactly these standard3 axioms.
This namespace count does not replace the full production-library audit.

Fixed controls all compile: the actual rational quotient to ZMod3
instantiates the entire residue theorem without a class-number hypothesis;
negation preserves NormLift; zero ideal multiplication is not injective;
zero modulus has zero kernel norm and is excluded from the nonzero residue
ideal construction. Norm magnitude is retained for arbitrary number fields.

From the repository root, the runner was invoked once:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase66.ps1 -Mode build
```

Its exact lake arguments, resource observations, source SHA256 and terminal
exit0 are in PHASE66_RESULTS.json. The source is byte-identical to the
accepted snapshot. PHASE66_RAW.zip contains all4 original source/log/result
files. Saved-evidence integrity can be checked without rerunning Lean:

```powershell
python research/ender_radius_bridge/verify_phase66_results.py
```

[Human proof](CLASS_FIBER_GUIDE.md). The bound is on ideal norm, not a future
binary-form leading coefficient. No basis/coefficient/discriminant theorem,
unramified-prime pair/four-representation multiplicity, arithmetic B,
ramification identification or new cutoff is supplied. This is standalone
research outside the production root/CI; no independent review is claimed.
PR32 CI40416976865 remains separate; no success is transferred to this file.
