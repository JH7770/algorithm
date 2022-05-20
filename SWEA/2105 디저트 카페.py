T = int(input())
N = 0
board = []

result = -1

dy = (1,  1,  -1, -1)
dx = (1, -1,  -1,  1)

visited = []
start_loc = ()

def out_of_range(y, x):
    return y < 0 or x < 0 or y >= N or x >= N


def dfs(y, x ,cafe_number, dir):
    print(id(cafe_number))
    if dir == 4:
        if (y, x) == start_loc:
            global result
            if result < len(cafe_number):
                result = len(cafe_number)
        return
    ny = y + dy[dir]
    nx = x + dx[dir]
    while not out_of_range(ny, nx) and board[ny][nx] not in cafe_number:
        cafe_number.append(board[ny][nx])
        dfs(ny, nx, cafe_number.copy(), dir+1)
        ny = ny + dy[dir]
        nx = nx + dx[dir]


for t_case in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    result = -1
    for y in range(N):
        for x in range(N):
            start_loc = (y, x)
            dfs(y, x, [], 0)
    print(f"#{t_case} {result}")