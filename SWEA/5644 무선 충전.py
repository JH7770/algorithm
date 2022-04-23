from collections import defaultdict
T = int(input())

dy = (0, -1,  0,  1,  0)
dx = (0,  0,  1,  0, -1)

def out_of_range(y, x):
    return y < 0 or x < 0 or y >= 10 or x >= 10


for t_case in range(1, T+1):
    board = [[list() for _ in range(10)] for _ in range(10)]
    M, A = map(int, input().split())
    move_a = list(map(int, input().split()))
    move_b = list(map(int, input().split()))
    bc2power = {}

    for i in range(A):
        x, y, c, p = map(int, input().split())
        y -= 1
        x -= 1
        bc2power[i] = p
        for y2 in range(10):
            for x2 in range(10):
                D = abs(x2-x) + abs(y2-y)
                if D <= c:
                    board[y2][x2].append(i)

    ay, ax = 0, 0
    by, bx = 9, 9

    max = 0
    result = 0
    a_bc = board[ay][ax]
    b_bc = board[by][bx]
    for i in a_bc:
        if max < bc2power[i]:
            max = bc2power[i]
    result += max
    max = 0

    for j in b_bc:
        if max < bc2power[j]:
            max = bc2power[j]
    result += max

    for i in range(M):
        ay = ay + dy[move_a[i]]
        ax = ax + dx[move_a[i]]
        by = by + dy[move_b[i]]
        bx = bx + dx[move_b[i]]

        a_bc = board[ay][ax]
        b_bc = board[by][bx]

        # print(f"{i+1} : {a_bc}, {b_bc}")
        max = 0

        if not a_bc and b_bc:
            for j in b_bc:
                power = bc2power[j]
                if max < power:
                    max = power
        elif not b_bc and a_bc:
            for j in a_bc:
                power = bc2power[j]
                if max < power:
                    max = power
        elif a_bc and b_bc:
            for bc_a in a_bc:
                power_a = bc2power[bc_a]
                for bc_b in b_bc:
                    power_b = bc2power[bc_b]
                    if bc_a == bc_b:
                        total_power = power_a
                    else:
                        total_power = power_a + power_b
                    if max < total_power:
                        max = total_power

        # print(f"{i} : {a_bc}, {b_bc}, {max}")
        result += max





    print(f"#{t_case} {result}")





