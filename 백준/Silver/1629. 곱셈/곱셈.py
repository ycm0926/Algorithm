import sys

a, b, c= map(int,input().split())

def f(a,b):

    if b == 1:
        return a
    
    elif b%2 == 0:
        tmp = f(a,b//2)
        return (tmp*tmp)%c
    else:
        tmp = f(a,(b-1)//2)
        return(tmp*tmp*a)%c

print(f(a,b)%c)