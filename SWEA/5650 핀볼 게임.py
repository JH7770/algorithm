from collections import defaultdict
T = int(input())
N = 0
BLACKHOLE = -1
 #     ↑  →  ↓  ←
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
dir2dir = [
    (),
#    UP   RIGHT  DOWN  LEFT
    (DOWN, LEFT, RIGHT, UP),
    (RIGHT, LEFT, UP, DOWN),
    (LEFT, DOWN, UP, RIGHT),
    (DOWN, UP, LEFT, RIGHT),
    (DOWN, LEFT, UP, RIGHT)
]

def p(board):
    for r in board:
        print(r)
    print()

def out_of_range(y, x):
    return y < 0 or x < 0 or y >= N or x >= N

for t_case in range(1, T+1):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]
    n2hole = defaultdict(list)
    for y in range(N):
        for x in range(N):
            if 6 <= board[y][x] <= 10:
                n2hole[board[y][x]].append((y, x))
    result = 0

    for y in range(N):
        for x in range(N):
            if board[y][x] != 0:
                continue
            for d in range(4):
                dir = d
                cnt = 0
                ny = y
                nx = x
                wall_flag = False
                while True:
                    ny = ny + dy[dir]
                    nx = nx + dx[dir]
                    # print(ny,nx)
                    if out_of_range(ny, nx):
                        dir = (dir + 2) % 4
                        cnt += 1
                    elif (ny, nx) == (y, x) or board[ny][nx] == BLACKHOLE:
                        break
                    elif 1 <= board[ny][nx] <= 5:
                        dir = dir2dir[board[ny][nx]][dir]
                        cnt += 1
                    elif 6 <= board[ny][nx] <= 10:
                        holes = n2hole[board[ny][nx]]
                        to_move = [hole for hole in holes if hole != (ny, nx)].pop()
                        ny = to_move[0]
                        nx = to_move[1]
                        # ny = ny + dy[dir]
                        # nx = nx + dx[dir]


                if result < cnt:
                    result = cnt
    print(f"#{t_case} {result}")


    p(board)
