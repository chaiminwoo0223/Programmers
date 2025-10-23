# [1차] 캐시
# deque(maxlen = x)
from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    cache = deque(maxlen=cacheSize)
    time = 0

    for city in cities:
        x = city.lower()

        if x in cache:
            cache.remove(x)
            cache.append(x)
            time += 1
        else:
            cache.append(x)
            time += 5

    return time
