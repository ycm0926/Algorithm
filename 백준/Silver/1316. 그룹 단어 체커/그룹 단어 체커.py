res = 0
for i in range(int(input())):
    word = input()
    lst = []
    cnt = True
    for j in range(len(word)):
        # 리스트 안에 단어가 있고 바로 전에 나온게 아니라면 False 반환
        if word[j] in lst and word[j] != word[j-1]:
            cnt = False
            break
        else:
            lst.append(word[j])
    if cnt == True:
        res += 1
print(res)