n = int(input())
A, B = list(map(int,input().split())), list(map(int,input().split()))
a, b = sorted(A), sorted(B, reverse=True)
res = 0
for i in range(len(a)):
    res += a[i]*b[i]
print(res)