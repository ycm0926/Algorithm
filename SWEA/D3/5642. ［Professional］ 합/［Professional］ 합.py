for i in range(1,int(input())+1):
    n = int(input())
    arr = list(map(int,input().split()))
    max_a = -100000
    sum_a = 0
    for j in range(n):
        sum_a += arr[j]
        if sum_a > max_a:
            max_a = sum_a
        if sum_a < 0:
            sum_a = 0
    print(f'#{i} {max_a}')