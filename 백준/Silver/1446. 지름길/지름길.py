import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 지름길의 개수 N, 고속도로의 길이 D
N, D = map(int,input().split())
graph = [[] for i in range(D+1)]
distance = [INF] * (D+1)

# 핵심 처음부터 끝까지 연결된 기본 고속도로 생성 
for i in range(D):
    graph[i].append((i+1,1))

for i in range(N):
    start, end, length = map(int,input().split())

    # 고속도로 길이보다 넘어가면 무시
    if end > D:
        continue
    graph[start].append((end,length))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐서, 다른노드로 이동하는 거리가 더 잛은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
                
dijkstra(0)
print(distance[D])