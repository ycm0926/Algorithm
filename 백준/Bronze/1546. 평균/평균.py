T = int(input())
N = list(map(int, input().split()))
m = max(N)

for i in range(len(N)):
    N[i] = N[i]/m

print((sum(N)/T*100))