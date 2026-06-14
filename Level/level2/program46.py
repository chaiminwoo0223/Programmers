# 숫자 카드 나누기
import math

def solution(arrayA, arrayB):
    num1 = math.gcd(*arrayA)
    num2 = math.gcd(*arrayB)

    result = [calc(num1, arrayB), calc(num2, arrayA)]

    return max(result)

def calc(num, array):
    if num == 1:
        return 0

    for a in array:
        if a % num == 0:
            return 0

    return num
