def solution(n):
    b = bin(n)[2:]
    cnt = b.count('1')
    for i in range(n+1,1000001):
        i_b = bin(i)[2:]
        
        if i_b.count('1') == cnt:
            return i