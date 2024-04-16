import heapq

def solution(operations):
    answer = [0,0]
    
    q = []
    
    for i in operations:
        a, b = i.split()
        
        if a == 'I':
            heapq.heappush(q, int(b))
        else:
            if len(q) > 0:
                if b == '-1':
                    heapq.heappop(q)
                else:
                    q.remove(max(q))
                    heapq.heapify(q)
    print(q)
    if len(q) > 0:
        answer[0] = max(q)
        answer[1] = min(q)
    
    return answer