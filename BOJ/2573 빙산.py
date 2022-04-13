from collections import deque
from copy import deepcopy
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def out_of_range(y, x):
    return y < 0 or x < 0 or y >= N or x >= M

def melt():
    global board
    new_board = deepcopy(board)

    exist_ice_flag = False
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                continue
            exist_ice_flag = True
            seawater = 0
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if out_of_range(ny, nx) or board[ny][nx] != 0:
                    continue
                else:
                    seawater += 1
            new_board[y][x] -= seawater
            if new_board[y][x] < 0:
                new_board[y][x] = 0

    if not exist_ice_flag:
        return False
    board = new_board
    return True


def area_count():
    global board
    visited = [[False] * M for _ in range(N)]

    cnt = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0 or visited[y][x]:
                continue
            else:
                cnt += 1

                q = deque()
                q.append((y, x))
                visited[y][x] = True

                while q:
                    sy, sx = q.popleft()
                    for d in range(4):
                        ny = sy + dy[d]
                        nx = sx + dx[d]

                        if out_of_range(ny, nx) or board[ny][nx] == 0 or visited[ny][nx]:
                            continue
                        else:
                            q.append((ny, nx))
                            visited[ny][nx] = True
    return cnt

cnt = 0
while True:
    cnt += 1
    if not melt():
        cnt = 0
        break
    if area_count() >= 2:
        break
print(cnt)








