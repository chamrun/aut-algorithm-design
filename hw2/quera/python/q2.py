def meets_conditions(conditions, a, b, c, d):
    for condition in conditions['odd']:
        sum_of_acts = a

        for act in condition:
            if act == 'b':
                sum_of_acts += b
            elif act == 'c':
                sum_of_acts += c
            elif act == 'd':
                sum_of_acts += d

        if sum_of_acts % 2 == 0:
            return False

    for condition in conditions['even']:
        sum_of_acts = a

        for act in condition:
            if act == 'b':
                sum_of_acts += b
            elif act == 'c':
                sum_of_acts += c
            elif act == 'd':
                sum_of_acts += d

        if sum_of_acts % 2 == 1:
            return False

    return True


def solve(n, abcd, ons, offs):
    # conditions = find_confitions(n, offs, ons)
    # possible_acts = fin_possible_acts(abcd, conditions)
    # del conditions
    # possible_states = find_possible_states(n, offs, ons, possible_acts)
    # del possible_acts

    # return possible_states
    pass

    # def find_confitions(n, offs, ons):
    conditions = {
        'odd': list(),
        'even': list(),
    }
    for i in range(n):
        if i in ons:
            i_changed = False
        elif i in offs:
            i_changed = True
        else:
            continue

        clicks_by_b = i % 2 == 0
        clicks_by_c = not clicks_by_b
        clicks_by_d = i % 3 == 0

        clicks_by = set()

        if clicks_by_b:
            clicks_by.add('b')
        if clicks_by_c:
            clicks_by.add('c')
        if clicks_by_d:
            clicks_by.add('d')

        if i_changed:
            conditions['odd'].append(clicks_by)
        else:
            conditions['even'].append(clicks_by)

    # def fin_possible_acts(abcd, conditions):
    possible_states = set()
    for a in range(abcd + 1):
        for b in range(abcd - a + 1):
            for c in range(abcd - a - b + 1):
                d = abcd - a - b - c

                if meets_conditions(conditions, a, b, c, d):
                    # possible_acts.append({
                    #     'a': a,
                    #     'b': b,
                    #     'c': c,
                    #     'd': d,
                    # })

                    act = {
                        'a': a,
                        'b': b,
                        'c': c,
                        'd': d,
                    }

                    state = ''

                    for i in range(n):
                        if i in ons:
                            state += '1'
                        elif i in offs:
                            state += '0'
                        else:
                            clicks_by_a = True
                            clicks_by_b = i % 2 == 0
                            clicks_by_c = not clicks_by_b
                            clicks_by_d = i % 3 == 0

                            i_is_on = True

                            if clicks_by_a and act['a'] % 2 == 1:
                                i_is_on = not i_is_on
                            if clicks_by_b and act['b'] % 2 == 1:
                                i_is_on = not i_is_on
                            if clicks_by_c and act['c'] % 2 == 1:
                                i_is_on = not i_is_on
                            if clicks_by_d and act['d'] % 2 == 1:
                                i_is_on = not i_is_on

                            if i_is_on:
                                state += '1'
                            else:
                                state += '0'

                    possible_states.add(state)

    # def find_possible_states(n, offs, ons, possible_acts):
    #     for act in possible_acts:
    #         state = ''
    #
    #         for i in range(n):
    #             if i in ons:
    #                 state += '1'
    #             elif i in offs:
    #                 state += '0'
    #             else:
    #                 clicks_by_a = True
    #                 clicks_by_b = i % 2 == 0
    #                 clicks_by_c = not clicks_by_b
    #                 clicks_by_d = i % 3 == 0
    #
    #                 i_is_on = True
    #
    #                 if clicks_by_a and act['a'] % 2 == 1:
    #                     i_is_on = not i_is_on
    #                 if clicks_by_b and act['b'] % 2 == 1:
    #                     i_is_on = not i_is_on
    #                 if clicks_by_c and act['c'] % 2 == 1:
    #                     i_is_on = not i_is_on
    #                 if clicks_by_d and act['d'] % 2 == 1:
    #                     i_is_on = not i_is_on
    #
    #                 if i_is_on:
    #                     state += '1'
    #                 else:
    #                     state += '0'
    #
    #         possible_states.add(state)
    return possible_states


def print_answer(ans):
    if len(ans) == 0:
        print('IMPOSSIBLE')
        return
    ans_list = list(ans)
    ans_list.sort()
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
