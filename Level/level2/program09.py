# 점프와 순간 이동
# 정확성, 효율성
# 역으로 생각(나누기, 빼기)
def solution(n):
    count = 0

    while n != 1:
        if n % 2 == 0:  # 짝수로 나누어 떨어지면
            n //= 2
        else:
            n -= 1
            count += 1

    return count + 1
