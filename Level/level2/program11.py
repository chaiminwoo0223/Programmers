# 귤 고르기
from collections import Counter

def solution(k, tangerine):
    result = 0
    counter = Counter(tangerine).values()

    for value in sorted(counter, reverse=True):
        k -= value
        result += 1

        if k <= 0:
            break

    return result
