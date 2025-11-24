# n^2 배열 자르기
# 2차원 -> 1차원
# 인덱스 활용, 규착
def solution(n, left, right):
    result = []

    for i in range(left, right + 1):
        result.append(max(i % n, i // n) + 1)

    return result
