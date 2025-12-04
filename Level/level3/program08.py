# 숫자 게임
# 속도: 2중 for문 << for문 인덱스
def solution(A, B):
    result = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    idx = 0

    for a in A:
        if a < B[idx]:
            result += 1
            idx += 1

    return result