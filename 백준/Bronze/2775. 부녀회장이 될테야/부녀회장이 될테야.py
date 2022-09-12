def recursion(k, n):
    ans = 0
    if k == 0:
        return (n)
    else:
        for i in range(1, n+1):
            ans += recursion(k-1, i)
        return ans


t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(recursion(k, n))