from time import time
from functools import lru_cache

@lru_cache(maxsize=32) # 호출한 인수의 결과를 최대 32회까지 캐싱
def my_fibo(n):
    if n == 0 : return 0
    elif n == 1 or n == 2: return 1
    else:
        return my_fibo(n-1) + my_fibo(n-2)

start_t = time()
print(my_fibo(40))
end_t = time()
print("exec time : ", end_t - start_t)