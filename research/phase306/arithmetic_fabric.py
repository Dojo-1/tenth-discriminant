#!/usr/bin/env python3
"""Phase306: exact typed arithmetic Worldlets and transport tests.

Not a physical quantum computer, conscious AI, gerbe classification,
or new number-field discriminant bound. All calculations use Python integers.
"""
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations


class TransportError(ValueError):
    pass


class GluingObstruction(TransportError):
    pass


class PromotionDenied(PermissionError):
    pass


def matrix(rows):
    out = tuple(tuple(int(x) for x in row) for row in rows)
    if not out or not out[0] or any(len(row) != len(out[0]) for row in out):
        raise TransportError("nonrectangular or empty matrix")
    return out


def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def transpose(a):
    return matrix(zip(*a))


def mmul(a, b):
    a, b = matrix(a), matrix(b)
    if len(a[0]) != len(b):
        raise TransportError("matrix types/shapes mismatch")
    t = transpose(b)
    return matrix([[sum(x * y for x, y in zip(row, col)) for col in t]
                   for row in a])


def matvec(a, x):
    a = matrix(a)
    if len(a[0]) != len(x):
        raise TransportError("vector rank mismatch")
    return tuple(sum(t * y for t, y in zip(row, x)) for row in a)


def mod_matrix(a, modulus):
    if modulus <= 1:
        raise TransportError("invalid precision")
    return matrix([[x % modulus for x in row] for row in a])


def det(a):
    a = matrix(a)
    n = len(a)
    if any(len(row) != n for row in a):
        raise TransportError("determinant needs square matrix")
    if n == 1:
        return a[0][0]
    m = [list(row) for row in a]
    prev = 1
    sign = 1
    for k in range(n - 1):
        if m[k][k] == 0:
            l = next((i for i in range(k + 1, n) if m[i][k] != 0), None)
            if l is None:
                return 0
            m[l], m[k] = m[k], m[l]
            sign *= -1
        pivot = m[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = m[i][j] * pivot - m[i][k] * m[k][j]
                if numerator % prev:
                    raise ArithmeticError("nonexact Bareiss division")
                m[i][j] = numerator // prev
            m[i][k] = 0
        prev = pivot
    return sign * m[-1][-1]


def inverse_unimodular(a):
    a = matrix(a)
    n = len(a)
    if len(a[0]) != n or abs(det(a)) != 1:
        raise TransportError("only integral unimodular gauges allowed")
    augmented = [[Fraction(v) for v in row] +
                 [Fraction(int(i == j)) for j in range(n)]
                 for i, row in enumerate(a)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if augmented[i][k]), None)
        if pivot is None:
            raise TransportError("singular frame")
        augmented[k], augmented[pivot] = augmented[pivot], augmented[k]
        u = augmented[k][k]
        augmented[k] = [x / u for x in augmented[k]]
        for i in range(n):
            if i != k:
                u = augmented[i][k]
                augmented[i] = [x - u * y for x, y in
                                zip(augmented[i], augmented[k])]
    candidate = tuple(tuple(v for v in row[n:]) for row in augmented)
    if any(v.denominator != 1 for row in candidate for v in row):
        raise TransportError("nonintegral inverse")
    inv = matrix([[int(v) for v in row] for row in candidate])
    if mmul(a, inv) != eye(n) or mmul(inv, a) != eye(n):
        raise ArithmeticError("failed integral inverse verification")
    return inv


def omega_mul(x, y, d=203):
    """Ring of integers of Q(sqrt(-d)), omega^2=omega-(d+1)/4."""
    if d % 4 != 3:
        raise TransportError("maximal omega coordinates require d=3 mod4")
    a, b = x
    c, e = y
    m = (d + 1) // 4
    return a * c - m * b * e, a * e + b * c + b * e


def omega_norm(z, d=203):
    a, b = z
    return a * a + a * b + ((d + 1) // 4) * b * b


def omega_pow(z, n, d=203):
    v = (1, 0)
    for _ in range(n):
        v = omega_mul(v, z, d)
    return v


def exact_original_jet_rows(points, degrees=(0, 1, 2), jets=2, d=203):
    """Monomials Z^r; ordinary derivative with W fixed, both omega coords."""
    rows = []
    for r in degrees:
        row = []
        for j in range(jets):
            for z in points:
                if j > r:
                    row.extend((0, 0))
                else:
                    power = omega_pow(z, r - j, d)
                    falling = 1
                    for t in range(j):
                        falling *= r - t
                    row.extend((falling * power[0], falling * power[1]))
        rows.append(row)
    return matrix(rows)


def actual_d203_points():
    """Six ACTUAL points of the unchanged rho=24 maximal-order norm ball."""
    points = ((0, 0), (1, 0), (0, 1), (1, 1), (-1, 1), (2, 0))
    assert len(set(points)) == 6
    assert all(omega_norm(z, 203) <= 24**2 for z in points)
    return points


def trace_gram(e, d=203):
    """Original hermitian trace form B_omega=[[2,1],[1,(d+1)/2]]."""
    e = matrix(e)
    if len(e[0]) % 2 or d % 4 != 3:
        raise TransportError("invalid observation channel or discriminant")
    m = (d + 1) // 2
    out = []
    for x in e:
        row = []
        for y in e:
            value = sum(2 * x[k] * y[k] + x[k] * y[k + 1] +
                        x[k + 1] * y[k] + m * x[k + 1] * y[k + 1]
                        for k in range(0, len(x), 2))
            row.append(value)
        out.append(row)
    return matrix(out)


@dataclass(frozen=True)
class Cage:
    """Nested arithmetic context, not a claim about a model's hidden state."""
    field_d: int
    p: int
    k: int
    source_id: str

    def __post_init__(self):
        if self.field_d <= 0 or self.p < 2 or self.k < 1 or not self.source_id:
            raise TransportError("invalid cage coordinates")

    @property
    def modulus(self):
        return self.p ** self.k


def transport_functor(u, e, cage, other=None):
    if other is not None and cage != other:
        raise TransportError("cage mismatch: field/prime/precision/source")
    if abs(det(u)) != 1:
        raise TransportError("not an integral frame")
    a = mod_matrix(mmul(u, e), cage.modulus)
    b = mod_matrix(mmul(mod_matrix(u, cage.modulus),
                         mod_matrix(e, cage.modulus)), cage.modulus)
    return a, b


def gram_covariance(u, e):
    if abs(det(u)) != 1:
        raise TransportError("not unimodular")
    old = trace_gram(e)
    moved = trace_gram(mmul(u, e))
    predicted = mmul(mmul(u, old), transpose(u))
    return moved, predicted, det(old), det(moved)


def symplectic_form(n):
    return matrix([[0 if i < n and j < n else
                    1 if i < n and j == i + n else
                    -1 if i >= n and j == i - n else 0
                    for j in range(2 * n)] for i in range(2 * n)])


def block_diag(a, b):
    a, b = matrix(a), matrix(b)
    return matrix([list(row) + [0] * len(b[0]) for row in a] +
                  [[0] * len(a[0]) + list(row) for row in b])


def cotangent_lift(u):
    u = matrix(u)
    return block_diag(u, transpose(inverse_unimodular(u)))


def symplectic_defect(lift, modulus):
    n2 = len(lift)
    if n2 % 2:
        raise TransportError("symplectic rank must be even")
    j = symplectic_form(n2 // 2)
    left = mmul(mmul(transpose(lift), j), lift)
    return mod_matrix(matrix([[left[i][k] - j[i][k] for k in range(n2)]
                              for i in range(n2)]), modulus)


def dual_pair(q, pi, modulus):
    if len(q) != len(pi):
        raise TransportError("dual pairing rank mismatch")
    return sum(a * b for a, b in zip(q, pi)) % modulus


def alternator(x, y, p):
    if len(x) != len(y) or len(x) % 2:
        raise TransportError("phase ranks mismatch")
    n = len(x) // 2
    return sum(x[i] * y[n + i] - x[n + i] * y[i]
               for i in range(n)) % p


def phase_cocycle(x, y, p=5):
    if p % 2 == 0:
        raise TransportError("requires odd prime")
    return (pow(2, -1, p) * alternator(x, y, p)) % p


def phase_add(x, y, p=5):
    if len(x) != len(y):
        raise TransportError("phase ranks mismatch")
    return tuple((a + b) % p for a, b in zip(x, y))


def heisenberg_product(a, b, p=5):
    x, t = a
    y, u = b
    return (phase_add(x, y, p), (t + u + phase_cocycle(x, y, p)) % p)


def cocycle_defect(x, y, z, p=5):
    """Group 2-cocycle condition: c(x,y)+c(x+y,z)=c(y,z)+c(x,y+z)."""
    return (phase_cocycle(x, y, p) +
            phase_cocycle(phase_add(x, y, p), z, p) -
            phase_cocycle(y, z, p) -
            phase_cocycle(x, phase_add(y, z, p), p)) % p


@dataclass(frozen=True)
class LocalSection:
    modulus: int
    observations: tuple  # ((point_id, value_mod_modulus), ...) pairs

    def __post_init__(self):
        if self.modulus <= 1:
            raise TransportError("invalid residue modulus")
        keys = [k for k, _ in self.observations]
        if len(set(keys)) != len(keys):
            raise TransportError("duplicate point in patch")
        if any(not 0 <= v < self.modulus for _, v in self.observations):
            raise TransportError("noncanonical residue")


def glue_sections(sections, universe):
    if not sections:
        raise GluingObstruction("empty cover")
    modulus = sections[0].modulus
    assembled = {}
    for section in sections:
        if section.modulus != modulus:
            raise GluingObstruction("incompatible fibers/precisions")
        for key, value in section.observations:
            if key not in universe:
                raise GluingObstruction("point outside actual source")
            if key in assembled and assembled[key] != value:
                raise GluingObstruction("overlap contradiction at " + str(key))
            assembled[key] = value
    if set(assembled) != set(universe):
        raise GluingObstruction("cover omits actual source points")
    return assembled


@dataclass(frozen=True)
class CRTReconstruction:
    residue: int
    modulus: int
    remainder_type: str = "unknown-integer-multiple-of-modulus"


def crt_pair(a, m, b, n):
    if m < 2 or n < 2:
        raise TransportError("invalid moduli")
    try:
        inv = pow(m, -1, n)
    except ValueError as err:
        raise TransportError("non-coprime chart moduli") from err
    residue = (a + m * (((b - a) * inv) % n)) % (m * n)
    return CRTReconstruction(residue, m * n)


@dataclass(frozen=True)
class Claim:
    claim_id: str
    author: str
    status: str
    kind: str
    source_sha: str


@dataclass(frozen=True)
class Attestation:
    reviewer: str
    mode: str
    evidence_uri: str


def promote_proved(claim, witness):
    if claim.status == "P":
        raise PromotionDenied("already proved; cannot self-relabel")
    if claim.kind != "formal_theorem":
        raise PromotionDenied("source experiments are not theorems")
    if claim.author == witness.reviewer:
        raise PromotionDenied("self-promotion: same author/reviewer")
    if witness.mode != "formal_kernel" or not witness.evidence_uri:
        raise PromotionDenied("external proof term and checker receipt required")
    # This function enforces a policy; it DOES NOT verify a proof or the receipt.
    return Claim(claim.claim_id, claim.author, "P", claim.kind, claim.source_sha)


class ContextTree:
    """Exact metric tree (0-hyperbolic), for project-context organization only."""

    def __init__(self, parents):
        self.parents = dict(parents)
        for node in self.parents:
            if node == self.parents[node]:
                raise TransportError("self-parent")
            self.ancestors(node)

    def ancestors(self, node):
        if node not in self.parents:
            raise TransportError("unknown context node")
        path = []
        seen = set()
        while node is not None:
            if node in seen or node not in self.parents:
                raise TransportError("cycle or missing context parent")
            seen.add(node)
            path.append(node)
            node = self.parents[node]
        return path

    def distance(self, a, b):
        pa = self.ancestors(a)
        pb = self.ancestors(b)
        common = set(pa) & set(pb)
        if not common:
            raise TransportError("different disconnected context trees")
        return min(pa.index(z) + pb.index(z) for z in common)

    def four_point_defect(self, a, b, c, d):
        sums = sorted([self.distance(a, b) + self.distance(c, d),
                       self.distance(a, c) + self.distance(b, d),
                       self.distance(a, d) + self.distance(b, c)])
        return sums[2] - sums[1]


def fixed_context_tree():
    return ContextTree({
        "repo": None,
        "field.D203": "repo",
        "field.D163": "repo",
        "local.p5": "field.D203",
        "precision.k1": "local.p5",
        "precision.k2": "local.p5",
        "source.jets": "precision.k2",
        "proof.claim": "field.D203",
    })


def all_tree_quadruples_zero(tree):
    return all(tree.four_point_defect(*four) == 0
               for four in combinations(tree.parents, 4))
