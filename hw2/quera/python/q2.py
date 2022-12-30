def is_prime(n):
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False

    return True


def find_upside_downs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                count += 1

    return count


def print_answer(ans):
    print(ans % (10 ** 5))


def get_input():
    # return [2, 3, 1]
    n = int(input())
    nums = []

    for _ in range(n):
        new_num = int(input())
        nums.append(new_num)

    return nums


def main():
    inp = get_input()
    ans = find_upside_downs(inp)
    print_answer(ans)


if __name__ == '__main__':
    main()
