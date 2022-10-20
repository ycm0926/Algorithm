import sys

array = []

for _ in range(int(input())):
    i = int(sys.stdin.readline())
    
    if i == 0:
        array.pop()  
    else:
        array.append(i)

print(sum(array))