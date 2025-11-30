# 택배상자
# 반복문 순서
def solution(order):
    result = 0
    container = []
    idx = 0

    for box in range(len(order)):
        container.append(box + 1)

        while container and container[-1] == order[idx]:
            container.pop()
            result += 1
            idx += 1

    return result