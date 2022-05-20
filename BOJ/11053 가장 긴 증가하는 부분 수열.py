import sys
from queue import PriorityQueue

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
pq = PriorityQueue()
pq.put((-1, numbers[0]))


for i in range(1, N):
    curNumber = numbers[i]
    flag = True
    tmp = list(pq.queue)
    for j in range(i):
        l, v = pq.get()
        if v < curNumber:
            tmp.append((l-1, curNumber))
            flag = False
    if flag:
        tmp.append((-1, curNumber))

    pq = PriorityQueue(tmp)
print(pq.get()[0]*-1)
