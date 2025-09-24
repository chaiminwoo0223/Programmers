# 최대공약수와 최소공배수
def gcm(x, y, num):
    return max(i for i in range(1, num + 1) if i <= num and x % i == 0 and y % i == 0)

def lcm(x, y):
    return x * y // gcm(x, y, min(x, y))

def solution(n, m):
    return [gcm(n, m, min(n, m)), lcm(n, m)]
