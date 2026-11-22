#!/usr/bin/env python3
"""Independent integer mirror of FiniteSieveBridge.smallSieveCandidate.

Checks the exact finite candidate identity used in the Phase381 Lean draft.
Does not compile Lean or prove the analytic 652 cutoff.
"""
BASE_PRIMES = (3,5,7,11,13,17,19,23)
NINE_RADICANDS = (1,2,3,7,11,19,43,67,163)


def modular_root(d, p):
    return any((r*r+d)%p == 0 for r in range(p))


def source_candidate(d):
    return d in (1,2,3,7) or (
        d%8 == 3 and all(4*p>d or not modular_root(d,p) for p in BASE_PRIMES)
    )


def main():
    finite=tuple(d for d in range(653) if source_candidate(d))
    assert finite == NINE_RADICANDS
    assert not source_candidate(58)
    assert source_candidate(10987)
    assert (2*2+10987)%29 == 0
    assert next(d for d in range(164,20000) if source_candidate(d)) == 10987
    discr=sorted((d if d%4 == 3 else 4*d) for d in finite)
    assert discr == [3,4,7,8,11,19,43,67,163]
    print("SOURCE MIRROR PASS: 653 inputs, 9 radicands, 9 actual discriminants")
    print("RANGE GUARD: first false positive beyond 163 is 10987, split at 29")


if __name__=="__main__":
    main()
