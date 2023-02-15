def solution(n):
    n_cnt = bin(n)[2:].count('1')
    for i in range(n+1,1000001):
        i_cnt = bin(i)[2:].count('1')
        
        if i_cnt == n_cnt:
            return i