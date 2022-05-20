from copy import deepcopy
import sys
sys.setrecursionlimit(10000)
N, M = map(int , input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

result = 0

def out_of_range(y, x):
    return y < 0 or x < 0 or y >= N or x >= M

for y in range(N):
    for x in range(M):
        if (y, x) == (0, 0):
            dp[y][x] = board[y][x]
            continue

        candylist = [0] * 3
        if not out_of_range(y-1, x):
            candylist[0] = dp[y-1][x]
        if not out_of_range(y, x-1):
            candylist[1] = dp[y][x-1]
        if not out_of_range(y-1, x-1):
            candylist[2] = dp[y-1][x-1]

        dp[y][x] = board[y][x] + max(candylist)


print(dp[N-1][M-1])


