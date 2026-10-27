# Phase85: one sealed scalar feasibility test

Result: first positive sample2^50=1125899906842624, margin>0.07.
At2^48 the margin is<-0.21. This is numerical scalar feasibility only.
It is NOT a new Lean theorem, all-D estimate, field result or cutoff.
[Human explanation](TWO_CLASS_FEASIBILITY_GUIDE.md).

Base1cf5f5ed564a7aad2e472dc00fac54812ffde55f.
Registration2d14a92ade1701672dbdaf448560a62c87e2ffe5 before code/execution.
[Protocol](PHASE85_PROTOCOL.md), [source](Phase85Feasibility.py),
[manifest](PHASE85_RESULTS.json), [raw archive](PHASE85_RAW.zip).

## What was run

Exactly N=36,38,...,64,80,96,128,18points, at100and200decimal digits,
in ONE invocation. No adaptation, extra point, precision change, fix or
rerun. The exact formula was

    (.159997*ln(D)-4.926)
      - ((4/sqrt(D)+1/sqrt(sqrt(D)))*(2+ln(D)*(1+ln(D)))+1/3).

Exact command executed from the root:

```sh
python research/ender_radius_bridge/Phase85Feasibility.py
```

The registered runner invoked that command once. It returned0 after
0.7618379seconds; internal calculation time was0.029030699995928444seconds.
The cap was120seconds. The runner recorded peak working set0 because the
process ended before a memory sample. This is MISSING observation, not
zero memory use or verified compliance with an observed8192MB maximum.
No resource stop was reported. Raw metadata is unchanged; no retry.
Python and libmpdec versions are in the raw JSON.

## Numerical and integrity checks

Basic arithmetic uses directed rounding. Decimal ln/sqrt are correctly
rounded half-even; adjacent representable values enclose their endpoint
results. The source contains no float constants in the calculation.
Eight controls passed at EACH precision: rational1/3, sqrt4, log1,
log4/2log2, three sign controls and detection of an omitted+1/3payment.
All18lower-precision interval tuples contain their higher-precision tuple.
Each precision has7negative,11positive,0unresolved samples. Full negative
results remain in the archived stdout, alongside all positive results.

The saved verifier checks four raw file hashes, the sealed grid/control
records, signs/nesting and the H/margin arithmetic with exact fractions;
it checks root enclosures by squaring/fourth powers. It does not reevaluate
logarithms or square roots and is not an independent transcendental
implementation. It also freezes1392prior source/evidence paths, including
all production proof files, older failed attempts and protocols.

```sh
python research/ender_radius_bridge/verify_phase85_results.py
```

## Limits that travel with this result

The scalar envelopes are class-free helper inequalities in the frozen
proof sources; no earlier h1cutoff theorem is assumed. The conservative
Hmajorization, all-D monotonic bound and complete new prime-mass/diagonal
composition still need a checked theorem. Earlier84root build/audit remain
their own result:5103logical/4327theorems, not new checks in this cycle.
No production Lean/tool/pin/certificate/CI gate changed. No external CI,
independent review, publication, merge or new class-number cutoff occurred.
The h1cutoff stays50billion. README stays61lines.

Reader checks: all 411 local links in the seven updated reader documents
resolve; README remains 61 lines. Changed-file whitespace checks pass.
