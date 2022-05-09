from collections import defaultdict
from copy import deepcopy
N = 10
board = [list(map(int, input().split())) for _ in range(N)]


def if_end(b):
    for y in range(N):
        for x in range(N):
            if b[y][x] == 1:
                return False
    return True

def out_of_range(y, x):
    return y < 0 or x < 0 or y >= N or x >= N


result = 987654321
def dfs(b, count):
    global result

    if sum(count) >= result:


        return
    if if_end(b):
        r = sum(count)
        if result > r:
            result = r
        return
    sy, sx = -1, -1

    for y in range(N):
        flag = False
        for x in range(N):
            if b[y][x] == 1:
                sy, sx = y, x
                flag = True
                break
        if flag:
            break

    for size in range(1, 5+1):
        if count[size] == 5:
            continue

        new_b = [r[:] for r in b]
        new_count = [c for c in count]
        flag = False
        for y in range(size):
            for x in range(size):
                if out_of_range(sy+y, sx+x) or new_b[sy+y][sx+x] != 1:
                    flag = True
                    break
                new_b[sy+y][sx+x] = -size
            if flag:
                break
        if not flag:
            new_count[size] += 1
            dfs(new_b, new_count)

dfs(board, [0]*6)
if result == 987654321:
    result = -1
print(result)