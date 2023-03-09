import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for i in range(N)]
answer = []

for i in range(N):
    
    if i+k > N:
        answer.append(len(set(sushi[i:]+sushi[:(i+k)%N]+[c])))
    else:
        answer.append(len(set(sushi[i:i+k]+[c])))


print(max(answer))