from collections import deque
T = int(input())

def pboard(board):
    print()
    for r in board:
        print(r)
    print()

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
for t_case in range(1, T+1):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1

    visited = [[False] * M for _ in range(N)]
    result = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0 or visited[y][x]:
                continue
            result += 1
            visited[y][x] = True
            q = deque()
            q.append((y, x))

            while q:
                sy, sx = q.popleft()
                for d in range(4):
                    ny = sy + dy[d]
                    nx = sx + dx[d]

                    if ny < 0 or nx < 0 or ny >= N or nx >= M:
                        continue
                    elif board[ny][nx] == 0 or visited[ny][nx]:
                        continue
                    else:
                        q.append((ny, nx))
                        visited[ny][nx] = True
    print(result)

