T = int(input())

for test_case in range(1, T + 1):

    times = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    a, b, c, d = map(int, input().split())
    tmp1, tmp2 = 0, 0
    for k,v in times.items():
        if k < a:
            tmp1 += v
        elif k == a:
            tmp1 += b

        if k < c:
            tmp2 += v
        elif k == c:
            tmp2 += d
            
    print(f"#{test_case} {tmp2-tmp1+1}")
