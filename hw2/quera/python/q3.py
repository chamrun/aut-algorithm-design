def solve(n, abcd, ons, offs):
    should_be_odd = {}

    for i in range(n):
        if i in ons:
            i_changed = False
        elif i in offs:
            i_changed = True
        else:
            continue

        by_six = i % 6

        if by_six == 0:
            if 'bd' in should_be_odd and should_be_odd['bd'] != i_changed:
                return []
            should_be_odd['bd'] = i_changed
        elif by_six == 1 or by_six == 5:
            if 'c' in should_be_odd and should_be_odd['c'] != i_changed:
                return []
            should_be_odd['c'] = i_changed
        elif by_six == 2 or by_six == 4:
            if 'b' in should_be_odd and should_be_odd['b'] != i_changed:
                return []
            should_be_odd['b'] = i_changed
        else:
            if 'cd' in should_be_odd and should_be_odd['cd'] != i_changed:
                return []
            should_be_odd['cd'] = i_changed

    possible_states = set()

    ab_should_be_odd = should_be_odd.get('b')
    ac_should_be_odd = should_be_odd.get('c')
    abd_should_be_odd = should_be_odd.get('bd')
    acd_should_be_odd = should_be_odd.get('cd')

    for a in range(abcd + 1):

        if ab_should_be_odd is not None:
            b_steps = 2
            if a % 2 == 0:
                if ab_should_be_odd:
                    b_start = 1
                else:
                    b_start = 0
            else:
                if ab_should_be_odd:
                    b_start = 0
                else:
                    b_start = 1
        else:
            b_start = 0
            b_steps = 1

        if ac_should_be_odd is not None:
            c_steps = 2
            if a % 2 == 0:
                if ac_should_be_odd:
                    c_start = 1
                else:
                    c_start = 0
            else:
                if ac_should_be_odd:
                    c_start = 0
                else:
                    c_start = 1
        else:
            c_start = 0
            c_steps = 1

        for b in range(b_start, abcd - a + 1, b_steps):

            if abd_should_be_odd is not None:
                d_steps = 2
                if (a + b) % 2 == 0:
                    if abd_should_be_odd:
                        d_start = 1
                    else:
                        d_start = 0
                else:
                    if abd_should_be_odd:
                        d_start = 0
                    else:
                        d_start = 1
            else:
                d_start = 0
                d_steps = 1

            for d in range(d_start, abcd - a - b + 1, d_steps):
                c = abcd - a - b - d

                state = ''

                for i in range(n):
                    if i in ons:
                        state += '1'
                    elif i in offs:
                        state += '0'
                    else:
                        clicks_by_b = i % 2 == 0
                        clicks_by_d = i % 3 == 0

                        total_clicks = a

                        if clicks_by_b:
                            total_clicks += b
                        else:
                            total_clicks += c

                        if clicks_by_d:
                            total_clicks += d

                        i_is_on = total_clicks % 2 == 0

                        if i_is_on:
                            state += '1'
                        else:
                            state += '0'
                possible_states.add(state)

    possible_states = list(possible_states)
    possible_states.sort()
    return possible_states


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