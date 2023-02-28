import sys

input = sys.stdin.readline
T = int(input())
for i in range(T):
    input()
    note1 = set(map(int, input().split()))
    input()
    note2 = list(map(int, input().split()))
    for i in note2:
        if i in note1:
            print(1)
        else:
            print(0)