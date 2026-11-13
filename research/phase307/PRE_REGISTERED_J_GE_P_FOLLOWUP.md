# Phase307-H — post-G follow-up preregistration: j>=p Frobenius quotient

Date 2026-11-13. Written after Phase307-G no-wrap controls passed and BEFORE the H code.

For a fixed prime p and ORIGINAL ordinary jet policy J=S>=p, the residue-field kernel quotient has defining monic polynomial

    (x^(p^2)-x)^min(J,p) = (x^(p^2)-x)^p = x^(p^3)-x^p   in Fp[x].

Thus x^n reduces to x^e where e=n for n<p, else e=p+((n-p) mod (p^3-p)). Proposed exact rank:

    rank = | { e(r+p*s): 0<=r<R, 0<=s<S } |
    h_p = R*S - rank.

**Prediction/validation:** compare this direct combinatorial formula to the independently authored Phase305 quotient-remainder Gaussian rank for bounded controls p=3,S in {3,4}, R in {9,15,25,30}; p=5,S in {5,6}, R in {15,25,40}. Check residue classes, no hidden Hasse substitution, ordinary jets j>=p vanish modp.

**Bounded native-policy range:** for R in {100,200,400,800,1600}, S=floor(R/25), examine every prime 3<=p<=S. Record h_p and existing w_p, max(h-w), whether any positive example occurs. NO prior sign assumption, no inference from finite grid to asymptotic h1 theorem, and not all primes are inert for any particular field.

**Falsifier:** a single mismatch against independent polynomial remainder rank invalidates the canonical exponent formula; preserve the failure and stop. The valuationWeight bound must never be double-counted with h_p.