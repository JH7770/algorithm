<<<<<<< HEAD
from collections import defaultdict

T = int(input())
MAN = 1
board = []
mans = []
stairs = []
stair2n = {}
n2stair = {}
result = 987654321
def move(s_list):
    # if s_list != [0, 0, 0, 0, 1, 1]:
    #     return
    global mans, result


    distance = []
    for i, s in enumerate(s_list):
        y, x = mans[i]
        y2, x2 = n2stair[s]
        dist = abs(y2 - y) + abs(x2 - x)
        distance.append(dist)

    cnt = 1
    in_the_stair = defaultdict(list)
    while True:
        cnt += 1
        for i, d in enumerate(distance):
            if d == 0:
                continue
            distance[i] -= 1
            if distance[i] == 0:
                s = s_list[i]
                y, x = n2stair[s]
                K = board[y][x]
                if len(in_the_stair[s]) < 3:
                    in_the_stair[s].append(K+1)
                else:
                    in_the_stair[s].append(K)

        to_pop = []
        for k in in_the_stair.keys():
            for i in range(3):
                if len(in_the_stair[k]) <= i:
                    break
                in_the_stair[k][i] -= 1
            in_the_stair[k] = [d for d in in_the_stair[k] if d != 0]
            if not in_the_stair[k]:
                to_pop.append(k)
        for k in to_pop:
            in_the_stair.pop(k)

        if sum(distance) == 0 and not in_the_stair:
            break
        # #
        # print(f"{cnt}분 후")
        # print(f"distance : {distance}")
        # print(f"in the stair : {in_the_stair}")
        # print()
    if result > cnt:
        result = cnt
    # print(cnt)


def dfs(s):
    if len(s) == len(mans):
        move(s)
        return

    for i in range(len(stairs)):
        s.append(i)
        dfs(s)
        s.pop()


for t_case in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    mans = [(y, x) for y in range(N) for x in range(N) if board[y][x] == MAN]
    stairs = [(y, x) for y in range(N) for x in range(N) if board[y][x] > 1]
    stair2n = {}
    n2stair = {}
    result = 987654321
    for i, v in enumerate(stairs):
        stair2n[v] = i
        n2stair[i] = v

    dfs([])
    print(f"#{t_case} {result}")
=======
E
>>>>>>> a7767397a8d87df81d9fe0eac6af1b1a8608da6c
