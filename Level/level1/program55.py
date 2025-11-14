# 실패율
# 람다식
from collections import Counter

def solution(N, stages):
    count = len(stages)
    clear = 0
    counter = Counter(stages)
    result = []

    for i in range(1, N + 1):
        if (count - clear) > 0:
            result.append((i, counter[i] / (count - clear)))
        else:
            result.append((i, 0))

        clear += counter[i]

    return [x for x, _ in sorted(result, key=lambda x: (-x[1], x[0]))]