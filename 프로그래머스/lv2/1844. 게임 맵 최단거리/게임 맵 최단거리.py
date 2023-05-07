from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    def bfs(x,y):
        q = deque([(x,y)])
        maps[x][y] = 2

        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if -1 < nx < n and -1 < ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx,ny))
                    
    bfs(0,0)
    
    return -1 if maps[n-1][m-1] == 1 else maps[n-1][m-1]-1