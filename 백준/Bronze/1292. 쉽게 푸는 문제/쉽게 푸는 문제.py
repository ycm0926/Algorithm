a, b = map(int, input().split())
res = [i for i in range(1,b+1) for j in range(1,i+1)]
print(sum(res[a-1:b]))