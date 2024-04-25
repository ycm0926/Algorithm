T = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for test_case in range(1, T + 1):
    n = int(input())
    graph = [[0] * (n+1) for i in range(n+1)]
    tmp = 1
    x, y = 0, 0

    while tmp <= (len(graph)-1)**2:
        for i in range(4):
            for j in range(n):
                x = x + dx[i]
                y = y + dy[i]

                if graph[x][y] != 0:
                    break

                graph[x][y] = tmp
                tmp += 1
            if i == 0  or i == 2:
                n -= 1
    print(f'#{test_case}')
    for i in range(len(graph)-1):
        for j in range(1,len(graph)):
            print(graph[i][j], end= ' ')
        print()
