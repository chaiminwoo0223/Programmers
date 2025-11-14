# 정수 삼각형
def solution(triangle):
    result = [[0] * len(triangle[i]) for i in range(len(triangle))]
    result[0][0] = triangle[0][0]

    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            for k in (j, j + 1):
                if result[i + 1][k] < triangle[i + 1][k] + result[i][j]:
                    result[i + 1][k] = triangle[i + 1][k] + result[i][j]

    return max(result[-1])
