def solution(board, skill):
    answer = 0

    for type, r1, c1, r2, c2, degree in skill:
        # (r1, c1) ~ (r2, c2) 값 추가
        for y in range(r1, r2 + 1, 1):
            for x in range(c1, c2 + 1, 1):
                board[y][x] += degree if type == 2 else -degree  # type == 2 인 경우 -degree 추가

    for row in board:
        answer += len(list(filter(lambda x: x > 0, row)))  # x > 0 이상인 리스트의 길이를 answer에 추가함

    return answer


a = [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]]

testCases = [
    (
        [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
        [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]],
        10
    ), (
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]],
        6
    )
]

for t in testCases:
    print(solution(t[0], t[1]), t[2])
    exit()
