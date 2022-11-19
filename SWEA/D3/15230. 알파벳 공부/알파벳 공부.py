word = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for tc in range(1, int(input())+1):
    words = input()
    cnt = 0
    for i in range(len(words)):
        if words[i] == word[i]:
            cnt +=1
        else:
            break
    print(f'#{tc} {cnt}')
