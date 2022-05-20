from collections import deque

T = int(input())
M = 0
board = []
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def out_of_range(y, x):
    return y < 0 or  x < 0 or y >= N or x >= N

def dist(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

def bfs(sy, sx, k):
    count = 0
    for y in range(N):
        for x in range(N):
            if board[y][x] == 0 or dist((sy, sx), (y, x)) > k - 1:
                continue
            count += 1
    return count

# def bfs(y, x, k):
#     visited = [[False] * N for _ in range(N)]
#     visited[y][x] = True
#
#     # q = deque()
#     # q.append((y, x))
#     # cnt = 0
#     # while q:
#     #     sy, sx = q.popleft()
#     #     if board[sy][sx] == 1:
#     #         cnt += 1
#     #     for d in range(4):
#     #         ny = sy + dy[d]
#     #         nx = sx + dx[d]
#     #
#     #         if out_of_range(ny, nx) or visited[ny][nx]:
#     #             continue
#     #         elif dist((sy, sx), (ny, nx)) > k:
#     #             continue
#     #         else:
#     #             visited[ny][nx] = True
#     #             q.append((ny, nx))
#
#     return cnt

for t_case in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for k in range(1, N+1):
        cost = k ** 2 + (k - 1) ** 2
        for y in range(N):
            for x in range(N):
                cnt = bfs(y, x, k)
                pay = cnt * M
                if pay >= cost:
                    if result < cnt:
                        result = cnt

    print(f"#{t_case} {result}")