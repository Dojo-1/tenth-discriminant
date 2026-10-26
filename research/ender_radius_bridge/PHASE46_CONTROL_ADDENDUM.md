# Fixed squarefree-guard counterexample, registered before its check

The main fixed constructor/transport target is accepted after one arity
repair: attempt1 FAIL69.393486s, attempt2 PASS24.5086311s. Its statements,
parameters and resource cap did not change. The first source snapshot and
all raw records remain preserved. This addendum changes no main proof.

Add one exact control to the fresh input checker, before its first run:
in the actual canonical field at d=1, take a=1000000*sqrt(-1) and
D=1000000000000. Verify a^2+D=0, degree two and actual class number one,
but D is not squarefree and D<100000000000 is false. Thus the public bound
cannot drop its squarefree premise merely because a root and degree two
have been supplied. This is a predetermined algebraic counterexample,
not a numerical pilot, parameter search or stronger analytic bound.

Use the existing root-square theorem, checked d=1 positive case, exact
integer arithmetic and the unchanged180s/8192MB input-check cap. Keep
the control OUTSIDE the library and outside the transported-bound proof
inputs. No new main build attempt or semantic change is authorized.
Preserve any elaboration failure; do not replace the witness to get PASS.
