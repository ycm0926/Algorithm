def solution(record):
    answer = []
    users = {}
    
    for i in record:
        user = i.split()
        
        if user[0] == 'Enter':
            users[user[1]] = user[2]
            answer.append([user[1],"님이 들어왔습니다."])
        elif user[0] == 'Leave':
            answer.append([user[1],"님이 나갔습니다."])
        else:
            users[user[1]] = user[2]
            
    for i in range(len(answer)):
        answer[i][0] = users[answer[i][0]]
        answer[i] = "".join(answer[i])        
            
    return answer