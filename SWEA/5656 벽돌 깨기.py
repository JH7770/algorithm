from copy import deepcopy
T = int(input())
board = list()
new_board = list()
N, W, H = 0, 0 ,0

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
result = 987654321


def delete_ball(y, x):
    global new_board
    distance = new_board[y][x]
    new_board[y][x] = 0
    for d in range(4):
        for dist in range(1, distance):
            ny = y + dy[d] * dist
            nx = x + dx[d] * dist

            if ny < 0 or nx < 0 or ny >= H or nx >= W or new_board[ny][nx] == 0:
                continue
            delete_ball(ny, nx)



def arrange_and_count():
    global new_board, result

    for x in range(W):
        for y in range(H-1, 0, -1):
            if new_board[y][x] == 0:
                to_change_y = y
                for y2 in range(to_change_y-1, -1, -1):
                    if new_board[y2][x] != 0:
                        new_board[to_change_y][x] = new_board[y2][x]
                        new_board[y2][x] = 0
                        break

    cnt = 0
    for y in range(H):
        for x in range(W):
            if new_board[y][x] != 0:
                cnt += 1

    if result > cnt:
        result = cnt


def drop(orders):
    global new_board
    new_board = deepcopy(board)
    for idx in orders:
        for y in range(H):
            if new_board[y][idx] != 0:
                delete_ball(y, idx)
                arrange_and_count()
                break


def perm(orders):
    if len(orders) == N:
        drop(orders)
        return

    for i in range(W):
        orders.append(i)
        perm(orders)
        orders.pop()



for t_case in range(1, T+1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    perm([])
    print(f"#{t_case} {result}")
    result = 987654321