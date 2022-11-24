import sys

input()
print(sum(list(s) == sorted(s, key=s.find) for s in sys.stdin.readlines()))