

from collections import defaultdict
from collections import deque
from copy import deepcopy

# 입력, 초기화
R, C, K = map(int, input().split(' '))
board = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
walls = [list(map(int, input().split(' '))) for _ in range(W)]

air_machines = [(x, y) for y in range(C) for x in range(R) if 0 < board[x][y] < 5]
check_list = [(x, y) for y in range(C) for x in range(R) if board[x][y] == 5]
temp_board = [[0] * C for _ in range(R)]
wall = [[[[False for _ in range(C)] for _ in range(R)] for _ in range(C)] for _ in range(R)]
# (x, y)의 벽 확인을 위한 dict 자료형
wall_list = [
    [], [], [], []
]

for x, y, t in walls:
    x -= 1
    y -= 1
    if t == 1:
        wall_list[0].append((x, y + 1))
        wall_list[1].append((x, y))
    else:
        wall_list[2].append((x - 1, y))
        wall_list[3].append((x, y))

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
d = [
    [(0, 1), (1, 1), (-1, 1)],  # RIGHT
    [(0, -1), (1, -1), (-1, -1)],  # LEFT
    [(-1, 0), (-1, 1), (-1, -1)],  # UP
    [(1, 0), (1, 1), (1, -1)]  # DOWN
]



def ptmpboard():
    for b in temp_board:
        print(b)
    print()


def turn_on():
    for x, y in air_machines:
        visited = [[False] * C for _ in range(R)]
        direction = board[x][y] - 1

        q = deque()
        start_x = x + dx[direction]
        start_y = y + dy[direction]
        if start_x < 0 or start_y < 0 or start_x >= R or start_y >= C:
            continue

        # start
        q.append((x + dx[direction], y + dy[direction], 5))

        visited[x][y] = True
        while q:
            sx, sy, tmp = q.popleft()
            temp_board[sx][sy] += tmp
            next_tmp = tmp - 1
            if next_tmp < 0:
                continue
            for dx2, dy2 in d[direction]:
                nx = sx + dx2
                ny = sy + dy2

                if nx < 0 or ny < 0 or nx >= R or ny >= C or visited[nx][ny]:
                    continue
                if (nx, ny) in wall_list[direction]:
                    continue

                q.append((nx, ny, next_tmp))
                visited[nx][ny] = True


def adjust_temp():
    global temp_board
    tmp = deepcopy(temp_board)

    for x in range(R):
        for y in range(C):
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue
                if (nx, ny) in wall_list[d]:
                    continue

                diff = (temp_board[x][y] - temp_board[nx][ny])
                tmp[x][y] -= int(diff / 4)

    temp_board = tmp


def reduce_temp():
    reduce_list = []
    for i in range(C):
        if (0, i) not in reduce_list:
            reduce_list.append((0, i))
        if (R-1, i) not in reduce_list:
            reduce_list.append((R - 1, i))
    for i in range(R):
        if (i, 0) not in reduce_list:
            reduce_list.append((i, 0))
        if (i, C-1) not in reduce_list:
            reduce_list.append((i, C-1))

    for x, y in reduce_list:
        if temp_board[x][y] > 0:
            temp_board[x][y] -= 1


def check_temp():
    # print([temp_board[x][y] for x, y in check_list])
    for x, y in check_list:
        if temp_board[x][y] < K:
            return False
    return True


def solve():
    choco = 0
    while choco <= 100:
        turn_on()
        adjust_temp()
        reduce_temp()
        choco += 1
        if check_temp():
            break
    print(choco)


solve()