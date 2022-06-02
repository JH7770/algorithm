import heapq
def solution(jobs):
    job_count = len(jobs)
    t_now = 0
    t_working = 0
    heap = []

    while True:
        # 작업 중 현재 시작 가능한 작업(작업 시작 시간 <= 현재 시간)만 heap에 추가함
        # 작업 길이를 기준으로 heap에 추가
        for start_t, working_time in [j for j in jobs if j[0] <= t_now]:
            heapq.heappush(heap, (working_time, start_t))
        # 남은 작업 갱신 (작업 시작 시간 > 현재 시간)
        jobs = [j for j in jobs if j[0] > t_now]

        # 만약 남은 작업이 모두 없는 경우 break
        if not heap and not jobs:
            break
        # 남은 작업은 있으나 heap에 아무것도 없는 경우
        # -> 남은 작업 중 시작 가능한 작업이 없음, 현재 시간을 +1
        if not heap:
            t_now += 1
            continue

        # eha
        l, t = heapq.heappop(heap)
        t_now += l
        t_working += t_now - t
    return t_working // job_count



jobs = [[0, 3], [1, 9], [2, 6]]

print(solution(jobs))