# 모의고사
def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == one[idx % len(one)]:
            scores[0] += 1
        if answer == two[idx % len(two)]:
            scores[1] += 1
        if answer == three[idx % len(three)]:
            scores[2] += 1
    
    max_score = max(scores)
    for idx, score in enumerate(scores):
        if max_score == score:
            result.append(idx+1)
    
    return result
