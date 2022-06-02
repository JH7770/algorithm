

def solution(n, times):
    # 이진 탐색으로 t초에 몇명 조사가 가능한지 범위를 줄여가며 조사한 후
    # 조사한 인원이 n인 경우의 t를 반환
    l, r = 1, max(times) * n
    while l <= r:
        mid = (l + r) // 2
        count = 0

        # 모든 심사관에 대해서 mid초 동안 몇명 조사했는지 count에 추가
        for t in times:
            count += mid // t
            if count == n: # 조사한 인원이 n인 경우 종료
                break

        # 탐색 범위 변경
        if count >= n: # 실제 조사한 인원이 더 많은 경우
            answer = mid
            r = mid -1
        elif count < n: # 실제 조사한 인원이 더 적은 경우
            l = mid + 1

    return answer


print(solution(6, [7, 10]))
