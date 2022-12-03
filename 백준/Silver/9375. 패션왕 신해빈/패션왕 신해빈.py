import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    clothes = defaultdict(list)
    res = 1
    for _ in range(n):
        a,b = input().split()
        clothes[b].append(a)
    for a, b in clothes.items():
        res *= len(b)+1
    print(res-1)

'''
TIL/회고
- 수포자의 수학... 결국 답지 보고 이해했다...
- defaultdict 써보고 싶어서 사용하여 풀어보았다.
- 아래는 이해한 내용

해빈이는 적어도 1개만 걸치면 밖에 나갈 수 있다. 
즉 옷을 입는 모든 경우의 수에서 전부다 안 입는 경우를 제외해서 계산하면 된다.
예를 들어 상의 2개, 바지 3개가 있다면 
(2 + 1(상의를 안 입는 경우)) * (3 + 1(바지를 안 입는 경우)) - 1
으로 총 경우의 수는 11이다.
'''