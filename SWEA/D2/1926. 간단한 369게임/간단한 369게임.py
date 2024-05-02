T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
nums_dict = {'3':0, '6':0, '9':0}
ans = ""
for i in range(1, T + 1):
    tmp_list = list(str(i))
    tmp = ""
    for j in tmp_list:

        if j in nums_dict:
            tmp += "-"
    if tmp == "":
        ans += str(i)
    else:
        ans += tmp
    ans += " "
print(ans)
