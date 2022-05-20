T = int(input())

result = 987654321
def check():
    global board, result
    safe = True
    for x in range(W):
        same_count = 1
        current = board[0][x]
        _safe = False
        for y in range(1, D):
            if board[y][x] == current:
                same_count += 1
                if same_count == K:
                    _safe = True
            else:
                same_count = 1
                current = board[y][x]
        if not _safe:
            safe = False
    return safe


def dfs(r, change_count, max_change):
    global result, D, W, board

    if change_count == max_change:
        if check():
            result = change_count
        return
    if r == D:
        return

    if result == 987654321:
        dfs(r+1, change_count, max_change)
        tmp = board[r]

        if max_change > change_count:
            board[r] = [0] * W
            dfs(r+1, change_count+1, max_change)

            board[r] = [1] * W
            dfs(r+1, change_count+1, max_change)
    
        board[r] = tmp

for t_case in range(1, T+1):
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]
    result = 987654321
    if K == 1:
        result = 0

    for i in range(K):
        dfs(0, 0, i)
        if result != 987654321:
            break
    if result == 987654321:
        result = K
    print(f"#{t_case} {result}")





