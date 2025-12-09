# 크레인 인형뽑기 게임
# 스택
# 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다.
# 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정합니다.
def solution(board, moves):
    result = 0
    stack = []

    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                if stack and stack[-1] == board[i][move - 1]:
                    stack.pop()
                    result += 2
                else:
                    stack.append(board[i][move - 1])

                board[i][move - 1] = 0
                break

    return result