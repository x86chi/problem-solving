from itertools import combinations
from typing import List, Tuple


def distance(A: str, B: str):
    count = 0
    for i in range(4):
        if A[i] != B[i]:
            count += 1
    return count


def main(characters: List[str]):
    if len(characters) >= 33:
        return 0

    def find(combination: Tuple[str, str, str]):
        A, B, C = combination
        return distance(A, B) + distance(B, C) + distance(A, C)
    return min(map(find, combinations(characters, 3)))


def test_sample():
    assert main(['ENTJ', 'INTP', 'ESFJ']) == 8
    assert main(['ESFP', 'ESFP', 'ESFP', 'ESFP']) == 0
    assert main(['INFP', 'INFP', 'ESTP', 'ESTJ', 'ISTJ']) == 4


def test_maximum():
    from utils import check_time_limit
    wrapped = check_time_limit(main, 2)

    all_cases = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP',
                 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']

    assert wrapped(all_cases * 2) == 2


if __name__ == "__main__":
    for __ in range(int(input())):
        input()
        print(main(input().split()))
