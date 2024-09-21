# 전화번호 목록
def solution(phoneBook):
    phoneBook.sort() # 전화번호 목록 정렬

    for p1, p2 in zip(phoneBook, phoneBook[1:]): # zip(리스트1, 리스트2)
        if p2.startswith(p1):
            return False
    return True
