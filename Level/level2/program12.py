# H-Index
def solution(citations):
    citations = sorted(citations, reverse=True)  # 내림차순 정렬
    paper_count = len(citations)

    for h_index in range(paper_count, -1, -1):
        if h_index <= sum([1 for citation in citations if citation >= h_index]):
            return h_index

    return 0
