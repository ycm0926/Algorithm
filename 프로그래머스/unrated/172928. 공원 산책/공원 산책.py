from collections import deque

def solution(park, routes):
    answer = [0,0]
    tmp = [0,0]
    move = {'N':(-1,0), 'S':(1,0), 'W':(0,-1), 'E':(0,1)}
    
    n = len(park)
    m = len(park[0])
                
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                answer[0], answer[1] = i, j
                break

    for i in routes:
        tmp[0], tmp[1] = answer[0], answer[1]
        
        for j in range(int(i[2:])):
            nx = tmp[0] + move[i[0]][0]
            ny = tmp[1] + move[i[0]][1]
            
            # 조건에 만족하면 tmp값을 next 해준다.
            if 0 <= nx < n and 0 <= ny < m and park[nx][ny] != 'X':
                tmp[0], tmp[1] = nx, ny
            else:   # 조건에 만족하지 않다면 처음 값으로 tmp 업데이트
                tmp[0], tmp[1] = answer[0], answer[1]
                break
                       
        answer[0], answer[1] = tmp[0], tmp[1]

    return answer