
R, C, M = map(int, input().split())

board = [[(0, 0, 0)] * C for _ in range(R)]
man_loc = (-1, -1)

dy = (-1, 1, 0, 0)
dx = ( 0,  0, 1, -1)

result = 0

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1
    board[r][c] = (s, d, z)

def move_man():
    global man_loc
    d = 2
    y, x = man_loc
    ny = y + dy[d]
    nx = x + dx[d]

    man_loc = (ny, nx)
    if nx == C:
        return False
    return True

def catch_nearest_shark():
    global result, board

    sy, sx = man_loc
    for y in range(R):
        if board[y][sx] != (0, 0, 0):
            result += board[y][sx][2]
            board[y][sx] = (0, 0, 0)
            break

def out_of_range(y, x):
    return y < 0 or x < 0 or y >= R or x >= C

def shark_move():
    global board
    new_board = [[(0, 0, 0)] * C for _ in range(R)]

    for y in range(R):
        for x in range(C):
            shark_info = board[y][x]
            if shark_info == (0, 0, 0):
                continue
            s, d, z = shark_info

            ny = y
            nx = x

            for _ in range(s):
                ny = ny + dy[d]
                nx = nx + dx[d]

                if out_of_range(ny, nx):
                    d = d + 1 if d in [0, 2] else d - 1
                    ny = ny + dy[d] * 2
                    nx = nx + dx[d] * 2

            if new_board[ny][nx] != (0, 0, 0):
                if new_board[ny][nx][2] < z:
                    new_board[ny][nx] = (s, d, z)
            else:
                new_board[ny][nx] = (s, d, z)
    board = new_board


cnt = 0

while move_man():
    catch_nearest_shark()
    shark_move()
    cnt += 1
print(result)