def solution(answers):
    first = [5 if i%5==0 else i%5 for i in range(1,len(answers)+1)]
    second = []
    third = []

    cnt = 1
    for i in range(len(answers)):
        if i % 2 == 0:
            second.append(2)
        else:
            second.append(cnt)
            cnt += 1
            if cnt == 2:
                cnt += 1
            if cnt == 6:
                cnt = 1

    cnt = 3
    for i in range(len(answers)):                                 
        third.append(cnt)                                   
        if len(third) % 2 == 0:                             
            if cnt == 3 :                                   
                cnt = 1                                    
            elif cnt == 5:                                  
                cnt = 3                                     
            else:                                          
                cnt += 1                                   
                if third[-1] == 2:
                    cnt = 4
    lis = [0,0,0]
    ans = []
    for i in range(len(answers)):
        if answers[i] == first[i]:
            lis[0] +=1
        if answers[i] == second[i]:
            lis[1] +=1
        if answers[i] == third[i]:
            lis[2] +=1

    for i in range(len(lis)):
        if max(lis) == lis[i]:
            ans.append(i+1)
    return ans
