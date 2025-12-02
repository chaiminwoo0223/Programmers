# 등굣길
# 좌표: 수학적 좌표 vs 코드적 좌표
def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]  # 넓게 보아야 문제가 풀린다.
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            elif [j, i] in puddles:
                dp[i][j] = 0  # 핵심: 웅덩이 위치의 값을 0으로 초기화
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007  # 나머지 연산 위치 중요

    return dp[-1][-1]