map = [[1, 1, 1, 1, 1],
       [1, 1, 0, 0, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 0, 1],
       [0, 0, 1, 1, 1]]


def num_path(m: int, n: int):
    if map[m][n] == 0:
        return 0
    if m == 0 and n == 0:
        return 1
    if m > 0 and n == 0:
        return num_path(m-1, n)
    if m == 0 and n > 0:
        return num_path(m, n-1)
    return num_path(m-1, n) + num_path(m, n-1)


def test_path():
    assert num_path(4, 4) == 11
