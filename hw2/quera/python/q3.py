def ways_to_select_n_from_m(n, m):
    if n > m:
        return 0
    if n == 0:
        return 1
    return ways_to_select_n_from_m(n - 1, m - 1) + ways_to_select_n_from_m(n, m - 1)


def solve(n, abcd, ons, offs):
    ab_should_be = None
    ac_should_be = None
    abd_should_be = None
    acd_should_be = None

    for i in range(n):
        if i in ons:
            i_changed = '1'
        elif i in offs:
            i_changed = '0'
        else:
            continue

        by_six = i % 6

        if by_six == 0:
            if abd_should_be is not None and abd_should_be != i_changed:
                return []
            abd_should_be = i_changed
        elif by_six == 1 or by_six == 5:
            if ac_should_be is not None and ac_should_be != i_changed:
                return []
            ac_should_be = i_changed
        elif by_six == 2 or by_six == 4:
            if ab_should_be is not None and ab_should_be != i_changed:
                return []
            ab_should_be = i_changed
        else:  # by_six == 3
            if acd_should_be is not None and acd_should_be != i_changed:
                return []
            acd_should_be = i_changed

    template = [None] * n

    possible_states = []

    conditions = [ab_should_be, ac_should_be, abd_should_be, acd_should_be]
    non_conditions = [x for x in conditions if x == '01']
    # non_conditions = conditions.count('01')

    answers = []
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    if a + b + c + d > abcd:
                        continue
                    if (abcd - (a + b + c + d)) % 2 == 1:
                        continue

                    answer = [None] * n

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

    # for b in ab_should_be_odd:
    #     template_b = template.copy()
    #     for i in range(2, n, 6):
    #         template_b[i] = b
    #     for i in range(4, n, 6):
    #         template_b[i] = b
    #
    #     for c in ac_should_be_odd:
    #         template_c = template_b.copy()
    #         for i in range(1, n, 6):
    #             template_c[i] = c
    #         for i in range(5, n, 6):
    #             template_c[i] = c
    #
    #         for bd in abd_should_be_odd:
    #             template_bd = template_c.copy()
    #             for i in range(0, n, 6):
    #                 template_bd[i] = bd
    #
    #             for cd in acd_should_be_odd:
    #                 template_cd = template_bd.copy()
    #                 for i in range(3, n, 6):
    #                     template_cd[i] = cd
    #
    #                 actions = [b, c, bd, cd]
    #                 actions_1 = [x for x in actions if x == '1']
    #
    #                 if len(actions_1) > abcd:
    #                     continue
    #
    #                 possible_states.append(template_cd)
    #
    # return possible_states

    # if bd_should_be_odd is not None:
    #     char = '0' if bd_should_be_odd else '1'
    #     for i in range(0, n, 6):
    #         template[i] = char
    #
    # if c_should_be_odd is not None:
    #     char = '0' if c_should_be_odd else '1'
    #     for i in range(1, n, 6):
    #         template[i] = char
    #     for i in range(5, n, 6):
    #         template[i] = char
    #
    # if b_should_be_odd is not None:
    #     char = '0' if b_should_be_odd else '1'
    #     for i in range(2, n, 6):
    #         template[i] = char
    #     for i in range(4, n, 6):
    #         template[i] = char
    #
    # if cd_should_be_odd is not None:
    #     char = '0' if cd_should_be_odd else '1'
    #     for i in range(3, n, 6):
    #         template[i] = char
    # n_of_nones = [bd_should_be_odd, c_should_be_odd, b_should_be_odd, cd_should_be_odd].count(None)
    #
    # if n_of_nones == 0:
    #     return [''.join(template)]
    #
    # n_possible_states = ways_to_select_n_from_m(abcd, n_of_nones)
    #
    # possible_states = [template for _ in range((n_of_nones))]
    #
    # for i in range(n_of_nones):
    #     for j in range(2 ** i, 2 ** (i + 1)):
    #         possible_states[j][i] = '0'
    #     for j in range(2 ** (i + 1), 2 ** (i + 2)):
    #         possible_states[j][i] = '1'
    #
    # return [''.join(state) for state in possible_states]
    #
    # # new_state = {}
    # #
    # # if 'b' in should_be_odd:
    # #     b_should_be_odd = should_be_odd['b']
    # #     if b_should_be_odd:
    # #         for i in range
    #
    # for a in range(abcd + 1):
    #
    #     if b_should_be_odd is None:
    #         b_start = 0
    #         b_steps = 1
    #     else:
    #         b_steps = 2
    #         if b_should_be_odd:
    #             b_start = 1
    #         else:
    #             b_start = 0
    #
    #     if c_should_be_odd is not None:
    #         c_steps = 2
    #         if c_should_be_odd:
    #             c_start = 1
    #         else:
    #             c_start = 0
    #     else:
    #         c_start = 0
    #         c_steps = 1
    #
    #     for b in range(b_start, abcd - a + 1, b_steps):
    #
    #         template_b = template.copy()
    #
    #         if b_should_be_odd is None:
    #             char = '0' if b % 2 == 1 else '1'
    #             for i in range(2, n, 6):
    #                 template_b[i] = char
    #             for i in range(4, n, 6):
    #                 template_b[i] = char
    #
    #         for c in range(c_start, abcd - a - b + 1, c_steps):
    #             d = abcd - a - b - c
    #
    #             if d < 0:
    #                 continue
    #
    #             new_state = template_b.copy()
    #
    #             if bd_should_be_odd is not None:
    #                 if bd_should_be_odd:
    #                     if (b + d) % 2 == 0:
    #                         continue
    #                 else:
    #                     if (b + d) % 2 == 1:
    #                         continue
    #             else:
    #                 char = '0' if (b + d) % 2 == 1 else '1'
    #                 for i in range(0, n, 6):
    #                     new_state[i] = char
    #
    #             if cd_should_be_odd is not None:
    #                 if cd_should_be_odd:
    #                     if (c + d) % 2 == 0:
    #                         continue
    #                 else:
    #                     if (c + d) % 2 == 1:
    #                         continue
    #             else:
    #                 char = '0' if (c + d) % 2 == 1 else '1'
    #                 for i in range(3, n, 6):
    #                     new_state[i] = char
    #
    #             if c_should_be_odd is None:
    #                 char = '0' if c % 2 == 1 else '1'
    #                 for i in range(1, n, 6):
    #                     new_state[i] = char
    #                 for i in range(5, n, 6):
    #                     new_state[i] = char
    #
    #             possible_states.add(''.join(new_state))
    #
    #         # if bd_should_be_odd is not None:
    #         #     d_steps = 2
    #         #     if (a + b) % 2 == 0:
    #         #         if bd_should_be_odd:
    #         #             d_start = 1
    #         #         else:
    #         #             d_start = 0
    #         #     else:
    #         #         if bd_should_be_odd:
    #         #             d_start = 0
    #         #         else:
    #         #             d_start = 1
    #         # else:
    #         #     d_start = 0
    #         #     d_steps = 1
    #         #
    #         # for d in range(d_start, abcd - a - b + 1, d_steps):
    #         #     c = abcd - a - b - d
    #         #
    #         #     state = ''
    #         #
    #         #     for i in range(n):
    #         #         if i in ons:
    #         #             state += '1'
    #         #         elif i in offs:
    #         #             state += '0'
    #         #         else:
    #         #             clicks_by_b = i % 2 == 0
    #         #             clicks_by_d = i % 3 == 0
    #         #
    #         #             total_clicks = a
    #         #
    #         #             if clicks_by_b:
    #         #                 total_clicks += b
    #         #             else:
    #         #                 total_clicks += c
    #         #
    #         #             if clicks_by_d:
    #         #                 total_clicks += d
    #         #
    #         #             i_is_on = total_clicks % 2 == 0
    #         #
    #         #             if i_is_on:
    #         #                 state += '1'
    #         #             else:
    #         #                 state += '0'
    #         #     possible_states.add(state)
    #
    # possible_states = list(possible_states)
    # possible_states.sort()
    # return possible_states


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
