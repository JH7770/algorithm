answer = 0
N, M = 0, 0
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
TURN_A, TURN_B = 0, 1
WINNER_A, WINNER_B = 1, 2
lose, win = 0, 123456789

def check_range(y, x):
    return y < 0 or x < 0 or y >= N or x >= M

def find(board, aloc, bloc, turn, count):
    global lose, win

    y = aloc[0] if turn == TURN_A else bloc[0]
    x = aloc[1] if turn == TURN_A else bloc[1]

    # 내가 밟고 있는 영역이 사라진 경우 패배
    if board[y][x] == 0:
        return True, count
    board[y][x] = 0
    can_go, isWin = False, False

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if check_range(ny, nx) or not board[ny][nx]: continue
        can_go = True
        if turn == TURN_A:
            ret = find(board.copy(), (ny, nx), bloc, TURN_B, count + 1)
        else:
            ret = find(board.copy(), aloc, (ny, nx), TURN_A, count + 1)

        print(ret)
        if ret[0] == True:
            lose = max(lose, ret[1])
        elif ret[0] == False:
            win = min(win, ret[1])
            isWin = True

    # 아무 좌표로도 이동할 수 없는 경우 패배(종료조건1)
    if not can_go:
        return False, count
    # 현재 순번이 이기는 경우
    elif isWin:
        return True, win
    # 현재 순번이 지는 경우
    else:
        return False, lose


def solution(board, aloc, bloc):
    global N, M
    N, M = len(board), len(board[0])
    ret = find(board.copy(), aloc, bloc, TURN_A, 0)

    return ret[1]


cases = [
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]),
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]),
    ([[1, 1, 1, 1, 1]], [0, 0], [0, 4]),
    ([[1]], [0, 0], [0, 0])
]

for c in cases:
    print(solution(c[0], c[1], c[2]))
    answer = 0

"""
answer = 0

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
TURN_A, TURN_B = 0, 1
WINNER_A, WINNER_B = 0, 1


def is_finish(board, loc):
    y, x = loc
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[0]):
            continue
        elif board[ny][nx] == 0:
            continue
        else:
            return False
    return True


def find(board, aloc, bloc, count, turn, winner):
    global answer
    if turn == TURN_A:
        if winner == WINNER_B and is_finish(board, aloc):
            answer = max(count, answer)
            return

        for i in range(4):
            ny = aloc[0] + dy[i]
            nx = aloc[1] + dx[i]

            if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[0]):
                continue
            elif board[ny][nx] == 0:
                continue
            board[aloc[0]][aloc[1]] = 0
            if winner == WINNER_A and aloc == bloc:
                answer = max(count + 1, answer)
            else:
                find(board, (ny, nx), bloc, count + 1, TURN_B, winner)

    elif turn == TURN_B:
        if winner == WINNER_A and is_finish(board, bloc):
            answer = max(count, answer)
            return

        for i in range(4):
            ny = bloc[0] + dy[i]
            nx = bloc[1] + dx[i]

            if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[0]):
                continue
            elif board[ny][nx] == 0:
                continue
            board[bloc[0]][bloc[1]] = 0
            if winner == WINNER_B and aloc == bloc:
                answer = max(count + 1, answer)
            else:
                find(board, aloc, (ny, nx), count + 1, TURN_A, winner)


def solution(board, aloc, bloc):
    find(board.copy(), aloc, bloc, 0, TURN_A, WINNER_A)
    find(board.copy(), aloc, bloc, 0, TURN_A, WINNER_B)

    return answer
"""
