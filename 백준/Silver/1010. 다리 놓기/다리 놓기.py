# 나의 풀이 (python3 112ms)
from math import factorial
import sys

input = sys.stdin.readline
for i in range(int(input())):
    w, s = map(int, input().split())
    print(factorial(s)//(factorial(s-w)*factorial(w))) # sCw 조합 구현
'''
# 다른 사람 풀이 (python 56ms)

import sys
r=sys.stdin.readline

for _ in range(int(r())):
    n,m=map(int,r().split())
    n=min(n,m-n)
    s=1
    for i in range(n):
        s=s*(m-i)//(i+1)
    print(s)

# 다른 사람 풀이2

from math import*
for i in range(int(input())):
    a,b=map(int,input().split())
    print(comb(b,a))

TIL/회고
- 이게 조합인지 몰랐다... 하 결국 답지를 보고 말았다...ㅠㅠ 
- 조합인지 알면 금방 풀렸지만 모르면 난이도 급상승
- 56ms인 1등 풀이는 아직 잘 모르겠다...
'''