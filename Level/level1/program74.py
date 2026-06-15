# 공원 산책
# 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
# 주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
# S : 시작 지점, O : 이동 가능한 통로, X : 장애물
def solution(park, routes):
    n, m = len(park), len(park[0])
    direction = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}
    step = [0, 0]

    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                step = [i, j]

    for route in routes:
        success = True

        for t in range(int(route[-1])):
            x = step[0] + direction[route[0]][0] * (t + 1)
            y = step[1] + direction[route[0]][1] * (t + 1)

            if not (0 <= x < n and 0 <= y < m and park[x][y] != "X"):
                success = False
                break # 해당 명령을 무시하고 다음 명령을 수행합니다.

        if success:
            step = [step[0] + direction[route[0]][0] * int(route[-1]), step[1] + direction[route[0]][1] * int(route[-1])]

    return step
