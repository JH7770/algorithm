T = int(input())

for t_case in range(T):
    W = int(input())
    board = [list(map(int, input().split()))
             for _ in range(2)]
    print(board)

