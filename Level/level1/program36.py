# 삼총사
from itertools import combinations


def solution(number):
    count = 0
    combination = combinations(number, 3)

    for c in combination:
        if sum(c) == 0:
            count += 1

    return count
