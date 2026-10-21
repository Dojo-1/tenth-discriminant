"""Elementary factorial replacement for BEAN's prime-distribution input.

See flow/PREREG_ENDER.txt and ledger/ender.txt for derivations and scope.
No prime-distribution estimates are imported or used.
"""
import argparse
import functools
from fractions import Fraction

from flint import arb, ctx

from green_h1 import F_exact, primes_upto
from green_h1_ellipse import upper_B


P = 10000
CS = (20, 40, 80, 160)


def floor_sum(R, q):
    k, m = divmod(R, q)
    return q * k * (k - 1) // 2 + k * m


def factorial_lower(R):
    n = arb(R - 1)
    return n * n / 2 * n.log() - 3 * n * n / 4 + n / 2 + arb(1) / 4


def tail_integral(P):
    return arb(P + 1).log() / P + (arb(1) + arb(1) / P).log()


@functools.lru_cache(maxsize=1)
def small_primes():
    return tuple(int(p) for p in primes_upto(P))


def prime_mass(R, S):
    if not (R >= 2 and 2 <= S <= R and P * S >= R):
        raise ValueError("need R>=S>=2 and P>=R/S")
    small, exact = arb(0), arb(0)
    for p in small_primes():
        lp = arb(p).log()
        q = p
        while q < R:
            small += lp * floor_sum(R, q)
            q *= p
        if p > 2:
            exact += lp * F_exact(p, R, S)
    V = R * (R - 1) // 2
    W = R * (R - 1) * (2 * R - 1) // 6
    I = tail_integral(P)
    tail = (arb(S) - arb(1) / 2) * (factorial_lower(R) - small - V * I) - W * I / 2
    return 2 * (exact + tail) if tail > 0 else 2 * exact


def radius_for(D, R, S):
    target = arb("1.001") * ((arb(3 * R + S) * arb(D).sqrt()) / arb.pi()).sqrt() + 10 * arb(D).sqrt()
    radius = int(target.upper().ceil().unique_fmpz())
    if not (arb(radius) >= target and arb(radius) < target + 2):
        raise ArithmeticError("increase Arb precision for radius selection")
    return radius


def certify(D1, D2, C):
    if not (163 < D1 <= D2 and C in CS):
        raise ValueError("need 163<D1<=D2 and a registered C")
    R = D1 // 4
    S = J = R // C
    if S < 2 or P * S < R:
        return False, arb(0)
    radius = radius_for(D2, R, S)
    rho = arb(radius)
    s1, s2 = arb(D1).sqrt(), arb(D2).sqrt()
    n_low = arb.pi() * rho * rho / s2 - 2 * rho / s2 - 6 * rho
    L = 2 * radius + 1
    M = 2 * int((rho / s1).upper().floor().unique_fmpz()) + 1
    if not (n_low > 3 * R + S and J >= L + M):
        return False, arb(0)
    n_up = arb.pi() * rho * rho / s1 + 2 * rho + M
    upper = upper_B(R, S, J, n_up, rho)
    lower = prime_mass(R, S)
    return bool(lower > upper), lower / upper


def cover(start, end, ratio=Fraction(5, 4)):
    if not (163 < start < end and ratio > 1):
        raise ValueError("need 163<start<end and ratio>1")
    count = 0
    while start < end:
        stop = min(end, max(start + 1, start * ratio.numerator // ratio.denominator))
        while True:
            hit = next(((C, margin) for C in CS
                        for ok, margin in [certify(start, stop, C)] if ok), None)
            if hit:
                break
            if stop <= start + 1:
                print(f"FAILED [{start}, {stop}]", flush=True)
                return False
            stop = (start + stop) // 2
        C, margin = hit
        print(f"CERTIFIED [{start}, {stop}] C={C} margin={margin.str(10)}", flush=True)
        count += 1
        start = stop
    print(f"COMPLETE intervals={count} end={end}", flush=True)
    return True


def asymptotic():
    """All D>=10^36: a linear envelope minus decreasing positive errors."""
    C, D0 = 80, 10**36
    d = arb(D0)
    u = d.log()
    I = tail_integral(P)
    B = sum((arb(p).log() / (p - 1) for p in small_primes()), arb(0)) + I
    slope = arb(1) / 4 - arb(5) / (4 * C)
    constant = arb(4).log() + arb(3) / 2 + B + arb(2 * C) * I / 3
    error_lower = (5 + 5 * (2 * u + 2) + 5 * C * u) / d
    error_upper = 5 * (arb(8).log() + 2 * u) / d + arb(2) / C * (5 * d ** (-arb(1) / 4) + 5 * u / d)
    margin = slope * u - constant - error_lower - error_upper
    checks = {
        "rho <= D^(3/4)": arb("1.001") * ((3 + arb(1) / C) / (4 * arb.pi())).sqrt()
        + 10 * d ** (-arb(1) / 4) + 2 * d ** (-arb(3) / 4) < 1,
        "n_lower > 3R+S": arb("0.002001") * 3 / 5 * d ** (arb(1) / 4) > 8,
        "J >= L+M": d ** (arb(1) / 4) > 60 * C,
        "R > rho": d ** (arb(1) / 4) > 5,
        "n_upper < 4D": arb.pi() + 2 * d ** (-arb(1) / 4)
        + 2 * d ** (-arb(3) / 4) + 1 / d < 4,
        "S >= R/(2C), P >= R/S": D0 // 5 >= 2 * C and P >= 2 * C,
        "positive factorial-tail envelope": u - arb(4).log() - 5 / d - arb(3) / 2
        - B - 5 * (2 * u + 2) / d > 0,
        "decreasing u/D errors": u > 1,
    }
    for label, ok in checks.items():
        print(f"{label}: {bool(ok)}")
    print(f"slope={slope.str(12)} margin_at_1e36={margin.str(12)}")
    ok = bool(margin > 0 and slope > 0) and all(checks.values())
    print(f"ENDER ASYMPTOTIC CERTIFIED: {ok}")
    return ok


def integer(value):
    rational = Fraction(value)
    if rational.denominator != 1:
        raise argparse.ArgumentTypeError("expected an exact integer")
    return rational.numerator


if __name__ == "__main__":
    ctx.prec = 160
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    interval = sub.add_parser("cover")
    interval.add_argument("start", type=integer)
    interval.add_argument("end", type=integer)
    interval.add_argument("ratio", type=Fraction, nargs="?", default=Fraction(5, 4))
    sub.add_parser("asymptotic")
    args = parser.parse_args()
    success = asymptotic() if args.command == "asymptotic" else cover(args.start, args.end, args.ratio)
    raise SystemExit(0 if success else 1)
