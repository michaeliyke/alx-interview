#!/usr/bin/python3
"""The N queens interview problem.

Challenge: Place N queens on an NxN chessboard so that no two queens
attack each other.

The solution is a recursive backtracking algorithm that places queens
on the board one by one.
If the current queen can't be placed, the algorithm backtracks to the
previous queen and tries a different position.
"""
import sys


def is_safe(board, row, col):
    """
    Check if there is a queen in the same column, upper left diagonal,
    or upper right diagonal.
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(n):
    """Solve the N queens problem."""
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions


def solve_nqueens_util(board, row, solutions):
    """Solve the N queens problem using backtracking."""
    if row == len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, solutions)
            board[row][col] = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
