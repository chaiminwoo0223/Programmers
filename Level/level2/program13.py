# 멀리 뛰기
# 동적 프로그래밍
# 직접 손으로 적어라
# 개수, 규칙, 관계, 요구사항 등을 파악하라
def solution(n):
    a, b = 1, 1  # 0, 1

    for i in range(n):
        a, b = b, a + b  # 1, 2 -> 2, 3 -> 3, 4 ...

    return a % 1234567
