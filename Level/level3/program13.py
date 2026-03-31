# 여행경로
# 주어진 항공권은 모두 사용해야 합니다.
# 그래프를 무조건 채우지 않아도 된다.
def solution(tickets):
    result = []
    visited = [0] * len(tickets)

    def dfs(airport, pathes):
        if len(pathes) == len(tickets) + 1:
            result.append(pathes)
            return

        for i, ticket in enumerate(tickets):
            if airport == ticket[0] and not visited[i]:
                visited[i] = 1
                dfs(ticket[1], pathes + [ticket[1]])
                visited[i] = 0

    dfs("ICN", ["ICN"])

    result.sort()

    return result[0]
