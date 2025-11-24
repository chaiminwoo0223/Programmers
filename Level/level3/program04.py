# 단어 변환
# bfs
# while문 안 for문, for문
from collections import deque

def solution(begin, target, words):
    result = 0

    if target not in words:
        return result
    else:
        result = bfs(begin, target, words)

    return result

def bfs(begin, target, words):
    queue = deque([[begin, 0]])
    visited = [0] * len(words)

    while queue:
        word, count = queue.popleft()

        if word == target:
            return count

        for i in range(len(words)):
            difference = 0

            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        difference += 1

                if difference == 1:
                    queue.append([words[i], count + 1])
                    visited[i] = 1

    return 0
