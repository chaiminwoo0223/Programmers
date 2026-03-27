# 배달
# 다익스트라 알고리즘
# 우선순위 큐
import heapq


def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    cnt = 0

    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    result = calculator(graph, 1, N, K)

    for r in result:
        if r <= K:
            cnt += 1

    return cnt

def calculator(graph, start, n, k):
    times = [k + 1] * (n + 1)
    times[start] = 0

    queue = []
    heapq.heappush(queue, [times[start], start])

    while queue:
        current_time, current_end = heapq.heappop(queue)

        if times[current_end] < current_time:
            continue

        for new_end, new_time in graph[current_end]:
            time = current_time + new_time

            if time < times[new_end]:
                times[new_end] = time
                heapq.heappush(queue, [time, new_end])

    return times
