def solution(height: int):
    paths = []

    def hanoi(n: int, start: int, to: int, aux: int):
        if n == 1:
            paths.append((start, to))
            return
        hanoi(n-1, start, aux, to)
        paths.append((start, to))
        hanoi(n-1, aux, to, start)
    hanoi(height, 1, 3, 2)
    return paths


def test_solution():
    assert solution(3) == [(1, 3), (1, 2), (3, 2),
                           (1, 3), (2, 1), (2, 3), (1, 3)]


if __name__ == "__main__":
    paths = solution(int(input()))
    for path in paths:
        print(*path)
