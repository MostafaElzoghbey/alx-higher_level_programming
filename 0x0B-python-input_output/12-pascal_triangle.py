#!/usr/bin/python3

"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    pascal_list = []
    for i in range(n):
        pascal_list.append([1 for j in range(i + 1)])
        if i == 0 or i == 1:
            continue
        for j in range(n - 1):
            if j == 0:
                continue
            if j < i:
                pascal_list[i][j] = pascal_list[i-1][j-1] + pascal_list[i-1][j]
    return pascal_list
