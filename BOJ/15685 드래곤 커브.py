from collections import defaultdict
N = int(input())

move_info = [list(map(int, input().split())) for _ in range(N)]
dy = (0, -1, 0, 1)
dx = (1, 0, -1, 0)

board = [[0] * 101 for _ in range(101)]
loc2connected = defaultdict(list)

def move(x, y, d, g):
    if g == 0:
        return [d]

    ret = move(x, y, d, g - 1)
    tmp = []
    for d in ret:
        tmp.append((d + 1) % 4)
    ret.extend(reversed(tmp))
    return ret



for x, y, d, g in move_info:
    d_list = move(x, y, d, g)
    board[y][x] = 1
    for d in d_list:
        x = x + dx[d]
        y = y + dy[d]

        if x < 0 or y < 0 or x >= 101 or y >= 101:
            break
        board[y][x] = 1

cnt = 0
for y in range(100):
    for x in range(100):
        if board[y][x] == 1 and board[y+1][x] == 1 and board[y][x+1] == 1 and board[y+1][x+1] == 1:
            cnt += 1
print(cnt)


