#!/usr/bin/env python3
"""Exact rational check of the final affine cutoff separation only."""

from fractions import Fraction


log_lower = Fraction(246304, 10000)
gap_slope = Fraction(999997, 1000000) - Fraction(4, 5)
gap_intercept = Fraction(5739, 1000) - Fraction(813, 1000)
margin = gap_slope * log_lower - gap_intercept

assert margin == Fraction(61088, 10_000_000_000)
print(f"PASS: exact affine margin = {margin} = {float(margin):.10f}")
