# 미로 탈출
# bfs 2번
# 시간 초과 방지: 방문 처리는 큐에 삽입할 때 같이 처리
from collections import deque

def solution(maps):
    count1 = bfs('S', 'L', maps)
    count2 = bfs('L', 'E', maps)

    if count1 != -1 and count2 != -1:
        return count1 + count2
    else:
        return -1


def bfs(start, end, maps):
    queue = deque()
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] == start:
                queue.append([i, j, 0])
                visited[i][j] = 1
                break

        if queue:
            break

    while queue:
        y, x, count = queue.popleft()

        if maps[y][x] == end:
            return count

        for i in range(4):  # 핵심: 방문 처리를 통해 중복을 제거하자!
            ty = y + dy[i]
            tx = x + dx[i]

            if 0 <= ty < n and 0 <= tx < m and maps[ty][tx] != 'X' and not visited[ty][tx]:
                queue.append([ty, tx, count + 1])
                visited[ty][tx] = 1

    return -1
