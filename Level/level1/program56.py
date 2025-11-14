# 덧칠하기
def solution(n, m, section):
    result = 1
    t = section[0]

    for s in section:
        if s - t >= m:
            t = s
            result += 1

    return result
