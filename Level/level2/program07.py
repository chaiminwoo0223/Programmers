# 피보나치 수
# 다이나믹 프로그래밍: 복잡한 문제를 작은 문제로 나누고, 그 결과를 저장하여 복잡한 문제를 해결하는 방법
def solution(n):
    fibonacci = [0] * (n+1)
    fibonacci[1] = 1
    
    for i in range(2, n+1):
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
        
    return fibonacci[n] % 1234567
