T = int(input())
    

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int,input().split())
    ans = 0
    graph = [list(map(int,input().split())) for i in range(n)]

    # 가로
    for i in range(n):
        tmp = 0
        for j in range(n):
            if graph[i][j] == 1:
                tmp += 1
                if tmp == k and j == n-1:
                    ans +=1
                elif tmp == k and j < n-1 and graph[i][j+1] == 0:
                    ans +=1
            else:
                tmp = 0
    # 세로
    for i in range(n):
        tmp = 0
        for j in range(n):
            if graph[j][i] == 1:
                tmp += 1
                if tmp == k and j == n-1:
                    ans +=1
                elif tmp == k and j < n-1 and graph[j+1][i] == 0:
                    ans +=1
            else:
                tmp = 0           

    print(f"#{test_case} {ans}")
    