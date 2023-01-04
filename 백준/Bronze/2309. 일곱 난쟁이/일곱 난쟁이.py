import sys
from itertools import combinations

d = [int(input()) for _ in range(9)]
print(*[sorted(i) for i in combinations(d,7) if sum(i) == 100][0],sep='\n')