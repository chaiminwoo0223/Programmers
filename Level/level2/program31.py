# [3차] 압축
# 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
from collections import Counter
from string import ascii_uppercase

def solution(msg):
    answer = []
    counter = Counter()

    for i, alphabet in enumerate(ascii_uppercase):
        counter[alphabet] = i + 1

    start = 0
    end = len(msg)
    index = 0
    value = 26
    word = ""

    # "다음"이 핵심이다.
    while start < end:
        word += msg[start]

        if word in counter:
            index = counter[word]
            start += 1
        else:
            value += 1
            counter[word] = value
            answer.append(index)
            word = ""

    if word:
        answer.append(index)

    return answer