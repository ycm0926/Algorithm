import sys

N, M = map(int,input().split())
input = sys.stdin.readline
lis = [0]       # 1번째 부터 값을 받기 위함
cnt = 0
for i in map(int,input().split()):
    cnt += i        # 누적 합을 위한 변수
    lis.append(cnt)
for _ in range(M):
    a,b = map(int, input().split())
    print(lis[b]-lis[a-1])

'''
TIL/회고
- 한번 구간합을 구하는 시간복잡도는 O(n)이고 m번동안 수행을 하게 된다면
- 총 시간복잡도는 O(nm)이 되는데 데이터가 10만개가 되면 시간초과 오류가 나게 된다.
- DP의 메모이제이션 처럼 누적합을 저장 후 각 자리에서 빼주는 방식으로 구현하면 된다.
- 처음 시간초과가 나왔을 때 한참을 봐도 틀린 부분을 찾기가 어려웠다.
'''