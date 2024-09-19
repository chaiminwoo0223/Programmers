# 모의고사
def solution(answers):
    answer = []
    
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    one_counter = 0
    two_counter = 0
    three_counter = 0
    
    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            one_counter += 1
        if answers[i] == two[i % len(two)]:
            two_counter += 1
        if answers[i] == three[i % len(three)]:
            three_counter += 1 
    
    # 세 값 비교
    max_counter = max(one_counter, two_counter, three_counter)
    if max_counter == one_counter:
        answer.append(1)
    if max_counter == two_counter:
        answer.append(2)
    if max_counter == three_counter:
        answer.append(3)

    return answer