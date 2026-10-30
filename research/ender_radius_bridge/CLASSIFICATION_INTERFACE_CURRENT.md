# The classification no longer needs a caller-chosen field chart

**Integrated unchanged in this branch; all four local checks pass.**
This composes existing mathematics. It does not introduce a new classification
method or constitute independent semantic review of the inherited proof.

For ANY totally complex degree-two number field K, the new statement is:

    h(K)=1 iff there exists positive squarefree d in
    [1,2,3,7,11,19,43,67,163] with a rational algebra equivalence
    Q(sqrt(-d)) equivalent to K.

The forward direction constructs a squarefree root from K's conjugation
and degree, obtains its algebra equivalence and transports class number.
The existing canonical iff then puts d in the list. The reverse direction
uses the canonical positive result for the listed d and transports h=1 back
to K. Neither direction asks the caller to supply a generator or finite
certificate. Positivity is explicit and supplies the field instance.

A second statement transports the actual signed NumberField.discr K into
[-4,-8,-3,-7,-11,-19,-43,-67,-163]. It is necessary membership, not an
asserted iff from discriminant membership alone or a uniqueness theorem.

The interface deliberately retains the existing canonical proof's separate
700-billion radicand bound and finite sieve. It does NOT replace that proof
with the new47.5-billion endpoint or silently shorten its certificate range.
The cutoff optimization and classification interface are different advances.

[Exact two Lean statements](Phase126Classification.lean) ·
[Protocol](PHASE126_PROTOCOL.md) · [Verification](PHASE126_VERIFICATION.md).
Two required/frozen targets passed together on the first complete check:
60.559438seconds, namespace2logical/2theorems, fresh closures61627/61633,
only standard3axioms. Four required representation/classification inputs
are present; eight newer cutoff roots are absent. No proof repair or second
call was used. [Integrated API](../../lean/TenthDiscriminant/FieldClassification.lean) and [Phase128 evidence](PHASE128_VERIFICATION.md) cover the production/root checks; exact-head CI and review remain separate.
