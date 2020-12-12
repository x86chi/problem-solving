from typing import List


from collections import deque

NEXT_X = [0, 0, -1, 1]
NEXT_Y = [1, -1, 0, 0]


def solution(square: List[List[int]]):

    result = [0, 0, 0]

    N = len(square)

    group = [[False]*N for __ in range(N)]

    def bfs(y, x):
        queue = deque()
        queue.append((y, x))
        group[y][x] = True

        TYPE = square[y][x]

        while queue:
            y, x = queue.popleft()
            for i in range(4):
                _y, _x = y+NEXT_Y[i], x+NEXT_X[i]
                if 0 <= _x < N and 0 <= _y < N and square[_y][_x] == TYPE and group[_y][_x] == False:
                    group[_y][_x] = True
                    queue.append((_y, _x))
        result[TYPE] += 1

    for x in range(N):
        for y in range(N):
            if group[y][x] == False:
                bfs(y, x)
    return result


def test_solution():
    assert solution([[0, 0, 1, 1], [1, 1, 1, 1], [
                    2, 2, 2, 1], [0, 0, 0, 2]]) == [2, 1, 2]
    assert solution([[0, 0, 1], [2, 2, 1], [0, 0, 0]]) == [2, 1, 1]
