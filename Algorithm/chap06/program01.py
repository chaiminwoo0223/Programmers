# 체육복
def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    reserved = reserve - lost # 여벌 체육복을 가지고 있지만, 도난당한 학생 제거
    losted = lost - reserve # 여벌 체육복을 가지고 있지만, 도난당한 학생 제거
    
    for r in sorted(reserved):
        if r-1 in losted:
            losted.remove(r-1)
        elif r+1 in losted:
            losted.remove(r+1)

    return n - len(losted)
