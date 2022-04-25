T = int(input())

from collections import deque

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

def out_of_range(y, x):
    global N
    return y < 0 or x < 0 or y >= N or x >= N

def _bfs(y, x):
    global board, result


    q = deque()
    visited = [[False] * N for _ in range(N)]
    q.append((y, x, 1))
    visited[y][x] = True
    max_s = 1

    while q:
        sy, sx ,s = q.popleft()
        if max_s < s:
            max_s = s

        for d in range(4):
            ny = sy + dy[d]
            nx = sx + dx[d]

            if out_of_range(ny, nx):
                continue
            elif board[sy][sx] > board[ny][nx]:
                q.append((ny, nx, s+1))
                visited[ny][nx] = True

    if max_s > result:
        result = max_s



def bfs():
    for y, x in max_loc:
        _bfs(y, x)




for t_case in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_height = 0
    for y in range(N):
        for x in range(N):
            if max_height < board[y][x]:
                max_height = board[y][x]
    max_loc = [(y, x) for y in range(N) for x in range(N) if board[y][x] == max_height]




    result = 0
    for y in range(N):
        for x in range(N):
            before = board[y][x]
            bfs()
            for k in range(K):
                board[y][x] -= 1
                bfs()
            board[y][x] = before

    print(f"#{t_case} {result}")



