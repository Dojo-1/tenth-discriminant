"""Typed fuzzy routing, empirical Z+ summaries and exact witness checking.

This module never uses a membership or probability as a proof of nonvanishing.
Run benchmark.py for the frozen, paired experiment. Python >= 3.10, SymPy 1.14.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Sequence
import hashlib
import json
import sympy as sp

Z, W = sp.symbols('Z W')


def canonical(f: sp.Expr) -> str:
    return sp.srepr(sp.Poly(f, Z, W, domain=sp.QQ).as_expr())


@dataclass(frozen=True)
class Target:
    """Witness identity includes the polynomial, coefficient field and matrix size."""
    polynomial: str
    degree: int
    field: str = 'Q'
    convention: str = 'fixed-ascending-F-then-derivative'
    normalization: str = 'unscaled-determinant'

    @classmethod
    def of(cls, f: sp.Expr, a: int) -> 'Target':
        actual = sp.Poly(f, Z).degree()
        if actual != a or a < 1:
            raise ValueError(f'exact global degree required: declared {a}, actual {actual}')
        return cls(canonical(f), a)

    @property
    def digest(self) -> str:
        return hashlib.sha256(json.dumps(self.__dict__, sort_keys=True).encode()).hexdigest()


@dataclass(frozen=True)
class Witness:
    target: Target
    point: Q
    determinant: Q
    provenance: str


def verify_nonzero_witness(f: sp.Expr, witness: Witness) -> bool:
    """Concrete exact check; ordinary resultant is computed BEFORE specialization.

    Derivative block sizes a and a-1 have even product, so the fixed ascending
    coefficient-map determinant agrees with this resultant convention.
    Does not claim equivalence with Lean for arbitrary inputs.
    """
    if Target.of(f, witness.target.degree) != witness.target:
        raise ValueError('witness target mismatch')
    exact = Q(sp.resultant(f, sp.diff(f, Z), Z).subs(W, sp.Rational(witness.point)))
    return exact == witness.determinant and exact != 0


def memberships(coefficients: Sequence[Q]) -> tuple[Q, Q, Q]:
    """Overlapping, rational memberships; scalar-rescaling invariant.

    Polynomial coordinate changes need not preserve these routing features.
    The all-zero specialization is retained and has well-defined memberships.
    """
    if not coefficients:
        raise ValueError('empty coefficient vector')
    height = max(abs(c) for c in coefficients)
    lead = abs(coefficients[-1]) / height if height else Q(0)
    const = abs(coefficients[0]) / height if height else Q(0)
    raw = (1 / (1 + 4*lead), 1 / (1 + 4*const), Q(1))
    total = sum(raw)
    return tuple(x/total for x in raw)


@dataclass(frozen=True)
class EmpiricalLocalModel:
    mass: tuple[Q, Q, Q]
    success: tuple[Q, Q, Q]
    source: str

    @classmethod
    def fit(cls, observations: Sequence[tuple[Sequence[Q], bool]], source: str):
        mass, success = [Q(0)]*3, [Q(0)]*3
        for coefficients, passed in observations:
            for i, weight in enumerate(memberships(coefficients)):
                mass[i] += weight
                success[i] += weight*int(passed)
        if any(v == 0 for v in mass):
            raise ValueError('empty empirical granule; do not invent a distribution')
        return cls(tuple(mass), tuple(success), source)

    def predict(self, coefficients: Sequence[Q]) -> Q:
        """Routing prediction only. No theorem-certification authority."""
        return sum(mu*s/m for mu,s,m in zip(memberships(coefficients),self.success,self.mass))


def order_candidates(policy: str, rows: Sequence[Sequence[Q]], model: EmpiricalLocalModel) -> list[int]:
    if policy == 'fixed':
        return list(range(len(rows)))
    if policy == 'crisp':
        score = lambda row: int(row[-1] != 0) + int(row[0] != 0)
    elif policy == 'fuzzy':
        score = lambda row: memberships(row)[2]
    elif policy == 'blend':
        score = model.predict
    else:
        raise ValueError('unknown policy')
    return sorted(range(len(rows)), key=lambda i: (-score(rows[i]), i))


@dataclass(frozen=True)
class Enclosure:
    """Exact interval for the SAME named scalar; sources are not independent votes."""
    target: str
    lower: Q
    upper: Q
    provenance: str

    def validate(self):
        if self.lower > self.upper:
            raise ValueError('reversed enclosure')


def blend_enclosures(records: Sequence[Enclosure], weights: Sequence[Q]) -> Enclosure:
    """Conditional composition: validity of each input enclosure is external.

    Type/shape checks cannot establish that supplied input bounds are sound.
    Only verified certificates should be passed by an application.
    """
    if not records or len(records) != len(weights):
        raise ValueError('empty or mismatched blend')
    if any(w < 0 for w in weights) or sum(weights) <= 0:
        raise ValueError('weights must be nonnegative with positive total')
    active = [(r,w) for r,w in zip(records,weights) if w > 0]
    target = active[0][0].target
    for r,w in active:
        r.validate()
        if r.target != target:
            raise ValueError('different targets/domains/units must not be averaged')
    total = sum(weights)
    return Enclosure(target, sum(w*r.lower for r,w in active)/total,
                     sum(w*r.upper for r,w in active)/total,
                     'conditional-blend:' + '|'.join(sorted({r.provenance for r,w in active})))


def intersect_enclosures(records: Sequence[Enclosure]) -> Enclosure:
    if not records:
        raise ValueError('uncovered target')
    target = records[0].target
    for r in records:
        r.validate()
        if r.target != target:
            raise ValueError('target mismatch')
    out = Enclosure(target, max(r.lower for r in records), min(r.upper for r in records),
                    'intersection:' + '|'.join(sorted({r.provenance for r in records})))
    out.validate()
    return out


def empirical_zplus(costs: Sequence[int], budget: int) -> dict:
    """Fuzzy event 'cheap successful certificate' and empirical cost distribution.

    X=probe count on success; X=budget+1 on budget failure, explicitly penalized.
    A(x)=max(0,min(1,(4-x)/3)). No assertion about future tasks or theorem truth.
    """
    if not costs or any(c < 1 or c > budget+1 for c in costs):
        raise ValueError('invalid operational sample')
    support = sorted(set(costs))
    pmf = {c: Q(costs.count(c),len(costs)) for c in support}
    membership = {c: max(Q(0), min(Q(1), Q(4-c,3))) for c in support}
    return {'variable':'penalized probes to first exact nonzero witness',
            'population':'declared finite test suite; empirical, not predictive calibration',
            'n':len(costs), 'failure_value':budget+1,
            'pmf':{str(c):str(p) for c,p in pmf.items()},
            'membership':{str(c):str(membership[c]) for c in support},
            'fuzzy_event_mass':str(sum(pmf[c]*membership[c] for c in support))}
