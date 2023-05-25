N = int(input())
M = int(input())
S = input()

cursor, cnt, ans = 0, 0, 0

# IOI라면 두칸씩 확인 시간 개선
while cursor < M-2 :
    if S[cursor:cursor+3] == "IOI" :
        cursor +=2
        cnt +=1
        if cnt == N :
          ans +=1
          cnt -=1

    else:    
        cursor += 1
        cnt = 0

print(ans)
