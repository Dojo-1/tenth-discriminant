# Task checkpoint

- 2026-10-24, Phase 18: Protocol-only commit `766c739` preceded edits.
  Lean now checks the missing disk-to-cell covering, exact cell area,
  finite-union bound, chosen-radius strict count, and upper-endpoint
  actual-Gram positivity. Closed cells intentionally overlap on edges;
  the proof uses subadditivity, so no partition assumption is hidden.
  `D=1,rho=0` refutes dropping the radius guard. Targeted Lean and the
  complete 6708-step local build pass, along with endpoint-only source
  correspondence, JSON and whitespace checks. Proof head `c513f51`
  passed pinned CI `40073516586` and CodeQL `40073513187`; a later
  documentation-only correction requires its own final-head check.
  Analytic cutoff and classification
  remain open.

- 2026-10-23, Phase 8 on draft PR #27: preregistered `c82d8f2` before proof edits. A local commutative-ring chart was proved identical to the repository's `ZMod p` pair multiplication/power and injective. Lean checks Euler's criterion gives `t^p=-t` for odd prime `p` and nonsquare `-D`, then Freshman's dream yields `a^p=conjugate(a)` for every original residue pair. The integer-coordinate transport discharges Phase 7's universal premise and proves exact `p^(2F(p))` divisibility for the actual Gram under that local guard. D=19,p=3 nonsquare and D=2,p=3 square controls pass. This is not a class-number-one to inertness theorem or a checked cutoff. First proof-script failures are in the Phase 8 protocol. Full 6699-step local build and source correspondence pass; final pinned CI pending.

- 2026-10-23, Phase 7 after PR #25 merged externally at `a4da896`: preregistered the actual-row bridge first in `710da33`. The exact binomial matrix now acts on the existing integer ordinary-derivative rows; bilinearity of the unchanged factor-two trace constructs `UGUᵀ=D_p K D_p` with integral `K`, yielding the exact `p^(2F(p))` determinant power under a universal coordinatewise Frobenius congruence. Targeted Lean files and full 6697-step local build pass. Optional D=19 corollary stalled locally and was removed. Inertness-to-Frobenius, Lean cell area, analytic cutoff and class-number classification remain open. Pinned Linux CI pending.

- 2026-10-23, Phase 6 operator-first continuation: PR #24 merged externally at `bf9ddff`, so new branch `codex/local-operator-closure` starts there, preserving generated untracked `lean/lake-manifest.json`. Protocol-only commit `6f45b4f` fixed the scope before proof edits. Lean now checks that exact conjugation is an involutive validity-preserving operator for the pair-coordinate Frobenius premise, and composes it with the existing all-order ordinary-jet theorem. A non-real `D=19,p=3` pilot is checked. Targeted Lean, source correspondence and full 6695-step local build pass. This does not establish the general premise from inertness, identify the binomial basis action on actual Gram rows, or check a cutoff/classification. Pinned Linux CI pending.

- 2026-10-23, Phase 5: PR #23 had merged externally at `d0d421f`; created `codex/rectangular-unimodular-basis` from that main, preserving generated untracked `lean/lake-manifest.json`. Registered the basis-matrix protocol in commit `75ee2c0` before Lean edits. New `RectangularBasisMatrix.lean` defines the sample-independent integer binomial matrix; Lean checks all active terms stay inside the canonical rectangle, every target column exists, strict lower-triangularity, diagonal one, determinant one (also empty grids), and entire `4×2,p=3` pilot rows. Compilation errors about `Fin` elimination, quotient–remainder, dual order, bounds and finite decision were repaired and recorded in the protocol. The stretch identity between this matrix's action and the actual integer derivative rows, hence the integral Gram factorization, remains open; no checked cutoff or classification follows. Targeted Lean, source correspondence and the final 6694-step full build passed; pinned CI pending.

- 2026-10-23, Phase 4: left draft PR #23 open and unmerged at locally checked Phase 3 head `059741a`; pinned Lean CI run `39973862730` and CodeQL passed there. Registered ordinary-jet power protocol separately at `86f40e7`, then proved in `JetPower.lean` the universal product-power rule, its `Z^p-W` specialization in `Zsqrtd`, coordinatewise `p^k` divisibility for every proposed transformed row at each original integer-pair sample, and a Hasse-derivative falsifier. First Lean proof-script failures (scalar evaluation, induction generality, associativity, and wrong evaluation lemma) were repaired and logged. Targeted Lean, source correspondence and full 6693-step local build passed. This does not construct the unitriangular row operation on the actual matrix or prove inertness, cutoff or classification. Final-head pinned CI pending; no Tao submission.

- 2026-10-23, Phase 3 after PR #22 merged: based `codex/frobenius-residue-bridge` on `7bc3ec8` and committed the exact-exponent protocol first (`68a91b9`). Lean now proves that the row-major rectangular exponents sum to Ender's original `F(p)`, with a top-row falsifier control, and derives the exact determinant power only under an explicit integral unimodular basis-factor hypothesis. First targeted proof attempts failed on finite-sum reflection and range guards; repaired, recorded in protocol, then targeted Lean, source correspondence and full 6692-step build passed. The basis factor itself, checked cutoff and classification remain open. No Tao comment has been posted; `TAO_REPLY_BRIEF.md` is AI-prepared evidence for a human-generated summary, not that summary.

- 2026-10-23, post-merge Phase 2: confirmed PR #21 merged at `08c7260`, branched `codex/uniform-frobenius-jet` from that `origin/main`, and preserved the unrelated generated untracked `lean/lake-manifest.json`. Registered Phase 2 in its own commit `04ee81d` before Lean edits. `FrobeniusJet.lean` now checks every ordinary jet of `Z^p-W` is coordinatewise p-divisible under the explicit zero-order congruence; it includes a noninert D=2,p=3 falsifier. The generic Frobenius/inertness interface, H^k product rule, rectangular basis, and class-number/analytic chain are not checked. Targeted Lean, source correspondence and full 6691-step local build passed; pinned CI on final head remains pending.

- 2026-10-23, uniform valuation cycle: explicit user approval obtained to publish a draft PR, not merge. `origin/main` remained `8ab2be0`. Branch `codex/tao-objective-accounting` contains accounting commit `9b976cb` and protocol-only commit `09b6455`; draft PR #21 opened. A preregistered rectangular unitriangular basis using `Z^p-W` gives a human-checkable paper derivation of the full `p^(2F(p))` inert-prime factor under residue irreducibility. New Lean theorem proves only the conditional abstract unimodular two-sided determinant step. Bounded basis/exponent and inert/noninert controls passed. Source correspondence and full 6690-step local build passed. The general polynomial/Frobenius instantiation, class-group/analytic chain, and final-head pinned CI remain open. Generated `lean/lake-manifest.json` is untracked and preserved.

- 2026-10-23, current Tao-objective accounting: synced main after PR #20 was merged externally at 8ab2be0, and created codex/tao-objective-accounting from that commit. The older TAO_OBJECTIVE_AUDIT.md remains a frozen 4c034f9 snapshot. A new current ledger treats its twelve rows as our operationalization of Tao's prose, distinguishes candidate cutoff and conditional sieve from Lean theorems, and separately classifies formal, paper, finite negative, and expository side discoveries. This is documentation-only. Local source-correspondence, Lean build, links, whitespace and JSON checks passed. An optional GitHub Markdown rendering preview was rejected by auto-review due external draft-content upload; no workaround was used. External publication and pinned remote CI await explicit approval.

- 2026-10-23, human-distillation continuation: added lean/MATHEMATICAL_SPINE.md as a concise entry point organized around one integer Gram determinant, its real energy/contact proof, exact residue reduction, and the fixed D=19,p=3 nine-divisibility theorem. The guide separates Lean-checked claims, the paper-only chosen-radius area count, recorded candidate computations, and the missing uniform valuation/class-number chain. Linked it from current reader pages and corrected unqualified historical divisibility wording. Local verify_sources.py, 6690-step lake build, git diff --check, task-state JSON parse, and local Markdown link resolution passed; CI on the final documentation commit remains pending.

- 2026-10-23: Synced a fresh checkout at `4c034f9`. Contrary to the earlier cached conversation, PR #15 (`47ec647`) and PR #16 (`4c034f9`) are merged on current `main`.
- The selected bounded replay is `flow/PREREG_RADIAL.txt`; its stated limitation forbids a cutoff improvement claim.
- Scope: documentation/evidence audit, pinned formal checks, and one bounded replay. No merge and no claim of a full classification proof.
- 2026-10-23: Replayed `tools/test_radial_bounds.py` in the preregistered environment: 9 tests passed. Documentation now records the objective audit, current merge state, and the distinction between this replay and a new cutoff result. Markdown local links and `git diff --check` pass; pinned CI remains to run on the branch.
- 2026-10-23: Pinned GitHub Actions workflow `39909040311` passed at `8fb10ce`: source correspondence, full Lean build, compiled dependency audit, and inherited negative controls. Draft PR #17 is open and unmerged.
- 2026-10-23, new bridge task: current main is `9f713b8`; PR #17 has since merged. Earlier draft status above is historical.
- Registered `research/lattice_bridge_r1/PROTOCOL.md` before editing proof. Current branch is `codex/lattice-sampling-bridge`.
- Lean checked exact finite ellipse membership, coordinate injectivity, cardinality transport and conditional determinant bounds; D=rho=1 cardinality control passes. The analytic lower count, Ender radius identification, integer determinant equality and valuation remain open.
- Local pinned `lake build` and `python verify_sources.py` passed. Compiled axiom audit and negative controls still running at this checkpoint.
- 2026-10-23, radius-count continuation: draft PR #18 at `2b69c2a` passed pinned Linux CI run `39913779228`; it remains unmerged. Local Windows wrappers timed out and the failed runs are preserved in `research/lattice_bridge_r1/PROTOCOL.md`.
- Registered `research/ender_radius_bridge/PROTOCOL.md` before proof edits. A cell-covering argument proves the inherited lower ellipse count and Ender's chosen-radius `n>3R+S` mathematically, with all boundary cases. It is not yet Lean-formalized; this is distinguished in `PROOF.md` and current reader docs.
- Lean checked `ellipsePairs_antitone_D`, endpoint cardinality transfer, the conditional Ender-guard determinant theorem, and the exact `D=19,rho=5` 21-point control. Pinned full CI still pending for the new head.
- Reconciliation: PR #18 merged externally at `6431e78` while this task was underway. The continuation was cherry-picked onto new branch `codex/ender-radius-count` based on that merge; no merge was performed by this task.
- 2026-10-23: PR #19 passed pinned CI run `39922982525` and was merged externally at `c77049288e0eac33f72739b255d8254ff3e6aca1`; no merge was performed by this task. The repository's historical `review/` records document AI adversarial audits, but the named files contain no Gemini/Argor attribution. `RESPONSE_Claude.md` records F5 as a timing issue with rerun requested, and flags post-clone code as not independently reviewed by that reviewer. `TAO_OBJECTIVE_AUDIT.md` is a frozen `4c034f9` snapshot; current `STATUS.md` and `lean/FORMALIZATION.md` carry the later ellipse/radius work. No mathematical classification claim follows from these audits.
- 2026-10-23, integer-Gram bridge: fetched current `origin/main` at `c770492` and created `codex/integer-trace-gram` without discarding checkpoint changes. Registered `research/integer_gram_bridge/PROTOCOL.md` before Lean proof edits. Target is an entrywise integer-pair/real trace-Gram identity for the same ellipse and row-major indexing; determinant valuation is out of scope.
- Lean now checks the generic entrywise equality, row-major matrix and determinant cast, ellipse specialization, count-conditional positive integer determinant, and D=3 asymmetric `[[2,6],[6,24]]` control. Full `lake build` and `verify_sources.py` passed. Sequential Windows `audit.py` and `negative_controls.py` both exited 1 on their existing subprocess timeouts (240s/120s); these failures are preserved in the protocol. Pinned Linux CI remains pending.
- 2026-10-23: Pinned Linux workflow `39930134039` passed at proof head `eea5c5f94dd919072a5fb970723754695f8ca382`, including source correspondence, full Lean build, compiled axiom audit and inherited negative controls. This does not erase the local Windows wrapper timeouts. A small documentation follow-up corrects stale chronology in README, STATUS, HUMAN_GUIDE and TraceGram's file comment; its final head requires its own CI.
- 2026-10-23: The documentation follow-up head `f12085372078a7958f4a1fc7995853fed49efb00` passed pinned Linux workflow `39931440763`; PR #20 remains draft and unmerged. New user-authorized task: preserve the global integer-to-complex identity while adding a residue-coordinate path and a precise determinant divisibility criterion. Registered `research/local_global_gram/PROTOCOL.md` before new Lean edits. Reduction of a set can identify distinct samples, so the local sum must retain their original multiplicities; a modulo-3 collision control is preregistered.
- 2026-10-23: Protocol-only commit `e8bb4d389c95bc24624d7b94174245314594dfba` passed pinned Linux workflow `39944972558`. New Lean modules give Zsqrtd coordinates, an independently computed residue Gram with determinant naturality and exact collision/asymmetric controls, a two-sided determinant lemma, and the fixed D=19,p=3 canonical eight-row theorem `9 ∣ det G` for arbitrary finite Q and J. The D=19 ellipse instance is positive; D=2,p=3 is a checked noninert falsifier. Targeted Lean and local source-correspondence checks passed. Full build and later checks still pending at this checkpoint; no general Ender/classification conclusion follows.
- 2026-10-23: Full `lake build` passed for all 6690 steps. Local `audit.py` exited 1 because the Windows apparatus-controls wrapper timed out after 240 seconds, despite import coverage and the compiled `AUDIT_OK` report (526 logical declarations, 435 theorems). Local `negative_controls.py` was deliberately stopped after four matched good/bad controls passed; its full suite is incomplete locally. The exact final proof commit requires its own pinned Linux CI; do not infer a pass from partial local output.
- 2026-10-23: Proof-head commit `d5945cf7fc5b891b54ef85986c40a55bec35843c` passed pinned Linux workflow `39954106722`, job `120415525126`: source correspondence, full build, compiled axiom audit and inherited negative controls. Draft PR #20 remains open and unmerged; its description was updated to the new fixed-pilot scope. This task-state-only follow-up will need its own CI before it can be called the final checked head.
- 2026-10-23, Phase 9: preregistered strict small-prime norm-to-local
  bridge in standalone commit `f4c2e56` before proof edits. Lean now
  proves the norm obstruction including the rational prime-square case,
  identifies `X²+D` irreducibility with nonsquareness of `-D` over
  `ZMod p`, and applies the existing actual-Gram valuation under the
  explicit root-to-principal-norm lifting premise. `D=15,p=3` proves
  that premise is not unconditional; `D=163,p=41` remains the strict
  endpoint witness. Targeted Lean, 6700-step local full build and source
  correspondence pass. Class-number one to lifting, analytic cutoff,
  and classification remain open; final-head pinned CI pending.
- 2026-10-23, Phase 10: preregistered the abstract class-number
  quotient-to-principal-norm proof in standalone commit `ac62da0`.
  Lean now proves for any number field that a map from its integer ring
  to `ZMod n`, plus class number one, gives an algebraic integer with
  absolute norm `n`; `K=ℚ,n=3` is a positive control. Targeted Lean,
  6701-step full local build and source correspondence passed. This
  discharges the abstract principality arrow, not the specific
  root-to-maximal-quadratic-order map or norm-coordinate identity.
  Pinned CI on the final head pending; no cutoff/classification claim.
- 2026-10-24, Phase 11: preregistered root-to-explicit-order quotient
  theorem in standalone commit `1b190b0`. Lean proves that odd-prime
  `z²=-D` yields a surjective map from
  `ℤ[T]/(T²-T+(D+1)/4)` to `ZMod p`, with `T↦(1+z)/2` and
  `z=2T-1` after mapping. `D=15,p=3` confirms a quotient can exist
  without principal norm lifting. Targeted Lean, 6702-step local build
  and source correspondence pass. The maximal-order identification,
  algebraic norm formula, area formalization, analytic cutoff and
  classification remain open; final-head pinned CI pending.

- 2026-10-24, Phase 12: Phase 11 head `5beb7d7` passed pinned CI run
  `40031979933` and CodeQL. Preregistered the explicit-order norm
  attempt separately at `8f3bf1e`. Lean now checks `T²=T-c` in the
  actual quotient, the nontrivial multiplication column, and the
  exact determinant `x²+xy+cy²` of the proposed 2×2 integer matrix;
  `D=15,c=4` is a control. Targeted Lean, full 6703-step build and
  source correspondence pass. The basis identification with
  `Algebra.norm` and the maximal-order identification are not proved;
  no checked cutoff or classification follows. Final-head CI pending.

- 2026-10-24, Phase 16: Phase 15 head `cf1c9db` passed pinned CI
  `40043319145` and CodeQL. Protocol-only `c519477` preceded edits.
  Targeted Lean proves class-number-one exact norm lifting, the
  strict-small-prime nonsquare guard and Ender's actual integer-Gram
  valuation, with `D=15,p=3` deriving class number not one. The sign
  step uses the checked four-times-norm sum-of-squares identity.
  Full 6707-step build and endpoint-only source correspondence pass;
  whitespace and state JSON checks pass. Pinned CI pending; area,
  analytic cutoff and final classification remain open. Proof head
  `7fbc7fc` passed pinned CI `40044997537`, including compiled
  dependency audit and negative controls, and CodeQL. A follow-up
  claim-map correction is documentation-only.

- 2026-10-24, Phase 15: Phase 14 head `8d15fbb` passed pinned CI
  `40039967991` and CodeQL. Protocol-only `c600ac5` preceded edits.
  Targeted Lean now proves the actual quadratic field and rational
  basis, an injective explicit order-to-integer-ring map, integer
  coordinates for every algebraic integer, the resulting ring
  equivalence, and the maximal-ring norm identity. `D=15,c=4` and
  reducible `c=0` controls compile. The full 6706-step build and
  endpoint-only source correspondence pass; whitespace and state JSON
  checks pass. Pinned dependency audit and negative controls are pending. The
  class-number-to-small-prime lifting composition is not yet checked.

- 2026-10-24, Phase 14: Phase 13 head `ca4bb0b` passed pinned CI
  `40037475255` and CodeQL. Protocol-only `18510c3` preceded edits.
  Lean now checks the squarefree rational denominator lemma, parity,
  coordinate reconstruction and converse, uniqueness, `D=15` and `D=9`
  controls. Targeted Lean and the full 6705-step build pass. Source
  correspondence passes endpoint-only; whitespace and state JSON checks
  pass. This is not yet a theorem identifying the explicit order with
  the maximal integer ring. Pinned CI on this proof head is pending.

- 2026-10-24, Phase 13: Phase 12 final head `4133023` passed pinned CI
  `40034568524` and CodeQL. Preregistered the algebraic norm target
  separately in `819f3f9`. Lean now checks a true rank-two power basis
  for `ℤ[T]/(T²-T+c)`, its actual multiplication matrix, and
  `Algebra.norm ℤ (x+yT)=x²+xy+cy²=principalNorm D x y` when
  `c=(D+1)/4`. The `D=15` generator and scalar controls pass. Targeted
  Lean, 6704-step full build and endpoint-only source correspondence
  pass. The maximal-order identification remains a separate open
  arrow, as do the area Lean proof, analytic cutoff and classification;
  final-head pinned CI is pending.
- 2026-10-24, Phase 17: Protocol-only commit `328c90b` preceded edits.
  Targeted Lean compiles the exact Ender radius-to-strict-count implication
  from an explicit cell-area premise, then transports the upper-endpoint
  count to positivity and Hadamard for the actual trace-Gram matrix. The
  disk-covering/measure proof of the premise remains paper-only; analytic
  cutoff and classification remain open. Full 6707-step local build,
  endpoint-only source correspondence, JSON and whitespace checks pass;
  pinned CI pending.
- 2026-10-24, Phase 19: Protocol-only commit `65bbaed` preceded proof edits.
  `PrimeMassAssembly.lean` now compiles a finite coprime-product divisor,
  a chosen-radius determinant/Hadamard sandwich, and the exact log-prime-mass
  inequality for all odd primes below `R` under squarefree `D≡3 (mod 4)`,
  class number one and strict `R<(D+1)/4`. Empty, singleton and duplicate
  controls compile. Initial elaboration/cast errors were repaired without
  deleting assumptions. The factorial/Arb analytic bounds and classification
  remain unproved. Full 6709-step local Lean build and endpoint-only
  source correspondence pass; pinned CI is pending.
- 2026-10-24, Phase 20: Phase 19 head `f7fe3cf` passed pinned CI
  `40075949893` and CodeQL. Protocol `6afa007` preceded proof edits and
  became `fc6427b` after preserving the external merge at `90b0f53`.
  `EnderUpperB.lean` targeted checks pass for the actual diagonal bound,
  original row-major sum, exact integral correction and production integer
  coefficients. The chosen-radius class-number theorem now reaches unchanged
  `upper_B` at positive integer radii, with its upper count input explicit.
  Seven controls compile; automatic implicit variables are disabled after
  detecting and repairing a sum-scope ambiguity. The upper ellipse count,
  factorial lower estimate and numerical/classification links remain open.
  Full 6710-step local build and endpoint-only source correspondence pass;
  pinned CI is pending.
- 2026-10-24, Phase 21: Phase 20 head `5f5614c` passed pinned CI
  `40091741093` and CodeQL `40091739149`. Protocol `157ba64` preceded
  proof edits. `EllipseUpperCount.lean` proves the unchanged upper count
  using disjoint open inward cells for off-axis points and exact axis
  boxes, including the origin once. It checks lower-endpoint interval
  transfer and safe line-count padding; the counted class-number theorem
  now reaches production `upper_B` without an abstract sample-count premise.
  Eight controls and the full 6711-step local build pass. Factorial,
  numerical certificate, universal-envelope and classification links remain
  open. Pinned CI pending.

- 2026-10-24, Phase 22: Phase 21 head `36e6f9a` passed pinned CI
  `40093798308` and CodeQL `40093795078`. Protocol-only `b7a43ea`
  preceded proof edits. `FactorialPrimeMass.lean` proves exact finite
  factorial/Legendre decomposition including prime two, log-product equality,
  the increasing integral envelope and unchanged production scalar lower
  bound for `R≥2`. Ten controls and full 6712-step local build pass.
  The short guide distinguishes factorial prime-power weights from the
  determinant's odd-prime weights. Full `prime_mass` subtraction, conversion,
  tail and clipping, numerical certificates and classification remain open.
  Pinned CI pending on the published proof head.

- 2026-10-24, Phase 23: Phase 22 head `c8a42a5` passed pinned CI
  `40096404959` and CodeQL `40096403109`. Protocol `e4736fd` preceded
  proof edits. `PrimeMassLower.lean` checks the staircase identity, exact
  small/large prime split, integer loss coefficients, padded enumeration,
  finite geometric and floor-square bounds, both clipping branches and
  actual counted `upper_B` composition conditional on one reciprocal-prime
  tail bound. Eight controls and full 6713-step local build pass. The
  analytic integral bound, numerical certificates, universal closure and
  classification remain open. Pinned CI pending on this published head.

- 2026-10-24, Phase 24: Phase 23 head `035454e` passed pinned CI
  `40098513168` and CodeQL `40098510944`. Protocol-only `e1fa9be`
  preceded proof edits. `PrimeTail.lean` proves the production tail bound
  by positive potential drops and finite telescoping, then composes the
  actual-Gram mathematical lower/upper comparison with no tail hypothesis.
  A strict real comparison now gives an explicit exclusion criterion; no
  saved Arb inequality or numerical guard is assumed verified. Eight controls
  and full 6714-step local build pass. Numerical interpretation, universal
  closure, even cases and classification remain open; published-head CI pending.

- 2026-10-24, Phase 25 in progress: Phase 24 head `6717eee` passed
  CI `40100457533` and CodeQL `40100456379`. Protocol `f109533`
  precedes all edits/replay. First production replay (flint 0.9.0,
  numpy 2.5.4, 160 bits) passed at rho `408406701`, Y `488`.
  Targeted `FirstIntervalGuards`, `LogEnclosure` with binary reduction,
  and `NumericalWeights` pass. Exact rational candidate outside Lean has
  a positive gap even with coarse valuation weights. The remaining work
  is kernel checking the 1229-row table and aggregate strict inequality;
  do not claim an interval exclusion from the replay/candidate. No full
  build/import/audit of the new Phase 25 files has yet been run.

- Phase 25 continuation checkpoint: `NumericalCertificate.lean` now proves
  sound complete-table aggregation and rejects empty coverage.
  `FirstIntervalScalars.lean` proves all six scalar log enclosures, the
  actual upper bound `572*10^31`, and lower bound `581*10^31` conditional
  on small-mass budgets. Efficient weights truncate to 38 powers and a
  universal staircase inequality; no F_exact identity is assumed.
  A 32-row kernel pilot passed. Monolithic full check failed with Windows
  `lean::stack_space_exception` after 77.335612 seconds; preserved in
  `PHASE25_PROOF_FAILURES.json`. Generator now packages 39 chunks of ≤32
  rows. Full attempt is LIVE in exec session `5421`, command `lake env lean
  -s 16384 --profile ../research/ender_radius_bridge/FirstIntervalTableCheck.lean`.
  Re-poll it; do not infer terminal status from notes or observation expiry.
  If accepted, move attempt into audited library, compose its coverage/budget
  proofs through `table_mass_bounds` and `strict_comparison_of_table_budgets`,
  then apply `FirstEnderInterval.exclusion_of_strict_comparison`. Root imports,
  current docs, full build and exact-head pinned CI remain to be done.
  No checked interval or cutoff claim yet. Generated table is untrusted data
  until all checks and CI pass. Preserve untracked generated lake manifest.

- Phase 25 terminal/checkpoint update: session `5421` crashed after
  539.5711452 s with stack exception. Session `77433` (integer monolith)
  was stopped after 306.3307974 s at observed 10646298624 bytes. Monitored
  sequential integer chunks, session `56662`, exited resource-stop 99 after
  222.7429775 s at 8590958592 bytes; logs in
  `PHASE25_INTEGER_CHUNKS_20261024154815.*`. No live proof process remains.
  All soundness/scalar/guard/conditional-conclusion modules have built.
  Registered next repair is quotient/remainder witnesses so the Boolean
  verifier never computes the enormous Nat divisions. Witness soundness
  must be proved using `Nat.div_mod_unique` and `floorSum_scaled`; power
  coverage and all existing row/list/budget checks remain required. No full
  table or interval theorem accepted. Old proof layouts archived as .txt.

- Phase 25 resumed from `bba9870`. `DivisionWitness.lean` now proves
  quotient/remainder, complete prime-power witness and fixed-square-mass
  checker soundness. Same numerical values and bounds throughout.
  All 1229 rows passed in an isolated row-wise proof (127.3084388 s,
  6014193664 bytes), then in compact 32-row blocks (25.814322 s,
  3632619520 bytes); the compact proof is `FirstIntervalRows.lean` and builds.
  Exact accepted row-wise source is archived as
  `FirstIntervalRowsOnly.rowwise_accepted.txt`.
  Full table/totals reductions still hit the 8-GB cap; logs are preserved.
  A `norm_num` proof-producing totals pilot plus first coverage block passed
  (18.9080559 s, 2931294208 bytes). Complete bounded-block composition is
  running. No concrete interval exclusion yet.
  Full root build passed (6724 steps); audit exceeded 300 s, preserved as
  failure and deadline increased to 900 s without removing any gate.
  An accidental build from repository root failed before proving anything;
  rerun from `lean/` built the new module successfully. Preserve manifest.

- Publication checkpoint: all totals/coverage attempts terminated without a
  complete proof. The four-part attempt hit the 8-GB cap, remaining identified
  child processes were stopped; its files are recoverably moved under
  `research/ender_radius_bridge/divided_totals_attempt/`, not deleted.
  The 16-MB coverage normalization pilot hit kernel recursion; its registered
  64-MB retry hit the 8-GB cap. No live numerical proof process remains.
  Root imports only accepted ingredients and `FirstIntervalRows`.
  Full build passes (6724). Shared use of the *same* pinned Lean axiom
  collector passes all 1532 logical roots (1221 theorems); matched apparatus
  controls are still running at this checkpoint. The inherited suite's
  concurrent local run timed out at its unchanged 120-s jet deadline; preserve
  the failure and require an idle rerun / exact-head pinned CI.
  New numerical guide and README/STATUS/claim map explicitly retain missing
  coverage and total budgets, no interval/cutoff/classification assertion.
  Next proof work should use small, independently checked integer coverage
  blocks and bounded sum proofs, not another unbounded whole-table reduction.
  This is a new implementation repair to preregister, not a parameter search.

- Publication correction: compiled audit succeeded, but its matched-control
  parent exceeded the unchanged 240-s limit while local verification still
  overlapped. This is not a complete `python audit.py` pass. Preserved the
  failure; start an idle rerun and require exact-head remote CI. Initial
  pushed checkpoint was `c3590eb62833f99ab715130f6c052a5b4ff8ad51`; the following
  evidence-only commit corrects pending local-control status. No proof changes.

- Phase 26 starts from clean tracked head `260c6ba`; previous goal turn was
  progress, not no-progress. Refreshed remote branch and PR: same head, draft,
  open. Preregistered fixed-input bounded-coverage/totals repair in `cf5ec1d`
  before proof edits. No subagents spawned. First pilot classifies 16 integers
  near 9973 and the zero endpoint, with an omitted-prime negative control.
  All prior failures remain preserved. A mismatched checkpoint patch failed
  atomically before any file change; inspected and retried it.

- Phase 26: direct Boolean normalization and proposition rewriting still
  caused kernel recursion. Standalone prime/nonprime propositions passed.
  Explicit `decide_eq_true/false` certificates followed by `simp only` on
  Boolean equalities now pass the 16-integer pilot and omitted-prime control.
  One unsupported simplifier name was rejected and removed, not bypassed.
  Both exact 1229-row totals and the two target budgets passed independently
  in `Phase26Totals.lean` (47.9981834 s, 2949898240 bytes). Complete bounded
  integer coverage is running under the same monitor; no exclusion yet.

- Phase 26 milestone: full integer coverage passed (95.0764805 s,
  4643332096 bytes), now `FirstIntervalCoverage.lean`. `FirstIntervalTotals`
  and its two invalid tighter-budget controls compile. Refactored the
  existing conditional conclusion to expose mass budgets, without changing
  its statement. `FirstIntervalChecked.first_interval_classNumber_ne_one`
  compiles: squarefree D congruent 3 mod 4 in [700000000000,875000000000]
  has actual constructed-field class number not one, no numerical premise.
  Its conservative numeric bounds are 581*10^31 and 572*10^31.
  Full build passes (6727); namespace audit passes all 2381 logical roots,
  2070 theorems, 11661 runtime-only auxiliaries reported; only permitted
  classical foundation. Matched controls are running. Global goal active:
  other 249 intervals, unbounded range, even cases and finite classification
  remain open. Re-read Tao's original official article on 24 October;
  corrected ledger keeps global objective incomplete and posting/human
  summary obligations separate. No novelty or optimized cutoff claim.

- Full Phase-26 root build passed; namespace audit passed as above. The
  parent apparatus-control subprocess exceeded its unchanged 240-s limit,
  so do not call the whole local audit.py driver green. Preserve this local
  failure and require direct matched-control completion / exact-head CI.

- Phase 27 starts from refreshed clean tracked head `44ee9ca`, same open
  draft remote PR. Previous turn was progress: first bounded exclusion
  proved with passing CI. Preregistered uniform envelope and ONE fixed
  rational pilot in `1417908` before edits. No subagents spawned.
  Proved general floor lower, factorial/geometric upper, retained-weight
  lower and clipped production/actual-Gram comparison in UniformPrimeMass.
  Controls reject dropping S>=1, floor error, quadratic loss or prime-two
  exclusion. Two development gaps (cast factor order and explicit singleton
  normalization in a control) corrected; not mathematical counterexamples.
  External exact-rational pilot with unchanged Q=7/P=10000 meets both old
  first-interval budgets. A/B/C/E units are recorded in PHASE27_RESULTS.
  The fixed four-constant checker, exact pairing/chunk totals and wrong-
  rounding controls compiled under the 8-GB monitor (45.6180409 s,
  3141103616 bytes). UniformPrimeMassCertified general composition is
  running; no new interval/cutoff/classification claim.

- Phase 27: all certified uniform modules compiled, including an antitone
  tail lemma and reusable rational-tail-budget exclusion criterion. The same
  first-interval budgets and actual-field exclusion are recovered from the
  four constants, not from per-R prime-power certificates. Constants and
  generic R,S scope are explained in UNIFORM_PRIME_MASS_GUIDE.md. No further
  interval was tested and Q/P/radius/budgets stayed fixed. Full root build
  passed (6732), namespace audit passed 2693 logical declarations / 2301
  theorems, with 14282 runtime-only auxiliaries reported and only permitted
  foundational axioms. Matched controls are still running. Main global
  objective remains active; do not mark completion from this arithmetic
  engine alone.

- Phase 27 publication checkpoint: complete local audit.py driver hit its
  unchanged 240-s apparatus parent limit after the namespace audit passed.
  Preserve that failure; require direct matched controls and full remote CI.
  Fixed exact input was rerun only for deterministic generation, with no
  new configuration, parameter search or interval. Generated proof/data
  hashes were identical across reproduction. All production tools, ledgers,
  flow protocols, frozen audit and dependency pins remain unchanged.
  Current guides were updated to distinguish one bounded actual-field
  exclusion from the remaining campaign, all-D envelope, even cases and
  finite classification. Frozen tools/ledger/flow/audit/pins unchanged.
