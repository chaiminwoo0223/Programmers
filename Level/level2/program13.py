# 멀리 뛰기
# 동적 프로그래밍: 직접 손으로 적어봐라!
# 피보나치 수열
def solution(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return b % 1234567