from collections import deque

def do_something(perm):
    print(perm)

M = 3
some_list = [1, 2, 3, 4]

visited = [False] * len(some_list)
result = []
def dfs(perm: deque):
    if len(perm) == M:  # 종료 조건 : M개를 모두 선택했을 때
        result.append(list(perm))
        do_something(perm)
        return

    for i, val in enumerate(some_list):
        if visited[i]: # 방문한 노드인 경우 제외
            continue
        # i번째 노드를 포함하여 재귀 호출
        perm.append(val)
        visited[i] = True
        dfs(perm)
        perm.pop()
        visited[i] = False

dfs(deque())


# def dfs(comb: deque, depth: int):
#     if len(comb) == M:  # 종료 조건 1 : M개를 모두 선택했을 때
#         do_something(comb)  # 선택 후의 알고리즘 호출
#         return
#     elif depth == len(some_list):  # 종료 조건 2: 리스트의 마지막 까지 탐색했을 때
#         return
#
#     # 현재 depth의 값 포함 재귀 호출
#     comb.append(some_list[depth])
#     dfs(comb, depth + 1)
#
#     # 현재 depth의 값 미포함 재귀 호출
#     comb.pop()
#     dfs(comb, depth + 1)

