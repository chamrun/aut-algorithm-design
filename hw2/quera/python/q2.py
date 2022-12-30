def find_upsidedowns(nums):
    if 1 >= len(nums):
        return 0

    middle_index = int(len(nums) / 2)
    left_nums = nums[:middle_index]
    right_nums = nums[middle_index:]

    left_upsidedowns = find_upsidedowns(left_nums)
    right_upsidedowns = find_upsidedowns(right_nums)
    cross_upsidedowns = find_cross_upsidedowns(left_nums, nums, right_nums)

    upsidedowns = left_upsidedowns + right_upsidedowns + cross_upsidedowns
    return upsidedowns


def find_cross_upsidedowns(left_nums, nums, right_nums):
    cross_upsidedowns = 0
    i = 0
    j = 0
    for k in range(len(nums)):
        if j >= len(right_nums):
            nums[k] = left_nums[i]
            i += 1
        elif i >= len(left_nums):
            nums[k] = right_nums[j]
            j += 1
        elif left_nums[i] > right_nums[j]:
            nums[k] = right_nums[j]
            j += 1
        else:
            nums[k] = left_nums[i]
            i += 1

        cross_upsidedowns += len(left_nums) - i
    return cross_upsidedowns


def print_answer(ans):
    print(ans % (10 ** 5))


def get_input():
    n = int(input())
    nums = []

    for _ in range(n):
        new_num = int(input())
        nums.append(new_num)

    return nums


def main():
    inp = get_input()
    ans = find_upsidedowns(inp)
    print_answer(ans)


if __name__ == '__main__':
    main()
