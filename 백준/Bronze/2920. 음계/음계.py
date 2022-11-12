A = input().split()

if ''.join(A) == '12345678':
    print('ascending')
elif ''.join(A) == '87654321':
    print('descending')
else :
    print('mixed')