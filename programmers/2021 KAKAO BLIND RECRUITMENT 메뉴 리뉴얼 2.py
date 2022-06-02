from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    all_combination = set()

    ###  이 부분 부터 잘못된거였네요.. ㅎㅎ 밑에 부분만 수정하다 보니 안풀렸던것 같습니다...여러분은 천사 오브 엔젤...

    # 주문한 내용으로 가능한 조합을 모두 all combinations에 추가
    for order in orders:
        for c in course:
            # order 중 c개 조합을 구함
            for comb in combinations(order, c):
                all_combination.add(tuple(sorted(comb)))   # ['X', 'Y']와 ['Y', 'X']는 같은 주문이기 때문에 정렬 후 set에 추가해서 중복 삭제


    course2size = defaultdict(int)
    course2best_courses = defaultdict(list)

    # 모든 조합에 대해 최대 매칭 수 조사
    for comb in all_combination:
        match_count = 0
        for order in orders:
            match = True
            for menu in comb:
                if menu not in order:
                    match = False
                    break
            if match:
                match_count += 1
        if match_count <= 1:
            continue
        n_course = len(comb)
        if course2size[n_course] < match_count:
            course2best_courses[n_course] = [comb]
            course2size[n_course] = match_count
        elif course2size[n_course] == match_count:
            course2best_courses[n_course].append(comb)

    answer = []
    for k, v in course2best_courses.items():
        for menu_list in v:
            answer.append("".join(menu_list))
    answer = sorted(answer)
    return answer


orders =["XYZ", "XWY", "WXA"]
course = [2, 3, 4]

print(solution(orders, course))