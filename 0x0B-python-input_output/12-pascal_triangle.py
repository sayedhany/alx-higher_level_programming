#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Represent Pascal
    """
    if n <= 0:
        return []

    tria = [[1]]
    while len(tria) != n:
        tri = tria[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        tria.append(tmp)
    return tria
