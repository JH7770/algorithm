from collections import deque
from math import lcm
N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]



def _rotate90(sy, ey, sx, ex):
    global board
    to_rotate = deque()
    locs = []
    for i in range(sx, ex+1,):
        to_rotate.append(board[sy][i])
        locs.append((sy, i))

    for i in range(sy + 1, ey):
        to_rotate.append(board[i][ex])
        locs.append((i, ex))

    for i in range(ex, sx-1, -1):
        to_rotate.append(board[ey][i])
        locs.append((ey, i))

    for i in range(ey-1, sy, -1):
        if sy < i < ey:
            to_rotate.append(board[i][sx])
            locs.append((i, sx))


    tmp = to_rotate.popleft()
    to_rotate.append(tmp)
    for i in range(len(locs)):
        y, x = locs[i]
        board[y][x] = to_rotate[i]


def rotate90():
    sy = sx = 0
    ey, ex = N-1, M-1

    while sy < ey and sx < ex:
        _rotate90(sy, ey, sx, ex)
        sy += 1
        sx += 1
        ey -= 1
        ex -= 1

def gcd_of_rotate():
    sy = sx = 0
    ey, ex = N-1, M-1

    nums = []
    while sy < ey and sx < ex:
        n = (ey - sy) * 2 + (ex - sx) * 2
        nums.append(n)
        sy += 1
        sx += 1
        ey -= 1
        ex -= 1

    if len(nums) == 1:
        return nums[0]
    answer = 1
    for n in nums:
        answer = lcm(answer, n)
    print(answer)
    return answer

R = R % gcd_of_rotate()
print(R)
for i in range(R):
    rotate90()

for r in board:
    s = str(r)
    s = s.replace("[", "")
    s = s.replace("]", "")
    s = s.replace(",", "")
    print(s)


