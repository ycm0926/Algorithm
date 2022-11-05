n, m = map(int, input().split())
n_list = list(map(int, input().split()))

start = 0
end = max(n_list)

result = 0
while (start <= end):
    total = 0
    mid = (start+end)//2
    for n in n_list:
        if n > mid:
            total += n - mid
    # total 이 작으므로 왼쪽으로 탐색
    if total < m:
        end = mid - 1
    # 오른쪽으로 탐색
    else:
        result = mid
        start = mid + 1

print(result)


