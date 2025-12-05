# 2 x n 타일링
# 다이나믹 프로그래밍
# Top-Down 방식, Bottom-Up 방식
# 연산자 우선순위
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return calculator(n)

def calculator(n):
    dp = [0, 1, 2] + [0] * (n - 2)

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

    return dp[n]