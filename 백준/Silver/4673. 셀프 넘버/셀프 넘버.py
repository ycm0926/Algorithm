lst = []
for i in range(10000): # 1~10000까지 생성자들 lst에 추가
    n_l = list(map(int, str(i)))
    lst.append(sum(n_l)+i)

for j in range(1,10000): # 1~100000까지 생성자 아니면 출력
    if j not in lst:
        print(j)