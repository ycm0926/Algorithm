a, b = input().split()

for i in a:
    if i in b:
        check = i
        break
where_a = a.index(check)
where_b = b.index(check)

for i in range(len(b)):
    if i == where_b:
        print(a)
        continue
    for j in range(len(a)):
        if j == where_a and j == len(a)-1:
            print(b[i], end='\n')
        elif j == where_a:
            print(b[i], end='')
        elif j == len(a)-1:
            print('.', end='\n')
        else:
            print('.', end='')
