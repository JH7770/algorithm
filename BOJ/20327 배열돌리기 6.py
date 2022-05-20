N, R = map(int, input().split())
N = 2 ** N
<<<<<<< HEAD
board = [list(map(int, input().split())) for _ in range(N)]
opers = [tuple(map(int, input().split())) for _ in range(R)]


def divide_by_l(l):
    global board
    ret = []
    length = 2 ** l

    for y in range(0, N, length):
        for x in range(0, N, length):
            ret.append((y, x))
    return ret


def rotate1(l, locs): # 부분배열 상하 반전
    global board
    length = 2 ** l
    new_board = [[0] * N for _ in range(N)]
    for sy, sx in locs:
        ey, ex = sy + length, sx + length

        for y in range(sy, ey):
            for x in range(sx, ex):
                new_board[y][x] = board[sy+ey-1-y][x]
    board = new_board

def rotate2(l, locs): # 부분배열 좌우 반전
    global board
    length = 2 ** l
    new_board = [[0] * N for _ in range(N)]
    for sy, sx in locs:
        ey, ex = sy + length, sx + length

        for y in range(sy, ey):
            for x in range(sx, ex):
                new_board[y][x] = board[y][sx+ex-1-x]
    board = new_board

def rotate3(l, locs): # 부분배열 오른쪽 90도 회전
    global board
    length = 2 ** l
    new_board = [[0] * N for _ in range(N)]
    for sy, sx in locs:
        ey, ex = sy + length, sx + length

        for y in range(sy, ey):
            for x in range(sx, ex):
                new_board[y][x] = board[ex-x-1+sy][y-sy+sx]
    board = new_board

def rotate4(l, locs):
    global board
    length = 2 ** l
    new_board = [[0] * N for _ in range(N)]
    for sy, sx in locs:
        ey, ex = sy + length, sx + length

        for y in range(sy, ey):
            for x in range(sx, ex):
                new_board[y][x] = board[x-sx+sy][ey-1-y+sx]
    board = new_board

def rotate5(l, locs):
    global board
    length = 2 ** l
    new_board = [[0] * N for _ in range(N)]
    for sy, sx in locs:
        ey, ex = sy + length, sx + length

        for y in range(sy, ey):
            for x in range(sx, ex):
                new_board[N-length-2*sy+y][x] = board[y][x]
    board = new_board


def rotate6(l, locs):
    global board
    length = 2 ** l
    new_board = [[0] * N for _ in range(N)]
    for sy, sx in locs:
        ey, ex = sy + length, sx + length

        for y in range(sy, ey):
            for x in range(sx, ex):
                new_board[y][N-length-2*sx+x] = board[y][x]
    board = new_board

def rotate7(l, locs):
    global board
    length = 2 ** l
    new_board = [[0] * N for _ in range(N)]
    for sy, sx in locs:
        ey, ex = sy + length, sx + length

        for y in range(0, length):
            for x in range(0, length):
                new_board[y + sx][N - length - sy + x] = board[sy+y][sx+x]
    board = new_board

def rotate8(l, locs):
    global board
    length = 2 ** l
    new_board = [[0] * N for _ in range(N)]
    for sy, sx in locs:
        ey, ex = sy + length, sx + length

        for y in range(0, length):
            for x in range(0, length):
                new_board[N - length - sx + y][sy + x] = board[sy+y][sx+x]
    board = new_board


def rotate(k, l, locs):
    if   k == 1: rotate1(l, locs)
    elif k == 2: rotate2(l, locs)
    elif k == 3: rotate3(l, locs)
    elif k == 4: rotate4(l, locs)
    elif k == 5: rotate5(l, locs)
    elif k == 6: rotate6(l, locs)
    elif k == 7: rotate7(l, locs)
    elif k == 8: rotate8(l, locs)


for k, l in opers:
    divided_locs = divide_by_l(l)
    rotate(k, l, divided_locs)

for r in board:
    print(str(r).replace("[","").replace("]","").replace(",",""))
=======

board = [list(map(int, input().split())) for _ in range(N)]
change_info = [tuple(map(int, input().split())) for _ in range(R)]


def rotate1(l):
    global board, N
    new_board = [[0] * N for _ in range(N)]

    n = 2 ** l
    for sy in range(0, N, n):
        for sx in range(0, N, n):
            for y in range(n):
                for x in range(n):
                    new_board[sy+y][sx+x] = board[sy+n-1-y][sx+x]
    board = new_board

def rotate2(l):
    global board, N
    new_board = [[0] * N for _ in range(N)]

    n = 2 ** l
    for sy in range(0, N, n):
        for sx in range(0, N, n):
            for y in range(n):
                for x in range(n):
                    new_board[sy+y][sx+x] = board[sy+y][sx+n-1-x]
    board = new_board

def rotate3(l):
    global board, N
    new_board = [[0] * N for _ in range(N)]

    n = 2 ** l
    for sy in range(0, N, n):
        for sx in range(0, N, n):
            for y in range(n):
                for x in range(n):
                    new_board[sy+y][sx+x] = board[sy+n-1-x][sx+y]
    board = new_board


def rotate4(l):
    global board, N
    new_board = [[0] * N for _ in range(N)]

    n = 2 ** l
    for sy in range(0, N, n):
        for sx in range(0, N, n):
            for y in range(n):
                for x in range(n):
                    new_board[sy+y][sx+x] = board[sy+x][sx+n-1-y]
    board = new_board

def rotate5(l):
    global board, N
    new_board = [[0] * N for _ in range(N)]

    n = 2 ** l
    for sy in range(0, N, n):
        for sx in range(0, N, n):
            ny = (N-sy-n) % N
            for y in range(n):
                for x in range(n):
                    new_board[sy+y][sx+x] = board[ny+y][sx+x]
    board = new_board

def rotate7(l):
    global board, N
    new_board = [[0] * N for _ in range(N)]

    n = 2 ** l
    for sy in range(0, N, n):
        for sx in range(0, N, n):
            for y in range(n):
                for x in range(n):
                    new_board[sy+y][sx+x] = board[N-n-sx+y][sy+x]
    board = new_board

def rotate8(l):
    global board, N
    new_board = [[0] * N for _ in range(N)]

    n = 2 ** l
    for sy in range(0, N, n):
        for sx in range(0, N, n):
            for y in range(n):
                for x in range(n):
                    new_board[sy+y][sx+x] = board[sx+y][N-n-sy+x]
    board = new_board

def rotate6(l):
    global board, N
    new_board = [[0] * N for _ in range(N)]

    n = 2 ** l
    for sy in range(0, N, n):
        for sx in range(0, N, n):
            nx = (N-sx-n) % N
            for y in range(n):
                for x in range(n):
                    new_board[sy+y][sx+x] = board[sy+y][nx+x]
    board = new_board

def p():
    for r in board:
        print(str(r).replace(',','').replace('[', '').replace(']', ''))
    print()

for k, l in change_info:
    if k == 1: rotate1(l)
    elif k == 2: rotate2(l)
    elif k == 3: rotate3(l)
    elif k == 4: rotate4(l)
    elif k == 5: rotate5(l)
    elif k == 6:rotate6(l)
    elif k == 7 : rotate7(l)
    elif k == 8: rotate8(l)
p()

>>>>>>> a7767397a8d87df81d9fe0eac6af1b1a8608da6c
