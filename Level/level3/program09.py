# 최고의 집합
# 곱셈을 하는 숫자끼리 차이가 크지 않아야지 가장 큰 곱셉을 만들어낼 수 있다.
# 골고루 나누고, 나머지를 분배하자.
def solution(n, s):
    result = []

    if n > s:
        return [-1]

    for _ in range(n):
        result.append(s // n)

    rest = s - sum(result)

    for i in range(rest):
        result[i] += 1

    return sorted(result)
