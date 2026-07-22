# 로또의 최고 순위와 최저 순위
# 시뮬레이션
def solution(lottos, win_nums):
    result = [6, 6, 5, 4, 3, 2, 1]

    zeros = lottos.count(0)
    matched = len(set(lottos) & set(win_nums))

    return [result[matched + zeros], result[matched]]
