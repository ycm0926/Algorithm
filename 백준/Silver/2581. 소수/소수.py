import sys
import math
m,n = map(int, sys.stdin.read().splitlines())
res = []
for i in range(m,n+1):
    if i == 1:
        continue
    cnt = 0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j == 0:
            cnt = 1
            break
    if cnt == 0:
        res.append(i)
if res:
    print(sum(res))
    print(min(res))
else:
    print(-1)