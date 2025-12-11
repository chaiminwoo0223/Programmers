# 성격 유형 검사하기
# 한쪽이 받거나 못받거나 둘 중 하나다.
def solution(survey, choices):
    result = ''
    personality = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i, choice in enumerate(choices):
        if choice > 4:
            compute(personality, survey[i][1], choice - 4)

        if choice < 4:
            compute(personality, survey[i][0], 4 - choice)

    for p1, p2 in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]:
        result += compare(personality, p1, p2)

    return result

def compute(personality, key, value):
    if personality[key]:
        personality[key] += value
    else:
        personality[key] += value

def compare(personality, p1, p2):
    if personality[p1] >= personality[p2]:
        return p1
    else:
        return p2
