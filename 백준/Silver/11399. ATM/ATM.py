n = int(input())
num = list(map(int, input().split()))
cnt = 0
num.sort()
for i in range(1,len(num)+1):
    cnt += sum(num[:i])
print(cnt)