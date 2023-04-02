from collections import deque

N = int(input())
graph = [[0]*N for i in range(N)]
graph[0][0] = 1

K = int(input())
for i in range(K):
    x, y = map(int,input().split())
    graph[x-1][y-1] = 'A'               # 시작 좌표가 1,1 주의

L = int(input())

tail = deque([[0,0]])                   # 꼬리가 이동해야 할 방향 메모
head = [[-1,0],[0,1],[1,0],[0,-1]]      # 머리 방향
d = 1
x, y = 0, 0
cnt = 0
change = deque()

for _ in range(L):
    tmp = input().split()
    change.append((int(tmp[0]), tmp[1]))

X, C = change.popleft()

while 1:
    nx = x + head[d][0]
    ny = y + head[d][1]
    
    # 범위 이탈 or 자기 몸
    if nx < 0 or nx >= N or ny < 0 or ny >= N or graph[nx][ny] == 1:
        print(cnt+1)
        exit() 
    else:
        cnt += 1
        tail.append([nx,ny])
        x, y = nx, ny

        # A가 아니라면 꼬리 좌표 이동
        if graph[x][y] != 'A':
            tx, ty = tail.popleft()
            graph[tx][ty] = 0

        graph[x][y] = 1

    if X == cnt:
        # 왼쪽
        if C == 'L':
            d -= 1
            if d == -1:
                d = 3
        
        # 오른쪽
        elif C == 'D':
            d += 1
            if d == 4:
                d = 0
        # 변환 조건이 남았다면
        if change:
            X, C = change.popleft()