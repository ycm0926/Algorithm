N = input()
n = N
if len(n) == 1:
    n = '0'+n
cnt = 0

while 1:
    n_l = list(map(int, str(n))) # n을 int형 리스트로 만들어준다.
    n_s = list(map(int, str(sum(n_l)))) # 리스트 값들 더한 후 int형 리스트로 만들어준다.
    n = int(str(n_l[-1])+str(n_s[-1])) # 가장 오른쪽 자릿수 들을 붙여준다.
    cnt += 1
    if n == int(N): # 입력값과 같다면 종료
        print(cnt)
        break

'''
TIL/회고
- 조금 헷갈릴 수 있는 문제지만 침착하게 풀면 할만한 문제
'''