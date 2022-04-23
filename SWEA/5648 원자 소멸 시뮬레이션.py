from copy import deepcopy
T = int(input())

dy = (1, -1, 0, 0)
dx = (0, 0, -1, 1)

loc2info = {}
new_loc2info = {}

def out_of_range(y, x):
    return y <= -1000 or y >= 1000 or x <= -1000 or x >= 1000

for t_case in range(1, T+1):
    N = int(input())
    loc2info = {}


    for _ in range(N):
        x, y, d, k = map(int, input().split())
        loc2info[(y, x)] = (d, k)

    result = 0
    while True:
        new_loc2info = {}
        to_pop = []
        for k, v in loc2info.items():
            y, x = k
            d, k = v

            ny = y + dy[d] * 0.5
            nx = x + dx[d] * 0.5

            if out_of_range(ny, nx):
                continue
                # new_loc2info[(y, x)] = (d, k)
            else:
                if (ny, nx) in new_loc2info.keys():
                    if (ny, nx ,d, k) not in to_pop:
                        to_pop.append((ny, nx, d, k))
                    d2, k2 = new_loc2info[(ny, nx)]
                    if (ny, nx, d2, k2) not in to_pop:
                        to_pop.append((ny, nx, d2, k2))
                else:
                    new_loc2info[(ny, nx)] = (d, k)

        for y, x, _, k in to_pop:
            if (y, x) in new_loc2info.keys():
                new_loc2info.pop((y, x))
            print(to_pop)
            result += k
        if len(new_loc2info) <= 1:
            break
        else:
            loc2info = new_loc2info

    print(f"#{t_case} {result}")
