def is_prime(n):
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False

    return True


def find_diehard_passwords(digits):
    diehards = [2, 3, 5, 7]

    for _ in range(digits - 1):
        new_diehards = []

        for diehard in diehards:
            for i in range(1, 10):
                number = diehard * 10 + i
                if is_prime(number):
                    new_diehards.append(number)

        diehards = new_diehards

    return diehards


def print_answer(ans):
    for element in ans:
        print(element)


def main():
    n = int(input())
    ans = find_diehard_passwords(n)
    print_answer(ans)


if __name__ == '__main__':
    main()
