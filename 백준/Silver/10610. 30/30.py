a = int(''.join(sorted(list(input()),reverse=True)))
print(a if a % 30 == 0 else -1)