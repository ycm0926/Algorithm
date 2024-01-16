from itertools import permutations

n, m = map(int,input().split())
arr = list(permutations([i for i in range(1, n+1)],m))
for i in range(len(arr)):
    print(*arr[i])
