def calculate_max_profit(length, prices):
    accumulate = 0
    for first in range(length):
        max_profit = 0
        for second in range(first+1, length):
            max_profit = max(max_profit, prices[second] - prices[first])
        accumulate += max_profit
    return accumulate


def test_calculate_max_profit():
    assert calculate_max_profit(3, [10, 7, 6]) == 0
    assert calculate_max_profit(3, [3, 5, 9]) == 10
    assert calculate_max_profit(5, [1, 1, 3, 1, 2]) == 5


if __name__ == "__main__":
    from sys import stdin
    for __ in range(int(stdin.readline())):
        length = int(stdin.readline())
        prices = list(map(int, stdin.readline().split(' ')))
        print(calculate_max_profit(length, prices))
