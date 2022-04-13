from copy import deepcopy
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
result = 0
def p(locs):
    b = [[0] * M for _ in range(N)]
    for y, x in locs:
        b[y][x] = 1

    for r in b:
        print(r)
    print()

def out_of_range(y, x):
    return y < 0 or x < 0 or y >= N or x >= M

visited = [[False] * M for _ in range(N)]
result = 0

def _dfs(y, x, sum, cnt):
    global visited
    if cnt == 4:
        global result
        if result < sum:
            result = sum
        return

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if out_of_range(ny, nx) or visited[ny][nx]:
            continue
        else:
            visited[ny][nx] = True
            _dfs(ny, nx, sum + board[ny][nx], cnt + 1)
            _dfs(y, x, sum+board[ny][nx], cnt+1)
            visited[ny][nx] = False


def dfs():
    global visited
    for y in range(N):
        for x in range(M):
            visited[y][x] = True
            _dfs(y, x, board[y][x], 1)


dfs()
print(result)

