_ = input()

arr = list(map(int, input().split()))
ans = 0

for i in arr:
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    # cnt가 2인 경우 즉, 1과 자기자신 일때만 카운트
    if cnt == 2:
        ans += 1

print(ans)