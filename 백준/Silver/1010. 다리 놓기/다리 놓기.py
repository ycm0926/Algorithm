import sys
from math import factorial

input = sys.stdin.readline
for i in range(int(input())):
    N,M = map(int,input().split())
    print(factorial(M)//(factorial(N)*factorial(M-N)))