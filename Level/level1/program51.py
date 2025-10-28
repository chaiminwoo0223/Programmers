# 소수 만들기
from itertools import combinations

def check(x):
    for i in range(2, x):
        if x % i == 0:
            return 0

    return 1

def solution(nums):
    result = 0

    for c in combinations(nums, 3):
        result += check(sum(c))

    return result
