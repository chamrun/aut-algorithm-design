def solve(n, abcd, ons, offs):

    b_should_be_odd = None
    c_should_be_odd = None
    bd_should_be_odd = None
    cd_should_be_odd = None

    for i in range(n):
        if i in ons:
            i_changed = False
        elif i in offs:
            i_changed = True
        else:
            continue

        by_six = i % 6

        if by_six == 0:
            if bd_should_be_odd is not None and bd_should_be_odd != i_changed:
                return []
            bd_should_be_odd = i_changed
        elif by_six == 1 or by_six == 5:
            if c_should_be_odd is not None and c_should_be_odd != i_changed:
                return []
            c_should_be_odd = i_changed
        elif by_six == 2 or by_six == 4:
            if b_should_be_odd is not None and b_should_be_odd != i_changed:
                return []
            b_should_be_odd = i_changed
        else:
            if cd_should_be_odd is not None and cd_should_be_odd != i_changed:
                return []
            cd_should_be_odd = i_changed

    template = [None] * n

    if bd_should_be_odd is not None:
        char = '0' if bd_should_be_odd else '1'
        for i in range(0, n, 6):
            template[i] = char

    if c_should_be_odd is not None:
        char = '0' if c_should_be_odd else '1'
        for i in range(1, n, 6):
            template[i] = char
        for i in range(5, n, 6):
            template[i] = char

    if b_should_be_odd is not None:
        char = '0' if b_should_be_odd else '1'
        for i in range(2, n, 6):
            template[i] = char
        for i in range(4, n, 6):
            template[i] = char

    if cd_should_be_odd is not None:
        char = '0' if cd_should_be_odd else '1'
        for i in range(3, n, 6):
            template[i] = char

    possible_states = set()

    for a in range(abcd + 1):

        if b_should_be_odd is None:
            b_start = 0
            b_steps = 1
        else:
            b_steps = 2
            if b_should_be_odd:
                b_start = 1
            else:
                b_start = 0

        if c_should_be_odd is not None:
            c_steps = 2
            if c_should_be_odd:
                c_start = 1
            else:
                c_start = 0
        else:
            c_start = 0
            c_steps = 1

        for b in range(b_start, abcd - a + 1, b_steps):

            template_b = template.copy()

            if b_should_be_odd is None:
                char = '0' if (a + b) % 2 == 1 else '1'
                for i in range(2, n, 6):
                    template_b[i] = char
                for i in range(4, n, 6):
                    template_b[i] = char

            for c in range(c_start, abcd - a - b + 1, c_steps):
                d = abcd - a - b - c

                if d < 0:
                    continue

                new_state = template_b.copy()

                bd_is_odd = (a + b + d) % 2 == 0
                    
                if bd_should_be_odd is not None:
                    if bd_should_be_odd:

                        if bd_is_odd:
                            continue
                    else:
                        if not bd_is_odd:
                            continue
                else:
                    char = '0' if bd_is_odd else '1'
                    for i in range(0, n, 6):
                        new_state[i] = char

                cd_is_odd = (a + c + d) % 2 == 1
                            
                if cd_should_be_odd is not None:
                    if cd_should_be_odd:
                        if not cd_is_odd:
                            continue
                    else:
                        if cd_is_odd:
                            continue
                else:
                    char = '0' if (a + c + d) % 2 == 1 else '1'
                    for i in range(3, n, 6):
                        new_state[i] = char

                if c_should_be_odd is None:
                    char = '0' if (a + c) % 2 == 1 else '1'
                    for i in range(1, n, 6):
                        new_state[i] = char
                    for i in range(5, n, 6):
                        new_state[i] = char

                possible_states.add(''.join(new_state))

            # if bd_should_be_odd is not None:
            #     d_steps = 2
            #     if (a + b) % 2 == 0:
            #         if bd_should_be_odd:
            #             d_start = 1
            #         else:
            #             d_start = 0
            #     else:
            #         if bd_should_be_odd:
            #             d_start = 0
            #         else:
            #             d_start = 1
            # else:
            #     d_start = 0
            #     d_steps = 1
            #
            # for d in range(d_start, abcd - a - b + 1, d_steps):
            #     c = abcd - a - b - d
            #
            #     state = ''
            #
            #     for i in range(n):
            #         if i in ons:
            #             state += '1'
            #         elif i in offs:
            #             state += '0'
            #         else:
            #             clicks_by_b = i % 2 == 0
            #             clicks_by_d = i % 3 == 0
            #
            #             total_clicks = a
            #
            #             if clicks_by_b:
            #                 total_clicks += b
            #             else:
            #                 total_clicks += c
            #
            #             if clicks_by_d:
            #                 total_clicks += d
            #
            #             i_is_on = total_clicks % 2 == 0
            #
            #             if i_is_on:
            #                 state += '1'
            #             else:
            #                 state += '0'
            #     possible_states.add(state)

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