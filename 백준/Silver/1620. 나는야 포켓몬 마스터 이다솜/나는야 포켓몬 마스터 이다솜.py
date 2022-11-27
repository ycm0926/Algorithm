import sys
input = sys.stdin.readline
N, M = map(int,input().split())

encyclopedia = {}
for i in range(1,N+1): # key:번호, value:포켓몬 딕셔너리 생성
    v = input().strip()
    encyclopedia[str(i)] = v
d = {v:k for k,v in encyclopedia.items()} #  key, value swap딕셔너리 생성
encyclopedia.update(d) # 두개의 딕셔너리 결합
for j in range(M): # 정답 출력
    q = input().strip()
    print(encyclopedia[q])

'''
TIL/회고
- 딕셔너리에 친숙해질 수 있었던 문제 재밌었다.
- 시간초과가 뜰 줄 몰랐다...
'''