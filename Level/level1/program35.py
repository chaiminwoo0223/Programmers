# 3진법 뒤집기
# int(a, b)
def solution(n):
    result = ""

    while n > 0:
        result += str(n % 3)
        n //= 3

    return int(result, 3)
