R, C = map(int, input().split(' '))
board = [list(map(str, input())) for _ in range(R)]
moves = list(map(int, input()))
EMPTY = -3
dy = (EMPTY, 1, 1, 1, 0, 0, 0, -1, -1, -1)
dx = (EMPTY, -1, 0, 1, -1, 0, 1, -1, 0, 1)

loc_jongsu = [(y, x) for y in range(R) for x in range(C) if board[y][x] == 'I'][0]
loc_ardu = [(y, x) for y in range(R) for x in range(C) if board[y][x] == 'R']


def pboard():
    for r in board:
        print("".join(r))


def isCrazyArduino(y, x):
    return board[y][x] == 'R'


def move_arduino(direction):
    global loc_jongsu
    y, x = loc_jongsu
    ny = y + dy[direction]
    nx = x + dx[direction]

    if isCrazyArduino(ny, nx):
        return False
    else:
        loc_jongsu = (ny, nx)
        board[y][x] = "."
        board[ny][nx] = "I"
        return True


def move_crazy_arduino():
    global loc_ardu
    man_y, man_x = loc_jongsu
    new_loc_ardu = []
    loc_count = {}

    for y, x in loc_ardu:
        board[y][x] = "."
        min_dist = 99999999
        min_loc = (0, 0)
        #check next location
        for d in range(1, 10, 1):
            if d == 5: continue
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or nx < 0 or ny >= R or nx >= C:
                continue
            dist = abs(ny - man_y) + abs(nx - man_x)
            if min_dist > dist:
                min_dist = dist
                min_loc = (ny, nx)

        if min_loc == loc_jongsu: # 아두이노와 만남
            return False
        new_loc_ardu.append(min_loc) # 아두이노가 안겹치는 경우

        # 위치에 대한 아두이노 개수 파악
        if min_loc in loc_count.keys():
            loc_count[min_loc] += 1
        else:
            loc_count[min_loc] = 1


    tmp_list = []
    for loc in new_loc_ardu:
        # 한 위치에 아두이노 여러개가 있는 경우 폭파했다고 가정하여 아두이노 리스트에 포함하지 않음
        if 음oc in tmp_list or loc_count[loc] > 1:
            continue
        tmp_list.append(loc)

    loc_ardu = tmp_list
    for y, x in tmp_list:
        board[y][x] = "R"
    return True


def solve():
    for i, d in enumerate(moves):
        if not move_arduino(d):
            print("kraj %d"%(i+1))
            exit()
        if not move_crazy_arduino():
            print("kraj %d"%(i+1))
            exit()
    pboard()

solve()
