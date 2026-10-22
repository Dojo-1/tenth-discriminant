# Granules, empirical Z+ information and exact certificates

**Research prototype. No changed discriminant cutoff, no universal nonvanishing
result, and no performance advantage over the registered crisp baseline.**

Frozen production target: `791ebf4815d8eb4be5da3b01527ca7f0877b6d0e`.
The source of `lean/multiplicity_exact_controls.py` has Git blob
`0c4ccb8f2dab99a5317f80345eae7920390fcbc0`; the benchmark refuses source drift.
This branch starts from main, not the still-draft comparator PR #9.

## The actual blend

A case carries (1) exact polynomial and original fixed matrix degree, (2)
overlapping rational fuzzy memberships, (3) empirical operational distributions,
and (4) an independently recomputed concrete witness. The three epistemic
coordinates are distinct: membership is not probability, probability is not proof.

The router uses three overlapping granules: near leading-degree loss, near zero
constant coefficient, and regular. Membership depends on normalized coefficient
ratios. Training estimates local success distributions from 168 labeled exact
probes, with explicitly declared membership weighting. The learned router mixes
these empirical local distributions to rank candidate observations. These are
predictions, not a calibrated distribution over future tasks or theorem truth.

Every successful candidate is checked again by SymPy's resultant implementation,
computed over Q[W] BEFORE specialization. The derivative block product a(a-1) is
even, so the two determinant conventions agree. A successful witness establishes
nonzero determinant for that concrete polynomial only. Failed probes remain
inconclusive; an exactly zero polynomial resultant is recorded by the reference,
not inferred from a small number of zero evaluations.

## Exact composition contract

For the SAME scalar target x, valid local enclosures [l_i,u_i] and nonnegative
weights w_i with sum 1 give

    sum_i w_i*l_i <= x <= sum_i w_i*u_i.

Every active input requires a valid bound. Domain, units, original matrix degree,
normalization, and witness identity cannot be blended away. A zero total weight
is an uncovered case, not a probability-zero case that can be discarded.

Averages cannot strengthen the strongest available scalar bound:

    sum_i w_i*l_i <= max_i l_i,
    min_i u_i <= sum_i w_i*u_i.

Therefore the exact bound layer retains the intersection (max lower, min upper)
when those verified enclosures concern the same scalar. Granules guide which
certificates to seek; they do not overrule already stronger certificates.
Conflicting intersections signal inconsistent inputs, and shared provenance
never becomes multiple independent votes. The Python enclosure API is explicitly
CONDITIONAL: it validates identities and shapes, not the truth of its input
bounds. There is no claimed universal Python-to-Lean equivalence.

`lean/TenthDiscriminant/GranuleCertificates.lean` contains eight generic theorem
statements with explicit hypotheses: lower and upper mixtures, positivity,
best-bound dominance, active support, normalization, and two counter-controls.
They are imported by the root library and hence included in its ordinary build
and transitive axiom audit. Read the exact CI revision before calling them checked.
No Ender or Sylvester theorem is discharged by those generic lemmas.

## Registered finite comparison

The protocol was saved and hashed before the first run. The 24 training tasks
and 96 test tasks use disjoint fixed seeds, six same-author generated families,
and seven candidate evaluation points per task. No post-result tuning.
They are not an external or distribution-shift benchmark. A post-run exact-content
audit found three test polynomials also in training and 92 distinct polynomials
among 96 test tasks. The overlapping tasks tie across all policies; removing
them does not alter the five-probe deficit. Seeds do not guarantee disjoint
content. The registered corpus is preserved, not silently redrawn.

| Policy | Actual probes on 96 tasks | Mean penalized probes | Failures |
|---|---:|---:|---:|
| Fixed shuffled candidate order | 201 | 217/96 | 16 |
| Crisp leading/constant coefficient heuristic | 194 | 35/16 | 16 |
| Fuzzy membership only | 199 | 215/96 | 16 |
| Fuzzy + empirical local distributions | 199 | 215/96 | 16 |

Each failed search performs seven probes and receives penalty eight. All sixteen
failures are globally repeated-factor controls. Each policy returns 80 nonzero
witnesses, all rechecked exactly. Across 840 precomputed training/test probes,
production rational determinants agree with symbolic resultants. All 672 test
candidate results were precomputed for paired evaluation-count replay; the table
is not a wall-clock speed comparison. Training costs another 168 labeled probes,
and exact membership fractions can grow large; neither cost is hidden.

Against crisp, the blend wins on 1 task, ties on 89 and loses on 6, for five extra
probes in total. Against fuzzy-only it ties on all 96. The registered performance
promotion rule FAILED. No scheduler-superiority claim is made, and the crisp
baseline remains preferred on this suite. This retires this round's advantage
claim, not all possible uses of granular structure.

## Operational Z+ summary

The explicit random variable is penalized probes to the first successful exact
witness on the declared uniform finite test population. Failure has value 8,
not an unreported censored runtime. The fuzzy event 'cheap successful certificate'
has membership A(x)=(4-x)/3 on 1<=x<=4, zero above 4 and below 1 (A(1)=1).
The PMF and fuzzy-event expectation are both exported. For the learned blend:

    P(X=1)=73/96, P(X=2)=7/96, P(X=8)=16/96,
    E[A(X)] = 233/288.

These are empirical operational summaries, NOT probabilities that the class-number
theorem is true. No Bayesian posterior, independence assumption or generalization
calibration is claimed. Normalized memberships are not themselves this PMF.

## Controls and limitations

17 Python test methods pass, one containing 512 seeded enclosure cases with
reordering and weight-rescaling checks. Malformed weights, targets, intervals,
empty empirical samples and forged determinant payloads are rejected. Exact zero
and tiny nonzero leading coefficients remain separate. Repeated factors and zero
specializations never become nonzero certificates merely because a granule has
high membership. All 384 policy/case scalar-rescaling comparisons pass.

Normal and optimized Python runs give identical substantive JSON after excluding
observed wall time. Python 3.13.5 and SymPy 1.14.0 were used. Code, generators and
interpretation share authorship. Symbolic resultants are a different algorithm,
not independent semantic/human review. Coordinate shifts can change routing
features; this is disclosed rather than called semantic invariance. Only scalar
rescaling and the named certificate identities were tested.

Coverage over an infinite domain, new interval bounds, automatic semantic granule
construction and a universally better router remain unimplemented. The next
scientific move is independent review or a separately registered harder corpus,
not adding richer vocabulary to rescue the failed advantage claim.

## Reproduce

From the repository root, in an environment with SymPy 1.14.0:

```sh
python -m unittest discover -s research/granules_r1 -p 'test_*.py' -v
python research/granules_r1/benchmark.py --source lean/multiplicity_exact_controls.py --output /tmp/granules-r1.json
python -O research/granules_r1/benchmark.py --source lean/multiplicity_exact_controls.py --output /tmp/granules-r1-optimized.json
cd lean
lake update
lake exe cache get
lake build
python3 audit.py
python3 negative_controls.py
```

The symbolic Python campaign is manual; it is not claimed to run in the existing
Lean-only CI. `PROTOCOL.md` specifies the comparison before results. No existing
numerical tools, guards, saved certificates or proof bodies were edited.

## Sources and attribution

- L. A. Zadeh, *A Note on Z-numbers*, Information Sciences 181 (2011), 2923-2932,
  DOI 10.1016/j.ins.2011.02.022. Z+=(A,p_X) combines fuzzy restriction and a supplied
  distribution; our operational application is a design, not Zadeh's theorem.
- L. A. Zadeh, *Toward a theory of fuzzy information granulation...*, Fuzzy Sets
  and Systems 90 (1997), 111-127, DOI 10.1016/S0165-0114(97)00077-8.
- FLINT Arb documentation, https://flintlib.org/doc/arb.html: numerical enclosure
  semantics remain distinct from confidence. Arb was not installed or rerun here.

This design blends exploration, explicit uncertainty and exact checking while
preserving the repository's existing evidence boundaries.
