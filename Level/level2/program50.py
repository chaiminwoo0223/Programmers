# N-Queen
# 백트래킹
def solution(n):
    chess = [0] * (n + 1)
    result = [0]

    def solve(row):
        if row == n:
            result[0] += 1
            return
        else:
            for i in range(n):
                if row == 0 and i == n // 2 and n % 2 == 0:
                    break

                chess[row] = i

                if check(row):
                    solve(row + 1)

    def check(row):
        for i in range(row):
            if chess[i] == chess[row]:
                return False

            if abs(row - i) == abs(chess[row] - chess[i]):
                return False

        return True

    solve(0)

    return result[0] if n % 2 == 1 else result[0] * 2
