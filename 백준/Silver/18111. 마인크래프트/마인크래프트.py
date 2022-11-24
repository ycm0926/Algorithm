# 첫번째 풀이
import sys

input = sys.stdin.readline
N, M ,B = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
res = []

#가장 깊은 땅과 가장 높은 땅 찾기
max_b = max(map(max, graph))
min_b = min(map(min, graph))
for k in range(min_b,max_b+1):
    time = 0
    b = B
    for i in range(N):
        for j in range(M):
            c = graph[i][j] - k #  그래프값에서 기준값 뺀 것을 기준
            if c > 0: # 기준이 0 보다 크다면 블록 제거
                b += c
                time += 2*c
            elif c < 0: # 기준이 0 보다 작다면 블록 놓기
                b += c
                time += -c
    if b >= 0: # 최종 남은 블록이 0과 같거나 큰 올바른 경우만 체크
        res.append((time, k))
res.sort(key = lambda x: (x[0],-x[1]))
print(res[0][0], res[0][1])
'''
TIL/회고
- 아니 채우기가 초반에 주어진 B로 전체를 채우는 줄 알았다,,,
- 그리고 순서대로 0,0 에서 0,1 진행하는 줄 알았다,,,
- 한참 뒤에 다른 반례들 보고 깨달음 왜 문제를 제대로 안읽지? ㅁㄴㅇㄹ 하루를 태웠네
- 문제를 천천히 분석하고 시작을 알맞게 하는 게 어렵다.
- 풀긴 풀었지만, 시험으로 나왔으면 시간 다 써도 못 풀었을 듯 ㅠㅠ
- python3 시간 초과는,,, 패스,,,
'''