# 연속 부분 수열 합의 개수
def solution(elements):
    count = len(elements)
    elements += elements
    result = set()

    for i in range(count):
        for j in range(count):
            result.add(sum(elements[i:i + j + 1]))

    return len(result)
