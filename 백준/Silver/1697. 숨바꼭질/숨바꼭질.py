from collections import deque

N ,K = map(int,input().split())
graph = [0] * 100001

def bfs(n):
    q = deque([n])
    while q:
        v = q.popleft()
        if v == K:
            return graph[v]
        
        for i in (v-1,v+1,v*2):
            if 0<=i<=100000 and not graph[i]:
                graph[i] = graph[v] + 1
                q.append(i)

print(bfs(N))