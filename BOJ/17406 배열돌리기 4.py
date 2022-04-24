from copy import deepcopy

N, M, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
b = deepcopy(board)
moves = []
result = 987654321
for _ in range(K):
    r, c, s = map(int, input().split())
    moves.append((r - 1, c - 1, s))


def rotate(r, c, s):
    """
    (r, c) -> 중심 좌표
    s - > 떨어진 거리
    """
    global b
    sy = r - s
    ey = r + s
    sx = c - s
    ex = c + s

    while sy < ey and sx < ex:
        to_rotate = []
        locs = []
        for x in range(sx, ex + 1):
            to_rotate.append(b[sy][x])
            locs.append((sy, x))

        for y in range(sy + 1, ey):
            to_rotate.append(b[y][ex])
            locs.append((y, ex))

        for x in range(ex, sx - 1, -1):
            to_rotate.append(b[ey][x])
            locs.append((ey, x))

        for y in range(ey - 1, sy, -1):
            to_rotate.append(b[y][sx])
            locs.append((y, sx))

        tmp = to_rotate.pop()
        to_rotate.insert(0, tmp)

        for i in range(len(locs)):
            y, x = locs[i]
            b[y][x] = to_rotate[i]

        sy += 1
        ey -= 1
        sx += 1
        ex -= 1


def _perm(l, visited):
    global result, b
    if len(l) == K:
        for i in l:
            r, c, s = moves[i]
            rotate(r, c, s)

        for r in b:
            result = min(result, sum(r))
        b = deepcopy(board)
        return

    for i in range(K):
        if visited[i]: continue
        visited[i] = True
        l.append(i)
        _perm(l, visited)
        l.pop()
        visited[i] = False


def perm():
    visited = [False] * K
    _perm([], visited)


perm()
print(result)
#
# rotate(2, 3, 1)
# for r in b:
#     print(r)