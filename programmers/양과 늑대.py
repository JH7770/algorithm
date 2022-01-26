from collections import defaultdict, deque  #

TestCases = [
    (
        [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]],
        5
    ),
    (
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]],
        5
    )
]

is_wolf = []
can_go = defaultdict(list)
result = 0


def find(current_loc, next_locs, nsheeps, nwolfs, used):
    used[current_loc] = True

    if is_wolf[current_loc]: nwolfs += 1
    else: nsheeps += 1

    if nsheeps <= nwolfs:
        return

    next_locs.extend(can_go[current_loc])
    for loc in next_locs:
        find(loc, )


def solution(info, edges):
    is_wolf = info.copy()
    used = [False] * len(is_wolf)

    for e1, e2 in edges:
        can_go[e1].append(e2)
        can_go[e2].append(e1)

    find(0, [], 0, 0, used.copy())


for data in TestCases:
    print(solution(data[0], data[1]) == data[2])
    exit()
