from collections import deque, defaultdict

T = int(input())
#     상 우 하 좌
U, R, D, L = 0, 1, 2, 3
dy = (-1, 0, 1, 0)
dx = ( 0, 1, 0, -1)

can_go = [
    [],
    [U, R, D, L],
    [U, D],
    [L, R],
    [U, R],
    [D, R],
    [D, L],
    [U, L]
]

def out_of_range(y, x):
    return y < 0 or x < 0 or y >= N or x >= M

def bfs(y, x):
    global N, M, C, L, board, connected

    visited = [[False] * M for _ in range(N)]

    q = deque()
    q.append((y, x, 1))
    visited[y][x] = True
    cnt = 1
    while q:
        sy, sx, s = q.popleft()
        if s  == L:
            continue
        for ny, nx in connected[(sy, sx)]:
            if visited[ny][nx]:
                continue
            if (sy, sx) not in connected[(ny, nx)]:
                continue
            visited[ny][nx] = True
            cnt += 1
            q.append((ny, nx, s+1))

    return cnt


for t_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    connected = defaultdict(list)

    board = [list(map(int, input().split())) for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                continue
            type = board[y][x]
            for d in can_go[type]:
                ny = y + dy[d]
                nx = x + dx[d]

                if out_of_range(ny, nx) or board[y][x] == 0:
                    continue
                connected[(y, x)].append((ny, nx))


    print(f"#{t_case} {bfs(R, C)}")