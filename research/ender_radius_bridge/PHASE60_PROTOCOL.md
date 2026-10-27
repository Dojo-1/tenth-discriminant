# Phase60: one fixed zero-row boundary check

Register before executable arithmetic. Base main21c7b78cae7da1fbaec14d1c96c751677f3f0082. No model agent or independent review is authorized. This is a preselected verification case derived from source inspection, not a blinded discovery experiment.

## Exact target and fixed case

Inspect the per-form prime-representation estimate suggested by flow/x.md O5 and the tools/cover_h.py derivation: for a primitive reduced positive form Q=a*x^2+b*x*y+c*y^2 of fundamental discriminant -D, compare the number of representations of odd primes at most t with

    2*pi*t/sqrt(D) + 4*sqrt(a*t/D) + 1.

The fixed form is (a,b,c)=(3,1,1001), D=4ac-b^2=12011, t=3, p=3. First verify positivity, primitive/reduced conditions, D=3 mod4, squarefreeness by exact trial division, p odd prime, p not dividing D, and -D a nonzero square modulo p. If any guard fails, report INCONCLUSIVE; no alternate form or search is allowed.

Count the prime representations exactly, including y=0, with coordinate bounds derived from completing the square: D*y^2<=4*a*t and D*x^2<=4*c*t. Use only integer/fraction arithmetic. Bound the candidate expression rigorously using pi<4, D>100^2 and a*t=9; no floating-point estimate is acceptance evidence. Include the principal-form control (1,1,3003), with the same D,t, to identify the role of the zero row.

## Limits and interpretation

One process invocation,60seconds and256MB, no retries or tuning. Preserve source, raw output/error, elapsed/exit record and hashes even on failure. Standard-library Python only; no external class-number or numerical oracle.

A violation of this per-form estimate is a counterexample to that inferred per-form lemma/derivation. It does NOT refute the aggregate all-class bound, compute the actual class number, refute the h<=2 cutoff or invalidate the checked h=1 proof. The aggregate bound could conceivably have another proof. Preserve that distinction, all historical candidate records and the successful conditional prototype on its separate branch.

Do not modify flow/c.md, old preregistrations, production tools, Lean proofs/root, certificates or CI gates. A possible correction to a per-form zero-row allowance is only a proposal until its proof and aggregate consequences are separately supplied. No new numerical cutoff, classification, novelty, optimality or independent/human review claim.
