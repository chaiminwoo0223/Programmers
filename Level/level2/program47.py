# 가장 먼 노드
# 최단경로
from collections import deque

def solution(n, vertex):
    graph = [[] for _ in range(n + 1)]  # 핵심
    visited = [0, 1] + [0] * (n - 1)

    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    queue = deque([1])

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[x] + 1

    result = [1 for v in visited if v == max(visited)]

    return len(result)
