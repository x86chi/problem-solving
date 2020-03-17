map = [[1, 1, 1, 1, 1],
       [1, 1, 0, 0, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 0, 1],
       [0, 0, 1, 1, 1]]

path = [[None for row in col] for col in map]


def num_path(m: int, n: int):
    path[0][0] = map[0][0]
    for i in range(1, m):
        if map[i][0] == 0:
            path[i][0] = 0
        else:
            path[i][0] = path[i-1][0]
    for j in range(1, n):
        if map[0][j] == 0:
            path[0][j] = 0
        else:
            path[0][j] = path[0][j-1]
    for i in range(1, m):
        for j in range(1, n):
            if map[i][j] == 0:
                path[i][j] = 0
            else:
                path[i][j] = path[i-1][j] + path[i][j-1]


def test_path():
    num_path(5, 5)
    assert path[4][4] == 11
