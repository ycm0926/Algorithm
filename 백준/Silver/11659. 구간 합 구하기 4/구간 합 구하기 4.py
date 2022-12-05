import sys

N, M = map(int,input().split())
input = sys.stdin.readline
lis = [0]       # 1번째 부터 값을 받기 위함
for i in map(int,input().split()):
    lis.append(i)
for i in range(1,N+1):      # 합을 구하는 반복문
    lis[i] = lis[i] + lis[i-1]
for _ in range(M):      # 누적 합
    a,b = map(int, input().split())
    print(lis[b]-lis[a-1])