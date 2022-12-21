def solution(n, m):
    a, b = n, m
    while b>0:          # 유클리드 호제법
        a, b = b, a % b
    return (a,(n*m)//a) # 최대공약수와 최소공배수