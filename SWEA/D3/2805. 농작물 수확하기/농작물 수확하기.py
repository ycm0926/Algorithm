T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    arr = [list(map(int, list(input()))) for i in range(N)]
    ans = 0

    s, e = N//2, N//2
    for i in range(N):
        for j in range(s, e+1):
            ans += arr[i][j]
        # mid 전 까지는 s-e 간격 늘리고 이후는 줄인다
        if i < N//2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print(f"#{test_case} {ans}")