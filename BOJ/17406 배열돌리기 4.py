from copy import deepcopy
N, M, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
moves = []
for _ in range(K):
    r, c, s = map(int, input().split())
    moves.append((r-1, c-1, s))


def rotate(r, c, s):
    to_rotate = []
    for y in range(r-s, r+s+1):
        to_rotate.append(board[y][c-s:c+s+1])

    for r in to_rotate:
        print(r)
    print()
    after_rotate = deepcopy(to_rotate)
    length = len(to_rotate)
    for y in range(length):
        for x in range(length):
            ny = 
            after_rotate[y][x] = to_rotate[][]

    for r in after_rotate:
        print(r)

rotate(2, 3, 2)