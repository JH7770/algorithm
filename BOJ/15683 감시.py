N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
wall = []
cctv = []

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


result = int(10e9)

for y in range(N):
    for x in range(M):
        if board[y][x] == 0:
            continue
        elif board[y][x] == 6:
            wall.append((y, x))
        else:
            cctv.append([y, x, board[y][x],0])

def out_of_range(y, x):
    return y < 0 or x < 0 or y >= N or x >= M

def check():
    global board, result
    new_board = [r[:] for r in board]
    for y, x, cctv_number, d in cctv:
        if cctv_number == 1:
            directions = [d]
        elif cctv_number == 2:
            directions = [d, (d+2)%4]
        elif cctv_number == 3:
            directions = [d, (d+1)%4]
        elif cctv_number == 4:
            directions = [d, (d+1)%4, (d+2)%4]
        elif cctv_number == 5:
            directions = [0, 1, 2, 3]

        for direction in directions:
            ny, nx = y, x
            while True:
                ny = ny + dy[direction]
                nx = nx + dx[direction]

                if out_of_range(ny, nx) or board[ny][nx] == 6:
                    break
                else:
                    new_board[ny][nx] = '#'
    cnt = 0
    for r in new_board:
        for v in r:
            if v == 0:
                cnt += 1
    if result > cnt:
        result = cnt
        #
        # for r in new_board:
        #     print(str(r).replace("'", ""))
        # print()

def dfs(depth):
    global cctv
    if depth == len(cctv):
        check()
        return

    for d in range(4):
        cctv[depth][3] = d
        dfs(depth+1)

if cctv == []:
    check()
else:
    dfs(0)

print(result)