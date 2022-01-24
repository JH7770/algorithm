def to_k_number(n, k):
    ret = ""

    # find bigest K
    big_power_k = 1
    while n > k ** big_power_k:
        big_power_k += 1

    for i in range(big_power_k, -1, -1):
        ret += str(n // (k ** i))
        n %= (k ** i)

    return int(ret)


def isitPrime(k):
    if k == 2 or k == 3: return True
    if k % 2 == 0 or k < 2: return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    k_num = str(to_k_number(n, k))

    for n in k_num.split('0'):
        if n == "": continue
        elif isitPrime(int(n)):
            answer += 1
    return answer

