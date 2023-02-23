def solution(n):
    DP = [0] * (n+2)
    
    DP[1] = 1
    DP[2] = 2
    
    if n < 3:
        return DP[n]
    
    for i in range(3, n+1):
        DP[i] = DP[i-2]+DP[i-1]
        
    return DP[n] % 1234567