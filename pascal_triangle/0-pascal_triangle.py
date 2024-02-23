#!/usr/bin/python3
"""
pascal's triangle
"""


def pascal_triangle(n):
    """
    Generates pascal's triangle (inteeractive approach)
    Args:
        n: the number of rows in the triangle
    Returns:
        A list of list representing the P triangle
    """
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
