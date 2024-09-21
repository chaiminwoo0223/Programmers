# 전화번호 목록
def solution(phone_book):
    phone_book.sort() # 전화번호 목록 정렬
    
    if len(phone_book) != 1:
        for i in range(1, len(phone_book)):
            if phone_book[i].startswith(phone_book[i-1]):
                return False
        return True
    else:
        return True
