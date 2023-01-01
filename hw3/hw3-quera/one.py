def remove_palindrome_sub(s: str) -> int:
    actions = 0
    i = 0
    while i < len(s):
        if s[i] == s[i + 1]:
            actions += 1
            i += 2
        else:
            i += 1
    return actions + 1


def main():
    test_cases = ['addbbggbb']
    print([remove_palindrome_sub(tc) for tc in test_cases])


if __name__ == '__main__':
    main()
