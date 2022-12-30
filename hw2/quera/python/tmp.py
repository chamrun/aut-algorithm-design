def radix_sort(arr, k):
    for i in range(k):
        # Create k buckets
        buckets = [[] for _ in range(k)]
        # Place elements in buckets based on their i-th digit
        for j in arr:
            digit = (j // (k ** i)) % k
            buckets[digit].append(j)
        # Concatenate buckets to get sorted list
        arr = [element for bucket in buckets for element in bucket]
    return arr


if __name__ == '__main__':
    numbers = [
        38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56,
        4, 1, 54, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
        57, 58, 68, 69, 70, 71, 72, 73, 74, 84, 85, 86, 87, 88, 89, 90, 91, 92,
        93, 94, 95, 96, 97, 98, 99, 59, 60, 61, 62, 63, 64, 65, 66, 67,
        75, 76, 77, 78, 79, 80, 81, 82, 83, 12, 14, 15, 16, 17, 18, 19, 20, 21,
    ]
    s = radix_sort(numbers, 4)
    print(s)
