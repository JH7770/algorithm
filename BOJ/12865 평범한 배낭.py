from operator import itemgetter
from queue import PriorityQueue

N, K = map(int, input().split())

pq = PriorityQueue()

stuff_list = [tuple(map(int, input().split())) for _ in range(N)]
stuff_list = sorted(stuff_list, key=itemgetter(1, 0))

pq.put((stuff_list[0]))

print(f"최대 무게 {K}")
result = 0
for i in range(1, N):
    w, v = stuff_list[i]
    print(f"무게 {w}, 가치 {v}, 최대 {result}")
    to_append = pq.queue
    while not pq.empty():
        w2, v2 = pq.get()
        result = max(result, v2)
        if w + w2 > K:
            continue
        else:
            to_append.append((w+w2, v+v2))

    for t in to_append:
        pq.put(t)

print(pq.get())
