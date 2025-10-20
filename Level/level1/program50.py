# 기사단원의 무기
def solution(number, limit, power):
    answer = 0
    weapon = []

    for i in range(1, number + 1):
        results = []

        for j in range(1, int(i ** (1 / 2)) + 1):  # 핵심
            if i % j == 0:
                results.append(j)
                results.append(i // j)

        result = len(set(results))

        if result > limit:
            weapon.append(power)
        else:
            weapon.append(result)

    answer = sum(weapon)

    return answer