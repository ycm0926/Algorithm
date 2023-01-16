import sys

li = list(map(int,sys.stdin.read().splitlines()))
res = []
def div(i,n):
    if n <= 1:
        return i
    n //= 3
    return div(i[:n],n)+' '*n+div(i[n*2:],n)

for i in li:
    res.append('-'*(3**i))
for i in res:
    print(div(i,len(i)))