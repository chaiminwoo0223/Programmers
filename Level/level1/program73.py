# 달리기 경주
# 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다.
# players[idx] = p
def solution(players, callings):
    race = {}

    for i, player in enumerate(players):
        race[player] = i

    for calling in callings:
        idx = race[calling]

        p = players[idx - 1]

        race[p] += 1
        race[calling] -= 1

        players[idx] = p
        players[idx - 1] = calling

    return players
