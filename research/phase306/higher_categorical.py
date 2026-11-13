#!/usr/bin/env python3
"""Phase306-B: genuine Hom-profunctor, finite Cech 2-class and quaternion controls.

The nontrivial H^2 witness lives on an abstract tetrahedral-boundary
simplicial nerve, NOT on an arithmetic scheme or on the sampled D203 source.
"""
from dataclasses import dataclass
from itertools import combinations

from arithmetic_fabric import TransportError, matrix, mmul, transpose, trace_gram


@dataclass(frozen=True)
class HomProfunctorElement:
    """One element of Hom_Z(V,W), contravariant in V, covariant in W."""
    source_rank: int
    target_rank: int
    linear_map: tuple

    def __post_init__(self):
        e = matrix(self.linear_map)
        if len(e) != self.target_rank or len(e[0]) != self.source_rank:
            raise TransportError("Hom-profunctor source/target rank mismatch")

    def pull_push(self, pre, post):
        """f:V'->V and g:W->W', send E to g E f."""
        pre, post = matrix(pre), matrix(post)
        if len(pre) != self.source_rank or len(post[0]) != self.target_rank:
            raise TransportError("profunctor arrow domain/codomain mismatch")
        transformed = mmul(post, mmul(self.linear_map, pre))
        return HomProfunctorElement(len(pre[0]), len(post), transformed)


def swap_complete_observation_points(q_count=6, jets=2, p0=0, p1=1):
    """Isometry of the original repeated trace blocks: swap ENTIRE point fibers."""
    if not 0 <= p0 < q_count or not 0 <= p1 < q_count or p0 == p1:
        raise TransportError("invalid point swap")
    n = 2 * q_count * jets
    perm = list(range(n))
    for j in range(jets):
        for coordinate in range(2):
            a = 2 * (j * q_count + p0) + coordinate
            b = 2 * (j * q_count + p1) + coordinate
            perm[a], perm[b] = perm[b], perm[a]
    return matrix([[int(column == perm[row]) for column in range(n)]
                   for row in range(n)])


def wrong_half_fiber_swap(q_count=6, jets=2):
    """Hostile map: exchanges omega components but NOT a B_omega-isometry."""
    n = 2 * q_count * jets
    perm = list(range(n))
    perm[0], perm[1] = perm[1], perm[0]
    return matrix([[int(column == perm[row]) for column in range(n)]
                   for row in range(n)])


@dataclass(frozen=True)
class Nerve:
    """Finite ordered simplicial complex, not an arithmetic scheme."""
    vertices: tuple
    edges: tuple
    faces: tuple
    tetrahedra: tuple

    def __post_init__(self):
        v = set(self.vertices)
        if len(v) != len(self.vertices):
            raise TransportError("duplicate nerve vertices")
        for simplices, length in ((self.edges, 2), (self.faces, 3),
                                  (self.tetrahedra, 4)):
            for simplex in simplices:
                if len(simplex) != length or tuple(sorted(simplex)) != simplex:
                    raise TransportError("simplicial orientation malformed")
                if not set(simplex).issubset(v):
                    raise TransportError("unknown vertex")
        e, faces = set(self.edges), set(self.faces)
        for f in self.faces:
            if any(tuple(x) not in e for x in combinations(f, 2)):
                raise TransportError("missing edge of triangle")
        for t in self.tetrahedra:
            if any(tuple(x) not in faces for x in combinations(t, 3)):
                raise TransportError("missing face of tetrahedron")


def tetrahedral_sphere_nerve(fill_interior=False):
    vertices = (0, 1, 2, 3)
    return Nerve(vertices, tuple(combinations(vertices, 2)),
                 tuple(combinations(vertices, 3)),
                 ((0, 1, 2, 3),) if fill_interior else ())


def fundamental_sphere_cycle():
    """Oriented boundary of formal simplex [0123]."""
    return {(1, 2, 3): 1, (0, 2, 3): -1,
            (0, 1, 3): 1, (0, 1, 2): -1}


def boundary_of_two_chain(chain):
    out = {}
    for (a, b, c), n in chain.items():
        for edge, sign in (((b, c), 1), ((a, c), -1), ((a, b), 1)):
            out[edge] = out.get(edge, 0) + sign * n
    return {edge: count for edge, count in out.items() if count}


def delta_one(cochain, nerve, p=5):
    """Cech coboundary of an F_p-valued edge 1-cochain."""
    return {t: (cochain.get((t[1], t[2]), 0) -
                cochain.get((t[0], t[2]), 0) +
                cochain.get((t[0], t[1]), 0)) % p
            for t in nerve.faces}


def delta_two(cochain, nerve, p=5):
    """Cech 3-cochain on every actual tetrahedral 3-simplex."""
    return {t: (cochain.get((t[1], t[2], t[3]), 0) -
                cochain.get((t[0], t[2], t[3]), 0) +
                cochain.get((t[0], t[1], t[3]), 0) -
                cochain.get((t[0], t[1], t[2]), 0)) % p
            for t in nerve.tetrahedra}


def pair_cycle_cocycle(chain, cochain, p=5):
    return sum(n * cochain.get(face, 0) for face, n in chain.items()) % p


def nontrivial_H2_certificate(cochain, nerve, p=5):
    """Nonzero evaluation on a closed 2-cycle refutes being a coboundary."""
    cycle = fundamental_sphere_cycle()
    if nerve.tetrahedra:
        raise TransportError("sphere witness invalid once 3-cell is filled")
    if boundary_of_two_chain(cycle):
        raise AssertionError("2-cycle is not closed")
    if any(value != 0 for value in delta_two(cochain, nerve, p).values()):
        return False
    return pair_cycle_cocycle(cycle, cochain, p) != 0


@dataclass(frozen=True)
class Quaternion:
    """Hamilton's 4-dimensional associative quaternion algebra over F_p."""
    a: int
    b: int
    c: int
    d: int
    p: int = 5

    def __post_init__(self):
        if self.p <= 2:
            raise TransportError("quaternion demo assumes odd characteristic")

    def mul(self, y):
        if self.p != y.p:
            raise TransportError("quaternion fields incompatible")
        a, b, c, d = self.a, self.b, self.c, self.d
        e, f, g, h = y.a, y.b, y.c, y.d
        p = self.p
        return Quaternion((a*e-b*f-c*g-d*h)%p,
                          (a*f+b*e+c*h-d*g)%p,
                          (a*g-b*h+c*e+d*f)%p,
                          (a*h+b*g-c*f+d*e)%p,p)

    def conj(self):
        return Quaternion(self.a%self.p,(-self.b)%self.p,
                          (-self.c)%self.p,(-self.d)%self.p,self.p)

    def norm(self):
        return (self.a**2+self.b**2+self.c**2+self.d**2)%self.p

    def coords(self):
        return tuple(x%self.p for x in (self.a,self.b,self.c,self.d))
