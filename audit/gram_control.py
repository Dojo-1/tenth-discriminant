#!/usr/bin/env python3
"""Exact pair-arithmetic reconstruction of the source's D=3 Gram control."""


def mul(d, a, b):
    return (a[0] * b[0] - d * a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def conjugate(a):
    return (a[0], -a[1])


def trace_pair(d, a, b):
    return 2 * (a[0] * b[0] + d * a[1] * b[1])


def main():
    d = 3
    z = (0, 1)
    zbar = conjugate(z)
    rows = {
        "1": [(1, 0), (0, 0)],
        "ZW": [mul(d, z, zbar), zbar],
    }

    def gram_entry(left, right):
        return sum(trace_pair(d, a, b) for a, b in zip(left, right))

    matrix = [
        [gram_entry(rows["1"], rows["1"]), gram_entry(rows["1"], rows["ZW"])],
        [gram_entry(rows["ZW"], rows["1"]), gram_entry(rows["ZW"], rows["ZW"])],
    ]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    assert matrix == [[2, 6], [6, 24]]
    assert determinant == 12
    print(f"PASS: exact Gram control {matrix}, determinant {determinant}")


if __name__ == "__main__":
    main()
