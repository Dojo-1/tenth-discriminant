# Phase294-B — preregister full 725-row NORMALIZED source covariance with MOVED observations

**2026-11-12; AFTER Phase294-A original residue-boundary rank40 PASS [CI #43313214413](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43313214413), BEFORE Phase294-B code/results.** The rank40 raw defect, parity20+20 and mod5 support mass104 are now retrospective regression facts, NOT blind predictions. This second experiment asks for a different and more demanding TRUE POSITIVE: can one realize the local field chart as a map of the FULL p5-Frobenius-normalized original evaluation source **provided the 383 observation points move with it**? This is explicitly NOT the source-preserving original-Q result rejected by Phase293-D.

## Original typed carriers and unchanged arithmetic convention

Field B: D587, whose true production source R146/Q383/n730 remains untouched. Take only the **first725 original row labels r<145, s<5** as a DIAGNOSTIC, all 5 original ordinary Z-jets holding W fixed, all original 383 field587 points and original trace B_B=diag(2,1174). Field A: D583 COMPLETE original R145/S=J5/Q383/n725, original B_A=diag(2,1166). Both original source helpers are frozen at Phase206 `3f954b59d9f86b06ad53667c869b5b24f2e6c7f6`, Phase204 `dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8`. Reuse frozen independent parameterized Phase292-A Frobenius source builder `research/phase292/matched_inert5_neighbor.py` blob `9216de10f311cf301413de663738804b5fbec203`, with p=5 K=9, and no edits to any of these files.

The original **unimodular integer row Frobenius polynomial frame** is the SAME for the two matched 725-row sources:
`F_(r,s)=Z^(r-5k) W^s (Z^5-W)^k,quad k=min(r//5,4-s)`;
OLD F5=`sum k=1350`, exactly once in each source. In each field these rows divide integrally by 5^k at all original/jetted points. No secondary Smith or primitive pairing operations are performed for this B experiment. The C0 rows are exactly the OLD normalized source, not p-saturated H.

Let `q=5^(K+maxk)=5^13`. By odd-p Hensel find the unique `alpha∈Z/q` with `alpha≡2 mod5` and `583 alpha²≡587 mod q`; it must reduce to 2 mod5,17 mod25,67 mod125. Map ALL 383 original field587 observation points `Q_B=(x,y)` to the **FORMAL p-adic displaced support** `phi Q_B=(x,alpha*y mod q)` in the D583 integer-pair coordinate model. This moved support is NOT the original Q583 ellipse or number-field proof source and does not give a new h1 field.

For the full ORIGINAL ordinary jet source E and its normalized source C0, with original row labels and no row mixing, the expected exact `Z/5^9` linear algebra relation is

```
C0_A(phi Q_B) = C0_B(Q_B) * Y,               over Z/(5^9),
Y = diag(1,alpha) on EACH original (j,q) real/imag value pair,
B_B = Y B_A Y^T  mod 5^9, and in fact mod 5^13.
```

This is **covariance with MOVED observations**, not `C0_A(Q_A)=...`; it does not contradict Phase293-D's fixed-index source square no-go. The extra four digits in alpha and source numerator modulus are mandatory: dividing the original Frobenius polynomial row by p^k (k<=4) is not justified by an equality known only modulo p^9. The test will verify all **725×3830 normalized entries**, not just a principal Gram.

## Frozen falsifiers and controls

1. Verify Hensel α modulo 5^13 from the root 2 mod5 and all lower residues 2,17,67; check `583 alpha²=587 mod5^13`; old α=2 alone MUST FAIL at precision25, confirming this test is not a trivial mod5 label relabelling.
2. Construct independently (through same source engine but different D and support) `C0_B(Q_B)` and `C0_A(phi Q_B)` to K9 with original ordinary j0..4, all first725 rows, all original 383 points, both original coordinate channels, and the OLD Frobenius frame divided by the SAME p^k (F=1350). Stop on ANY of the 2,776,750 original coordinate entries differing from the Y-transformed source modulo 5^9. Check exact original integer-jet oracle on 16 row labels, ALL five jet orders, 3 original point indices for BOTH sources, with the transported Q supplied to A (still integer coordinates).
3. Verify `Y B_A Y^T=B_B` at mod 5^13 and the 6x6 normalized Gram computed from C0_A(phi Q) with original B_A equals C0_B(Q) B_B C0_B(Q)^T mod5^9, using overflow-safe modular matrix products (reduce coordinate weights BEFORE accumulation).
4. Negative controls:
  - row Z=(r1,s0), k0, at original q=(22,1) the **fixed point** coordinates fail to match under Y already mod5; only MOVED q=(22,alpha) is covariant;
  - original Q as an integer set is NOT phi Q and already mod5 has 104 transported residue mismatches;
  - α=2 does not solve the field relation modulo25;
  - raw congruence a≡b mod5 with a=5,b=10 does NOT survive quotient by p when comparing a/p and b/p mod5;
  - second fake source field at a split prime has no Frobenius normalized integer source and is NOT allowed by this test.
5. Do NOT reconstruct primitive H or claim that **actual original** D583 Q and D587 Q are source-isometric. Phase293-D proved no fixed-point-index canonical Y works even over F5. Preserve this opposition explicitly. No new class-one or discriminant bound, no extra 5-adic factor and no automatic statement about all possible observation Y. Keep PR draft and review #50/#51.

**Evidence taxonomy:** [P-paper conditional] p-adic ring isometry, exact polynomial/ordinary-jet naturality and controlled p-division; [M after CI] all matched 725x3830 normalized source entries transported over Z/5^9 with moved Q; [H] gluing such a moved-support identity back to the ORIGINAL ellipse after full p-saturation; [R] forcing p5-normalized source covariance from a modulo5 identity without paying p-adic precision debt.
