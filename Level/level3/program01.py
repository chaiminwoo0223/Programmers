# 네트워크
# dfs
def solution(n, computers):
    answer = 0
    visited = [0] * n

    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1

    return answer

def dfs(computers, visited, i):
    visited[i] = 1

    for j in range(len(computers[i])):
        if not visited[j] and computers[i][j]:
            dfs(computers, visited, j)
