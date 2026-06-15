# 디펜스 게임
from heapq import heappush, heappop

def solution(n, k, enemy):
    result = 0
    enemies = 0

    heap = []

    for i, e in enumerate(enemy):
        heappush(heap, -e)  # 최대힙

        enemies += e

        if enemies > n:
            if k > 0:
                enemies += heappop(heap)
                k -= 1
            else:
                break

        result += 1

    return result
