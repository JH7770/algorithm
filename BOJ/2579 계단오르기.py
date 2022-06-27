from collections import deque
N = int(input())
stairs = [int(input()) for _ in range(N)]
scores = [0] * N
if N == 1:
    print(stairs[0])
    exit()
elif N == 2:
    print(stairs[0] + stairs[1])
    exit()
elif N == 3:
    print(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
    exit()

scores[0] = stairs[0]
scores[1] = stairs[0] + stairs[1]
scores[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, N):
    scores[i] = max(
        scores[i-3] + stairs[i-1] + stairs[i],
        scores[i-2] + stairs[i]
    )

print(scores[N-1])
