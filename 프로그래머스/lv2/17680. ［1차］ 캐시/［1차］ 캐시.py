from collections import deque

def solution(cacheSize, cities):
    
    if cacheSize == 0: 
        return len(cities)*5
    
    answer = 0
    q = deque([])
  
    for i in range(len(cities)):             # 모든 cities 소문자로 변환
        cities[i] = cities[i].lower()
    
    for i in cities:                                          
        if len(q) < cacheSize:              # q의 길이가 cacheSize보다 작고
            if i in q:                      # i가 q에 있는 경우
                q.remove(i)
                answer += 1  
            else:                           # i가 q에 없는 경우
                answer += 5

            q.append(i)

        else:                               # q의 길이가 cacheSize보다 같거나 크고
            if i in q:                      # i가 q에 있는 경우
                if q[0] == i:               # q[0]에 있다면
                    q.popleft()
                else:                       
                    q.remove(i)

                q.append(i)
                answer += 1

            else:                           # i가 q에 없는 경우
                q.popleft()
                q.append(i)

                answer += 5

    return answer