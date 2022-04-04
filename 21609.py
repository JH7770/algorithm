from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

EMPTY, BLACK, RAINBOW = -2, -1, 0
used = [[False] * N for _ in range(N)]
score = 0
dy, dx = (-1, 0, 1, 0), (0, -1, 0, 1)


def pboard():
    print("score : {}".format(score))
    for b in board:
        print(b)
    print()


def out_ot_range(y, x):
    return y < 0 or x < 0 or y >= N or x >= N


def bfs(y, x, block_number):
    global used
    q = deque()
    q.append((y, x))
    used[y][x] = True
    block_group = []
    rainbows = []

    while q:
        sy, sx = q.popleft()
        block_group.append((sy, sx))
        for d in range(4):
            ny = sy + dy[d]
            nx = sx + dx[d]

            if out_ot_range(ny, nx) or used[ny][nx]:
                continue
            elif board[ny][nx] in [RAINBOW, block_number]:
                q.append((ny, nx))
                used[ny][nx] = True
                if board[ny][nx] == RAINBOW:
                    rainbows.append((ny, nx))
    for y, x in rainbows:
        used[y][x] = False
    return block_group, len(rainbows)


def is_greater(best_group, best_rainbows, best_start_loc,
               compared_group, compared_rainbows, compared_start_loc):
    if len(best_group) < len(compared_group):
        return True
    elif len(best_group) == len(compared_group):
        if best_rainbows < compared_rainbows:
            return True
        elif best_rainbows == compared_rainbows:
            if best_start_loc[0] < compared_start_loc[0]:
                return True
            elif best_start_loc[0] == compared_start_loc[0]:
                if best_start_loc[1] < compared_start_loc[1]:
                    return True
    return False


def find_block_group():
    global used
    used = [[False] * N for _ in range(N)]
    best_group = []
    best_rainbows = 0
    best_start_loc = (-1, -1)

    for y in range(N):
        for x in range(N):
            if used[y][x] or board[y][x] in [EMPTY, BLACK, RAINBOW]: continue
            block_group, rainbows = bfs(y, x, board[y][x])
            if is_greater(best_group, best_rainbows, best_start_loc, block_group, rainbows, (y, x)):
                best_group = block_group
                best_rainbows = rainbows
                best_start_loc = (y, x)
    return best_group


def get_score_and_del_blocks(best_group):
    global board, score
    for y, x in best_group:
        board[y][x] = EMPTY
    score += len(best_group) ** 2


def work_gravity():
    for y in range(N - 2, -1, -1):
        for x in range(N):
            if board[y][x] < 0: continue
            for z in range(y + 1, N):
                if board[z][x] == EMPTY:
                    board[z - 1][x], board[z][x] = board[z][x], board[z - 1][x]
                else:
                    break


def rotate90():
    global board
    new_board = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            new_board[y][x] = board[x][N - 1 - y]
    board = new_board


while True:
    best_group = find_block_group()
    if len(best_group) == 1:
        break
    get_score_and_del_blocks(best_group)
    work_gravity()
    rotate90()
    work_gravity()
print(score)

