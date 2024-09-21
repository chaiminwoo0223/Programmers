# 의상
def solution(clothes):
    # 딕셔너리 생성
    new_clothes = dict()
    
    # 옷 종류 분류
    for c in clothes:
        item, category = c 
        if category in new_clothes: # 해당 category가 딕셔너리 안에 있는가?
            new_clothes[category] += 1
        else:
            new_clothes[category] = 1
            
    # 조합 계산(확률적 선택)
    answer = 1
    for count in new_clothes.values():
        answer *= (count+1) # 각 category에서 안 입는 경우를 추가
    answer -= 1 # 모든 category에서 아무것도 안 입는 경우를 제외
        
    return answer
