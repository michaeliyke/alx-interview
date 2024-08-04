#!/usr/bin/python3
"""The N queens interview problem.

Challenge: Place N queens on an NxN chessboard so that no two queens
attack each other.

The solution is a recursive backtracking algorithm that places queens
on the board one by one.
If the current queen can't be placed, the algorithm backtracks to the
previous queen and tries a different position.
"""


def nqueens(n):
    """Return all solutions to the N queens problem.

    Args:
        n: The number of queens to place on the board.

    Returns:
        A list of solutions, where each solution is a list of queen
        positions. Each queen position is a tuple (row, column).
    """
    def is_safe(queens, row, col):
        """Check if a queen can be placed at the given position.

        Args:
            queens: A list of queen positions.
            row: The row to place the queen.
            col: The column to place the queen.

        Returns:
            True if the queen can be placed at the given position, False
            otherwise.
        """
        for r, c in queens:
            if row == r or col == c or abs(row - r) == abs(col - c):
                return False
        return True

    def solve(queens, row):
        """Recursively find all solutions to the N queens problem.

        Args:
            queens: A list of queen positions.
            row: The row to place the queen.

        Returns:
            A list of solutions.
        """
        if row == n:
            return [queens]

        solutions = []
        for col in range(n):
            if is_safe(queens, row, col):
                solutions += solve(queens + [(row, col)], row + 1)
        return solutions

    return solve([], 0)


def print_board(board):
    """Print the board with queens placed.

    Args:
        board: A list of queen positions.
    """
    for row, col in board:
        line = ['.'] * len(board)
        line[col] = 'Q'
        print(' '.join(line))


def main():
    """Test the nqueens function."""
    n = 4
    for i, board in enumerate(nqueens(n), 1):
        print(f'Solution {i}:')
        print_board(board)
        print()


if __name__ == '__main__':
    main()
