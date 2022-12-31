def solve(n, abcd, ons, offs):
    ab_should_be = None
    ac_should_be = None
    abd_should_be = None
    acd_should_be = None

    for i in range(n):
        if i in ons:
            i_should_be = '1'
        elif i in offs:
            i_should_be = '0'
        else:
            continue

        by_six = i % 6

        if by_six == 0:
            if abd_should_be is not None and abd_should_be != i_should_be:
                return []
            abd_should_be = i_should_be
        elif by_six == 1 or by_six == 5:
            if ac_should_be is not None and ac_should_be != i_should_be:
                return []
            ac_should_be = i_should_be
        elif by_six == 2 or by_six == 4:
            if ab_should_be is not None and ab_should_be != i_should_be:
                return []
            ab_should_be = i_should_be
        else:  # by_six == 3
            if acd_should_be is not None and acd_should_be != i_should_be:
                return []
            acd_should_be = i_should_be

    answers = []
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    if a + b + c + d > abcd:
                        continue
                    if (abcd - (a + b + c + d)) % 2 == 1:
                        continue

                    answer = [''] * n

                    ab_is = '0' if (a + b) % 2 == 1 else '1'
                    if ab_should_be and ab_should_be != ab_is:
                        continue

                    ac_is = '0' if (a + c) % 2 == 1 else '1'
                    if ac_should_be and ac_should_be != ac_is:
                        continue

                    abd_is = '0' if (a + b + d) % 2 == 1 else '1'
                    if abd_should_be and abd_should_be != abd_is:
                        continue

                    acd_is = '0' if (a + c + d) % 2 == 1 else '1'
                    if acd_should_be and acd_should_be != acd_is:
                        continue

                    for i in range(0, n, 6):
                        try:
                            answer[i] = abd_is
                            answer[i + 1] = ac_is
                            answer[i + 2] = ab_is
                            answer[i + 3] = acd_is
                            answer[i + 4] = ab_is
                            answer[i + 5] = ac_is
                        except IndexError:
                            break

                    answers.append(''.join(answer))

    answers.sort()
    return answers


def print_answer(ans):
    if len(ans) == 0:
        print('IMPOSSIBLE')
        return
    ans_list = list(ans)
    for s in ans_list:
        print(s)


def get_input():
    n = int(input())
    abcd = int(input())

    ons = set((int(x) - 1) for x in input().split())
    ons.remove(-2)

    offs = set((int(x) - 1) for x in input().split())
    offs.remove(-2)

    return n, abcd, ons, offs


def main():
    n, abcd, ons, offs = get_input()
    ans = solve(n, abcd, ons, offs)
    print_answer(ans)


if __name__ == '__main__':
    main()
