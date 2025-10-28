# [PCCE 기출문제] 9번 / 지폐 접기
def solution(wallet, bill):
    answer = 0

    while min(bill) > min(wallet) or max(bill) > max(wallet):
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2

        answer += 1

    return answer
