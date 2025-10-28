# 소수 찾기
from math import sqrt

def check(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return 0

    return 1

def solution(n):
    result = 0

    for i in range(2, n + 1):
        result += check(i)

    return result
