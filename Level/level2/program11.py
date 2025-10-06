# 귤 고르기
from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    result = 0

    for _, n in counter.most_common():
        k -= n
        result += 1

        if k <= 0:
            break

    return result