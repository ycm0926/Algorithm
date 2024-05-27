from collections import Counter

words = sorted(input())
words_cnt = Counter(words)

cnt = 0
ans = ''
mid = ''

for k, v in list(words_cnt.items()):

    if v % 2 != 0:
        cnt += 1
        mid = k
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()

for k, v in sorted(words_cnt.items()):
    ans += (k * (v // 2)) 

print(ans + mid + ans[::-1])