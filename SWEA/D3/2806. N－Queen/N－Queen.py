def dfs(n):
    global ans

    if n == N:
        ans += 1 
        return

    for i in range(N):
        if v1[i] == v2[n+i] == v3[n-i] == 0:
            v1[i] = v2[n+i] = v3[n-i] = 1
            dfs(n+1)
            v1[i] = v2[n+i] = v3[n-i] = 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    ans = 0

    # 행열, 대각선1, 대각선2 체크 배열
    v1, v2, v3 = [[0]*N*2 for _ in range(3)]
    dfs(0)
    print(f"#{test_case} {ans}")