T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int,input().split())
    ans = 0
    graph = [list(map(int,input().split())) for i in range(n)]

    for i in range(n):
        for j in range(n):
            if n <= i+m-1 or n <= j+m-1:
                break
            else:
                tmp = 0
                for k in range(i, i+m):
                    for l in range(j, j+m):
                        tmp += graph[k][l]
                        # print(tmp,graph[k][l])
                # print()
                ans = max(ans,tmp)
    print(f"#{test_case} {ans}")
