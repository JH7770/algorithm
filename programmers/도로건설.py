dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

from collections import deque

visited = list()
b = list()
money_map = list()
min_result = int(10e9)
N = 0



def bfs(y, x, last_d):
    if (y, x) == (N-1, N-1):
        return

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if ny < 0 or nx < 0 or ny >= N or nx >= N or (ny, nx) == (0, 0):
            continue
        if b[ny][nx] == 1:
            continue

        new_money = money_map[y][x] + 100 if d == last_d else money_map[y][x] + 600

        if money_map[ny][nx] == 0 or money_map[ny][nx] >= new_money:
            money_map[ny][nx] = new_money
            bfs(ny, nx, d)




def solution(board):
    global visited, b, min_result, N, money_map
    N = len(board)
    b = board
    visited = [[False] * len(board) for _ in range(len(board))]
    min_result = int(10e9)
    money_map = [[0]*N for _ in range(N)]

    visited[0][0] = True
    for d in range(2):
        bfs(0, 0, d)
    answer = money_map[N-1][N-1]

    return answer

tc = [
    ([[0,0,0],[0,0,0],[0,0,0]],	900),
    ([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]],	3800),
    ([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]],	2100),
    ([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]],	3200)
    ]

for b, result in tc:
    print(solution(b), result)
    
    


"""
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

from collections import deque

visited = list()
b = list()
min_result = int(10e9)
N = 0
def bfs(y, x, last_d, result):
    global min_result
    if result > min_result:
        return
    if (y, x) == (N-1, N-1):
        if min_result > result:
            min_result = result
        return

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if ny < 0 or nx < 0 or nx >= N or ny >= N:
            continue
        if visited[ny][nx] or b[ny][nx] == 1:
            continue

        visited[ny][nx] = True
        new_result = result + 100 if d == last_d else result + 600
        bfs(ny, nx, d, new_result)
        visited[ny][nx] = False


def solution(board):
    global visited, b, min_result, N
    N = len(board)
    b = board
    visited = [[False] * len(board) for _ in range(len(board))]
    min_result = int(10e9)

    visited[0][0] = True
    for d in range(2):
        bfs(0, 0, d, 0)
    answer = min_result
    return answer"""