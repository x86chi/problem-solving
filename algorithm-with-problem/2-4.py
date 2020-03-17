from copy import deepcopy

map = [[1, 2, 2, 1, 5],
       [1, 4, 4, 3, 1],
       [2, 1, 1, 1, 2],
       [1, 3, 5, 1, 1],
       [1, 5, 1, 2, 2]]


def num_path(n: int, m: int, map: list):
    path = [[None for row in col] for col in map]
    from_ = deepcopy(path)

    path[0][0] = map[0][0]

    for i in range(1, n):
        path[i][0] = map[i][0]
        from_[i][0] = 'LEFT'
    for j in range(1, m):
        path[0][j] = map[0][j]
        from_[i][0] = 'UP'
    for i in range(1, n):
        for j in range(1, m):
            if path[i-1][j] > path[i][j-1]:
                from_[i][j] = 'LEFT'
            else:
                from_[i][j] = 'UP'
            path[i][j] = max(path[i-1][j], path[i][j-1]) + map[i][j]
    print_path(n-1, m-1, from_)
    return path[n-1][m-1]


def print_path(n: int, m: int, from_: list):
    if m == 0 and n == 0:
        return
    print(f'{n} {m}')
    if from_[n][m] == 'LEFT':
        return print_path(n-1, m, from_)
    return print_path(n, m-1, from_)


def test_num():
    assert num_path(5, 5, map) == 22
