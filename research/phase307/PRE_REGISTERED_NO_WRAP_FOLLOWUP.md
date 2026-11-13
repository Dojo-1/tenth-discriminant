# Phase307-G — post-result follow-up preregistration: no-wrap regime

2026-11-13. This theorem target was formulated **after** the successful Phase307 A–F experimental suite; it is not part of the initial prior-to-code preregistration. Freeze the definition of `kernel_census` from Phase305 and `valuationWeight` from Phase304/Lean Arithmetic before running G.

Let p be a prime, R,S positive integers, J=S, j=min(S,p), and let T=(Z^(p^2)-Z)^j in Fp[Z]. The rectangular original source images are monomials Z^(r+p*s) for 0<=r<R, 0<=s<S. If maxdegree=R-1+p(S-1) < deg T=p^2 j, all source monomials stay unreduced in the truncated quotient.

**Predicted theorem [P-paper candidate]:**
h_p(R,S,S)=(S-1)*max(R-p,0), and h_p(R,S,S) <= valuationWeight(R,S,p).
Proof target: the exponent sets are S integer intervals of length R separated by p, so the union has size R*S if R<=p, else R+p(S-1). Existing w includes a unit for every r>=p and every s>=1.

**Boundary hostile test:** p5,S2,J2: deg50, maxdeg=R+4. For R45, maxdeg49 and predicted h=40,w=40. For R46, maxdeg50, no-wrap hypothesis FAILS; expect new exact quotient rank50, h=42,w=41, gain+1. Verify using the frozen Phase305 polynomial remainder implementation, a second independent mod5 row Gaussian method for R45/46, and exact original integer weight sum. Do NOT assert all wrap cases yield extra improvement.

**Field bridge stop rule:** This theorem restricts where extra first-level p5 contribution is even possible. It does not establish any positive uniform extra prime mass under hypothetical class-number-one fields, and cannot be added to the existing higher p-adic weight. Keep as standalone source arithmetic research until linked to same-original-Gram upper/lower comparison.