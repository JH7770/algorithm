from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
WALL, VIRUS = 1, 2
virus_list = [(y, x) for x in range(N) for y in range(N) if board[y][x] == VIRUS]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
ACTIVE, NON_ACTIVE = 0, -3
def spread_virus(virus):
    virus_map = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == WALL:
                virus_map[i][j] = -WALL
            elif board[i][j] == VIRUS:
                virus_map[i][j] = NON_ACTIVE
    q = deque()
    for i, j in virus:
        virus_map[i][j] = -VIRUS
        q.append((i, j, 0))
        visited[i][j] = True

    max_n = 0
    while q:
        y, x, n = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or nx < 0 or ny >= N or nx >= N or visited[ny][nx]:
                continue
            elif virus_map[ny][nx] == NON_ACTIVE:
                visited[ny][nx] = True
                q.append((ny, nx, n+1))
                virus_map[ny][nx] = n+1
            elif virus_map[ny][nx]  == 0:
                visited[ny][nx] = True
                q.append((ny, nx, n+1))
                virus_map[ny][nx] = n+1
                if n + 1 > max_n:
                    max_n = n + 1

    for i in range(N):
        for j in range(N):
            if virus_map[i][j] == 0:
                return -1
    return max_n




result = 987654321
def select_virus(virus:deque, m):
    if len(virus) == M:
        t = spread_virus(virus)
        global result
        if t == -1: return
        elif t < result:
            result = t
        return
    if m == len(virus_list): return
    virus.append(virus_list[m])
    select_virus(virus, m+1)
    virus.pop()
    select_virus(virus, m+1)

select_virus(deque(), 0)
if result == 987654321:
    result = -1
print(result)