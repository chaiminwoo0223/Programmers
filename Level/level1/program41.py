# 푸드 파이트 대회
def solution(food):
    answer = ""

    for i, x in enumerate(food[1:]):
        answer += str(i + 1) * (x // 2)

    return answer + "0" + answer[::-1]
