from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])

    q = deque()
    q.append((0, 0))

    while q:
        y, x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or nx < 0 or ny >= n or nx >= m or maps[ny][nx] == 0:
                continue
            elif maps[ny][nx] == 0 or maps[ny][nx] > maps[y][x]:
                maps[ny][nx] = maps[y][x] + 1
                q.append((ny, nx))
    for r in maps:
        print(r)
    return maps[n - 1][m - 1] if maps[n - 1][m - 1] != 1 else -1