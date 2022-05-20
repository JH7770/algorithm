from collections import deque
from operator import itemgetter
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
shark = []
for y in range(N):
    for x in range(N):
        if board[y][x] == 9:
            board[y][x] = 0
            shark = [y, x, 2]
            break

def out_of_range(y, x):
    return y < 0 or x < 0 or y >= N or x >= N

cnt = 0
shark_eat_count = 0
def move():
    global shark_eat_count, shark, cnt
    shark_y, shark_x, shark_size = shark

    q = deque()
    q.append((shark_y, shark_x, 0))
    visited = [[False] * N for _ in range(N)]
    visited[shark_y][shark_x] = True

    dist_map = [[0] * N for _ in range(N)]
    min_dist = int(10e9)
    can_eat_list = []
    while q:
        sy, sx, dist = q.popleft()
        if 0 < board[sy][sx] < shark_size:
            if min_dist > dist:
                min_dist = dist
            can_eat_list.append((sy, sx, dist))
            dist_map[sy][sx] = dist

        for d in range(4):
            ny = sy + dy[d]
            nx = sx + dx[d]

            if out_of_range(ny, nx) or visited[ny][nx]:
                continue
            elif board[ny][nx] <= shark_size:
                q.append((ny, nx, dist+1))
                visited[ny][nx] = True

    if can_eat_list == []:
        return False
    can_eat_list = sorted([(y, x, d) for y, x, d in can_eat_list if d == min_dist], key=itemgetter(0, 1))
    y, x, dist = can_eat_list[0]
    board[y][x] = 0
    shark_eat_count += 1
    shark = [y, x, shark_size]
    if shark_eat_count == shark_size:
        shark = [y, x, shark_size+1]
        shark_eat_count = 0
    cnt += dist
    return True



while move():
    continue
print(cnt)
# def count_fish():
#     fish_list = []
#     for y in range(N):
#         for x in range(N):
#             if board[y][x] == 0:
#                 continue
#             if board[y][x] > 0 and board[y][x] != 9 and board[y][x] < shark[2]:
#                 fish_list.append((y, x))
#     return fish_list
#
# def get_to_eat(fish_list):
#     dist_list = []
#     shark_y, shark_x, shark_size = shark
#     for y, x in fish_list:
#         dist = abs(y - shark_y) + abs(x - shark_x)
#         dist_list.append(dist)
#     min_dist = min(dist_list)
#
#     to_eat = (-1, -1)
#     for i, loc in enumerate(fish_list):
#         if dist_list[i] != min_dist:
#             continue
#         if to_eat == (-1, -1):
#             to_eat = loc
#         else:
#             if to_eat[0] > loc[0]:
#                 to_eat = loc
#             elif to_eat[0] == loc[0] and to_eat[1] > loc[1]:
#                 to_eat = loc
#     return to_eat
#
# def out_of_range(y, x):
#     return y < 0 or x < 0 or y >= N or x >= N
#
# eat_count = 0
# def eat_to_go(to_eat):
#     global shark, eat_count
#     shark_y, shark_x, shark_size = shark
#     print(shark)
#     q = deque()
#     q.append((shark_y, shark_x, 0))
#     visited = [[False] * N for _ in range(N)]
#     visited[shark_y][shark_x] = True
#
#     while q:
#         y, x, dist = q.popleft()
#         if (y, x) == to_eat:
#             board[y][x] = 0
#             eat_count += 1
#             shark = [y, x, shark_size]
#             if eat_count == shark_size:
#                 shark = [y, x, shark_size+1]
#                 eat_count = 0
#             return dist
#         for d in range(4):
#             ny = y + dy[d]
#             nx = x + dx[d]
#             if out_of_range(ny, nx) or visited[ny][nx]:
#                 continue
#             elif board[ny][nx] > shark_size:
#                 visited[ny][nx] = True
#                 continue
#             else:
#                 q.append((ny, nx, dist+1))
#                 visited[ny][nx] = True
#
#     return 0
#
# cnt = 0
# while True:
#     fish_list = count_fish()
#
#     if fish_list == []:
#         break
#     to_eat = get_to_eat(fish_list)
#     print(f"shark : {shark}")
#     print(f"fish list : {fish_list}")
#     print(f"to_eat : {to_eat}")
#     for r in board:
#         print(r)
#
#     dist = eat_to_go(to_eat)
#     cnt += dist
#     print(f"dist : {dist} cnt : {cnt}")
#     print()
#
#
#
# print(cnt)
