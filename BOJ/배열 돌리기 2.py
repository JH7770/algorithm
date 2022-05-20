from collections import deque
from math import lcm
N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

sy, sx = 0, 0
ey, ex = N - 1, M - 1
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
    return answer

R = R % gcd_of_rotate()
while sy < ey and sx < ex:
    q = deque()

    for x in range(sx, ex+1):
        q.append(board[sy][x])
    for y in range(sy+1, ey):
        q.append(board[y][ex])
    for x in range(ex,sx-1,-1):
        q.append(board[ey][x])
    for y in range(ey-1, sy, -1):
        q.append(board[y][sx])

    for _ in range(R):
        tmp = q.popleft()
        q.append(tmp)

    for x in range(sx, ex+1):
        board[sy][x] = q.popleft()
    for y in range(sy+1, ey):
        board[y][ex] = q.popleft()
    for x in range(ex,sx-1,-1):
        board[ey][x] = q.popleft()
    for y in range(ey-1, sy, -1):
        board[y][sx] = q.popleft()
    sy += 1
    sx += 1
    ey -= 1
    ex -= 1



for r in board:
    print(str(r).replace('[', '').replace(']','').replace(',',''))