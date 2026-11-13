# Phase308-B — post-discovery, pre-code adaptive torsion family

Date: 2026-11-13. This is **not** a preregistration of the discovery itself. The candidate ranks/orders below arose in exploratory human/AI discussion and a one-off local brute-force computation. The following is a *prospective validation protocol* for a new independent implementation and hosted CI, frozen BEFORE the new B code.

## Candidate family of genuine quadratic ideal classes

For fundamental imaginary quadratic discriminants -D, O_D=Z[omega] with omega²=omega-m and m=(D+1)/4, choose a simple split prime p and root r0 of f(X)=X²-X+m modp. The ideal I=(p,omega-r0) has normp. Its kth power is represented by the coherent Hensel residue kernel

    ker(O_D -> Z/p^k, omega -> r_k),   r_k mod p^k.

For candidate principalization I^k=(alpha), alpha=a+b omega, necessarily N(alpha)=p^k and a+b r_k =0 mod p^k. Conversely, if these two exact equations hold then alpha∈I^k and equal ideal norms imply equality (using standard split-prime ideal theory). The finite-search certificate MUST be complete at each k via the identity

    4 N(a+b omega) = (2a+b)^2 + D b^2.

Bound |b| by 4 p^k/D and solve the remaining perfect-square condition, not via arbitrary rectangular brute force.

### Candidate controls to validate independently

|D|p|r0|expected first principal power k|generator alpha|optional rank100 determinant class modk|
|---|---|---|---|---|---|
|163|41|0|1|omega|0|
|187|7|2|2|omega-2|0|
|203|3|0|4|omega-6|0|
|167|2|0|11|7omega-2|1|

The exploratory Hensel root for D167/p2 at level 11 was r11=878. The norm candidate N(7omega-2)=2048=2^11. Verify both independently from the formula and the newly implemented Hensel procedure. Enumerate all k<11 and document every failed level; this is a *bounded exact result for that particular field*, not a uniform formula.

### Independent controls and stop rules

1. For all k<=first success, enumerate EVERY possible (a,b) with N=p^k by perfect-square discriminant, and verify the Hensel-residue condition. If an earlier valid generator exists, RETIRE the proposed order immediately.
2. Compute the reduced primitive positive binary quadratic forms of discriminant -D by a separate routine; expected form counts (class numbers) are 1,2,4,11, and should agree with the detected ideal order. Classical reduction theorem remains an imported mathematical theorem, not newly Lean-proved.
3. **Falsification of scalar collapse:** the optional twisted rank-100 Steinitz determinant class is trivial for D163,187,203 but not D167. A *deliberately naive* principal/nonprincipal classifier that treats trivial determinant as principal must make false positives for the order-2 and order-4 cases; the typed Picard-class gate must distinguish all four. This is an in-sample representation-discriminator, NOT an independent general-intelligence benchmark or a performance claim.
4. Split versus inert, incorrect residue root, precision mismatch, and unrelated integer source must be rejected.
5. No code may change the original 100-row integer Gram, class-number-one field theorem, or existing bound. No Work mode or merges.
