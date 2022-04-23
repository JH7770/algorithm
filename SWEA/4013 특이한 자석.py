from collections import deque

T = int(input())
magnets = list()
moves = ()
connected = [
    [(1, 6)], [(0, 2), (2, 6)], [(1, 2), (3, 6)], [(2, 2)]
]

visited = []

def dfs(m, dir):
    global visited, magnets
    if visited[m]: return

    visited[m] = True
    for m2, x2 in connected[m]:
        x = 2 if x2 == 6 else 6
        if magnets[m][x] != magnets[m2][x2]:
            dfs(m2, dir*-1)

    if dir == 1:
        tmp = magnets[m].pop()
        magnets[m].insert(0, tmp)
    else:
        tmp = magnets[m].pop(0)
        magnets[m].append(tmp)


for t_case in range(1, T+1):
    K = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]
    moves = [tuple(map(int, input().split())) for _ in range(K)]
    result = 0

    for m, dir in moves:
        m -= 1
        visited = [False] * 4
        dfs(m, dir)

    for i in range(4):
        if magnets[i][0] == 1:
            result += 2 ** i
    print(f"#{t_case} {result}")
