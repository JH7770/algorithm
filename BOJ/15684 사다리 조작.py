N, M, H = map(int, input().split())

connected = {}
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    connected[(a, b)] = (a, b+1)
    connected[(a, b+1)] = (a, b)


def move(y, x):
    ny, nx = y, x
    visited = [(ny, nx)]
    while ny < H:
        if (ny, nx) in connected.keys():
            cy, cx = connected[(ny, nx)]
            if (cy, cx) not in visited:
                ny = cy
                nx = cx
            else:
                ny += 1
        else:
            ny += 1
        visited.append((ny, nx))
    return ny, nx

def check():
    for i in range(N):
        ey, ex = move(0, i)
        if ex != i:
            return False
    return True

def dfs(l, i):
    global finish, connected, can_set
    if 0 < len(l) <= 3:
        for y, x in l:
            connected[(y, x)] = (y, x+1)
            connected[(y, x+1)] = (y, x)
        if check():
            finish = True
            print(len(l))
        for y, x in l:
            if (y, x) in connected.keys():
                connected.pop((y, x))
            if (y, x+1) in connected.keys():
                connected.pop((y, x+1))

    if finish or i == len(can_set):
        return
    if len(l) < 3:
        y, x = can_set[i]
        if (y, x-1) not in l:
            l.append(can_set[i])
            dfs(l, i+1)
            l.pop()
        dfs(l, i+1)



finish = False
visited = []
can_set = []
def solve():
    global can_set, finish
    if check():
        finish = True
        print(0)
        return

    can_set = []
    for y in range(H):
        for x in range(N-1):
            if (y, x) not in connected.keys() and (y, x+1) not in connected.keys():
                can_set.append((y, x))

    # for i in range(1, 4):
    dfs([], 0)
        # if finish:
        #     print(i)
        #     break
    if not finish:
        print(-1)
solve()
