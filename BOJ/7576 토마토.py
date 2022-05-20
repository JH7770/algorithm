400
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

q = deque()
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            q.append((y, x, 0))

max_nd = 0
while q:
    sy, sx, d = q.popleft()
    if max_nd < d:
        max_nd = d
    nd = d + 1
    for d in range(4):
        ny = sy + dy[d]
        nx = sx + dx[d]

        if ny < 0 or nx < 0 or ny >= N or nx >= M:
            continue
        elif board[ny][nx] != 0:
            continue
        else:
            q.append((ny, nx, nd))
            board[ny][nx] = nd

unavailable = False
for r in board:
    if 0 in r:
        print(-1)
        unavailable = True
        break
if not unavailable:
    print(max_nd)
