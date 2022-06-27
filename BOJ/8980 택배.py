from operator import itemgetter
from collections import deque

N, C = map(int, input().split())
M = int(input())
delivery_info = [
    tuple(map(int, input().split())) for _ in range(M)
]

for _from, _to, _size in delivery_info:
    print(f"send : {_from}, to : {_to}, size : {_size}")

print("After sorted")
delivery_info=sorted(delivery_info, key=itemgetter(0, 1, 2))
for _from, _to, _size in delivery_info:
    print(f"send : {_from}, to : {_to}, size : {_size}")

q = deque()
qsize = 0
