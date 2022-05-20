from collections import deque

N, M = map(int, input().split())
board = [[False] * M for _ in range(N)]
for i in range(N):
    s = input()
    for j in range(M):
        if s[j] == '1':
            board[i][j] = 1



dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def bfs():
    dist_map = [[0] * M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    dist_map[0][0] = 1
    while q:
        y, x = q.popleft()
        nd = dist_map[y][x] + 1
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or nx < 0 or ny >= N or nx >= M or board[ny][nx] == False:
                continue
            elif dist_map[ny][nx] != 0: #and dist_map[ny][nx] < nd:
                continue
            else:
                dist_map[ny][nx] = nd
                q.append((ny, nx))

    # for r in dist_map:
    #     print(r)

    print(dist_map[N-1][M-1])
bfs()