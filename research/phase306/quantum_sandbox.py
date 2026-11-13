#!/usr/bin/env python3
"""Phase306-C: optional exact quantum-mathematical toy controls.

No physical quantum device, Schrödinger time simulation, or link to field bound.
Use coefficient matrices over Q as a subset of complex Hilbert space states.
"""
from fractions import Fraction


def rows(a):
    m = tuple(tuple(Fraction(x) for x in row) for row in a)
    if not m or not m[0] or any(len(row) != len(m[0]) for row in m):
        raise ValueError("empty/nonrectangular amplitude matrix")
    return m


def rational_rank(a):
    m = [list(row) for row in rows(a)]
    rank = 0
    for col in range(len(m[0])):
        pivot = next((i for i in range(rank, len(m)) if m[i][col]), None)
        if pivot is None:
            continue
        m[rank], m[pivot] = m[pivot], m[rank]
        u = m[rank][col]
        m[rank] = [x / u for x in m[rank]]
        for i in range(len(m)):
            if i != rank:
                u = m[i][col]
                m[i] = [x - u*y for x, y in zip(m[i], m[rank])]
        rank += 1
        if rank == len(m):
            break
    return rank


def schmidt_rank(a):
    """For bipartite pure state coefficients, Schmidt rank=matrix rank."""
    return rational_rank(a)


def reduced_purity(a):
    """Tr(rho_A^2), with the state norm handled exactly."""
    m = rows(a)
    d = len(m)
    gram = tuple(tuple(sum(m[i][k]*m[j][k] for k in range(len(m[0])))
                       for j in range(d)) for i in range(d))
    norm_sq = sum(gram[i][i] for i in range(d))
    if norm_sq == 0:
        raise ValueError("zero quantum state")
    return sum(gram[i][j]*gram[j][i] for i in range(d)
               for j in range(d)) / (norm_sq ** 2)


def bell_like(d=5):
    """Unnormalized |Phi_d> = sum_i |ii>, normalization is 1/sqrt(d)."""
    if d < 2:
        raise ValueError("need two or more local dimensions")
    return rows([[int(i == j) for j in range(d)] for i in range(d)])


def product_state(d=5):
    if d < 2:
        raise ValueError("need two or more local dimensions")
    return rows([[int(i == 0 and j == 0) for j in range(d)]
                 for i in range(d)])


def tight_binding_barrier(g=1, barrier=7):
    """Hermitian three-site tight-binding matrix, exact integer entries."""
    g, barrier = Fraction(g), Fraction(barrier)
    return rows(((0, g, 0), (g, barrier, g), (0, g, 0)))


def transition_second_order_coefficient(h):
    """Coefficient of t^2 for <right|exp(-itH)|left>, not a probability."""
    h = rows(h)
    if len(h) != 3 or len(h[0]) != 3:
        raise ValueError("three-site Hamiltonian required")
    if any(h[i][j] != h[j][i] for i in range(3) for j in range(3)):
        raise ValueError("non-Hermitian real Hamiltonian")
    second = sum(h[2][k]*h[k][0] for k in range(3))
    return -second / 2


def avoided_crossing_gap_squared(s, epsilon):
    """Eigenvalue gap squared for H(s)=[[s,e],[e,-s]]."""
    s, epsilon = Fraction(s), Fraction(epsilon)
    return 4*(s*s + epsilon*epsilon)


def adiabatic_scale_proxy(epsilon, duration):
    """A heuristic smallness parameter, NOT an adiabatic theorem error bound."""
    epsilon = Fraction(epsilon)
    duration = Fraction(duration)
    if epsilon == 0 or duration <= 0:
        raise ValueError("positive gap and positive duration required")
    return 1/(4*epsilon*epsilon*duration)
