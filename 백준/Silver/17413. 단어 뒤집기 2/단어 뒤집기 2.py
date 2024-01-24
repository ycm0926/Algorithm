words = input()
ans = ""
tmp = ""
check = True

for i in words:
    if i == '<':
        if tmp:
            ans += tmp[::-1]
            tmp =""
        check = False
        ans += i
    elif i == '>':
        ans += i 
        check = True
    elif check == False:
        ans += i
    elif check == True and i == " ":
        ans += tmp[::-1]
        ans += " "
        tmp = ""
    else:
        tmp += i

if tmp:
    ans += tmp[::-1]
print(ans)