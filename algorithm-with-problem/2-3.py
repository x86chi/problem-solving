map = [[1, 1, 2, 1, 5],
       [1, 4, 4, 3, 1],
       [2, 1, 1, 1, 2],
       [1, 3, 5, 1, 1],
       [1, 5, 1, 2, 2]]


def num_path(n: int, m: int):
    if m == 0 and n == 0:
        return map[0][0]
    if m > 0 and n == 0:
        return num_path(m-1, n) + map[m][n]
    if m == 0 and n > 0:
        return num_path(m, n-1) + map[m][n]
    return max(num_path(m-1, n), num_path(m, n-1)) + map[m][n]


def test_num():
    assert num_path(4, 4) == 21
