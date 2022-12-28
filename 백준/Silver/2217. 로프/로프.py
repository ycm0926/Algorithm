import sys
input = sys.stdin.readline

dummy = []
for i in range(int(input())):
    dummy.append(int(input()))
res = 0
dummy.sort(reverse=True)
while dummy:
    res = max(res,dummy[-1]*len(dummy))
    dummy.pop()
print(res)