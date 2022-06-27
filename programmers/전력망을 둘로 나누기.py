from collections import defaultdict

def check(n, available, wires):
    connected = defaultdict(list)
    for i, wire in enumerate(wires):
        if available[i]:
            n1, n2 = wire
            connected[n1].append(n2)
            connected[n2].append(n1)

    visited = [False] * (n + 1)
    area_list = []
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        area = []
        q = [i]
        # bfs 탐색으로 i번과 연결된 선을 모두 area에 추가함
        while q:
            n = q.pop(0)
            for n2 in connected[n]:
                if visited[n2]:
                    continue
                if n2 not in area:
                    area.append(n2)
                q.append(n2)
                visited[n2] = True
        area_list.append(area)

    return abs(len(area_list[0]) - len(area_list[1]))




def solution(n, wires):
    answer = int(10e9)
    available = [True] * len(wires)
    for i in range(len(wires)):
        available[i] = False
        answer = min(answer, check(n, available, wires))



        available[i] = True
    print(answer)
    return answer


solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])