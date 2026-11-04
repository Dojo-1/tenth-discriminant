# Round201 continuation: finite-level ghosts, residue-balanced source fibers, and transport corrections

Date 2026-11-04. All results below are **after** the frozen Round201 preregistration, T5 preregistration and T6 preregistration. No changes to original Gram, ordinary derivatives or 322^4 proof.

## T5 — mod-p^m kernels are not nested; transition morphisms matter

Predicted in [PREREG_T5_TRANSITION_2026-11-04.md](PREREG_T5_TRANSITION_2026-11-04.md) and implemented by [transition_tower_test.py](transition_tower_test.py). Passed [exact CI run 41793367422](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41793367422).

For the scalar matrix G=[3], its kernel K_m in Z/3^m is the set {0,3^(m-1),2*3^(m-1)} of cardinality3 at every m>=1. But each reduction K_(m+1)->K_m sends every element to zero. Thus these finite-level nonzero solutions **do not** define nonzero compatible inverse-limit vectors. For G=[0] reductions are surjective and the limit is Z_3 (this control falls outside positive-definite/nonsingular Grams).

For C=diag(1,3,27), the exact finite data are:

| m | |K_m(C)| | image size of K_(m+1)->K_m |
|---:|---:|---:|
| 1 | 9 | 3 |
| 2 | 27 | 9 |
| 3 | 81 | 9 |
| 4 | 81 | 9 |

And for E=diag(1,9,9):

| m | |K_m(E)| | image size |
|---:|---:|---:|
| 1 | 9 | 9 |
| 2 | 81 | 9 |
| 3 | 81 | 9 |
| 4 | 81 | 9 |

**P (standard algebra, paper proof):** for any nonsingular integer matrix G, ker(G:Z_p^n->Z_p^n)=0. Indeed adj(G)*G=det(G)*I and Z_p is an integral domain with det(G) != 0. Therefore lim_inv K_m(G)=0. Kernel *counts* recover Smith depth but the inverse system has trivial persistent kernel when the original real Gram is positive definite and thus det(G) != 0.

The n=1 nonliftability has been added as a separate Lean lemma (pending exact-head CI at initial recording). This observation is a new **semantic guard** for our loss ledger, not a novel theorem or extra discriminant bound.

## T6 — source-exact additional F3 kernel direction at radius6, lost at radius7

After the exact T3 pilot produced a 12-dimensional kernel vector v=2e_(0,1)+e_(3,2) for the **original** D=19, R=4, S=J=3, p=3 Gram, the theoretical explanation was reconstructed and recorded in [RESIDUE_FIBER_MECHANISM_2026-11-04.md](RESIDUE_FIBER_MECHANISM_2026-11-04.md).

The held-out radius-7 prediction was frozen in [PREREG_T6_RESIDUE_CONTROL_2026-11-04.md](PREREG_T6_RESIDUE_CONTROL_2026-11-04.md), **followed by a pre-execution correction** in [T6_PRE_EXECUTION_AMENDMENT_2026-11-04.md](T6_PRE_EXECUTION_AMENDMENT_2026-11-04.md). The initial preregistration incorrectly predicted the characteristic-three pairing identity as an exact *integer* equality. This was explicitly retired before tests: Frobenius is only a congruence modulo3.

The corrected exact test [source_kernel_certificate.py](source_kernel_certificate.py) passed [CI 41793551262](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41793551262):

| rho | number of non-real y^2=1 nodes | integer value of (G(Q_rho) v)_(0,1) | residue mod 3 |
|---:|---:|---:|---:|
| 5 | 10 | -65176 | 2 |
| 6 | 18 | 30624 | 0 |
| 7 | 22 | 595244 | 2 |

At rho=6 the *whole vector* G(Q_6) v is zero modulo3. At radius5 and radius7 its (0,1) coordinate is nonzero. The residue-fiber proof is the correct explanation: modulo3, f(Z,W)=Z^3 W^2+2W is Z-W, its first two ordinary Z derivatives vanish, and the non-real x=-4,...,4 layers repeat each residue modulo3 exactly three times. Thus the sum of each trace pairing vanishes modulo3. The original real Grams remain positive definite on supports as checked for radius5 and6.

**Caution:** extra modular kernel direction alone does not imply a *quantified* new determinant valuation beyond the known diagonal row factor: the remaining matrix K may have invertible determinant despite a singular principal block. Any claimed gain needs a source-exact determinantal-divisor/Smith lower, not only a rank drop. This test is an instance of support-dependent modular cancellation, not a uniform p-adic bound.

## What is newly formalized and what is not

- P, scoped to the Lean encoding: [LossLedger201.lean](../../lean/TenthDiscriminant/LossLedger201.lean) contains the exact T0 nonfaithfulness counterworld, with a successful earlier isolated Lean/axiom CI [41793120405](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41793120405).
- The new mod3/mod9 nonliftability theorem in the same module requires its **own new exact-head CI**; passing the earlier run does not certify it.
- P, paper-only: adjugate proof that positive-determinant integer Grams have trivial persistent p-adic kernel despite nontrivial finite quotients.
- M: T5, T6 exact finite tests passed in the given scope.
- H remains: a new uniform original-Q partial-minor or valuation-filtration inequality yielding an improved discriminant bound.
- R: unrestricted inference from field-like/F1 language to information preservation; from PSD observation order to modular rank order; and from a mod3 congruence to integer equality.

## Next discriminating action

Rather than spending compute on a generic category theory scaffold, select a named original-Q p-adic minor/graded piece and search for a **uniform** source-exact geometric inequality. If the residue-balanced fiber condition cannot be enforced for all eligible D or cannot improve the existing normalized scalar gap, record it as an explanatory finite mechanism and move on. The original 322^4 PR #126 remains independent, ready for review but unmerged, pending semantic review #50.
