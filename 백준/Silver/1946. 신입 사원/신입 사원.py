import sys

input = sys.stdin.readline
for i in range(int(input())):
    N = int(input())
    graph = []
    cnt = 1
    m_c = 0
    dum = []
    for i in range(1,N+1):
        a, b =map(int,input().split())
        graph.append((a,b))
    g = sorted(graph)
    m_c = g[0][1]
    a,b = g[0]
    e = b
    for c,d in g[1:]:
        if d < b:
            b = min(b,d)
            cnt +=1
    print(cnt)