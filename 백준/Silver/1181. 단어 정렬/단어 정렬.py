ans = []
for i in range(int(input())):
    ans.append(input())

ans.sort()
ans.sort(key=len)

for i in set(ans):
    print(i)