def find_longest_common_substring(s1, s2):
    """Return the longest common substring of s1 and s2.
    >>> find_longest_common_substring('TGCATTA', 'AGTTCG')
    'TT'
    >>> find_longest_common_substring('abcde', 'abfce')
    'ab'
    >>> find_longest_common_substring('abc', 'def')
    ''
    """

    if len(s1) > len(s2):
        s1, s2 = s2, s1

    dp = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]

    max_len = 0

    last_index_of_substring = None

    for offset in range(len(s2)):
        for i in range(len(s1) - offset):
            if s1[i] == s2[i + offset]:
                new_sub_len = dp[offset][i - 1] + 1
                dp[offset][i] = new_sub_len

                if new_sub_len > max_len:
                    max_len = new_sub_len
                    last_index_of_substring = i

    if max_len != 0:
        return s1[last_index_of_substring - max_len + 1: last_index_of_substring + 1]
    else:
        return ''
