# 개인정보 수집 유효기간
# 모든 달은 28일까지 있다고 가정합니다.
def solution(today, terms, privacies):
    result = []
    expires = dict()

    for term in terms:
        a, b = term.split()
        expires[a] = int(b)

    year, month, day = spliterator(today)

    for i, privacy in enumerate(privacies):
        privacy = privacy.split()
        y, m, d = spliterator(privacy[0])
        expire = expires[privacy[-1]]
        y += expire // 12
        m += expire % 12

        y, m, d = calculator(y, m, d)

        if y < year or (y == year and m < month) or (y == year and m == month and d < day):
            result.append(i + 1)

    return result

def spliterator(today):
    today = today.split('.')

    return int(today[0]), int(today[1]), int(today[2])

def calculator(year, month, day):
    day -= 1

    if day == 0:
        day = 28
        month -= 1

    if month > 12:
        year += (month // 12)
        month = month % 12

    if month == 0:
        month = 12
        year -= 1

    return year, month, day
