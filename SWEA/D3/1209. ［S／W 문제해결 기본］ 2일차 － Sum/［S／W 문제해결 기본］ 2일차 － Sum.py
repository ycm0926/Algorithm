for tc in range(1, 11):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    sm_d1, sm_d2, sm_r = 0, 0, 0
    sm_c = [0] * 100
    for i in range(100):
        sm_r = max(sm_r,sum(arr[i]))
        sm_d2 += arr[i][-(i + 1)]
        for j in range(100):
            if i == j:
                sm_d1 += arr[i][j]
            sm_c[i] += arr[j][i]
    sm_c = max(sm_c)
    print(f'#{tc} {max(sm_r,sm_c,sm_d1,sm_d2)}')
