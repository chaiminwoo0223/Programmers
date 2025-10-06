# 추억 점수
def solution(name, yearning, photo):
    answer = []

    for people in photo:
        answer.append(sum(yearning[name.index(person)] for person in people if person in name))

    return answer
