
from collections import defaultdict

result = []
def check(banned_id, banned_list_by_banid, depth, comb):
    if depth == len(banned_id): # 끝까지 탐색한경우
        comb = sorted(comb) # 정렬하여, 기존에 만들 수 있는 조합이 아니라면 result에 추가
        if comb not in result:
            result.append(comb)
        return

    for ban_id in banned_list_by_banid[banned_id[depth]]:
        # ban_id가 comb list에 없다면 추가하여 dfs() 호출
        if ban_id not in comb:
            comb.append(ban_id)
            check(banned_id, banned_list_by_banid, depth+1, comb)
            comb.pop()


def solution(user_id, banned_id):
    global result
    result = []
    banned_list_by_banid = defaultdict(list) # str : list()
    answer = 0

    for ban_idx, to_ban in enumerate(banned_id):
        for id_num, user in enumerate(user_id):
            if len(to_ban) != len(user):
                continue

            star_idxs = [i for i in range(len(to_ban)) if to_ban[i] == '*'] # to_ban[i] == '*' 인 index만 가져옴
            comp_user_id = "" # 기존 user_id에서 '*' 변환 , frodo -> fr*d*
            for i in range(len(user)):
                if i in star_idxs:
                    comp_user_id += "*" # i 가 star_idxs list에 있는 경우 '*' 추가
                else:
                    comp_user_id += user[i] # 아닌 경우 기존의 문자 추가
            # 변환된 user_id와 to_ban 비교
            if comp_user_id == to_ban:
                if user not in banned_list_by_banid[to_ban]: # banlist에 추가되지 않았다면
                    banned_list_by_banid[to_ban].append(user)

    # banned_list_by_banid 를 이용하여 dfs로 모든 조합 탐색
    check(banned_id, banned_list_by_banid, 0, [])
    return len(result)
