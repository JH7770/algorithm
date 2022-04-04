from collections import defaultdict

N, M, K = map(int, input().split())
fireballs = defaultdict(list)

for i in range(M):
    r, c, m ,s, d = map(int, input().split())
    fireballs[(r-1, c-1)].append((m, s, d))

dy8 = (-1, -1, 0, 1, 1, 1, 0, -1)
dx8 = (0, 1, 1, 1, 0, -1, -1, -1)

def move_fireballs():
    # 파이어 볼 이동
    global fireballs
    new_fireballs = defaultdict(list)
    for loc, info_list in fireballs.items():
        sy, sx = loc
        for m, s, d in info_list:
            ny = (sy + dy8[d] * s) % N
            nx = (sx + dx8[d] * s) % N
            new_fireballs[(ny, nx)].append((m, s, d))

    fireballs = new_fireballs.copy()

def all_odd_or_even(dirs):
    odd_flag, even_flag = False, False
    for d in dirs:
        if d % 2 == 1:
            odd_flag = True
        if d % 2 == 0:
            even_flag = True

    if odd_flag and even_flag:
        return False
    return True


def change_duplicate_fireballs():
    global fireballs
    new_fireballs = defaultdict(list)
    for loc, info_ilst in fireballs.items():
        if len(info_ilst) == 1:
            new_fireballs[loc].append(info_ilst[0])
            continue
        sum_m, sum_s, dirs = 0, 0, []
        for m, s, d in info_ilst:
            sum_m += m
            sum_s += s
            dirs.append(d)
        new_m = int(sum_m / 5)
        if new_m == 0:
            continue
        new_s = int(sum_s/len(info_ilst))
        new_dirs = [0, 2, 4, 6] if all_odd_or_even(dirs) else [1, 3, 5, 7]
        for new_d in new_dirs:
            new_fireballs[loc].append((new_m, new_s, new_d))

    fireballs = new_fireballs.copy()


for _ in range(K):
    move_fireballs()
    change_duplicate_fireballs()

result = 0
for loc, info_list in fireballs.items():
    for m, s, d in info_list:
        result += m
print(result)
