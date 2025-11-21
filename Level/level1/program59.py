# 문자열 나누기
def solution(s):
    counter = [0, 0]  # 같은거, 다른거
    result = 0
    x = s[0]

    for i, c in enumerate(s):
        if x == c:
            counter[0] += 1
        else:
            counter[1] += 1

        if counter[0] == counter[1]:
            result += 1
            counter = [0, 0]

            if i + 1 < len(s):
                x = s[i + 1]

    if sum(counter) != 0:
        result += 1

    return result
