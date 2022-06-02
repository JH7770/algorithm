from collections import defaultdict
from copy import deepcopy
menu_list = []
n2best_size = defaultdict(int)
n2best_courses = defaultdict(list)
g_orders = []


def dfs(comb, depth, course):
    global n2best_courses, n2best_size
    if len(comb) == course:
        match_list = []
        set_comb = set(comb)
        for order in g_orders:
            if not set_comb - set(order):
                match_list.append(order)

            # # match = True
            # # for menu in comb:
            # #     if menu not in order:
            # #         match = False
            # #         break
            # if match:
            #     match_list.append(order)
        if len(match_list) <= 1:
            return

        match_size = len(match_list)
        if n2best_size[course] < match_size:
            n2best_courses[course] = [comb[:]]
            n2best_size[course] = match_size
            # print(comb)
            # print(n2best_courses)
        elif n2best_size[course] == match_size:
            n2best_courses[course].append(comb[:])

        return
    if depth == len(menu_list):
        return

    comb.append(menu_list[depth])
    dfs(comb, depth + 1, course)
    comb.pop()
    dfs(comb, depth + 1, course)


def solution(orders, course):
    global n2best_courses, g_orders, menu_list
    g_orders = orders
    for order in orders:
        for c in order:
            if c not in menu_list:
                menu_list.append(c)
    menu_list = sorted(menu_list)
    for c in course:
        dfs([], 0, c)

    result = []
    for k, v in n2best_courses.items():
        for l in v:
            result.append("".join(l))
    result = sorted(result)
    return result

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]

print(solution(orders, course))
