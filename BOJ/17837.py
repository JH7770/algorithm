from collections import defaultdict

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
loc2horses = defaultdict(list)
num2horses = defaultdict(tuple)

for num in range(K):
    y, x, d = map(int, input().split())
    loc2horses[(y - 1, x - 1)].append((num, d - 1))
    num2horses[num] = (y - 1, x - 1, d - 1)

# →, ←, ↑, ↓
dy = (0, 0, -1, 1)
dx = (1, -1, 0, 0)
W, R, B = 0, 1, 2


def out_of_range(y, x):
    return y < 0 or x < 0 or y >= N or x >= N


def update():
    global loc2horses, num2horses
    num2horses = defaultdict(tuple)
    for k, v in loc2horses.items():
        y, x = k
        if len(v) >= 4:
            return False
        for n, d in v:
            num2horses[n] = (y, x, d)
    return True



def move(num):
    global loc2horses, num2horses
    y, x, d = num2horses[num]

    ny = y + dy[d]
    nx = x + dx[d]

    cur_horse_idx = 0
    for i, v in enumerate(loc2horses[(y, x)]):
        if v[0] == num:
            cur_horse_idx = i

    if out_of_range(ny, nx) or board[ny][nx] == B:
        d = d + 1 if d in [0, 2] else d - 1
        ny = y + dy[d]
        nx = x + dx[d]
        loc2horses[(y, x)][cur_horse_idx] = (num, d)
        if out_of_range(ny, nx) or board[ny][nx] == B:
            return
        elif board[ny][nx] == W:
            to_move = loc2horses[(y, x)][cur_horse_idx:]
            loc2horses[(ny, nx)].extend(to_move)
            loc2horses[(y, x)] = loc2horses[(y, x)][:cur_horse_idx]
        elif board[ny][nx] == R:
            to_move = list(reversed(loc2horses[(y, x)][cur_horse_idx:]))
            loc2horses[(ny, nx)].extend(to_move)
            loc2horses[(y, x)] = loc2horses[(y, x)][:cur_horse_idx]
            # loc2horses[(y, x)].pop(cur_horse_idx)
            # loc2horses[(ny, nx)].append((num, d))
    elif board[ny][nx] == W:
        to_move = loc2horses[(y, x)][cur_horse_idx:]
        loc2horses[(ny, nx)].extend(to_move)
        loc2horses[(y, x)] = loc2horses[(y, x)][:cur_horse_idx]
    elif board[ny][nx] == R:
        to_move = list(reversed(loc2horses[(y, x)][cur_horse_idx:]))
        loc2horses[(ny, nx)].extend(to_move)
        loc2horses[(y, x)] = loc2horses[(y, x)][:cur_horse_idx]

    if len(loc2horses[(y, x)]) == 0:
        loc2horses.pop((y, x))
def p():
    for i in range(N):
        print([len(loc2horses[(i, j)]) for j in range(N)])
    print()
def solve():
    turn = 0
    while turn <= 1000:
        turn += 1
        for i in range(K):
            move(i)
            if not update():
                print(turn)
                exit()
                break
    print(-1)


solve()
