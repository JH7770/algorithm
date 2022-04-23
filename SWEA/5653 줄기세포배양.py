from collections import defaultdict

T = int(input())
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

for t_case in range(1, T+1):
    N, M, K = map(int, input().split())

    board = {}
    loc2life = {}
    for i in range(N):
        for j, life in enumerate(list(map(int, input().split()))):
            if life != 0:
                board[(i, j)] = [life, life]
                loc2life[(i, j)] = life

    for _ in range(K):
        spread_loc = []
        for k, v in board.items():
            if v == [-1, -1] or v == [0, 0]:
                continue
            if v[0] > 0: # activate remain
                board[k][0] -= 1
            elif v[0] == 0: # spread
                board[k][0] -= 1
                board[k][1] -= 1

                y, x = k
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    life = loc2life[(y, x)]

                    if (ny, nx) in spread_loc:
                        if loc2life[(ny, nx)] < life:
                            loc2life[(ny, nx)] = life
                    elif (ny, nx) in board.keys():
                        continue
                    else:
                        loc2life[(ny, nx)] = life
                        spread_loc.append((ny, nx))

            elif v[1] >= 0:
                board[k][1] -= 1

        for y, x in spread_loc:
            life = loc2life[(y, x)]
            board[(y, x)] = [life, life]
    cnt = 0

    for k, v in board.items():
        if v == [-1, -1] or v == [0, 0] or v ==[-1, 0]: continue
        cnt += 1
    print(f"#{t_case} {cnt}")


