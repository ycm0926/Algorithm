def solution(n):
    a = [False,False] + [True]*(n-1)
    primes= 0

    for i in range(2,n+1):
        if a[i]:
            primes += 1
            for j in range(2*i, n+1, i):
                a[j] = False
        
    return primes