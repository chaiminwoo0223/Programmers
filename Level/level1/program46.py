# 카드 뭉치
def solution(cards1, cards2, goal):
    for card in goal:
        if cards1 and card == cards1[0]:
            cards1.pop(0)
        elif cards2 and card == cards2[0]:
            cards2.pop(0)
        else:
            return "No"

    return "Yes"
