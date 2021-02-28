from typing import List


def solution(sticker: List[int]):
    length = len(sticker)

    if length <= 3:
        return max(sticker)

    omitEnd = [-1 for __ in range(length - 1)]

    omitEnd[0] = sticker[0]
    omitEnd[1] = sticker[1]

    for i in range(2, length - 1):
        omitEnd[i] = max(
            omitEnd[i - 2] + sticker[i], omitEnd[i - 1])

    omitStart = [-1 for __ in range(length)]
    omitStart[1] = sticker[1]

    for i in range(2, length):
        omitStart[i] = max(
            omitStart[i - 2] + sticker[i], omitStart[i - 1])

    return max(omitEnd[-1], omitStart[-1])


def test_solution():
    assert solution([1, 2, 3, 1]) == 4
    assert solution([14, 6, 5, 11, 3, 9, 2, 10]) == 36
    assert solution([1, 3, 2, 5, 4]) == 8
