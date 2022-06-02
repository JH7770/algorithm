import math
from collections import deque
def solution(progresses, speeds):

    answer = []
    q = deque()

    for i in range(len(progresses)):
        progress_duration = math.ceil((100 - progresses[i]) / speeds[i])
        q.append(progress_duration)
    while q:
        end_day = q.popleft()

        cnt = 1
        if not q:
            answer.append(cnt)
            break
        while q:
            comp_end_day = q.popleft()

            if comp_end_day <= end_day:
                cnt += 1
            else:
                q.appendleft(comp_end_day)
                break
        answer.append(cnt)
    return answer

# solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5 ,10, 7])
