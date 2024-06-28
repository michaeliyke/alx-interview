#!/usr/bin/python3
"""Pascal's Triangle module"""

# fantastica
# things
# superhuman
# Trello


def print_triangle(triangle):
    """Print Pascal's triangle"""
    for row in triangle:
        print(" ".join([str(x) for x in row]))


def pascal_triangle(N):
    """Pascal's triangle implementation"""
    triangle = [[1]]
    for i in range(1, N):
        row = [1] + [
            triangle[i-1][j-1] + triangle[i-1][j]
            for j in range(1, i)
        ] + [1]
        triangle.append(row)
    return triangle
