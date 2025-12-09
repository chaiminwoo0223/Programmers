# 단속카메라
# 구간
def solution(routes):
    result = 0
    routes.sort()
    camera = routes[0]

    for route in routes[1:]:
        if route[0] <= camera[1]:
            camera = [route[0], min(route[1], camera[1])]
        else:
            camera = route
            result += 1

    result += 1

    return result