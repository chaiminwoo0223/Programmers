# 이상한 문자 만들기
# split(구분자)
def solution(s):
    result = ""

    for w in s.split(" "):
        for i, c in enumerate(w):
            if i % 2 == 0: # 홀수 번째
                result += c.upper()
            else: # 짝수 번째
                result += c.lower()

        result += " "

    return result[:-1]
