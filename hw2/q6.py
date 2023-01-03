def main():
    numbers = [10, 1, 2, 4, 5, 9, 6, 7, 8, 3, 0, 3, 3, 4]
    max_number = 10
    print(counting_sort(numbers, max_number))
    print(stable_counting_sort(numbers, max_number))


def counting_sort(numbers, max_number):
    counts = [0] * (max_number + 1)
    for number in numbers:
        counts[number] += 1
    result = []
    for i in range(len(counts)):
        for _ in range(counts[i]):
            result.append(i)
    return result



if __name__ == '__main__':
    main()
