'''
# base64 라이브러리 사용 풀이
from base64 import b64decode
 
T = int(input())
 
for tc in range(1, T + 1):
 
    word = input()
    res = b64decode(word).decode('UTF-8')
 
    print('#{} {}'.format(tc,res))

'''
table = {s: idx for idx, s in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}

for tc in range(1, int(input())+1):
    words = input()
    bit_l = ''.join([bin(table[i])[2:].zfill(6) for i in words])
    res = ''.join([chr(int(bit_l[j:j+8], 2))for j in range(0, len(bit_l), 8)])
    print(f'#{tc} {res}')
