# 행렬의 곱셈
# 수학 살짝
def solution(arr1, arr2):
    result = [[0] * len(arr2[0]) for _ in range(len(arr1))]  # 핵심

    for i in range(len(arr1)):  # 방향
        for j in range(len(arr2[0])):  # 방향
            for k in range(len(arr1[0])):  # 방향
                result[i][j] += arr1[i][k] * arr2[k][j]

    return result