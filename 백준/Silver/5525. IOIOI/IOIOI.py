N = int(input())
M = int(input())
graph = list(input())
tmp = 'IO'*N+'I'
cnt = 2*N+1
ans = 0

# KMP 알고리즘
for i in range(0,M-(2*N+1)+1):
    if graph[i] == 'I' and graph[i+cnt-1] == 'I' and ''.join(graph[i:i+cnt]) == tmp:
       ans += 1
print(ans)