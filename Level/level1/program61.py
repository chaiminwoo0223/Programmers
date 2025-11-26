# 로또의 최고 순위와 최저 순위
# 조건을 정확히 반영해야 문제가 풀린다.
def solution(lottos, win_nums):
    ranking = [6, 6, 5, 4, 3, 2, 1]
    zero = lottos.count(0)
    hit = sum(1 for win_num in win_nums if win_num in lottos)

    return [ranking[zero + hit], ranking[hit]]
