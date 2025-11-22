# 기사단원의 무기
# 핵심: 약수 구하기(제곱근) -> O(루트(N))
from math import sqrt

def solution(number, limit, power):
    result = 0

    for n in range(1, number + 1):
        result += weapons(n, limit, power)

    return result

def weapons(x, limit, power):
    weapon = set()

    for i in range(1, int(sqrt(x) + 1)):
        if x % i == 0:  # 핵심
            weapon.add(i)
            weapon.add(x // i)

    if len(weapon) > limit:
        return power
    else:
        return len(weapon)
