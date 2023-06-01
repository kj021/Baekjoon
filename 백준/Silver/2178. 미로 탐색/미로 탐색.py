import sys
sys.setrecursionlimit(10**6)
from collections import deque
import sys
sys.setrecursionlimit(10*6)


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0]*M for _ in range(N)]


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x, y))
    v[x][y] = 1

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and v[nx][ny] == 0:
                q.append((nx, ny))
                v[nx][ny] = v[cx][cy] + 1

    return v[N-1][M-1]


print(bfs(0, 0))