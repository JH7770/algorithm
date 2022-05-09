R, C, T = map(int, input().split())
board = [list(map(int ,input().split())) for _ in range(R)]


upper_air = (-1, -1)
lower_air = (-1, -1)

RIGHT, UP, LEFT, DOWN = 0, 1, 2, 3
dy = (0, -1, 0, 1)
dx = (1, 0, -1, 0)

def out_of_range(y, x):
    return y < 0 or x < 0 or y >= R or x >= C


def spread_dust():
    global board
    new_board = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if board[y][x] == -1:
                new_board[y][x] = -1
            elif board[y][x] > 0:
                total_spread = 0
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]

                    if out_of_range(ny, nx) or board[ny][nx] == -1:
                        continue
                    dust = board[y][x] // 5
                    new_board[ny][nx] += dust
                    total_spread += dust
                new_board[y][x] += board[y][x] - total_spread

    board = new_board

def air_machine_work():
    global board
    d_list = [UP, RIGHT, DOWN, LEFT]
    y, x = upper_air
    for d in d_list:
        while True:
            ny = y + dy[d]
            nx = x + dx[d]

            if out_of_range(ny, nx) or ny > upper_air[0] or board[ny][nx] == -1:
                break
            if board[y][x] != -1:
                board[y][x] = board[ny][nx]
                board[ny][nx] = 0
            y = ny
            x = nx
    d_list = [DOWN, RIGHT, UP, LEFT]
    y, x = lower_air
    for d in d_list:
        while True:
            ny = y + dy[d]
            nx = x + dx[d]

            if out_of_range(ny, nx) or ny < lower_air[0] or board[ny][nx] == -1:
                break
            if board[y][x] != -1:
                board[y][x] = board[ny][nx]
                board[ny][nx] = 0
            y = ny
            x = nx



for y in range(R):
    if board[y][0] == -1:
        upper_air = (y, 0)
        lower_air = (y+1, 0)
        break


if __name__ == "__main__":
    for i in range(T):
        spread_dust()
        air_machine_work()
    sum = 0
    for y in range(R):
        for x in range(C):
            if board[y][x] == -1:
                continue
            sum += board[y][x]
    print(sum)
