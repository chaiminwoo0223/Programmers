# n^2 배열 자르기
# 2차원 -> 1차원
# 규칙
def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)

    return answer
