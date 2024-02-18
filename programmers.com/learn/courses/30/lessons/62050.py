from collections import deque

NEXT_X = [0, 0, -1, 1]
NEXT_Y = [1, -1, 0, 0]

MAX = 10000
NONE = MAX + 1


def solution(land, height):
    matrix = make_matrix(land, *label_tag(1, land))
    edges = matrix_to_edge_list(matrix)

    edges.sort(key=lambda item: item[2])

    link = [i for i in range(len(edges))]

    def find(x: int):
        if x == link[x]:
            return x
        link[x] = find(link[x])
        return link[x]

    def same(a: int, b: int):
        return find(a) == find(b)

    def unite(a: int, b: int):
        a = find(a)
        b = find(b)
        link[a] = b

    answer = 0
    for edge in edges:
        if not same(edge[0], edge[1]):
            unite(edge[0], edge[1])
            answer += edge[2]

    return answer


def matrix_to_edge_list(matrix: list):
    result = []
    length = len(matrix)
    visit_matrix = [[False]*length for __ in range(length)]

    for x in range(length):
        for y in range(length):
            if matrix[x][y] != NONE and visit_matrix[x][y] == False and visit_matrix[y][x] == False:
                visit_matrix[x][y] = True
                result.append((x, y, matrix[x][y]))

    return result


def make_matrix(square: list, group: list, count: int):
    N = len(group)
    matrix = [[MAX+1]*count for __ in range(count)]
    visit = [[False]*N for __ in range(N)]

    def bfs(y, x):
        visit[y][x] = True

        queue = deque()
        queue.append((y, x))
        while queue:
            y, x = queue.popleft()
            for i in range(4):
                _y, _x = y+NEXT_Y[i], x+NEXT_X[i]
                if 0 <= _x < N and 0 <= _y < N and group[y][x] != group[_y][_x]:
                    matrix[group[y][x]-1][group[_y][_x]-1] = min(
                        matrix[group[y][x]-1][group[_y][_x]-1], abs(square[y][x] - square[_y][_x]))

    for x in range(N):
        for y in range(N):
            if visit[y][x] == False:
                bfs(y, x)
    return matrix


def label_tag(height: int, square: list):
    N = len(square)

    count = 0
    group = [[0]*N for __ in range(N)]

    def bfs(y, x, count):
        queue = deque()
        queue.append((y, x))
        group[y][x] = count
        while queue:
            y, x = queue.popleft()
            for i in range(4):
                _y, _x = y+NEXT_Y[i], x+NEXT_X[i]
                if 0 <= _x < N and 0 <= _y < N and abs(square[y][x] - square[_y][_x]) <= height and group[_y][_x] == 0:
                    group[_y][_x] = count
                    queue.append((_y, _x))

    for x in range(N):
        for y in range(N):
            if group[y][x] == 0:
                count += 1
                bfs(y, x, count)
    return group, count


cases = {
    'square': [
        [[1, 4, 8, 10],
         [5, 5, 5, 5],
         [10, 10, 10, 10],
         [10, 10, 10, 20]],

        [[10, 11, 10, 11],
         [2, 21, 20, 10],
         [1, 20, 21, 11],
         [2, 1, 2, 1]]
    ],
    'grouped': [
        [[1, 1, 1, 1],
         [1, 1, 1, 1],
         [2, 2, 2, 2],
         [2, 2, 2, 3]],

        [[1, 1, 1, 1],
         [2, 3, 3, 1],
         [2, 3, 3, 1],
         [2, 2, 2, 2]]
    ],
    'height': [3, 1],
    'count': [3, 3],
}


def test_label_tag():
    grouped, count = label_tag(cases['height'][0], cases['square'][0])

    assert grouped == cases['grouped'][0]
    assert count == cases['count'][0]

    grouped, count = label_tag(cases['height'][1], cases['square'][1])

    assert grouped == cases['grouped'][1]
    assert count == cases['count'][1]


def test_make_matrix():

    graph = make_matrix(cases['square'][0],
                        cases['grouped'][0], cases['count'][0])
    assert graph == [[NONE, 5, NONE], [5, NONE, 10], [NONE, 10, NONE]]

    graph = make_matrix(cases['square'][1],
                        cases['grouped'][1], cases['count'][1])
    assert graph == [[NONE, 8, 10], [8, NONE, 19], [10, 19, NONE]]


def test_matrix_to_edge_list():
    matrix_to_edge_list([[NONE, 8, 10], [8, NONE, 19], [10, 19, NONE]]) == [
        (0, 1, 8), (0, 2, 10), (1, 2, 19)]
    matrix_to_edge_list([[NONE, 5, NONE], [5, NONE, 10], [
                        NONE, 10, NONE]]) == [(0, 1, 5), (1, 2, 10)]


def test_solution():
    assert solution(cases['square'][0], cases['height'][0]) == 15
    assert solution(cases['square'][1], cases['height'][1]) == 18
