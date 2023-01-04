from itertools import combinations
print(*[sorted(i) for i in combinations([int(input()) for _ in range(9)],7) if sum(i) == 100][0],sep='\n')