n, m, l = map(int, input().split())

total_cnt = [0]*n
total_cnt[0] = 1

p = 0
cnt = 0
while 1:
    if m == 1:
        print(0)
        break
    elif total_cnt[p] % 2 == 1:
        p += l
        if len(total_cnt) <= p:
            p %= len(total_cnt)
        total_cnt[p] += 1
        cnt += 1

    elif total_cnt[p] % 2 == 0:
        p -= l
        if -len(total_cnt) > p:
            p += len(total_cnt)
        total_cnt[p] += 1
        cnt += 1
    if total_cnt[p] == m:
        print(cnt)
        break

