def num_path(n: int, m: int, map: list):
    path = [[None for row in col] for col in map]
    path[0][0] = map[0][0]

    for i in range(1, n):
        path[i][0] = map[i][0]
    for j in range(1, m):
        path[0][j] = map[0][j]
    for i in range(1, n):
        for j in range(1, m):
            path[i][j] = max(path[i-1][j], path[i][j-1]) + map[i][j]
    return path[n-1][m-1]


def test_num():
    map = [[1, 1, 2, 1, 5],
           [1, 4, 4, 3, 1],
           [2, 1, 1, 1, 2],
           [1, 3, 5, 1, 1],
           [1, 5, 1, 2, 2]]

    assert num_path(5, 5, map) == 21
