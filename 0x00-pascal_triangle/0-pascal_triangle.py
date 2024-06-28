"""Pascal's Triangle module"""


def gen_curr_nxt(arr):
    """Generates pairs of output: adds a leading None value"""
    arr = list(arr)
    length = len(arr)
    if length == 0:
        return ()
    for i in range(length):
        if i == 0:
            yield None, arr[0]
        else:
            yield arr[i-1], arr[i]


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []
    rows = []
    prv = []

    for _ in range(n):
        row = []
        for curr, nxt in gen_curr_nxt(prv):
            if curr is None:
                row.append(1)
            elif nxt is None:
                row.append(1)
            else:
                row.append(curr+nxt)
        row.append(1)
        rows.append(row)
        prv = row

    return rows
