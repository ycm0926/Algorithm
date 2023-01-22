import sys
import math

input = sys.stdin.readline
N, L = map(int, input().split())
res, dumy = 0, 0
li = sorted([list(map(int,input().split()))for i in range(N)])
for s, e in li:
    s = max(dumy,s)         # 널빤지가 겹치는지 확인, 겹친다면 dumy값이 s가 된다.
    a = math.ceil((e-s)/L)  # 웅덩이에 필요한 널빤지 개수
    res += a                # 총 널빤지 개수 카운트
    dumy = s+a*L            # 겹치는지 확인을 위한 지점

print(res)