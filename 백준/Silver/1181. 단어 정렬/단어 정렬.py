ans = []
for i in range(int(input())):
    ans.append(input())

ans.sort()
ans.sort(key=lambda ans: len(ans))

for i in set(ans):
    print(i)