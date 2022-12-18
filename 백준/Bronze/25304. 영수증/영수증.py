x = int(input())
res = 0
for i in range(int(input())):
    a,b = map(int,input().split())
    res += a*b
if res == x:
    print('Yes')
else:
    print('No')