# 연속된 부분 수열의 합
# 비내림차순
# 투포인터
def solution(sequence, k):
    result = [0, len(sequence)]
    l, r = 0, 0
    num = sequence[0]

    while True:
        if num < k:
            r += 1

            if r == len(sequence):
                break

            num += sequence[r]
        else:
            if num == k and (r - l < result[1] - result[0]):
                result = [l, r]

            num -= sequence[l]
            l += 1

    return result
