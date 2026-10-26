# A boundary row that the higher-class-number count must retain

**A counterexample to a suggested per-form estimate, not to the aggregate bound or a class-number cutoff.** One preselected exact-arithmetic test was registered and executed. No class number was computed.

The old higher-class-number derivation suggests bounding prime representations in each reduced form by

    U = 2*pi*t/sqrt(D) + 4*sqrt(a*t/D) + 1.

Take Q(x,y)=3x^2+x*y+1001y^2, D=12011, t=3. The form is primitive, positive and reduced; D is squarefree and 3 mod 4. Both (-1,0) and (1,0) represent the odd prime 3. There are no others: completing squares bounds |y| by 0 and |x| by 1 in Q<=3.

Yet

    U = (6*pi+12)/sqrt(12011)+1
      <36/100+1 =34/25 <2,

using only pi<4 and 12011>100^2. Thus even the count of prime representations, not merely all lattice points, exceeds this proposed per-form bound.

## Why this row matters

For the principal form x^2+x*y+3003y^2 with the same discriminant, y=0 gives squares and contributes no odd-prime representations. That positive control passed. For the nonprincipal-form candidate above, y=0 gives 3x^2 and contributes two. A principal-form exclusion of this row cannot be transferred unchanged to arbitrary forms.

The documented split-prime argument sums per-form estimates and divides by four representations per unramified split prime. This test exposes a gap in that per-form justification. Other classes might supply enough slack for the aggregate inequality, or the aggregate inequality might have another proof. Neither the aggregate bound nor the historical X(2)=70000 claim was tested or disproved here. Its independent review remains open.

## A repair direction, not a new certificate

On y=0, a*x^2 can be prime only for x=+/-1 and prime a, giving at most two contributions per form. Separating this row would suggest a conservative +2 allowance, hence an H/2 constant after dividing by four, if the nonzero-row and all-class steps are justified. No revised interval campaign or cutoff calculation was run. Do not substitute this proposed coefficient into the old certificates and call them verified.

The conditional excluded-prime bridge in [PR30](https://github.com/Dojo-1/tenth-discriminant/pull/30) deliberately keeps its count estimate as an assumption. This case explains why supplying that estimate is a substantive arithmetic task. The checked class-number-one result remains unchanged at 50 billion.

[Registered case](PHASE60_PROTOCOL.md) · [Raw result manifest](PHASE60_RESULTS.json). The raw output, source snapshot and process record are preserved in PHASE60_RAW.zip. No Lean verification or independent/human review is claimed for this boundary test.
