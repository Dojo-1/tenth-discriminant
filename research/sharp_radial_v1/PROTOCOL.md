# Sharp radial same-integer bound: registered cycle 132 (draft)

Base and frozen state: PR #47 head \`0c7f4186d434f2b334218686060051a8d6881abf\`. All pre-existing source, old protocols, previous errors, PRs #45/#46/#47, target cutoff and historical CI remain unchanged. New branch \`research/sharp-radial-same-gram-v1\` is add-only except appending separately identified lemmas to the existing \`RadialJetMajorant\` module to reuse its already checked private coefficient bound. No edit of any previously proved theorem's type or body.

## Mathematical targets, in dependency order

(A) For integer radius rho>=10, original center a=floor(rho^2/2), all complex z in disc |z|<=rho: \`|z*conj z-a| <= (101/200)*rho^2\`. Floor/odd-radius rounding must be explicit; **false** with exact-half bound at rho=11 and zero.

(B) For S>=1, s<S,j<S,r>=9S, all same ordinary derivative jets, \`|jet a r s j z| <= (63/100)^s*(r)_j*rho^(r+s-j)\`. The old zero-derivative and r<s cases remain intact; coefficient bound is the original, not a novel error-term replacement.

(C) For S>=100 and 25S<=R<=26S, prove exact new savings
\`(11/1000)*(R^2*S) <= (R-9S)*S*(S-1)*log(100/63)\` in real arithmetic, with a sound positive-log certificate.

(D) Transport the improved all-jet estimate to the EXACT original \`integerRectangularTraceGram\`: determinant Hadamard bound (new row factors only), normalized saving >=0.011 and, if the old unchanged \`Tuned.normalized_upper\` admits it, \`log detG/(R^2*S) <= 0.8*log D-0.824\` for all D>=41006250000.

(E) Only after D: attempt an improved *actual-field* endpoint with a **new** logarithm certificate and full class-number implication. Candidate D0=47,100,000,000 is a conjectural target, not accepted. The field discriminant is never the same as the jet Gram determinant.

## Controls and stop rules

- Canonical coefficient counterexample s=1,r=1,j=1 prevents attaching a centering saving to every differentiated factor.
- Odd rho=11, z=11 (the outer boundary, not the origin) rejects exact h=1/2 while respecting the new h=101/200.
- r<s and j>r cannot be omitted from the full diagonal proof.
- Original Gram and its factor-two metric must remain exact, positive under the same point-count guard.
- The existing 13/20 bound and original 47.5b theorem must compile unchanged; old negative controls preserved.
- Independent semantic review remains open even with Green CI; no new optimality or priority claim.
- Lean compile and audit are not interchangeable. Build a targeted small module first, then separated gates to avoid the inherited 25-minute monolithic CI wall-time cancellation.
- Limit proof-only elaboration repairs to at most three source revisions after the first public CI result. Do not relax the mathematical target silently; on failure, archive evidence and stop the current cycle.
- No merge, no Mathlib submission, and no Tao posting in this cycle.

Evidence: pre-existing declarations [P at already pinned heads]; A/B/C/D/E [H until exact-head kernel build]; finite test numbers [M only for declared bounded cases]; toroidal/polyholonomic controller [S/H]. All algebraic parameters and guards are written explicitly so another mathematician can reconstruct this without the project history.

## First correction (before accepting any CI result)

The initial negative-control draft incorrectly used z=0 at odd radius rho=11. It gave deviation 60, which does NOT falsify the half-radius envelope 60.5. The correct falsifier is the boundary z=11: norm difference |121-60|=61>60.5. Retain source history showing the failed draft; this change is a mathematical correction to the control, not a proof of the target.
