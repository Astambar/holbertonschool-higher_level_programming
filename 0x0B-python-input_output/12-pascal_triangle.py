#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    The pascal_triangle function takes a single integer as
    an argument and returns a list of lists containing the
    Pascal's triangle up to the nth row.
    If n is less than or equal to 0, an empty list will be returned.

    :param n: Define the number of rows that will be printed
    :return: A list of lists, where each list is a row in the triangle
    :doc-author: Trelent
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        tmp.extend(tri[i] + tri[i + 1] for i in range(len(tri) - 1))
        tmp.append(1)
        triangles.append(tmp)
    return triangles
