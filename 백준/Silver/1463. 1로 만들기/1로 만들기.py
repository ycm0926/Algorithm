x = int(input())
d = [0]*(x+1)      # x+1 이유는 1번째 개수는 d[2]=1 이기 때문이다. 즉, d[1]이 시작점

for i in range(2,x+1):  # 1일 경우 0이기 때문에 2부터 시작 (바텀 업 방식)
    d[i] = d[i-1] + 1       # 1을 먼저 빼는 이유는 다음에 계산할 나누기가 1을 뺀 값보다 작거나 큼에 따라 교체되기 때문
                            # +1은 바로 전 횟수에서 +1 한 것이 지금 횟수
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)     # 2로 나눠진다면, 2로 나눠지는 횟수와 -1의 횟수 비교
    if i%3 == 0:        # elif, else 사용하면 안 된다. %2,%3이 된다면 모두 비교해야 하기 때문이다.
        d[i] = min(d[i], d[i//3]+1)     # 3으로 나눠진다면, 3으로 나눠지는 횟수와 -1 또는 2의 횟수 비교

print(d[x])

'''
TIL/회고
- 안 풀려서 다시 생각해보니 어디서 보았던 문제라 생각이 들어 나의 블로그를 보고 다시 이해했다.
- 바텀 업과 탑 다운, BFS와 DFS 다 가능한 문제로 복습하기에 좋은 문제라고 생각한다.
'''