T = int(input())

for test_case in range(1, T + 1):

    times = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    a, b, c, d = map(int, input().split())
    tmp1, tmp2 = 0, 0
    for k,v in times.items():
        if k == a:
            tmp1 += b
            break
        tmp1 += v


    for k, v in times.items():
        if k == c:
            tmp2 += d
            break
        tmp2 += v

    print(f"#{test_case} {tmp2-tmp1+1}")
