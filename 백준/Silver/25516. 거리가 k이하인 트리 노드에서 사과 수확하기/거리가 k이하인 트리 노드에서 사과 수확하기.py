'''
            0
     1      2       3
    4 5   6 7 8   9 10
'''
import sys
sys.setrecursionlimit(10**6)        # 최대 재귀 깊이를 1000 -> 1,000,000
N, K = map(int,input().split())
input = sys.stdin.readline

tree = [[] * N for i in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)

apple = list(map(int, input().split()))
cnt = 0

def dfs(n,k):
    global cnt
    if k > K:       # 깊이가 목적 깊이 보다 커진다면 종료
        return
    cnt += apple[n]     # 사과 개수 카운트
    for i in tree[n]:       # tree안의 노드들 꺼내서 재귀
        dfs(i,k+1)
dfs(0,0)
print(cnt)

'''
TIL/회고
- 코드는 간결했지만 dfs파라미터를 무엇을 줘야 하는지 바로 생각하지 못했다....
- 최대 100.000 까지 깊어지므로 최대깊이를 생각했어야 했다.
- 깊이가 깊으면 dfs보다는 bfs로 풀자.
'''