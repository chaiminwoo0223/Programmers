# 콜라 문제
def solution(a, b, n):
    result = 0

    while n >= a:
        result += (n // a) * b
        n = (n % a) + ((n // a) * b)

    return result
