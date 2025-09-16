# 짝지어 제거하기
# 스택
def solution(s):
    words = [] # 임시 보관함

    if len(s) % 2 == 1: # 홀수면 무조건 0
        return 0
    else:
        for word in s:
            if words and words[-1] == word:
                words.pop()
            else:
                words.append(word)

        if words:
            return 0
        else:
            return 1
