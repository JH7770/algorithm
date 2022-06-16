def solution(rows, columns, queries):
    board = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    for r in board:
        print(r)
    answer = []
    for y1, x1, y2, x2 in queries:
        y1, x1, y2, x2 = y1 - 1, x1 - 1, y2 -1, x2 - 1
        q = []
        loc_list = []
        for x in range(x1, x2+1):
            q.append(board[y1][x])
            loc_list.append((y1, x))

        for y in range(y1+1,y2):
            q.append(board[y][x2])
            loc_list.append((y, x2))

        for x in range(x2, x1-1, -1):
            q.append(board[y2][x])
            loc_list.append((y2, x))
        
        for y in range(y2-1, y1, -1):
            q.append(board[y][x1])
            loc_list.append((y, x1))

        tmp = q.pop()
        q.insert(0, tmp)
        answer.append(min(q))

        for i, loc in enumerate(loc_list):
            y, x = loc
            board[y][x] = q[i]
    print(answer)
    return answer

solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])