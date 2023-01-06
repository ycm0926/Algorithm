a = input()
print(''.join(sorted(a)[::-1])if sum(map(int,a))%3==0 and'0'in a else-1)