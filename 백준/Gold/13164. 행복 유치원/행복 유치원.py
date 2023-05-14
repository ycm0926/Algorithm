N, K = map(int, input().split())
children = list(map(int, input().split()))

diff = []
answer = 0

for i in range(len(children) - 1):
    diff.append(children[i + 1] - children[i])

diff.sort()

for i in range(N-K):
    answer += diff[i]

print(answer)