#!/usr/bin/python3
"""
'Rotate 2D Matrix' project
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise
    Steps:
        1. Transpose the matrix
        2. Reverse each row
    Details of the steps:
    1. Transpose the matrix:
        - For each row, swap the elements with the corresponding column
        - For example, matrix[0][1] = matrix[1][0]
    2. Reverse each row:
        - For each row, reverse the elements
        - For example, matrix[0] = matrix[0][::-1]

    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
