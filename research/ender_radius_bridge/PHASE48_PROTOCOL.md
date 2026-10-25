# Phase48: diagnose the current affine-envelope limitation

Registered after Phase47 head 2f519884790c8c38bc8ffae4a2d0dba4c74e1876.
The same exact-head CI run 40208552511 is live; this local protocol does
not cancel it, change Lean sources, or authorize a replacement run.

Purpose: distinguish an endpoint-rounding opportunity from an improvement
requiring stronger analytic envelopes. This is one exact rational diagnostic,
not a new cutoff proof, parameter search, or independent semantic review.

Frozen inputs from HUNDRED_BILLION_GUIDE.md and TunedAnalyticCutoff.lean:
lower envelope L0(u)=999997*u/1000000-5820/1000;
upper envelope U0(u)=4*u/5-813/1000, with u=log D.
The inherited theorem gives L/(R^2*S)>=L0 and U/(R^2*S)<=U0,
under its full arithmetic, geometric and floor/ceiling guards.

Single computation: use Python Fraction arithmetic to derive the exact
gap slope, intercept and unique zero; evaluate the gap only at the fixed
controls u=25 and u=253/10. Verify that the gap is respectively negative
and positive and that the zero lies strictly between those controls.
No parameter scan, transcendental approximation or finite classification
input. Do not infer a D cutoff from the zero without checking log bounds
and every inherited guard. Do not infer failure of the underlying method
from overlapping one-sided envelopes.

Budget: one execution, 30 seconds, no proof build, no retry or data-dependent
change. Any failed assertion or execution failure is retained as a negative
result. Output records exact fractions, source hashes and runtime provenance.
Success means only the rational identities and fixed controls check.

Delivery: a concise reader-facing explanation of what tighter rounding
could and could not accomplish. No new analytic constant, novelty, full
classification, higher-class-number progress, review, merge or submission.
