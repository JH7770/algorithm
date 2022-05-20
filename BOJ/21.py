
a = [15, 16, 18, 19, 20, 31]
visited = [False] * 6

result = 0
def dfs2(l, d):
    if len(l) == 3:
        sum_l = 0
        for i in l:
            sum_l += a[i]
        if sum_l == result:
            print("!@!#!@#")
        print(sum_l, result)
        return
    if d == 6:
        return

    if not visited[d]:
        l.append(d)
        dfs2(l, d+1)
        l.pop()
    dfs2(l, d+1)

def dfs(l, d):
    global result
    if len(l) == 2:
        sum_l = 0
        for i in l:
            visited[i] = True
            sum_l += a[i]

        result = sum_l
        dfs2([], 0)

        for i in l:
            visited[i] = False
        return
    elif d == 6:
        return

    l.append(d)
    dfs(l, d+1)
    l.pop()
    dfs(l, d+1)

dfs([], 0)

