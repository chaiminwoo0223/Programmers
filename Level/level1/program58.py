# [PCCE 기출문제] 9번 / 이웃한 칸
def solution(board, h, w):
    n = len(board)
    result = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]

        if 0 <= h_check < n and 0 <= w_check < n and board[h][w] == board[h_check][w_check]:
            result += 1

    return result
