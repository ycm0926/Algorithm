n = int(input())
max_res = 0
ans = []
for i in range(n):
    ans.append(int(input()))
ans.sort()
for j in ans:
    max_res = max(max_res, j*n)
    n -= 1
print(max_res)