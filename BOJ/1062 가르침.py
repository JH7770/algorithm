N, K = map(int, input().split())
slist = [
    input()
        .replace('a', '')
        .replace('n', '')
        .replace('t', '')
        .replace('c', '')
        .replace('i', '')
for _ in range(N)]

if K < 5:
    print(0)
    exit()
else:
    K -= 5


alphalist = set()
for s in slist:
    for c in s:
        alphalist.add(c)
alphalist = list(alphalist)

# for s in slist:
#     print(s)
# print(alphalist)

result = 0
def check(l):
    global result
    cnt = 0
    for s in slist:
        if [c for c in s if c not in l] == []:
            cnt += 1
    if result < cnt:
        result = cnt

def dfs(l, d):
    if len(l) == K or len(l) == len(alphalist):
        check(l)
        return
    if d == len(alphalist):
        return

    l.append(alphalist[d])
    dfs(l, d+1)
    l.pop()
    dfs(l, d+1)
dfs([], 0)
print(result)