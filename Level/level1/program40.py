# 두 개 뽑아서 더하기
from itertools import combinations


def solution(numbers):
    result = []

    for x, y in combinations(numbers, 2):
        result.append(x + y)

    return sorted(set(result))
