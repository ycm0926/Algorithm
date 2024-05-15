
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    times = [list(map(int, input().split())) for i in range(N)]
    ans = [[0]*N for i in range(N)]

    print("#{}".format(test_case))
    # 90도, 180,도 270도 회전한 행렬 초기화
    times_90 = [[0 for _ in range(N)] for _ in range(N)]
    times_180 = [[0 for _ in range(N)] for _ in range(N)]
    times_270 = [[0 for _ in range(N)] for _ in range(N)]

    # arr 행렬 90도 회전
    for i in range(N):
        for j in range(N):
            times_90[i][j] = times[N - 1 - j][i]
    # arr_90 행렬을 90도 회전하면 arr_180 행렬
    for i in range(N):
        for j in range(N):
            times_180[i][j] = times_90[N - 1 - j][i]

    # arr_180 행렬을 90도 회전하면 arr_270 행렬
    for i in range(N):
        for j in range(N):
            times_270[i][j] = times_180[N - 1 - j][i]

    for i in range(N):
        for a in range(N):
            print(times_90[i][a], end='')
        print(end=' ')
        for b in range(N):
            print(times_180[i][b], end='')
        print(end=' ')
        for c in range(N):
            print(times_270[i][c], end='')
        print()