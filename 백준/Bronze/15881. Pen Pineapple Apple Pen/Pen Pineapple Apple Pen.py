n = int(input())
words = (input())
cnt = 0
i = 0
while 1:
    if words[i] == 'p' and words[i+1] == 'P' and words[i+2] == 'A' and words[i+3] == 'p':
        cnt += 1
        i += 4
    else:
        i += 1
    if i >= n-3:
        break
print(cnt)
