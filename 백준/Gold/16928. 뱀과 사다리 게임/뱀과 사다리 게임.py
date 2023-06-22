from collections import deque

n, m = map(int,input().split())
dict = {}

def bfs():
    v[1] = True
    q = deque([1])

    while q:
        y = q.popleft()

        if y == 100:
            print(board[-1])
            break

        for dice in range(1,7):
            ny = y + dice

            if ny <= 100 and not v[ny]:
                if ny in dict:
                    ny = dict[ny]
                if not v[ny]:
                    v[ny] = True
                    board[ny] = board[y] + 1
                    q.append(ny)

for i in range(n+m):
    a,b = map(int,input().split())
    dict[a] = b

board = [0]*101
v = [False]*101
bfs()
