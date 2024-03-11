import sys
n, m = input().split()
n = int(n)

members = set(list(sys.stdin.readline() for i in range(n)))

if m == 'Y':
    print(len(members))
elif m == 'F':
    print((len(members))//2)    
else:
    print((len(members))//3)