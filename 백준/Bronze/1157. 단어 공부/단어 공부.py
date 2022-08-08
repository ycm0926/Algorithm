words = input().upper()
unique_words = list(set(words)) # 중복 제거 리스트
cnt_list = [] # 각 개수들의 리스트
for i in unique_words:
    cnt = words.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(unique_words[cnt_list.index(max(cnt_list))])