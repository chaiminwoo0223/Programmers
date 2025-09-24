# 행렬의 덧셈
# zip
def solution(arr1, arr2):
    return [[e1 + e2 for e1, e2 in zip(a, b)] for a, b in zip(arr1, arr2)]
