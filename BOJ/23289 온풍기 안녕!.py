R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
W = int(input())

wall = [[[[False for _ in range(C)] for _ in range(R)] for _ in range(C)] for _ in range(R)]
for _ in range(3):
    y, x, t = map(int, input().split())
    y -= 1
    x -= 1

