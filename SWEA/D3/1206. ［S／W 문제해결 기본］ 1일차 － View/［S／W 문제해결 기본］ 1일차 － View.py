for i in range(1,11):
    n = map(int, input().split())
    b = list(map(int,input().split()))
    ans = 0
    for j in range(2, len(b)-2):
        k = max(b[j+1],b[j+2],b[j-1],b[j-2])
        l = b[j] - k
        if l > 0:
            ans += l
    print(f'#{i} {ans}')
