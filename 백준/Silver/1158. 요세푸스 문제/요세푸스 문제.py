N, K = map(int, input().split())

lis =[i for i in range(1,N+1)]
res = []
cnt = K-1
while 1:
    if len(lis) == 1:       # lis 남은 개수가 한 개면 바로 넣어준다.
        res.append(lis.pop())
        break
    res.append(lis.pop(cnt))
    cnt += K-1      # cnt를 K-1 만큼 증가
    cnt = cnt % len(lis)        # 나머지 연산으로 cnt가 lis길이안에서 돌게끔 설정
print(f"<{str(res)[1:-1]}>")