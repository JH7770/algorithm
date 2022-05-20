from copy import deepcopy
from collections import deque

N, K = map(int, input().split())
board = [[0] * N for _ in range(N)]
board[0] = list(map(int, input().split()))


dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def add_fishes():
    global board

    min_fish_count = min(board[0])
    for i in range(N):
        if board[0][i] == min_fish_count:
            board[0][i] += 1

def move_fishes():
    global board

    sx = 0
    ly, lx = 1, 1

    while sx + ly + lx <= N:

        # print("sx:", sx, " ly:",ly, " lx:",lx)
        for y in range(ly):
            for x in range(lx):
                board[lx-x][sx+y+lx] = board[y][sx+x]
                board[y][sx+x] = 0


        sx += lx
        if ly == lx: ly += 1
        else: lx += 1



def adjust_fishes():
    global board
    new_board = deepcopy(board)

    for y in range(N):
        for x in range(N):
            if board[y][x] == 0:
                continue

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if ny < 0 or nx < 0 or ny >= N or nx >= N or board[ny][nx] == 0:
                    continue

                diff = int((board[ny][nx] - board[y][x]) / 5)
                new_board[y][x] += diff

    board = new_board

    q = []
    for x in range(N):
        for y in range(N):
            if board[y][x] != 0:
                q.append(board[y][x])

    board = [[0] * N for _ in range(N)]
    board[0] = q

def move_fishes2():
    global board

    sx = 0
    ly, lx = 1, int(N/2)

    for i in range(2):
        # print("sx:", sx, " ly:",ly, " lx:",lx)

        global board
        for y in range(ly):
            for x in range(lx):
                board[2*ly-y-1][N-1-x] = board[y][sx+x]
                board[y][sx+x] = 0

        sx += lx
        ly = int(ly*2)
        lx = int(lx/2)


def if_end():
    return (max(board[0]) - min(board[0])) <= K


if __name__ == "__main__":
    result = 0
    while not if_end():
        add_fishes()
        move_fishes()
        adjust_fishes()

        move_fishes2()
        adjust_fishes()
        result += 1
    print(result)
