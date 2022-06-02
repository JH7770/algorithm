from collections import defaultdict

n2winlist = defaultdict(list)
n2loselist = defaultdict(list)

def check(n):
    loser_from_n = n2winlist[n]
    winner_from_n = n2loselist[n]

    for winner in winner_from_n:
        for loser in loser_from_n:
            if loser not in n2winlist[winner]:
                n2winlist[winner].append(loser)


    for loser in loser_from_n:
        for winner in winner_from_n:
            if winner not in n2loselist[loser]:
                n2loselist[loser].append(winner)



def solution(n, results):
    answer = 0
    for winner, loser in results:
        n2winlist[winner].append(loser)
        n2loselist[loser].append(winner)

    for num in range(1, n+1):
        check(num)

    for num in range(1, n+1):
        answer += len(n2winlist[num]) + len(n2loselist[num]) == n - 1
    return answer


print(solution(
    n=5,
    results=[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
))