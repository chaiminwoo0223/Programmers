# 둘만의 암호
# String.replace(a, b)와 index
# 꼭 import를 사용하지 않아도 된다.
def solution(s, skip, index):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for x in skip:
        alphabet = alphabet.replace(x, "")

    for c in s:
        result += alphabet[(alphabet.index(c) + index) % len(alphabet)]

    return result
