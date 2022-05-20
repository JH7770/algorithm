from collections import defaultdict, deque
from copy import deepcopy

M, S = map(int, input().split())
loc2fishes = defaultdict(list)
smells = [[0] * 4 for _ in range(4)]
copy_loc2fishes = defaultdict(list)

dy8 = (0, -1, -1, -1, 0, 1, 1, 1)
dx8 = (-1, -1, 0, 1, 1, 1, 0, -1)

dy4 = (-1, 0, 1, 0)
dx4 = (0, -1, 0, 1)

d2d = ['←','↖','↑', '↗', '→', '↘', '↓','↙']
for _ in range(M):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1
    loc2fishes[(r, c)].append(d)
shark_y, shark_x = map(int, input().split())
shark_y -= 1
shark_x -= 1

def out_of_range(y, x):
    return y < 0 or x < 0 or y >= 4 or x >= 4


def copy():
    global loc2fishes, copy_loc2fishes
    copy_loc2fishes = deepcopy(loc2fishes)

def fish_move():
    global loc2fishes
    new_loc2fishes = defaultdict(list)

    for k, v in loc2fishes.items():
        y, x = k
        for d in v:
            cnt = 0
            nd = d
            while True:
                if cnt > 8:
                    ny, nx, nd = y, x, d
                    break
                cnt += 1
                ny = y + dy8[nd]
                nx = x + dx8[nd]

                if out_of_range(ny, nx) or (shark_y, shark_x) == (ny, nx) or smells[ny][nx] > 0:
                    nd = (nd - 1)%8
                else:
                    break
            new_loc2fishes[(ny, nx)].append(nd)
    loc2fishes = new_loc2fishes
    # for k, v in new_loc2fishes.items():
    #     print(k,':',[d2d[d] for d in v])


move_result = []
def dfs(move, fish_count, loc, d):
    global move_result
    if len(move) == 3:
        move_result.append({
            'move':move[:],
             'fish_count':fish_count,
             'shark_loc':loc,
            'directions': d
             })
        return
    y, x = loc
    for i in range(4):
        ny = y + dy4[i]
        nx = x + dx4[i]

        if out_of_range(ny, nx):
            continue
        if (ny, nx) in move:
            move.append((ny, nx))
            dfs(move, fish_count, (ny, nx), d)
            move.pop()
            continue
        move.append((ny, nx))
        fish = len(loc2fishes[(ny, nx)])
        dfs(move, fish_count+fish, (ny, nx), d + str(i))
        move.pop()

def shark_move():
    global shark_y, shark_x, move_result, smells
    move_result = []
    dfs([], 0, (shark_y, shark_x), "")

    max_fish_count = 0

    for d in move_result:
        fish_count = d['fish_count']
        if max_fish_count < fish_count:
            max_fish_count = fish_count
    move_result = [d for d in move_result if d['fish_count'] == max_fish_count][0]

    for loc in move_result['move']:
        y, x = loc
        if len(loc2fishes[loc]) > 0:
            loc2fishes.pop(loc)
            smells[y][x] = 3

    shark_y, shark_x = move_result['shark_loc']

def delete_smell():
    global smells
    for y in range(4):
        for x in range(4):
            if smells[y][x] > 0:
                smells[y][x] -= 1


def add_copy():
    global loc2fishes, copy_loc2fishes
    new_loc2fishes = defaultdict(list)

    for k, v in loc2fishes.items():
        new_loc2fishes[k].extend(v)
    for k, v in copy_loc2fishes.items():
        new_loc2fishes[k].extend(v)

    loc2fishes = new_loc2fishes
    copy_loc2fishes = defaultdict(list)


def p():
    print(f"상어  {(shark_y, shark_x)}")
    for r in smells:
        print(r)
    for k, v in loc2fishes.items():
        if v == []:
            continue
        print(k, ':', [d2d[d] for d in v])

    cnt = 0

for _ in range(S):
    copy()
    fish_move()

    cnt = 0
    shark_move()
    delete_smell()
    add_copy()
    # p()
    # print(shark_y, shark_x)
#



for k, v in loc2fishes.items():
    cnt += len(v)
print(cnt)
