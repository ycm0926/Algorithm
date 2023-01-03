def solution(n):
    if n == 1:
        return n
    res = []
    for i in range(2,n+1):
        cnt = False
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                cnt = True
                break
        if cnt == False:
            res.append(i)
    return len(res)