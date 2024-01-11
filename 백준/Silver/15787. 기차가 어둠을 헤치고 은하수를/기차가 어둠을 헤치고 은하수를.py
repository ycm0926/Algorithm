from collections import deque
import sys

N, M = map(int, input().split())
input = sys.stdin.readline

trains = [deque([False] * 20) for _ in range(N)]

for i in range(M):
    command = list(map(int, input().split()))

    if command[0] == 1:
        trains[command[1] - 1][command[2] - 1] = True
    
    elif command[0] == 2:
        trains[command[1] - 1][command[2] - 1] = False

    elif command[0] == 3:
        trains[command[1] - 1].rotate(1)
        trains[command[1] - 1][0] = False

    else:
        trains[command[1] - 1].rotate(-1)
        trains[command[1] - 1][-1] = False

result = set(tuple(trains[i]) for i in range(N))
print(len(result))
