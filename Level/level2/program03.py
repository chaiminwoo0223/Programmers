# JadenCase 문자열
# 다중 공백 처리
def solution(s):
    result = ""

    for i, word in enumerate(s):
        if word in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            result += word
        elif word == " ":
            result += " "
        elif len(result) == 0 or result[-1] == " ":
            result += word.upper()
        else:
            result += word.lower()

    return result