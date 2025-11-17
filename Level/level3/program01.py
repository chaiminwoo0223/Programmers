# 네트워크
# dfs
def solution(n, computers):
    visited = [0] * len(computers)
    result = 0

    for i in range(len(computers)):
        if not visited[i]:
            dfs(i, computers, visited)
            result += 1

    return result

def dfs(x, computers, visited):
    visited[x] = 1

    for j in range(len(computers)):
        if not visited[j] and computers[x][j]:
            dfs(j, computers, visited)
