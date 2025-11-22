# 미로 탈출
# bfs 2번
# 시간 초과 방지: 방문 처리는 큐에 삽입할 때 같이 처리
from collections import deque

def solution(maps):
    count1 = bfs('S', 'L', maps)
    count2 = bfs('L', 'E', maps)

    if count1 != 0 and count2 != 0:
        return count1 + count2
    else:
        return -1

def bfs(start, end, maps):
    queue = deque()
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    for i in range(len(maps)):  # y
        for j in range(len(maps[0])):  # x
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

            if 0 <= ty < len(maps) and 0 <= tx < len(maps[0]) and maps[ty][tx] != 'X' and not visited[ty][tx]:
                queue.append([ty, tx, count + 1])
                visited[ty][tx] = 1

    return 0
