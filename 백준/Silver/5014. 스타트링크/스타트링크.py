from collections import deque

F, S, G, U, D = map(int,input().split())
el = [i for i in range(F+1)]
cnt = [0]*(F+1)
def bfs(S):
    global cnt
    q = deque()
    q.append(S)
    while q:
        v = q.popleft()
        if v == G:
            return print(cnt[v])
        for nv in (v+U, v-D):        # 2가지 U,D 케이스 가져온다.
            if 0 < nv <= F and nv != v:        # 엘베 범위 안이고 시작 지점이 아닐 시 수행
                if cnt[nv] == 0:        # 첫 방문인지 체크
                    cnt[nv] = cnt[v]+1        # 방문 시 개수를 적어준다.
                    q.append(nv)
    return print('use the stairs')
bfs(S)

'''
TIL/회고
- 66%에서 계속 에러나서 질문검색에 반례를 찾아보다 겨우 이유를 알았다.
- 10 10 1 0 1 같은 경우 시작 지점이 1로 카운트돼서 오류가 발생했었다.
'''