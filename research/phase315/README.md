# Phase315 · the wild second digit

> The first wild coordinate remembers a residue.  
> The second remembers how that residue was lifted.  
> Neither alone remembers a global ideal class.

A stacked research **draft** for Dojo-1/tenth-discriminant. Its base is the Phase313 research branch, after Phase314's successful research-only PR #206 merge. No main merge; no change to the reported \(322^4\) cutoff, the original Lean field theorem, or the exact fixed-field \(v_5=77\) result. Preregistered protocol: PRE_REGISTERED_CONDUCTOR125.md.

## Correct the defect before transporting it

For a local 5-unit \(z\in\mathcal O_D/125\), with \(\mathcal O_D=\mathbb Z[\omega]\), \(\omega^2-\omega+(D+1)/4=0\), define

\[
d(z)=\frac{z^5-\bar z}{5\bar z}\pmod{25}.
\]

Dividing by 5 is done on the numerator in the integral quadratic ring **before** taking a residue; the remaining denominator is inverted only for units. At this precision the *raw* defect is not additive:

\[
d(xy)=d(x)+d(y)+5d(x)d(y)\pmod{25}.
\]

But the corrected two-digit logarithm

\[
\boxed{L(z)=d(z)-15d(z)^2\pmod{25}}
\]

satisfies \(L(xy)=L(x)+L(y)\), \(L(-z)=L(z)\), and commutes with conjugation. Here \(15=5/2\bmod25\). A narrow Lean theorem checks the **exact polynomial remainder** underlying this modular identity; it does not formalize the quadratic-field interpretation.

Exhaustive tests on \(D=163\) (class number one), \(D=183\) (class number eight), and \(D=187\) (class number two) check **15,000 local units per field**, **7,500 signed ray125 classes per field**, 625 two-digit wild coordinates above each exact nonzero mod5 residue, and **150,000 multiplicative identity checks per field**. The nonzero \(5d(x)d(y)\) correction has explicit witnesses in all three fields.

\[
(\mathcal O_D/125)^\times/\{\pm1\}
\cong C_{12}\times(\mathbb Z/25)^2.
\]

When 2 is inert, the signed **conductor-250** local ray group includes its \(\mathbb F_4^\times\cong C_3\) factor: \(3\times7500=22,500\) classes. The structure is local and cannot by itself detect class number.

## The same original Gram, one more digit deep

This time the target is the literal original Lean integer-order source in \(\mathbb Z[\sqrt{-163}]\), NOT the maximal order:

- Original \(\rho=21\), \(Q=109\), \(R=40\), \(S=J=1\), and trace pairing \(2(ac+163bd)\)
- Exactly 15 integral Frobenius-25 row shears \(Z^r-Z^{r-24}\), \(r=25,\dots,39\)
- Raw source evaluated modulo 125, followed by the **exact division by 5**, yielding 40 primitive rows modulo 25

The tagged unit ray125 classes recover both signed original generator residues modulo125. The nonunits require a separate first lift \(u=z/5\pmod{25}\), rather than an invented unit tag. A completely separate native integer-pair evaluator checks the resulting 8,720 source coordinates and all 1,600 primitive Gram entries modulo25.

At the GLOBAL level, h1 \(D=163\) admits full maximal-order ideal convolution. The conductor250 representation retains the mod2 class, and multiplication is performed **before** the original-order selection:

~~~mermaid
flowchart TD
    M["Maximal-order h1 ideal norm shells"] --> C["Conductor250 signed rays<br/>22,500 possible classes"]
    C -->|"Full coprime convolution"| G["Global ray distributions"]
    G -->|"Odd norms: F4 residue = 1"| O["Original integer-order unit counts"]
    E["Even-norm 2-divisible original elements"] --> O
    N["5-divisible source observations<br/>u = z / 5 mod25"] --> P["Original primitive Gram mod25"]
    O -->|"Signed unit ray125 reconstruction"| P
    P -. "additional uniform determinant mass not established" .-> H["Open tenth-discriminant theorem"]
~~~

Hosted arithmetic CI verified **177** independent ideal norm-shell counts and **270 full conductor250 coprime convolution identities**, then retained 26 odd-norm and 24 even-norm selected original principal ideals plus nine 5-divisible observations. The original primitive Gram agrees in every one of its **1,600 entries modulo25**; its rank modulo5 remains23.

## Why the first-level 78 moments are insufficient

There is a direct, bounded non-field-source-pair example in the SAME residue algebra:

\[
z_1=1,\qquad z_2=26.
\]

They have identical signed conductor25 data (same tame residue and same first wild logarithm mod5). Their signed primitive Gram contributions agree modulo5. But their conductor125 logarithms differ, and their **mod25** primitive Gram contributions differ: the first unequal cell is \((0,26)\), by \(5\).

These are formal local residues, not two elements of the fixed original \(Q_{109}\) norm ball. The witness says precisely that the Phase314 78-coordinate mod5 quotient cannot be assumed sufficient for the next source digit; it does **not** produce an additional valuation or distinguish class numbers.

## What survives and what does not

**[P-paper]** The twisted defect product and corrected log law modulo25, conditional on the inert quadratic unit ring. The exact polynomial remainder has a narrow Lean check.

**[M]** Finite original-source Gram reconciliation, exhaustive 7,500-class enumerations and conductor250 ray-shell controls, with the exact CI head recorded in PR #207.

**[H]** Derive a *uniform class-number-one-only* relation on native large-field ray moments that forces extra primitive Gram valuation **beyond** the existing source-weight filtration.

**[R]** The raw depth2 defect is additive; the original 78 wild moments modulo5 recover the full primitive Gram modulo25; local unit structure diagnoses class number.

The earlier counterworlds remain mandatory: \(D=163\) (h1) and \(D=183\) (h8) share the matched exact integer-source \(v_5=77\) at \(R40/Q109\); \(D=187\) (h2) shares inert2/inert5 local ray structure but fails principal ideal convolution at \(11\cdot17=187\). No change to the global cutoff, no claim of physical quantum effects, and no independent mathematical peer review.
