# 기지국 설치
import math

def solution(n, stations, w):
    result = 0
    distances = []

    # 설치된 기지국 사이에 전파가 닿지 않는 거리 저장
    for i in range(1, len(stations)):
        distances.append((stations[i] - w) - (stations[i - 1] + w) - 1)

    # 처음 아파트 - 처음 기지국 사이에 전파 닿지 않는 거리 저장
    distances.append(stations[0] - w - 1)

    # 마지막 기지국 - 마지막 아파트 사이에 전파 닿지 않는 거리 저장
    distances.append(n - (stations[-1] + w))

    for distance in distances:
        if distance <= 0:
            continue
        else:
            result += math.ceil(distance / (w * 2 + 1))  # 닿지 않는 거리에 설치할 수 있는 개수 더함

    return result