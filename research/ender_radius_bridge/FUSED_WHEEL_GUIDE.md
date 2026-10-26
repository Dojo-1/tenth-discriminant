# Split the search, not the mathematical obligation

The full target is still class-number classification below the checked
global cutoff 700000000000. This phase changes how one finite certificate
is organized; it does not improve that analytic constant.

## The idea to retain

The old checker first built a large list of wheel residues, then tested
its leaves. Its four registered attempts exceeded the memory threshold.
The new traversal tests a leaf as soon as it is generated. It also cuts
the search into eleven subtrees, one for each allowed residue modulo 184
(8 times 23). Each subtree gets a separate kernel check.

The important statement is NOT that eleven examples passed. Lean proves
that, for EVERY Boolean leaf predicate f,

    all eleven subtree checks of f = the old complete wheel check of f.

The eleven seeds are exactly
3,27,35,59,75,123,131,139,147,163,179. Their complete-list equality is
checked, not inferred from a matching count. The split changes traversal
order, not which leaves must pass. No subtree may be omitted.
For exclusion we need complete coverage, not a count or a claim that each
leaf has a unique enumeration witness.

`maskWheelVisit_all` proves the general traversal identity.
`phase35_partition` specializes it to the fixed complete seed partition.
The earlier residue-mask theorem still supplies the arithmetic meaning;
the old quotient/remainder theorem still supplies interval coverage.

Geometrically, the base wheel is a repeating cell of allowed residues.
But the 200 extra prime tests need not repeat with that cell. For example,
the test at prime 29 accepts residue d=163 and rejects d=163+892371480.
Lean checks this control. One translate therefore cannot certify all others
by symmetry: translation preserves the base wheel, not every extra test.

## A certificate must reach the actual field

If the actual field Q(sqrt(-d)) has class number one, the previously proved
small-prime obstruction forces all guarded prime tests to pass, and forces
d into the complete wheel. A checked empty translate contradicts those
necessary tests. The new bridge supplies all 208 mask equalities, all odd
prime labels, positivity and the exact guard 4*p<=d. It does not assume
independence, a classification, or an unverified numerical certificate.

All eleven blocks for translate zero passed the registered pilot. They
were then rechecked as separate library theorems and assembled with the
coverage and actual-field bridges. The full library build accepts
`classNumber_one_iff_below_first_period`: for positive squarefree d below
892371480, actual class number one iff d belongs to the nine-value list.
There is no hidden certificate or numerical hypothesis in that statement.
The endpoint is the full wheel period.
That number is a computational boundary, not an optimized analytic cutoff.
Exact published-head build/signature/audit/CI records accompany this
statement; a local build alone is not a full CI or human-review claim.

## What the fixed cost pilot actually did

The pilot kept the original four translates 0,1,392,784, the same eight
base primes and the same 200 extras. Its limits were 8192 MB and at most
180 seconds per block, with a 720-second aggregate budget.

- Translate 0: all eleven blocks passed.
- Translate 1: five blocks passed; the sixth had only one second remaining
  under the aggregate budget and was time-stopped. Five more were skipped.
- Translates 392 and 784: all twenty-two blocks were skipped because the
  aggregate budget was exhausted. They are NOT successful or failed tests.

Thus 16 blocks passed, one was aggregate-time-stopped, and 27 were skipped.
Observed aggregate wall time was 721.4877611 seconds, including startup
and polling/termination overhead. The budget was not raised. Passing block
peaks were about 5.3 billion bytes, below the unchanged threshold. There
was no memory stop in this pilot. Only one translate is complete.

This demonstrates a working memory-bounded certificate organization for
that translate, NOT a full-range runtime or an isolated speedup due to
fusion. Fusion and partitioning changed together; a block contains less
work than the old monolithic translate. Phase34's failures remain preserved.

## The frontier, without rounding it into success

There are 785 padded quotient indices for the original interval. This
phase supplies only the first complete one. The actual-field composition
extends the nine-value iff from one million to 892371480. The interval
[892371480,700000000000) still needs a complete
certificate or a stronger proved argument. Partial checks in translate 1
cannot be rounded up to a larger complete interval.

All nine positive fields were already proved by small ideals and Minkowski.
No new positive field, optimized global bound, independent human review,
Mathlib upstream acceptance, merge or Tao submission is claimed here.

[Protocol](PHASE35_PROTOCOL.md) · [Pilot records](PHASE35_PILOT_RESULTS.json) ·
[Build and verification checkpoint](PHASE35_VERIFICATION.txt) ·
[Collected terminal records](PHASE35_RESULTS.json) ·
[The arithmetic representation](RESIDUE_MASK_GUIDE.md) ·
[The nine positive proofs](NINE_POSITIVE_GUIDE.md).
