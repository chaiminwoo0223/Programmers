# 땅따먹기
# 동적 프로그래밍
# 누적합
def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:]) # 핵심

    return max(land[-1])
