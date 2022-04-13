N = int(input())

def do_something():
    pass

from collections import deque

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)

def out_ot_range(y, x): # 격자에서 벗어났는지 확인하는 함수
    return y < 0 or x < 0 or y >= N or x >= N


def bfs(y, x):
    q = deque() # queue
    # 시작 좌표(y, x) 삽입 및 visited 표시
    q.append((y, x))
    visited = [[False] * N for _ in range(N)]
    visited[y][x] = True

    while q: #queue에 값이 존재하는 동안 반복
        sy, sx = q.popleft()
        for d in range(4): # pop한 좌표의 4방향 탐색
            ny = sy + dy[d]
            nx = sx + dx[d]

            if out_ot_range(ny, nx) or visited[ny][nx]: # 격자에서 벗어났거나, 방문한 좌표의 경우 continue
                continue
            else: # 아닌 경우 (상황에 따라 다른 예외가 있는 경우 처리해야합니다.)
                do_something() # 이후 동작 호출(혹은 코드를 바로 작성하여도 무방)
                q.append((ny, nx)) # queue에 탐색한 좌표 추가 및 방문 기록
                visited[ny][nx] = True
