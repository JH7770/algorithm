def solution(n):
    s = ""
    # 3진법을 처리하는 것과 유사하게 처리
    while n:
        if n % 3 == 0:
            s += "4"
            n = n // 3 - 1
        else:
            s += str(n % 3)
            n = n // 3

    return ''.join(reversed(s))

for i in range(1, 10):
    print(i, solution(i))
