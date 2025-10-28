# 게임 맵 최단거리
# bfs
# q.popleft()
from collections import deque

def solution(maps):
    q = deque([[0, 0]])
    n = len(maps)
    m = len(maps[0])

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    while q:
        x, y = q.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < n and 0 <= ty < m and maps[tx][ty] == 1:
                maps[tx][ty] += maps[x][y]
                q.append([tx, ty])

        if x == n - 1 and y == m - 1 and maps[x][y] > 1:
            return maps[x][y]

    return -1
