def solutio2n(n, works):
    for i in range(n):
        works[works.index(max(works))] -= 1
    result = sum([w ** 2 for w in works if w > 0 ])
    return result


def solution(n, works):
    works = sorted(works)

    while n > 0:
        max = works[-1]
        for i in range(len(works)):
            if works[i] == max:
                n -= 1
                works[i] -= 1
            if n == 0:
                break
    result = sum([w ** 2 for w in works if w > 0])


    return result


tc = [
    ([4, 3, 3], 4, 12),
    ([2, 1, 2], 1, 6),
    ([1, 1], 3, 0)
]

for works,n, result in tc:
    solution(n, works)
    print()