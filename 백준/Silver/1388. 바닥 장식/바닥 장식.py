N, M = map(int, input().split())
graph = [list(input()) for i in range(N)]
check_c = 0
check_r = 0
cnt = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == '-':
            check_c += 1
        elif graph[i][j] == '|':
            if check_c >= 1:
                cnt +=1
            check_c = 0
    if check_c >= 1:
        cnt +=1
    check_c = 0

for i in range(M):
    for j in range(N):
        if graph[j][i] == '|':
            check_r += 1
        elif graph[j][i] == '-':
            if check_r >= 1:
                cnt +=1
            check_r = 0
    if check_r >= 1:
        cnt +=1
    check_r = 0

print(cnt)