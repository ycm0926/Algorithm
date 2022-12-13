import math
N = int(input())
dp = 4
for i in range(int(math.sqrt(N)),0,-1):
    n = N
    if i**2 == N:
        dp = min(dp,1)
    for j in range(int(math.sqrt(n-i**2)),0,-1):
        if i**2 + j**2 == N:
            dp = min(dp, 2)
        for k in range(int(math.sqrt(n-i**2+j**2)),0,-1):
            if i**2 + j**2 + k**2 == N:
                dp = min(dp, 3)
print(dp)