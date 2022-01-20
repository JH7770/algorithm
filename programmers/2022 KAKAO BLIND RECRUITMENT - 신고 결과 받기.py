TestCase = [
    (
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2,
        [2, 1, 1, 0]
    ),
    (
        ["con", "ryan"],
        ["ryan con", "ryan con", "ryan con", "ryan con"],
        3,
        [0, 0]
    )
]
from collections import defaultdict

def solution(id_list, report, k):
    answer = []

    report_dict = defaultdict(set)
    report_list = defaultdict(set)
    for r in report:
        report_from, report_to = r.split(' ')
        report_dict[report_to].add(report_from)
        report_list[report_from].add(report_to)

    for i, _id in enumerate(id_list):
        cnt = 0
        for r_id in report_list[_id]:
            if len(report_dict[r_id]) >= k:
               cnt += 1
        answer.append(cnt)
    return answer


for inp in TestCase:
    ret = solution(inp[0], inp[1], inp[2])
    print(ret == inp[3])
    if not ret == inp[3]:
        print(ret, inp[3])
