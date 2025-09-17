# 정수 제곱근 판별
from math import sqrt

def solution(n):
    x = int(sqrt(n))

    if x ** 2 == n:
        return (x + 1) ** 2
    else:
        return -1
