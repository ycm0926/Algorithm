n = int(input())
ans = 1
cnt = 0
for i in range(1,n+1): # 팩토리얼 코드
    ans *= i

lst = list(str(ans))
for j in lst[-1::-1]: # 0 개수 확인
    if j == '0':
        cnt +=1
    if cnt != 0 and j != '0':
        break

print(cnt)