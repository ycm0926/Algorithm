import heapq

def solution(n, works):
    answer = 0
    print(works)

    q = []
    
    for i in works:
        heapq.heappush(q, -i)
        
    if sum(works) > n:
        
        while n > 0:  
            
            tmp = -heapq.heappop(q)
            tmp -= 1
            n -= 1
            heapq.heappush(q,-tmp)
        
        for i in q:
            answer += i**2
            
        return answer
    
    return answer