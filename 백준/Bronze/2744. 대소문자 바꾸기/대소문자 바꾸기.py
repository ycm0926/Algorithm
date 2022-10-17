words = input()
ans = []
for i in words:
    if i.isupper():
        ans.append(i.lower())
    else:
        ans.append(i.upper())
print(*ans, sep='')
