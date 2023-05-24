N = int(input())
M = int(input())
graph = list(input())
tmp = 'IO'*N+'I'
cnt = 2*N+1
ans = 0

for i in range(0,M-(2*N+1)+1):
    if ''.join(graph[i:i+cnt]) == tmp:
       ans += 1
print(ans)