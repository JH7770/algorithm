from collections import defaultdict


class Trie:
    def __init__(self, menu="", depth=-1, menu_prefix = ""):
        self.menu = menu
        self.children = []
        self.children_menus = []
        self.menu_prefix = menu_prefix
        self.depth = depth
        self.count = 0

root = Trie()

def trie_insert(order):
    global root

    tmp = root
    for i, v in enumerate(order):
        if v not in tmp.children_menus:
            prefix = tmp.menu_prefix
            tmp.count += 1
            tmp.children.append(Trie(v, i, prefix+v))
            tmp.children_menus.append(v)
            tmp = tmp.children[-1]
        else:
            idx = tmp.children_menus.index(v)
            tmp.count += 1
            tmp = tmp.children[idx]

def solution(orders, course):
    global root
    for order in orders:
        trie_insert(sorted(order))

    # print(root.children_menus)
    q = [root]

    n2best_size = defaultdict(int)
    n2best = defaultdict(list)
    while q:
        tmp = q.pop(0)
        print(tmp.menu_prefix, tmp.count)
        menu_len = len(tmp.menu_prefix)
        if n2best_size[menu_len] < tmp.count:
            n2best_size[menu_len] = tmp.count
            n2best[menu_len] = [tmp.menu_prefix]
        elif n2best_size[menu_len] == tmp.count:
            n2best[menu_len].append(tmp.menu_prefix)

        q.extend(tmp.children)
    answer = []
    for c in course:
        answer.extend(n2best[c])
    answer = sorted(answer)
    return answer



orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]

print(solution(orders, course))