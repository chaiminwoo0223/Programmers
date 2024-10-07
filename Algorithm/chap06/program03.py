# 구명보트
# 양쪽에서 사람을 태운다.
def solution(people, limit):
    people = sorted(people) # 무게를 오름차순으로 정렬
    i = 0 # i는 가장 가벼운 사람
    j = len(people) - 1 # j는 가장 무거운 사람
    count = 0
    
    while i <= j:
        if (people[i] + people[j]) <= limit: # 가장 가벼운 사람과 가장 무거운 사람이 함께 탈 수 있다면
            i += 1 # 가장 가벼운 사람을 태움
        j -= 1 # 무거운 사람은 무조건 태움(i <= j이면 혼자라도 태움)
        count += 1

    return count
