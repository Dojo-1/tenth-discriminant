# Minimal counterexamples

No counterexample to either principal theorem or to a stated load-bearing lemma was found in this review. Accordingly, no artificial failing theorem or inconsistent assumption is supplied.

The closest boundary attack is not a counterexample to the frozen statement: \(D=163,\ p=41\) gives \(-D\equiv1\pmod{41}\), but \(p=(D+1)/4\), while the theorem requires the strict inequality \(p<(D+1)/4\). The source includes this control in `lean/TenthDiscriminant/SmallPrimeBridge.lean`.

The review's independent executable sieve check is `../sieve_oracle.py`. It checks mask literals and samples, not the full finite-coverage theorem; it is intentionally not presented as a counterexample or as a substitute for kernel replay.
