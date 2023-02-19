def solution(arr):
    
    def gcd(a,b):
        while b > 0:
            a, b = b, a % b
        return a
    
    a = arr.pop()
    while arr:
        b = arr.pop()
        a = a*b//gcd(a,b)
        
    return a