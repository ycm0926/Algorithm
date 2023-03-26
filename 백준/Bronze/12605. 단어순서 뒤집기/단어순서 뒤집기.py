import sys
input = sys.stdin.readline

for i in range(int(input())):
    tmp = input().split()
    print(f"Case #{i+1}: ", end='')
    for j in tmp[::-1]:
        print(j,end=' ')
    print()