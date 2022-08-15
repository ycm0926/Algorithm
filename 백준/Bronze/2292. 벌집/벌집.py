n = int(input())
cnt = 1
for i in range(0, 1000000001):
    cnt += (6*i)

    if cnt >= n:
        print(i+1)
        break