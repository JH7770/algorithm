class Member:
    def __init__(self, name, parent):
        self.name = name # 이름
        self.parent = parent # 부모 멤버의 이름ㅁ
        self.amount = 0 # 수익금


def solution(enroll, referral, seller, amount):
    name2id = {}
    member_list = []
    member_list.append(Member("center", "-"))
    name2id["center"] = 0

    # 모든 멤버 연결
    for i in range(len(enroll)):
        name = enroll[i]
        parent = referral[i]
        if parent == "-":
            parent = "center"
        member_list.append(Member(name, parent))
        name2id[name] = i + 1

    # 수익금  확인 및 분배
    for i in range(len(seller)):
        name = seller[i]
        amt = amount[i] * 100
        mid = name2id[name]

        tmp = member_list[mid]
        while True:
            tmp.amount += amt - amt // 10
            amt = amt // 10

            if tmp.parent == "-" or amt == 0: # root 노드이거나 수익금이 없는 경우 탈출
                break

            # tmp = tmp -> parent 노드로 설정
            parent_name = tmp.parent
            parent_mid = name2id[parent_name]
            tmp = member_list[parent_mid]


    member_list.pop(0) # root 노드 삭제
    answer = [m.amount for m in member_list]
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

solution(enroll, referral, seller, amount)

