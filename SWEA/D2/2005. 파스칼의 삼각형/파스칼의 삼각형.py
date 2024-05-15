T = int(input())

for tc in range(T):
    N = int(input())
    arr = [[0]*N for i in range(N)]
    arr[0][0] = 1

    print(f"#{tc+1}")
    print(1)
    for i in range(1, N):
        for j in range(i+1):
            if j == 0 or j == i:
                arr[i][j] = 1
                print(arr[i][j], end=' ')
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
                print(arr[i][j], end=' ')
        print()