N, S = map(int, input().split())
nlist = list(map(int, input().split()))

result = 0
def dfs(l:list, d:int):
    global nlist, result
    if d == N:
        if l and sum(l) == S:
            result += 1
        return
    l.append(nlist[d])
    dfs(l, d+1)
    l.pop()
    dfs(l, d+1)


dfs([], 0)
print(result)