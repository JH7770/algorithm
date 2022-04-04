from collections import deque
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
def out_of_range(x, y, d1, d2):
    """
    (d1, d2 ≥ 1
    0 ≤ x < x+d1+d2-1 ≤ N,
    0 ≤ y-d1 < y < y+d2 < N)
    """
    if d1 < 1 or d2 < 1: return True
    elif not (x < x + d1 + d2 < N): return True
    elif not (0 <= y - d1): return True
    elif not (y+d2 < N): return True
    return False


def divide(x, y, d1, d2):
    if out_of_range(x, y, d1, d2):
        return 9999999
    boundarys = set()
    for d in range(d1 + 1):
        boundarys.add((x + d, y - d))
        boundarys.add((x + d2 + d, y + d2 - d))

    for d in range(d2 + 1):
        boundarys.add((x + d, y + d))
        boundarys.add((x + d1 + d, y - d1 + d))

    boundarys = list(boundarys)
    b = []
    for i in range(N):
        b.append([int((i, j) in boundarys) for j in range(N)])

    # for r in b:
    #     print(r)
    # print()
    for r in range(N):
        start_c = -1
        for c in range(N):
            if b[r][c]:
                if start_c == -1:
                    start_c = c
                else:
                    for k in range(start_c, c):
                        b[r][k] = 1
                    break
    # for r in b:
    #     print(r)
    #     print()
    boundary_board = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if b[r][c] == 1:
                boundary_board[r][c] = 5
            elif 0 <= r < x + d1 and 0 <= c <= y:
                boundary_board[r][c] = 1
            elif 0 <= r <= x + d2 and y <= c < N:
                boundary_board[r][c] = 2
            elif x + d1 <= r < N and 0 <= c < y - d1 + d2:
                boundary_board[r][c] = 3
            elif x + d2 < r < N and y - d1 + d2 <= c < N:
                boundary_board[r][c] = 4

    # for r in boundary_board:
    #     print(r)
    sum_by_boundarys =[0] * 6
    for r in range(N):
        for c in range(N):
            b_num = boundary_board[r][c]
            sum_by_boundarys[b_num] += board[r][c]
    sum_by_boundarys.pop(0)

    return max(sum_by_boundarys) - min(sum_by_boundarys)

# print(divide(2, 2, 1, 1))
#
min_diff = 987654321
for x in range(N):
    for y in range(N):
        for d1 in range(N):
            for d2 in range(N):
                diff = divide(x, y, d1, d2)
                if diff < min_diff:
                    min_diff = diff
print(min_diff)