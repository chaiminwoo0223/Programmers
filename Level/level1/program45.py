# 명예의 전당 (1)
def solution(k, score):
    scores = []
    result = []

    for i in range(len(score)):
        scores.append(score[i])
        scores = sorted(scores, reverse=True)

        if len(scores) > k:
            scores = scores[:-1]

        result.append(scores[-1])

    return result
