# 순위
# results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다.
# 어떤 한 선수의 순위를 알기 위해서는, 다른 모든 선수와의 경로가 존재해야 한다.
def solution(n, results):
    answer = 0

    graph = [[None for _ in range(n)] for _ in range(n)]

    for win, lose in results:
        graph[win - 1][lose - 1] = True
        graph[lose - 1][win - 1] = False

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[j][i] == None:
                    continue

                if graph[j][i] == graph[i][k]:
                    graph[j][k] = graph[j][i]
                    graph[k][j] = not graph[j][i]

    for i in range(n):
        if None in graph[i][:i] + graph[i][i + 1:]:
            continue

        answer += 1

    return answer
