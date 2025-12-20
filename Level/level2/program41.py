# 시소 짝꿍
# 조합
# 중복 제거
# / → 정확한 비율
# // → 다른 무게로 왜곡
from collections import Counter

def solution(weights):
    result = 0
    counter = Counter(weights)

    for key, value in counter.items():
        if value >= 2:
            result += ((value * (value - 1)) // 2)

    weights = set(weights)

    for weight in weights:
        if weight * 2 / 3 in weights:
            result += (counter[weight] * counter[weight * 2 / 3])
        if weight * 3 / 4 in weights:
            result += (counter[weight] * counter[weight * 3 / 4])
        if weight * 2 / 4 in weights:
            result += (counter[weight] * counter[weight * 2 / 4])

    return result
