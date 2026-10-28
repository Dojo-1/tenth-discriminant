"""One sealed scalar feasibility experiment, not a field/cutoff proof."""
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction
from pathlib import Path
import decimal
import hashlib
import json
import sys
import time

GRID = list(range(36, 66, 2)) + [80, 96, 128]
PRECISIONS = [100, 200]
PRECISION = 100


def rounded(operation, direction):
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = direction
        return operation()


class Interval:
    def __init__(self, lo, hi=None):
        self.lo = lo if isinstance(lo, Decimal) else Decimal(lo)
        self.hi = self.lo if hi is None else (hi if isinstance(hi, Decimal) else Decimal(hi))
        assert self.lo.is_finite() and self.hi.is_finite() and self.lo <= self.hi

    @staticmethod
    def coerce(other):
        return other if isinstance(other, Interval) else Interval(other)

    def __add__(self, other):
        other = self.coerce(other)
        return Interval(rounded(lambda: self.lo + other.lo, ROUND_FLOOR),
                        rounded(lambda: self.hi + other.hi, ROUND_CEILING))

    __radd__ = __add__

    def __neg__(self):
        return Interval(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        pairs = [(x, y) for x in [self.lo, self.hi] for y in [other.lo, other.hi]]
        return Interval(min(rounded(lambda: x * y, ROUND_FLOOR) for x, y in pairs),
                        max(rounded(lambda: x * y, ROUND_CEILING) for x, y in pairs))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        assert other.hi < 0 or other.lo > 0, 'division interval contains zero'
        pairs = [(x, y) for x in [self.lo, self.hi] for y in [other.lo, other.hi]]
        return Interval(min(rounded(lambda: x / y, ROUND_FLOOR) for x, y in pairs),
                        max(rounded(lambda: x / y, ROUND_CEILING) for x, y in pairs))

    def __rtruediv__(self, other):
        return self.coerce(other) / self

    def transcendental(self, method):
        assert self.lo > 0 if method == 'ln' else self.lo >= 0
        # Decimal's ln/sqrt are correctly rounded half-even. An adjacent
        # representable value on either side encloses the exact endpoint.
        with localcontext() as ctx:
            ctx.prec = PRECISION
            ctx.rounding = ROUND_HALF_EVEN
            a = getattr(self.lo, method)()
            b = getattr(self.hi, method)()
            return Interval(a.next_minus(context=ctx), b.next_plus(context=ctx))

    def contains(self, other):
        other = self.coerce(other)
        return self.lo <= other.lo and other.hi <= self.hi

    def classification(self):
        return 'positive' if self.lo > 0 else ('negative' if self.hi < 0 else 'unresolved')

    def record(self):
        return {'lo': str(self.lo), 'hi': str(self.hi)}


def envelope(d):
    d = Interval(d)
    u = d.transcendental('ln')
    root = d.transcendental('sqrt')
    fourth = root.transcendental('sqrt')
    base = (4 / root + 1 / fourth) * (2 + u * (1 + u))
    h = base + Interval(1) / 3
    margin = Interval('0.159997') * u - Interval('4.926') - h
    return u, root, fourth, base, h, margin


def controls():
    third = Interval(1) / 3
    u, root, fourth, base, h, margin = envelope(2**36)
    tests = {
        'rational_third': Fraction(third.lo) <= Fraction(1, 3) <= Fraction(third.hi),
        'sqrt_four': Interval(4).transcendental('sqrt').contains(2),
        'log_one': Interval(1).transcendental('ln').contains(0),
        'log_four_contains_twice_log_two': Interval(4).transcendental('ln').contains(2 * Interval(2).transcendental('ln')),
        'positive_sign': Interval(1).classification() == 'positive',
        'negative_sign': Interval(-1).classification() == 'negative',
        'zero_straddling_sign': Interval(-1, 1).classification() == 'unresolved',
        'constant_mutation_detected': (h - base).contains(third) and base.hi < h.lo,
    }
    assert all(tests.values()), tests
    return tests


def main():
    global PRECISION
    started = time.perf_counter()
    result = {
        'phase': 85, 'scope': 'sealed scalar feasibility only; not an all-D or field cutoff proof',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python': sys.version, 'libmpdec': decimal.__libmpdec_version__,
        'grid_N': GRID, 'precisions': {},
        'formula': '(.159997*ln(D)-4.926)-((4/sqrt(D)+1/sqrt(sqrt(D)))*(2+ln(D)*(1+ln(D)))+1/3)',
    }
    intervals = {}
    for precision in PRECISIONS:
        PRECISION = precision
        tests = controls()
        samples = []
        for n in GRID:
            d = 2**n
            values = envelope(d)
            keys = ['logD', 'sqrtD', 'fourthRootD', 'without_constant', 'H', 'margin']
            row = {'N': n, 'D': str(d), 'R': str(d // 4), 'S': str((d // 4) // 25),
                   **{key: value.record() for key, value in zip(keys, values)},
                   'classification': values[-1].classification()}
            intervals[precision, n] = dict(zip(keys, values))
            samples.append(row)
        result['precisions'][str(precision)] = {'controls': tests, 'samples': samples,
            'first_positive_N': next((row['N'] for row in samples if row['classification'] == 'positive'), None)}
    nesting = {}
    for n in GRID:
        nesting[str(n)] = all(intervals[100, n][key].contains(value)
                             for key, value in intervals[200, n].items())
    assert all(nesting.values()), nesting
    result['precision_nesting'] = nesting
    result['elapsed_seconds'] = time.perf_counter() - started
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
