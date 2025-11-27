# 124 나라의 숫자
# 10진법 -> 3진법 -> 124 나라
def solution(n):
    result = ""

    while n > 0:
        mod = n % 3

        if not mod:  # 핵심
            mod = 4
            n -= 1

        n //= 3
        result += str(mod)

    return result[::-1]
