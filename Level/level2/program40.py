# [1차] 프렌즈4블록
# 카카오 문제는 구현이 핵심이다.
# 블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.
def solution(m, n, board):
    result = 0
    board = [list(x) for x in board]

    while True:
        hit = set()

        for i in range(m - 1):
            for j in range(n - 1):
                t = board[i][j]

                if t == []:
                    continue
                else:
                    block(board, hit, i, j, t)

        print(hit, len(hit))
        result += len(hit)

        if hit:
            for i, j in hit:
                board[i][j] = []
        else:
            break

        # 핵심
        while True:
            moved = False

            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] and board[i + 1][j] == []:
                        board[i + 1][j] = board[i][j]
                        board[i][j] = []
                        moved = True

            if not moved:
                break

    return result

def block(board, hit, i, j, t):
    if (board[i][j + 1] == t and board[i + 1][j] == t and board[i + 1][j + 1] == t):
        hit.add((i, j))
        hit.add((i, j + 1))
        hit.add((i + 1, j))
        hit.add((i + 1, j + 1))