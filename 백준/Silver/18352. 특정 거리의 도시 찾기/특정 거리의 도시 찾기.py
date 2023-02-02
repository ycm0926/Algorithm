import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)              # 무한 설정

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 입력 받기 
N, M, K, X = map(int,input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(N+1)]
# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF]*(N+1)

# 간선 정보 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b,1))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        
        # 값이 작다는 것은 이미 처리되어 최소 값이 들어가 있다는 의미
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) 


dijkstra(X)

if K not in distance:
    print(-1)
else:
    for i in range(1,N+1):
        if distance[i] == K:
            print(i)