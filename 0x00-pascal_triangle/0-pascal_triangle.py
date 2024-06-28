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
            triangle[-1][i] + triangle[-1][i+1]
            for i in range(len(triangle[-1])-1)
        ] + [1]
        triangle.append(row)
    return triangle
