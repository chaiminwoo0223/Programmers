# 야근 지수
# 매 시간 작업량이 가장 많은 작업을 수행
import heapq

def solution(n, works):
    works = [-work for work in works]
    heapq.heapify(works)

    for _ in range(n):
        work = heapq.heappop(works)
        heapq.heappush(works, work + 1)

    return sum(work ** 2 for work in works if work < 0)