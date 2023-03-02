def solution(s):
    answer = []
    s = sorted(s[2:-2].split('},{'), key=len)
    answer.append(int(s[0]))

    for i in s[1:]:
        idx = 0
        
        for j in range(len(i)):
            if i[j] == ',' :
                tmp = int(i[idx:j])
                if tmp not in answer:
                    answer.append(tmp)
                idx = j+1
                
        if int(i[idx:]) not in answer:
            answer.append(int(i[idx:]))
            
    return answer