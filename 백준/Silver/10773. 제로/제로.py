import sys

array = []
for _ in range(int(input())):
    array.append(int(sys.stdin.readline()))
    if array[-1] == 0:
        array.pop()
        array.pop()
print(sum(array))
