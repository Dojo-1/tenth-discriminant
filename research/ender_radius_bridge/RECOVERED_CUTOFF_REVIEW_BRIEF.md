# Review the62.5-billion proof by checking its joints

Frozen mathematical target: commit
`86abe21f1ca023f9f62f99d1f785cdb361d86010`, tree
`7383bdcc0fa035bc83628420785813240b0e535e`.
This is a review brief, not a completed review. No reviewer is dispatched
by preparing it. The earlier Phase45/51 reports predate this endpoint.

The claim is about an actual totally complex rational degree-two number
field K, with actual class number one: its actual absolute discriminant
is below62500000000. There is no supplied generator or numerical premise.
This brief does not ask a reviewer to endorse novelty, optimality, the
finite classification, higher class numbers or the whole repository.

Read the proof sources first, then the
[human explanation](RECOVERED_CUTOFF_GUIDE.md) and
[verification record](PHASE54_VERIFICATION.md). The new module is only
111 lines; the inherited apparatus still matters to its interpretation.

1. **Recover terms without inventing divisibility.** Inspect
   `SmallPrimeRecovery.lean`. Reconstruct the disjoint3/5/retained>=7
   sum and clipping argument. Confirm the larger proxy remains below the
   same production expression, not merely below an unrelated lower bound.
   Check the original ordinary-Z derivatives and factor-two Gram convention.
2. **Count saturated rows with integer guards.** Inspect
   `SmallPrimeRecoveryGain.lean`. Re-derive
   `2F(p)>=(R-pS)S(S-1)` for positive p. Check truncated subtraction,
   finite ranges, and that the degree-weight index is not a derivative
   order. Verify the3/50 gain uses S>=100 and25S<=R<=26S. Inspect p0/S1
   controls; neither establishes sharpness of the retained guards.
3. **Verify the entire endpoint, not just the affine arithmetic.** Compare
   `TunedRadiusFamily.lean` and the upper helpers in
   `TunedAnalyticCutoff.lean` against their versions at bd2a207. Check
   floor/ceiling estimates, strict inertness, radius admissibility, count,
   error terms and scale positivity at500^4. Re-derive logD>=24.8 from
   2^8*5^12 and the stated rational log certificates. Old100b statements
   remain available; their presence is not a premise for the new proof.
4. **Check the inequality directions at the actual determinant.** Read
   `RecoveredAnalyticCutoff.lean`, especially
   `odd_large_classNumber_ne_one_recovered`. The chain must be
   upper<recovered(budget)<=recovered(actual tail)<=production<=upper.
   Verify tail antitonicity, R/S/inertness hypotheses and identical Gram
   inputs. Re-derive the strict rational gap. The log24.7 rejection is
   failure of these coarse estimates, not impossibility of the method.
5. **Check the actual-field conclusion.** Trace the odd chart, the separate
   even case, conjugation-based squarefree-root existence and algebra
   equivalence. Confirm actual class number and actual discriminant are
   transported, with no confusion between radicand and discriminant.
   Inspect the new theorem's compiled dependency closure for older cutoff
   or finite-answer inputs; importing their modules alone is not use.
6. **Read the public claim literally.** Compare README, STATUS,
   FORMALIZATION and challenge accounting against the theorem types.
   Distinguish local acceptance, exact-head CI, earlier AI source reviews
   and independent human review. Confirm failed sources and incomplete
   interrupted logs remain, with no full-classification or optimality claim.

For each obligation report RE-DERIVED, SOURCE-TRACED, CANNOT-VERIFY, or a
specific FATAL/GAP/SLOPPY finding, with source locations and the smallest
counterexample or missing implication. State inherited results assumed,
commands actually run and resource/time limits. A bounded absence of
findings is not certification of the entire development. Preserve the
first report and disagreements; do not reroll for a favorable verdict.
