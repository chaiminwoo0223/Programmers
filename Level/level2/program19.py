# n^2 배열 자르기
# 2차원 -> 1차원
# 인덱스 활용
def solution(n, left, right):
    return [max(i // n, i % n) + 1 for i in range(left, right+1)]
