def solution(n):
    answer = 0
    Finn = [i for i in range(1,(n//2)+2)]
    l_Finn = len(Finn)
    
    for i in range(l_Finn):
        cnt = Finn[i]
        for j in range(i+1, l_Finn):
            cnt += Finn[j]
            if cnt == n:
                answer += 1
                break
            if cnt > n:
                break

    return answer+1
                
