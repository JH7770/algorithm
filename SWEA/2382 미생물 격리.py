from collections import defaultdict
T = int(input())
N, M, K = 0, 0, 0

dy = (0, -1,  1,  0, 0)
dx = (0,  0,  0, -1, 1)


def red_zone(y, x):
    return y == 0 or x == 0 or y == N - 1 or x == N -1


for t_case in range(1, T+1):
    N, M, K = map(int, input().split())

    bug_info = {}
    for _ in range(K):
        y, x, n, d = map(int, input().split())
        bug_info[(y, x)] = (n, d)

    for _ in range(M):
        new_bug_info = defaultdict(list)

        for k, v in bug_info.items():
            y, x = k
            n, d = v
            ny = y + dy[d]
            nx = x + dx[d]

            if red_zone(ny, nx):
                n = n // 2
                d = d + 1 if d in [1, 3] else d - 1
            new_bug_info[(ny, nx)].append((n, d))

        bug_info = {}
        for k, v in new_bug_info.items():
            sum_n = 0
            final_d = 0
            max_n = 0
            for (n, d) in v:
                if n > max_n:
                    max_n = n
                    final_d = d
                sum_n += n
            bug_info[k] = (sum_n, final_d)

    sum = 0
    for k, v in bug_info.items():
        sum += v[0]
    print(f"#{t_case} {sum}")