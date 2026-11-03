# Phase 170 — original thin-ellipse count at fourth-root 377

Status: Lean candidate, not an improved field-discriminant cutoff.

## Frozen observations

The original integer-pair support is

```math
Q_{\rm thin}(D)=\mathrm{ellipsePairs}(D,\lceil(11/25)D^{3/4}\rceil),\quad
R(D)=\lfloor D/4\rfloor,\quad S(D)=\lfloor R(D)/25\rfloor.
```

The target is the same sufficient interpolation criterion
$2(R-1)+(S-1)<|Q_{\rm thin}(D)|$, not a necessary count
or a new source lattice. The original ordinary-Z derivative, both
2,2D trace weights and field charts remain untouched.

## Why 377 appears

The previously used cell-area lemma requires

```math
\rho\ge (1001/1000)\sqrt{(2R+S)\sqrt D/\pi}+10\sqrt D.
```

From the exact integer R,S definitions, $2R+S\le(51/100)D$;
the existing rational pi bound gives the sufficient square-root
majorant $(413/1000)D^{3/4}$. Since
$\rho_{\rm thin}\ge(11/25)D^{3/4}$, sufficiency reduces to

```math
(11/25-(1001/1000)(413/1000))D^{1/4}\ge10.
```

The coefficient equals $26587/1000000$. At root 377
the excess is $23299/1000000>0$; at root 376 it is
$-3288/1000000<0$. Thus 377 is the first integer root floor
**for this particular sufficient certificate**; it does not rule
out a stronger certificate at a smaller floor.

## Lean modules and decision gates

The new ThinEllipseCount377.lean declares
fourthRoot_ge_377, thin_chosen_radius_377 and
thin_radius_interpolation_count_377. The theorem is geometric,
for every natural D >= 377^4, without squarefreeness, class-number-one
or prime assumptions. Require focused pinned Lean 4.19.0 compilation,
whole-root source correspondence, permitted axiom and known-false
negative-control checks, and CodeQL.

The historical lower and upper analytic envelopes still require
D >= 450^4. Combining them with the binary quarter contribution
at 377^4 is **only conditional**, with a prospective normalized
numerical margin > 979289/10000000 > 9/100 if both envelopes survive
rederivation. Re-establish the arithmetic lower, same-Q analytic
upper, positivity and field bridge separately. No smaller
field-discriminant result follows from the count alone.

Kill if the new proof borrows Tuned.root_large,
Tuned.dimensions or the former interpolation theorem under its
450^4 premise, changes the source Gram, fails Lean verification, or
mistakes a sufficient condition for a necessary one.

Tracking: Issue #82 (threshold audit); Issue #50 (independent
semantic reconstruction).
