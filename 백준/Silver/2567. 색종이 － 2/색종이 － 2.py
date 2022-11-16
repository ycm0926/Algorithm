n = int(input())

graph = [[0] * 101 for _ in range(101)]

dx = [1, 0 ,-1, 0]
dy = [0, -1, 0, 1]

cnt = 0
max_x = 0
max_y = 0
for _ in range(n):
    x, y = map(int, input().split())
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    for n in range(x, x+10):
        for m in range(y, y+10):
            graph[n][m] = 1

for i in range(max_x+10):
    for j in range(max_y+10):
        if graph[i][j] == 1:
            check = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if graph[nx][ny] == 1:
                    check += 1
            if check == 3:
                cnt += 1
            elif check == 2:
                cnt += 2
print(cnt)