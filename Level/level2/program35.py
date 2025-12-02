# 숫자 변환하기
# 속도: 리스트 <<< 집합
from collections import deque

def solution(x, y, n):
    if x != y:
        return bfs(x, y, n)
    else:
        return 0

def bfs(x, y, n):
    queue = deque([[x, 0]])
    visited = set()

    while queue:
        x, count = queue.popleft()

        for num in (x + n, x * 2, x * 3):
            if num == y:
                return count + 1
            if num < y and num not in visited:
                queue.append([num, count + 1])
                visited.add(num)

    return -1
