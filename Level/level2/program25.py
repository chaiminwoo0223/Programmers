# 방문 길이
# Edge Case: 다시 돌아가는 것도 지나간 것이다.
def solution(dirs):
    x, y = 0, 0
    road = set()
    move = {'U': (0, 1), 'D': (0, -1), 'R': (-1, 0), 'L': (1, 0)}

    for d in dirs:
        dx, dy = move[d]
        tx = x + dx
        ty = y + dy

        if -5 <= tx <= 5 and -5 <= ty <= 5:
            road.add(((x, y), (tx, ty)))
            road.add(((tx, ty), (x, y)))
            x = tx
            y = ty

    return len(road) // 2
