from collections import deque
N, M = map(int,input().split())
lis = list(map(int,input().split()))
q = deque(i for i in range(1,N+1))
cnt = 0
for i in lis:
    while i != q[0]:        # q의 첫 번째 값이 i가 아니라면 반복
        if q.index(i) > len(q)//2:      # 절반의 길이 보다 i의 index가 크다면 오른쪽으로 한 칸 이동
            q.appendleft(q.pop())
            cnt += 1
        else:
            q.append(q.popleft())       # 절반의 길이 보다 i의 index가 작다면 왼쪽으로 한 칸 이동
            cnt += 1
    q.popleft()
print(cnt)