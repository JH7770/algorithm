N, R = map(int, input().split())
N = 2 ** N

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

