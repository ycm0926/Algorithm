n = int(input())
cnt = 0
for i in range(1,n+1):
    for j in range(1, int(i**0.5)+1):
        if i % j == 0:
            cnt += 1
print(cnt)