# 옹알이 (2)
def solution(babbling):
    count = 0

    for word in babbling:
        check = word
        for sound in ["aya", "ye", "woo", "ma"]:
            if sound * 2 not in check: # 연속된 발음이 없는지를 검사한다.
                check = check.replace(sound, ' ')
        
        if check.strip() == '':
            count += 1
    
    return count
