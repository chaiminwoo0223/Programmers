# 게임 맵 최단거리
# bfs
# q.popleft()
from collections import deque

def solution(maps):
    return bfs(maps)

def bfs(maps):
    queue = deque([[0, 0, 1]])
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]

    while queue:
        y, x, count = queue.popleft()

        if y == (n - 1) and x == (m - 1):
            return count

        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]

            if 0 <= ty < n and 0 <= tx < m and maps[ty][tx] != 0 and not visited[ty][tx]:
                queue.append([ty, tx, count + 1])
                visited[ty][tx] = 1

    return -1
