# 侘未来 · Phase332
## A second horizontal binary scale

> The seam is not discarded. It becomes another integral null direction.

**Research-only.** This dossier records a stronger mixed basis candidate for
the original ordinary-\(Z\)-jet trace Gram. It is *not* a proof of a smaller
discriminant cutoff. Phase331's \(315^4\) source/field proof is a separate
exact-head validation target.

### The original rectangle survives

Let \(R,S>0\), \(0\le r<R\), \(0\le s<S\).
Define
\[
 b_{r,s}=\min\left(\left\lfloor\frac r2\right\rfloor,
                  \left\lfloor\frac{S-1-s}{2}\right\rfloor\right),\quad
 k_{r,s}=\left\lfloor\frac{r-2b_{r,s}}4\right\rfloor,\quad
 c_s=\left\lfloor\frac s4\right\rfloor.
\]
The proposed basis is
\[
 P_{r,s}(Z,W)=
 Z^{r-4k_{r,s}-2b_{r,s}}\,
 W^{s-4c_s}\,
 (Z^4-Z^2)^{k_{r,s}}\,
 (Z^2-W^2)^{b_{r,s}}\,
 (W^4-W^2)^{c_s}.
\]
All exponents are nonnegative. The monomial \(Z^rW^s\) occurs with
coefficient **one**. A nonleading term has exponents
\[
  (r-2t-2u,\ s+2u-2v),
 \qquad 0\le t\le k,\quad 0\le u\le b,\quad 0\le v\le c.
\]
The guards make both coordinates valid original columns:
\(r-2t-2u\ge0\) and \(0\le s+2u-2v<S\).
For any nonleading term, either \(r\) strictly decreases, or \(r\)
stays fixed while \(s\) strictly decreases. Thus the proposed entire
\(RS\times RS\) coefficient matrix is lower triangular with diagonal
one. A universal Lean proof of this exact matrix is **still open**.

### Why the factor is genuinely source-null

For every original integer-pair sample
\(z=x+y\sqrt{-D}\), \(w=\bar z=x-y\sqrt{-D}\), with
ordinary derivatives in \(Z\) and \(W\) held fixed,
\[
H(z,w)=z^2-w^2=4xy\sqrt{-D},\quad
\partial_Z H=2z,\quad \partial_Z^2H=2,\quad
\partial_Z^jH=0\ (j>2).
\]
Every ordinary-\(Z\) derivative of \(H\) is divisible by two
in the original quadratic order. The same source all-jet property is
already available for \(F(Z)=Z^4-Z^2\); \(F(W)\) is constant under
ordinary-\(Z\) differentiation and has even value.
The existing mixed-jet Leibniz lemma predicts:
\[
 2^{k_{r,s}+b_{r,s}+c_s}\mid
 \left.\partial_Z^j P_{r,s}(Z,W)\right|_{Z=z,W=w}
 \quad\text{for every }j\ge0.
\]
The crucial remaining obligation is one combined **source-typed**
integer row action, rather than multiplying overlapping Gram divisors.

### A positive combinatorial gain

Compared with Phase331's bidirectional exponent
\(\lfloor r/4\rfloor+\lfloor s/4\rfloor\), the mixed candidate satisfies
\[
 \left\lfloor\frac{r-2b}{4}\right\rfloor+b
   -\left\lfloor\frac r4\right\rfloor
 \ \ge\ \left\lfloor\frac b2\right\rfloor\ge0.
\]
If \(R\ge S-1\), then for each row with \(r\ge S-1\):
\[
 b=\left\lfloor\frac{S-1-s}{2}\right\rfloor,\qquad
 \left\lfloor\frac b2\right\rfloor=
 \left\lfloor\frac{S-1-s}{4}\right\rfloor.
\]
Summing the source rectangular row indices therefore gives the
proposed **additional** exponent budget
\[
 \boxed{(R-S+1)\sum_{t=0}^{S-1}\left\lfloor\frac t4\right\rfloor}.
\]
This would add a second horizontal-scale binary valuation to the
unchanged original Gram, if the universal joint-source row-action and
Gram-factor proof close. The extra normalized mass has leading size
approximately \((1-S/R)(S/(4R))\log2\), about \(0.00665\)
for the current aspect ratio, rather than another decorative frame
operation.

### Evidence ledger

- **P (previously checked, imported source):** all-order null jets for
  \(F(Z)\), \(H(Z,W)\), and the conjugate \(F(W)\); the generic trace-Gram
  divisor theorem
- **M (this phase):** five exact Python tests passed; 80,000 original
  ordinary-jet evaluations, source rectangle/triangularity,
  improved exponents and a negative quadratic \(W^2-W\) control
- **H (not proved):** complete universal unimodular matrix, universal
  joint original-jet divisibility, determinant divisor, and a
  strengthened normalized field lower
- **H (future endpoint):** \(313^4\) is a plausible next *target*, not
  a claimed result; the entire 313-domain geometry and Hadamard bound
  must be re-established from their own guards
- **R (excluded shortcut):** multiplying independent 2-adic divisors,
  replacing ordinary derivatives by W-derivatives, changing source Q,
  or promoting finite tests to a global determinant theorem

**Implementation:** [exact bounded pilot](mixed_binary_increasing.py).
**Verification:** [Phase332 GitHub Actions](../../.github/workflows/phase332-mixed-binary.yml).

> A new direction earns its place only when its source map, inverse
> determinant, remainder, and arithmetic payoff all close.
