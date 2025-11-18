# 둘만의 암호
# String.find(k)
# String.replace(a, b)와 index
# 꼭 import를 사용하지 않아도 된다.
def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ""

    for i in list(skip):
        alpha = alpha.replace(i, "")

    for a in s:
        answer += alpha[(alpha.find(a) + index) % len(alpha)]

    return answer
