# 섬 연결하기
# 그래프를 최소 비용으로 모두 연결하는 최소 신장 트리(MST)
def solution(n, costs):
    result = 0

    # 건설 비용을 기준으로 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    # 각 섬의 부모 노드를 자기 자신으로 초기화
    parents = [i for i in range(n)]

    # 루트 노드를 찾는 함수
    def find_parent(parents, x):
        if parents[x] != x:
            parents[x] = find_parent(parents, parents[x])
        return parents[x]

    # 두 섬을 연결하는 함수 (Union)
    def union_parent(parents, x, y):
        X = find_parent(parents, x)
        Y = find_parent(parents, y)

        if X < Y:
            parents[Y] = X
        else:
            parents[X] = Y

    for cost in costs:
        if find_parent(parents, cost[0]) != find_parent(parents, cost[1]):
            result += cost[2]
            union_parent(parents, cost[0], cost[1])

    return result
