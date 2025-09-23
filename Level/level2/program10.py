# 짝지어 제거하기
# 스택
def solution(s):
    words = []

    for word in s:
        if words and words[-1] == word:
            words.pop()
        else:
            words.append(word)

    if words:
        return 0
    else:
        return 1
