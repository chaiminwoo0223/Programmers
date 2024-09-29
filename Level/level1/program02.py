# 옹알이 (2)
def solution(babbling):
    check = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        temp = word
        for sound in check:
            if sound * 2 not in temp: # 연속된 발음이 없는지를 검사한다.
                temp = temp.replace(sound, ' ')
        
        if temp.strip() == '':
            count += 1
    
    return count
