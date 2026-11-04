# Round201 T8 preregistration — entrywise modular collapse of balanced nonreal fibers

Date: 2026-11-04. This hypothesis is recorded **after** observing T7 source ranks 9 and 13, but **before** executing the stronger T8 entrywise comparison. This is a post-observation mechanistic prediction, not a retroactively preregistered T7 result.

Freeze the original integer ordinary-Z-jet Gram with D=19, p=3, R=4, S=J=4 and the same trace pairing 2(ac+19bd). Let Q_rho=ellipsePairs 19 rho and A_rho={q∈Q_rho : y=0}, the *real-axis* support used only as a **comparison and modular witness**, not as a replacement production Gram.

**T8a (predicted exact congruence):**
    G(Q_6) = G(A_6) (mod 3) entrywise,
because the omitted nonreal y=±1 layers x=-4,...,4 give exactly 3 copies of every x residue mod3 for each y, so the sum of any integer polynomial trace-pairing integrand over each layer is zero modulo3.

**T8b (rank bound):**
    rank_F3 G(A_6) <= p * min(J,p) = 9,
since after reduction mod3, every ordinary derivative of order j>=p vanishes (falling factorial contains p), and each of the j=0,1,2 channels depends on at most three real-axis residue classes x mod3. The exact rank of G(Q_6) was 9 in T7; rerun independently on A_6 to verify rank=9.

**T8c (held-out negative control):**
    G(Q_7) != G(A_7) modulo3.
At row (0,0), every observation contributes integerPairTrace(1,1)=2, and there are 22 nonreal Q_7 points, so (G(Q_7)-G(A_7))_(0,0)=2*22=44=2 (mod3). At rho6 the same entry has 18 nonreal points and difference 36=0 (mod3).

This proves a *finite* algebraic mechanism, not uniform additional p-adic determinant divisibility at the production Q_thin(D). No new number-field conclusion, no p=3 support modification in PR #126, no use of float eigenvalues. A failure of any exact-entry comparison falsifies the proposed residue-balance explanation.
