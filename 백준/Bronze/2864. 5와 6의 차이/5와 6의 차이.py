a, b = map(int, input().split())

a = list(str(a))
b = list(str(b))
max_a, max_b = [], []
min_a, min_b = [], []
for i in a:
    if i == '5' or i == '6':
        min_a.append('5')
        max_a.append('6')
    else:
        min_a.append(i)
        max_a.append(i)

for i in b:
    if i == '5' or i == '6':
        min_b.append('5')
        max_b.append('6')
    else:
        min_b.append(i)
        max_b.append(i)
a1 = int(''.join(min_a))
b1 = int(''.join(min_b))
a2 = int(''.join(max_a))
b2 = int(''.join(max_b))

print(a1+b1,a2+b2)