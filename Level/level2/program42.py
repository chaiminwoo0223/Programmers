# 삼각 달팽이
# 별 삼각형 변형
# 패턴
def solution(n):
    result = [[0] * n for _ in range(n)]
    x, y = -1, 0
    num = 1

    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0: # Down
                x += 1
            elif i % 3 == 1: # Right
                y += 1
            else: # Up
                x -= 1
                y -= 1

            result[x][y] = num
            num += 1

    return [result[i][j] for i in range(n) for j in range(i + 1)]
