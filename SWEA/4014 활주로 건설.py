T = int(input())
N, X = 0, 0

def out_of_range(x):
    return x < 0 or x >= N


def can_make(l):
    before = l[0]
    visited = [False] * N
    for i in range(1, len(l)):
        if visited[i]: continue
        current = l[i]
        if before < current: # 커지는 경우
            if current - before > 1:
                return False
            for j in range(i-1, i-X-1,-1):
                if visited[j]:
                    return False
                visited[j] = True
                if out_of_range(j):
                    return False
                if current - l[j] != 1:
                    return False
        elif before > current: # 작아지는 경우
            if before - current > 1:
                return False
            for j in range(i, i+X):
                if out_of_range(j):
                    return False
                if before - l[j] != 1:
                    return False
                visited[j] = True

        before = current
    return True

for t_case in range(1, T+1):

    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for r in board:
        if can_make(r):
            cnt += 1
    new_board = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            new_board[y][x] = board[N-x-1][y]
    for r in new_board:
        if can_make(r):
            cnt += 1

    print(f"#{t_case} {cnt}")

    # 1 7
    # 2 4
    # 3 11
    # 4 11
    # 5 15
    # 6 4
    # 7 4
    # 8 1
    # 9 5
    # 10 8
