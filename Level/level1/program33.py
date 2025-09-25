# 크기가 작은 부분문자열
def solution(t, p):
    P = len(p)
    result = 0

    for i in range(len(t) - P + 1):
        if int(t[i:i + P]) <= int(p):
            result += 1

    return result
