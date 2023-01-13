import sys
a = list(map(int,sys.stdin.read().splitlines()))
for i in a:
    if i < 40:
        a[a.index(i)] = 40
print(sum(a)//len(a))