import re


def solution(card_numbers):
    answer = []
    for _card_number in card_numbers:
        if isValid(_card_number):
            card_number = _card_number.replace('-', '')
            if ((even(card_number) + odd(card_number)) % 10 == 0):
                answer.append(1)
                continue
        answer.append(0)
    return answer


def even(card_number: str):
    answer = 0
    for cursor_x in card_number[-2::-2]:
        multiplied = 2 * int(cursor_x)
        temp = 0
        for cursor_y in str(multiplied):
            temp += int(cursor_y)
        answer += temp
    return answer


def odd(card_number: str):
    return sum(map(int, card_number[-1::-2]))


def isValid(card_number: str):
    if re.match('^[0-9]{16}$', card_number):
        return True

    if re.match('^[0-9]{4}(-[0-9]{4}){3}$', card_number):
        return True

    return False


def test_cases():
    card_number = '3285376499342453'
    assert even(card_number) == 42
    assert odd(card_number) == 38


def test_valid():
    assert isValid('3285376499342453') == True
    assert isValid('3285-3764-9934-2453') == True
    assert isValid('3285-3764-99342453') == False


def test_solution():
    assert solution(["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453",
                     "328537649934245", "3285376499342459", "3285-3764-9934-2452"]) == [1, 1, 0, 0, 0, 0]
