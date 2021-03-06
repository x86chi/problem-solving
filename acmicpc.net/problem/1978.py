def prime(n):
    if (n < 2):
        return False
    i = 2
    while (i*i <= n):
        if n % i == 0:
            return False
        i += 1
    return True


def test_prime():
    list(map(prime, [1, 3, 5, 7])).count(True) == 3


if __name__ == '__main__':
    input()
    print(list(map(prime, map(int, input().split()))).count(True))
