def find_least_palindrome_deletion(word: str) -> int:
    dp_size = len(word) + 1
    dp = [[0 for _ in range(dp_size)] for _ in range(dp_size)]

    for column in range(len(word)):
        row = column
        dp[row][column] = 1

    for curr_column in range(1, len(word)):
        row = 0

        for column in range(curr_column, len(word)):
            dp[row][column] = dp[row + 1][column] + 1

            if word[row] == word[row + 1]:
                dp[row][column] = min(dp[row + 2][column] + 1, dp[row][column])

            for occurrence in range(row + 2, column + 1):
                if word[row] == word[occurrence]:
                    dp[row][column] = min(dp[row + 1][occurrence - 1] + dp[occurrence + 1][column], dp[row][column])

            row += 1

    return dp[0][-2]


def main():
    inp = input()
    least_deletions = find_least_palindrome_deletion(inp)
    print(least_deletions)


if __name__ == '__main__':
    main()
