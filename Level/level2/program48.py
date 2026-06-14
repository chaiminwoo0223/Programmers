# 무인도 여행
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    graph = [list(map) for map in maps]
    visited = [[0] * m for _ in range(n)]
    queue = deque()

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'X':
                visited[i][j] = -1

    result = []

    for i in range(n):
        for j in range(m):
            num = 0

            if not visited[i][j]:
                num = int(graph[i][j])
                queue.append([i, j])
                visited[i][j] = 1

                while queue:
                    x, y = queue.popleft()

                    for k in range(4):
                        tx = x + dx[k]
                        ty = y + dy[k]

                        if 0 <= tx < n and 0 <= ty < m and not visited[tx][ty]:
                            num += int(graph[tx][ty])
                            queue.append([tx, ty])
                            visited[tx][ty] = 1

            if num != 0:
                result.append(num)

    if result:
        return sorted(result)
    else:
        return [-1]
