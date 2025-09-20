# 가운데 글자 가져오기
def solution(s):
    index = len(s) // 2

    if len(s) % 2 == 1:
        return s[index]
    elif len(s) == 1:
        return s
    else:
        return s[index - 1:index + 1]
