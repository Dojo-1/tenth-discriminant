# Phase57: exact saturated-regime staircase count

Base published21a1b88. Its CI40363061933 is live; no push/cancel/restart
while live. No new reviewer authorized. Preserve the50b cutoff and its
mathematical sources unchanged in this cycle.

Fixed proof-bridge target: for natural R,S,p with p>0 and
p*(S-1)<=R, prove the REAL-cast identity

    6*valuationWeight(R,S,p)
      = S*(S-1)*(3*R-p*(S+1)).

The subtraction on the displayed right side is real subtraction; the
guard uses Nat subtraction. This differs from the inherited unsaturated
quadratic-floor identity and must not discard its quotient guard. It
counts the SAME original weight, not a stronger determinant valuation.

Method: introduce the clipped column sum C(R,p,t)=sum_(r<R)min(floor(r/p),t).
Prove its increment C(t+1)-C(t) counts r>=p(t+1), hence equals the
truncated Nat quantity R-p(t+1). Under p*t<=R derive the exact real
formula2C=t*(2R-p(t+1)), then sum columns/induct S. The finite counting
operator changes summation order and preserves cardinality. No floating
arithmetic, search, new prime/log table or production-tool edit.

Controls: reject dropping p>0 atR4,S2,p0; reject dropping the rectangle
guard atR1,S3,p2 (negative candidate RHS). Check the saturated R8,S2,p2
example against the original weight; it must not be confused with the
old false unsaturated-polynomial identity. Do not claim guard sharpness.

Budget: at most3 target builds,600s/8192MB per process,1200s cumulative;
stop after any resource stop. Preserve each failed full source/raw record
before at most2 local proof repairs. No weakened target, alternative
formula or partial-lemma substitution as success. Negative/incomplete
attempts remain. New StaircaseExact module and root import only; no
inherited mathematical statement/body changes.

After acceptance: root, signatures/controls/axioms, source coverage,
evidence integrity and a short human explanation. Update current
README/STATUS/FORMALIZATION and supplementary accounting without changing
the50b cutoff or implying earlier review covers this addition. No new
endpoint, valuation exponent, classification, novelty, optimality,
human review, merge, or Tao submission. Exact-head CI remains separate.
