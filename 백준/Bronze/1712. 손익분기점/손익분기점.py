a,b,c = map(int,input().split())
if b >= c:
    print(-1)
else:
    res = c - b
    print(a//res+1)