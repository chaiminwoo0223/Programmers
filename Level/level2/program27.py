# 뒤에 있는 큰 수 찾기
# 스택
# 배열 순회를 하지 않고 인덱스를 이용한 탐색은 시간을 단축시킨다.
def solution(numbers):
    stack = []  # 인덱스 스택
    result = [-1] * len(numbers)

    for i, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            idx = stack.pop()
            result[idx] = number

        stack.append(i)

    return result
