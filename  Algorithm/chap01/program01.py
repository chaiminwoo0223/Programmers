# 같은 숫자는 싫어
def solution(elements):
    result = []
    for element in elements:
        if len(result) == 0 or result[-1] != element:
            result.append(element)
    return result