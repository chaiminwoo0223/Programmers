# 음양 더하기
def solution(absolutes, signs):
    result = 0

    for i, absolute in enumerate(absolutes):
        if signs[i] == True:
            result += absolute
        else:
            result -= absolute

    return result
