from collections import deque

def bfs(x,y,n,computers):
    
    q = deque([[x,y]])
    computers[x][y] = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(n):
            if computers[y][i] == 1:
                computers[y][i] = 0
                q.append([y,i])


def solution(n, computers):
    global answer
    answer = 0
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                bfs(i,j,n,computers)
                
                answer += 1

    return answer