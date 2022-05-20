N = int(input())
nlist = list(map(int, input().split()))
sum_list = []
min_num = 1
def dfs(l, d):
    global sum_list, min_num
    if d == N:
        if l:
            s = sum(l)
            sum_list.append(s)
        return
    l.append(nlist[d])
    dfs(l, d+1)
    l.pop()
    dfs(l, d+1)

dfs([], 0)
sum_list = sorted(list(set(sum_list)))

comp_num = 1
result = -1
for n in sum_list:
    if n == comp_num:
        comp_num += 1
        continue
    else:
        result = comp_num
        break
if result == -1:
    result = comp_num
print(result)