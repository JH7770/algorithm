N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
rlist = list(map(int, input().split()))

def rotate1():
    global board
    new_board = [[0] * M for _ in range(N)]

    for y in range(N):
        for x in range(M):
            new_board[N-1-y][x] = board[y][x]
    board = new_board

def rotate2():
    global board
    new_board = [[0] * M for _ in range(N)]

    for y in range(N):
        for x in range(M):
            new_board[y][M-1-x] = board[y][x]
    board = new_board

def rotate3():
    global board, M, N
    new_board = [[0] * N for _ in range(M)]

    for x in range(N):
        for y in range(M):
            new_board[y][x] = board[N-x-1][y]

    board = new_board
    N, M = M, N

def rotate4():
    global board, M, N
    new_board = [[0] * N for _ in range(M)]

    for x in range(N):
        for y in range(M):
            new_board[y][x] = board[x][M-y-1]

    board = new_board
    N, M = M, N

def rotate5():
    divided_board = [[[0] * int(M/2) for _ in range(int(N/2))] for _ in range(4)]
    n = int(N/2)
    m = int(M/2)

    for y in range(N):
        for x in range(M):
            if 0 <= y < n and 0 <= x < m:
                divided_board[0][y][x] = board[y][x]
            elif 0 <= y < n and m <= x < M:
                divided_board[1][y][x-m] = board[y][x]
            elif n <= y < N and m <= x < M:
                divided_board[2][y-n][x-m] = board[y][x]
            elif n <= y < N and 0 <= x < m:
                divided_board[3][y-n][x] = board[y][x]

    tmp = divided_board.pop(3)
    divided_board.insert(0, tmp)

    for y in range(N):
        for x in range(M):
            if 0 <= y < n and 0 <= x < m:
                board[y][x] = divided_board[0][y][x]
            elif 0 <= y < n and m <= x < M:
                board[y][x] = divided_board[1][y][x-m]
            elif n <= y < N and m <= x < M:
                board[y][x] = divided_board[2][y-n][x-m]
            elif n <= y < N and 0 <= x < m:
                board[y][x] = divided_board[3][y-n][x]



def rotate6():
    divided_board = [[[0] * int(M/2) for _ in range(int(N/2))] for _ in range(4)]
    n = int(N/2)
    m = int(M/2)

    for y in range(N):
        for x in range(M):
            if 0 <= y < n and 0 <= x < m:
                divided_board[0][y][x] = board[y][x]
            elif 0 <= y < n and m <= x < M:
                divided_board[1][y][x-m] = board[y][x]
            elif n <= y < N and m <= x < M:
                divided_board[2][y-n][x-m] = board[y][x]
            elif n <= y < N and 0 <= x < m:
                divided_board[3][y-n][x] = board[y][x]

    tmp = divided_board.pop(0)
    divided_board.append(tmp)

    for y in range(N):
        for x in range(M):
            if 0 <= y < n and 0 <= x < m:
                board[y][x] = divided_board[0][y][x]
            elif 0 <= y < n and m <= x < M:
                board[y][x] = divided_board[1][y][x-m]
            elif n <= y < N and m <= x < M:
                board[y][x] = divided_board[2][y-n][x-m]
            elif n <= y < N and 0 <= x < m:
                board[y][x] = divided_board[3][y-n][x]




for r in rlist:
    if r == 1:
        rotate1()
    elif r == 2:
        rotate2()
    elif r == 3:
        rotate3()
    elif r == 4:
        rotate4()
    elif r == 5:
        rotate5()
    elif r == 6:
        rotate6()

for r in board:
    s = str(r).replace("[", "").replace("]", "").replace(",", "")
    print(s)

