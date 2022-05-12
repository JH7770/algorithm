from copy import deepcopy
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))


result = 0
def dfs(nlist, visited):
    global result
    for y in range(N):
        for x in range(M):
            if visited[y][x]:
                continue
            else:
                n = board[y][x]
                visited[y][x] = True
                nlist.append(int(n))
                dfs(nlist, deepcopy(visited))
                nlist.pop()

                last_k = N
                for k in range(1, N):
                    if y+k == N or visited[y+k][x]:
                        last_k = k
                        break
                    n += board[y+k][x]
                    nlist.append(int(n))
                    visited[y+k][x] = True
                    dfs(nlist, deepcopy(visited))
                    nlist.pop()

                for k in range(1, last_k):
                    visited[y+k][x] = False

                n = board[y][x]
                last_k = M
                for k in range(1, M):
                    if x+k == M or visited[y][x+k]:
                        last_k = k
                        break
                    n += board[y][x+k]
                    nlist.append(int(n))
                    visited[y][x+k] = True
                    dfs(nlist, deepcopy(visited))
                    nlist.pop()

                for k in range(1, last_k):
                    visited[y][x+k] = False

                visited[y][x] = False
                return

    s = sum(nlist)
    if result < s:
        result = s

dfs([], [[False] * M for _ in range(N)])
print(result)