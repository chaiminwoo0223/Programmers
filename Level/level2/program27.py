# 네트워크
# bfs
from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n

    for i in range(n):
        if visited[i] == 0:
            bfs(n, computers, i, visited)
            answer += 1

    return answer

def bfs(n, computers, i, visited):
    visited[i] = 1
    queue = deque([i])

    while queue:
        i = queue.popleft()
        visited[i] = 1

        for j in range(n):
            if not visited[j] and computers[i][j]:
                queue.append(j)
