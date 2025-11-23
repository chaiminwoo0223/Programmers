# H-Index
# sorted(citations, reverse=True)를 통해 나머지 논문이 h번 이하 인용 처리
def solution(citations):
    h_index = 0

    for citation in sorted(citations, reverse=True):
        if citation > h_index:
            h_index += 1

    return h_index
