def meets_conditions(conditions, a, b, c, d):
    for condition in conditions['odd']:
        sum_of_acts = a

        if 'b' in condition:
            sum_of_acts += b
        elif 'c' in condition:
            sum_of_acts += c

        if 'd' in condition:
            sum_of_acts += d

        if sum_of_acts % 2 == 0:
            return False

    for condition in conditions['even']:
        sum_of_acts = a

        if 'b' in condition:
            sum_of_acts += b
        elif 'c' in condition:
            sum_of_acts += c

        if 'd' in condition:
            sum_of_acts += d

        if sum_of_acts % 2 == 1:
            return False

    return True


def solve(n, abcd, ons, offs):
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

    possible_states = set()
    for a in range(abcd + 1):
        for b in range(abcd - a + 1):
            for c in range(abcd - a - b + 1):
                d = abcd - a - b - c

                if meets_conditions(conditions, a, b, c, d):

                    state = ''

                    for i in range(n):
                        if i in ons:
                            state += '1'
                        elif i in offs:
                            state += '0'
                        else:
                            clicks_by_b = i % 2 == 0
                            clicks_by_c = not clicks_by_b
                            clicks_by_d = i % 3 == 0

                            total_clicks = a

                            if clicks_by_b:
                                total_clicks += b
                            elif clicks_by_c:
                                total_clicks += c
                            if clicks_by_d:
                                total_clicks += d

                            i_is_on = total_clicks % 2 == 0

                            if i_is_on:
                                state += '1'
                            else:
                                state += '0'

                    possible_states.add(state)
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
