import sys
from collections import deque

'''
    쌓아올려지는 상자의 수를 나타내는 H가 주어진다.
    M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수
    단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다.
    정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 
    토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 
    만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고,
    토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다. 

'''

input = sys.stdin.readline
M, N, H = map(int, input().split())
ans = 1
L = N * H
dx = [0, 1, 0, -1, N, -N]
dy = [1, 0, -1, 0, 0, 0]

boxes = [list(map(int, input().split())) for i in range(L)]


def bfs():
    global ans

    while q:
        x, y = q.popleft()

        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < L and 0 <= ny < M and boxes[nx][ny] == 0:
                # x좌표의 경계조건을 높이 생각한 위충, 아래층 조건
                if k == 1 and x % N == N - 1:
                    continue
                if k == 3 and x % N == 0:
                    continue

                q.append((nx, ny))
                boxes[nx][ny] = boxes[x][y] + 1


q = deque([])
for i in range(L):
    for j in range(M):
        if boxes[i][j] == 1:
            q.append((i, j))
bfs()
for i in range(L):
    ans = max(ans, max(boxes[i]))
    if 0 in boxes[i]:
        print(-1)
        exit()
else:
    print(ans - 1)
