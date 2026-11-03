# Phase194 — the original thin Gram's analytic upper at fourth root 328

*3 November 2026 · a source-matched analytic theorem target until focused Lean compilation and source checks pass.*

The preceding [Phase191 arithmetic](https://github.com/Dojo-1/tenth-discriminant/tree/research/phase191-328-arithmetic-preflight) has already compiled under the positive ORIGINAL source-Gram premise; [Phase193 geometry](https://github.com/Dojo-1/tenth-discriminant/tree/research/phase193-original-geometry328) now attempts that positivity at $D\ge328^4$. This phase tests the other side of the determinant sandwich. It does **not** transplant a $331^4$ theorem by weakening its hypothesis; the original analytic scalar obligations are rederived at 328.

## The invariant and the comparison

Keep, without substitution, the old source dimensions $R=\lfloor D/4\rfloor$, $S=\lfloor R/25\rfloor$, original thin radius $\mathrm{thinRadius}(D)$, original ellipse $Q_D=\mathrm{ellipsePairs}(D,\mathrm{thinRadius}(D))$, ordinary-$Z$ polynomial jets holding $W$ fixed, integer evaluation lattice, and trace pairing with channel weights $2,2D$. The single auxiliary integer is

```math
\Delta_D=\det\big(E_{Q_D}B_{Q_D}E_{Q_D}^{\mathsf T}\big).
```

The [UpperScalars328.lean](../../lean/TenthDiscriminant/UpperScalars328.lean) candidate retains the same radius and count majorants as in the accepted 331 proof, but derives each numerical prerequisite from $D\ge328^4$, including the new sound lower enclosure $\log D\ge23.172$ from Phase191. The inherited 328 geometry still gives $\rho/R\le521/80000$ and $\log D/R\le1/9000$; the relevant error estimate uses their sum only through a coarser $1/100$ budget.

The [ThinUpper328.lean](../../lean/TenthDiscriminant/ThinUpper328.lean) candidate then specializes the existing source-exact Hadamard and radial-saving bound to **the original thin $Q_D$**. The padded ellipse is used only for a point-count majorant, never for a different determinant. The desired numerical upper is

```math
\frac{\log\Delta_D}{R^2S}
\le \frac45\log D-\frac{1849}{2000}.
```

With Phase191's separately compiled original odd-plus-one-binary lower, the intended conditional normalized sandwich would be

```math
\frac{999997}{1000000}\log D
-\frac{57321}{10000}+\frac14\log 2
\le \frac{\log\Delta_D}{R^2S}
\le \frac45\log D-\frac{1849}{2000}.
```

The exact **fixed** conservative scalar gap is $1371/250000000=0.000005484>0$ from the sound $\log328$ enclosure. Phase192 has proved a stronger *generic* $0.0895$ source-floor gain, but propagating it to this exact original thin Gram and the field return is a separate theorem obligation; do not count it here without that proof.

## Why this is not yet the field theorem

The following edges remain distinct: original $Q_D$ finite interpolation count; strict positivity of the original integer Gram; number-field class-number-one prime-divisor lower; Hadamard/radial analytic upper on that *same* determinant; exact scalar non-overlap; odd/even maximal-order chart return to the **field discriminant**. This phase is responsible only for the analytic upper and its source geometry dependencies.

**P in previous exact-head focused runs:** 328 logarithmic/odd/binary arithmetic Phase191 and generic 0.0895 gain Phase192, under their stated hypotheses. **H until this branch's exact-head CI succeeds:** Phase193 328 source-geometry positivity and the new same-Gram upper. **H until later field compilation and full-root audit:** 328 actual-field cutoff. **External semantic review:** [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50), unchanged.

**Kill criteria:** an imported theorem requiring $D\ge331^4$ is silently used at 328; the padded Gram replaces the original thin Gram; the original ordinary derivative or trace metric changes; the analytic constant weakens enough to erase the scalar separation; or a new axiom/Lean admission appears. Failure of this sufficient bound must not be relabelled impossibility of all 328 methods.
