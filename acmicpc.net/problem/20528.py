def palindrome(word: str):
    return word == word[::-1]


def main(raw_words: str):
    words = raw_words.split()

    for i in range(len(words) - 1):
        cursor = words[i]
        next_cursor = words[i+1]
        if palindrome(cursor) and cursor[-1] == next_cursor[0]:
            continue
        return False
    return True


def test_sample():
    assert main('pqqp pqpqp pbbbp') == True
    assert main('aba c dd') == False


if __name__ == "__main__":
    input()
    if (main(input())):
        print(1)
    else:
        print(0)
