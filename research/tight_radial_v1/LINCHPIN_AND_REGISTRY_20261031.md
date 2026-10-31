# Four linchpins for the strict 47-billion actual-field statement

**31 October 2026 · Issue #50 · proposed independent-review surface, not a referee report.** This is informed by [Thomas Hales, *Linchpin Theorems* (Hexagon 2610.00289v1)](https://hexagonmath.org/2610.00289v1), [Palomar's statement/proof separation](https://palomar-registry.org/statement), [Palomar's comparator and submission rules](https://palomar-registry.org/how-to-submit), and the [Harvard CMSA Summit on Math Research in the Age of AI](https://cmsa.fas.harvard.edu/aimathresearch_summit/) (22–23 October 2026). The exact Summit PDF was not accessible during this session; no paragraph of it is quoted or claimed inspected. The first source discloses extensive AI generation; it is a proposal for a method, not mathematical validation of this project.

The point is not to multiply proofs. A linchpin is a **small mathematical statement whose intended meaning can be audited independently**, connected by an inspectable map to the large Lean dependency tower. If a reviewer can reject one of these without understanding the entire 12,000+-line library, the audit has become more useful.

## The precise external theorem

The target declaration in [TightRadialEndpoint.lean](../../lean/TenthDiscriminant/TightRadialEndpoint.lean) has the shape

```lean
theorem totallyComplex_degree_two_classNumber_one_discriminant_bound_47b
    (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K = 2)
    (hc : NumberField.classNumber K = 1) :
    (NumberField.discr K).natAbs < 47000000000
```

This must be audited as a theorem about the **actual ring-of-integers field discriminant**, not as a theorem about a chosen nonmaximal order or the Gram determinant. The inner Lean proof has already passed source/axiom/negative-control gates at its recorded revision; the human interpretation and independently reconstructible analytic argument are not externally certified.

## Linchpin A — the field chart can be checked with two tiny examples

For squarefree positive d, in the field K=Q(sqrt(-d)) the absolute field discriminant is d if d≡3 (mod 4), otherwise 4d. In particular, for d=3 it is **3**, not 12; for d=2 it is **8**, not 2. Any chart using Z[sqrt(-d)] as the full ring of integers for d≡3 (mod4) is wrong. Ask the referee to reconstruct both parity cases, preserve class number under the actual field equivalence, and explain why a discriminant bound on the parameter d becomes one on NumberField.discr K. [Chart source](../../lean/TenthDiscriminant/QuadraticFieldChart.lean).

## Linchpin B — the arithmetic exponent is **twice** the row index

Freeze the identical integer ordinary-jet E and original full ellipse Q. B has the integral trace weights diag(2,2D) at every observation, and G=E B E^T. Given U_p E=Delta_p C with U_p unimodular and Delta_p diagonal p^{k_i}, det G=p^{2 sum k_i} det(C B C^T). The factor two is not an optional convention: one Delta_p sits on each side of the metric. A one-row toy (E=[3,0], B=I) has Gram determinant 9, not 3. The referee should not substitute a selected minor, a changed sample set, or a Hasse derivative matrix for G. [Exact implementation](../../lean/TenthDiscriminant/RectangularGramFactor.lean) · [exterior-volume derivation](../ender_radius_bridge/EXTERIOR_VOLUME_GUIDE.md).

## Linchpin C — positivity is a theorem on the ORIGINAL observations

Under the production interpolation/point-count guard, the exact original real Gram must be strictly positive. From that, Hadamard yields an upper on the WHOLE determinant. For E=[1,1] and B=I, the whole Gram determinant is 2, while each selected one-by-one minor squared equals 1: **one minor's upper is not the Gram upper.** Conversely full row rank of the normalized p-quotient alone need not force its residual B-restricted Gram to be a unit modulo p. Make both negative controls part of a human explanation. [Area and point-count source](../../lean/TenthDiscriminant/EllipseCellArea.lean) · [issue #51](https://github.com/Dojo-1/tenth-discriminant/issues/51).

## Linchpin D — the finite rational inequality is not the analytic proof

The [endpoint](../../lean/TenthDiscriminant/TightRadialEndpoint.lean) derives, for u >= 24573/1000,

```text
(999997/1000000*u - 5739/1000)
 - (4/5*u - 1649/2000)
 >= 26281/1000000000 > 0.
```

The arithmetic may be checked in isolation. Yet a referee must separately establish the effective prime mass and reciprocal tail, the original full-ellipse count, the ordinary derivative Hadamard estimate, the log lower bracket at 47,000,000,000 and every application to a single det G. Inspect [Human reconstruction](HUMAN_RECONSTRUCTION.md) and [review entry](INDEPENDENT_REVIEW_ENTRY.md); do not promote a correct final subtraction to certification of the preceding inequalities.

## Palomar compatibility assessment — **not a submission**

Palomar requires a small independently specified Challenge statement, a Solution, comparator configuration, pinned immutable Git commit, axiom discipline, independent-kernel replay, and formalization provenance. Its present submission rules additionally require `module` headers and restrict the Challenge import closure to Lean core, pinned Mathlib or Tau Ceti. The existing project uses a separate pinned Lean 4.19.0/Mathlib generation and substantial local source dependencies. We have **not** tested that the current theorem compiles in a Palomar-compatible pinned toolchain; we have not constructed a strict Mathlib-only Challenge/Solution separation, a Comparator export, a conforming metadata file, or an independent checker replay. Those are concrete, potentially costly remaining tasks, not silently completed safeguards.

A plausible next isolated interface is a 20–40-line Challenge declaration stated *only* in terms of ordinary Mathlib NumberField notions, paired with a Solution whose local imports entail exactly that statement. It must be checked that the independently stated theorem has the same actual-field meaning, not just the same identifier. Do not submit to Palomar, assert registration eligibility, or contact anyone on another's behalf before this is actually implemented and independently audited. Palomar explicitly says registration is **not** novelty certification or external peer review.

Hexagon is instead a possible later **dissemination** channel for transparently AI-assisted mathematical research; its public moderation is not correctness verification. [Hexagon](https://hexagonmath.org/) and [First Proof Third Batch](https://hexagonmath.org/2610.00244v1) reinforce keeping logical soundness, exposition and attribution as different review axes. No external submission or contact has occurred.

## Reviewer return artifact

A useful result for #50 is a signed-by-author short reconstruction of one linchpin, plus its precise connection to the encoded theorem and any unstated hypothesis. An independent mathematician should be able to describe the first wrong arrow or assert that a bounded crossing survived scrutiny. Four individually accepted local checks still require a **global compatibility argument** joining them. A fresh AI audit, passing CI, or this document alone does not close #50.
