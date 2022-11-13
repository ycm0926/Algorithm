import sys
input()
input = sys.stdin
m = []
for i in map(int, input):
    m.append(i) if i != 0 else m.pop()
print(sum(m))