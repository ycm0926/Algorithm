# 나의 풀이
from math import factorial

for i in range(int(input())):
    w, s = map(int, input().split())
    print(factorial(s)//(factorial(s-w)*factorial(w)))
