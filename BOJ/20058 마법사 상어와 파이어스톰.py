from copy import deepcopy
from collections import deque
N, Q = map(int, input().split())
N = 2 ** N
board = [list(map(int, input().split())) for _ in range(N)]
L_list = list(map(int, input().split()))

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def rotate_by_l(l):
    global board
    length = 2 ** l
    new_board = [[0] * N for _ in range(N)]

    for sy in range(0, N, length):
        for sx in range(0, N, length):
            for y in range(length):
                for x in range(length):
                    new_board[sy+y][sx+x] = board[sy+length-1-x][sx+y]

    board = new_board

def out_of_range(y, x):
    return y < 0 or x < 0 or y >= N or x >= N

def melting():
    global board
    new_board = deepcopy(board)

    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    for y in range(N):
        for x in range(N):
            cnt = 0
            if board[y][x] == 0:
                continue

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if out_of_range(ny, nx) or board[ny][nx] == 0:
                    continue
                cnt += 1
            if cnt < 3:
                new_board[y][x] -= 1
    board = new_board


def get_ice_and_biggest_area():
    sum_of_ice = 0
    biggest_area_cnt = 0
    for r in board:
        sum_of_ice += sum(r)

    visitied = [[False] * N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if board[y][x] == 0:
                continue

            q = deque()
            visitied[y][x] = True
            q.append((y, x))
            cnt = 0
            while q:
                sy, sx = q.popleft()
                cnt += 1

                for d in range(4):
                    ny = sy + dy[d]
                    nx = sx + dx[d]
                    if out_of_range(ny, nx) or board[ny][nx] == 0 or visitied[ny][nx]:
                        continue
                    else:
                        visitied[ny][nx] = True
                        q.append((ny, nx))

            if cnt > biggest_area_cnt:
                biggest_area_cnt = cnt
    print(sum_of_ice)
    print(biggest_area_cnt)


for L in L_list:
    rotate_by_l(L)
    melting()

get_ice_and_biggest_area()
